#!/usr/bin/env python3
"""Generate a version-stamped Atlassian CLI reference from installed --help output.

Safety invariant: this script only invokes `acli --version` and `acli ... --help`.
It never executes create/edit/delete/transition/authenticated data-changing commands.
"""
from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

DEFAULT_ACLI = shutil.which("acli") or "/opt/homebrew/bin/acli"
DEFAULT_OUTPUT = Path(__file__).with_name("ACLI-REFERENCE.md")
NON_JIRA_GROUPS = {"admin", "auth", "confluence", "guard", "rovodev", "config", "feedback"}
SKIP_CHILDREN = {"help", "completion"}

# Commands rendered with full flag tables. Everything else is listed in the command
# tree only, with guidance to run `--help`. Keeping the reference small matters: it is
# loaded into an agent's context, and the unscoped version is roughly ten times this
# size while documenting boards, dashboards, fields and filters we never touch.
DETAIL_ALLOWLIST: set[tuple[str, ...]] = {
    (),
    ("jira",),
    ("jira", "auth"),
    ("jira", "auth", "status"),
    ("jira", "project"),
    ("jira", "project", "view"),
    ("jira", "workitem"),
    ("jira", "workitem", "view"),
    ("jira", "workitem", "search"),
    ("jira", "workitem", "create"),
    ("jira", "workitem", "edit"),
    ("jira", "workitem", "transition"),
    ("jira", "workitem", "assign"),
    ("jira", "workitem", "delete"),
    ("jira", "workitem", "comment"),
    ("jira", "workitem", "comment", "create"),
    ("jira", "workitem", "comment", "update"),
    ("jira", "workitem", "comment", "list"),
    ("jira", "workitem", "link"),
    ("jira", "workitem", "link", "create"),
}

SENSITIVE_PATTERNS = [
    (re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"), "<redacted-email>"),
    (re.compile(r"https?://[^\s,)]+"), "<redacted-url>"),
    (re.compile(r"([A-Za-z0-9-]+\.)+atlassian\.net"), "<redacted-site>"),
]

@dataclass
class Flag:
    short: str = ""
    long: str = ""
    type: str = ""
    default: str = ""
    description: str = ""
    section: str = "Flags"

@dataclass
class CommandDoc:
    words: tuple[str, ...]
    help_text: str
    returncode: int
    children: list[tuple[str, str]] = field(default_factory=list)
    purpose: str = ""
    usage: str = ""
    examples: str = ""
    flags: list[Flag] = field(default_factory=list)

    @property
    def command(self) -> str:
        return " ".join(("acli",) + self.words)


def run_readonly(acli: str, args: list[str]) -> tuple[int, str]:
    """Run only allowed read-only invocations."""
    if args != ["--version"] and (not args or args[-1] != "--help"):
        raise RuntimeError(f"Refusing non-help command: {args}")
    proc = subprocess.run([acli, *args], text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out = proc.stdout
    for pattern, replacement in SENSITIVE_PATTERNS:
        out = pattern.sub(replacement, out)
    return proc.returncode, out.rstrip()


def split_sections(text: str) -> dict[str, list[str]]:
    sections: dict[str, list[str]] = {"__preamble__": []}
    current = "__preamble__"
    header_re = re.compile(r"^(Usage|Aliases|Examples|Available Commands|Additional Commands|Flags|Global Flags):?\s*$")
    for line in text.splitlines():
        match = header_re.match(line)
        if match:
            current = match.group(1)
            sections.setdefault(current, [])
        else:
            sections.setdefault(current, []).append(line)
    return sections


def parse_children(sections: dict[str, list[str]]) -> list[tuple[str, str]]:
    children: list[tuple[str, str]] = []
    for section in ("Available Commands", "Additional Commands"):
        for line in sections.get(section, []):
            if not line.strip():
                continue
            match = re.match(r"^\s{2,}([\w-]+)\s+(.*)$", line)
            if match:
                name, desc = match.groups()
                if name not in SKIP_CHILDREN:
                    children.append((name, desc.strip()))
    # Preserve order while deduplicating.
    seen: set[str] = set()
    unique: list[tuple[str, str]] = []
    for name, desc in children:
        if name not in seen:
            seen.add(name)
            unique.append((name, desc))
    return unique


def parse_usage(sections: dict[str, list[str]]) -> str:
    usage_lines = [line.rstrip() for line in sections.get("Usage", []) if line.strip()]
    return "\n".join(usage_lines)


def parse_examples(sections: dict[str, list[str]]) -> str:
    lines = sections.get("Examples", [])
    while lines and not lines[0].strip():
        lines = lines[1:]
    while lines and not lines[-1].strip():
        lines = lines[:-1]
    return "\n".join(lines)


def parse_purpose(sections: dict[str, list[str]], text: str) -> str:
    for line in sections.get("__preamble__", []):
        stripped = line.strip()
        if stripped and not stripped.startswith("✗ Error"):
            return stripped
    for line in text.splitlines():
        stripped = line.strip()
        if stripped:
            return stripped
    return ""


def parse_flag_line(line: str, section: str) -> Flag | None:
    if not line.startswith("  ") or not line.strip():
        return None
    stripped = line.strip()
    # Two or more spaces separate the flag signature from its description.
    if "  " in stripped:
        sig, desc = re.split(r"\s{2,}", stripped, maxsplit=1)
    else:
        sig, desc = stripped, ""
    default = ""
    default_match = re.search(r"\(default (?P<default>[^)]+)\)", desc)
    if default_match:
        default = default_match.group("default")
        desc = (desc[:default_match.start()] + desc[default_match.end():]).strip()
    short = ""
    long = ""
    typ = ""
    parts = [part.strip() for part in sig.split(",")]
    for part in parts:
        if part.startswith("--"):
            toks = part.split(None, 1)
            long = toks[0]
            if len(toks) > 1:
                typ = toks[1]
        elif part.startswith("-"):
            toks = part.split(None, 1)
            short = toks[0]
            if len(toks) > 1 and not typ:
                typ = toks[1]
    if not (short or long):
        return None
    return Flag(short=short, long=long, type=typ, default=default, description=desc, section=section)


def parse_flags(sections: dict[str, list[str]]) -> list[Flag]:
    flags: list[Flag] = []
    for section in ("Flags", "Global Flags"):
        continuation_for: Flag | None = None
        for line in sections.get(section, []):
            parsed = parse_flag_line(line, section)
            if parsed:
                flags.append(parsed)
                continuation_for = parsed
            elif continuation_for and line.startswith("      ") and line.strip():
                continuation_for.description = (continuation_for.description + " " + line.strip()).strip()
    return flags


def parse_doc(words: tuple[str, ...], returncode: int, text: str) -> CommandDoc:
    sections = split_sections(text)
    return CommandDoc(
        words=words,
        help_text=text,
        returncode=returncode,
        children=parse_children(sections),
        purpose=parse_purpose(sections, text),
        usage=parse_usage(sections),
        examples=parse_examples(sections),
        flags=parse_flags(sections),
    )


def discover(acli: str) -> list[CommandDoc]:
    docs: list[CommandDoc] = []
    seen: set[tuple[str, ...]] = set()

    def visit(words: tuple[str, ...], recurse: bool) -> CommandDoc:
        if words in seen:
            raise RuntimeError(f"Duplicate command discovered: {words}")
        seen.add(words)
        rc, text = run_readonly(acli, [*words, "--help"] if words else ["--help"])
        doc = parse_doc(words, rc, text)
        docs.append(doc)
        if recurse:
            for child, _desc in doc.children:
                visit((*words, child), recurse=True)
        return doc

    root = visit((), recurse=False)
    top_names = [name for name, _ in root.children]

    for name in top_names:
        if name == "jira":
            visit(("jira",), recurse=True)
        elif name in NON_JIRA_GROUPS:
            # One-level inventory only: collect this group's --help and parse its immediate children.
            visit((name,), recurse=False)

    return docs


def md_escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", "<br>")


def render_flags(flags: Iterable[Flag]) -> str:
    flags = list(flags)
    if not flags:
        return "_No flags listed._\n"
    lines = ["| Flag | Short | Type | Default | Description |", "|---|---|---|---|---|"]
    for flag in flags:
        lines.append(
            "| {long} | {short} | {typ} | {default} | {desc} |".format(
                long=md_escape(flag.long or ""),
                short=md_escape(flag.short or ""),
                typ=md_escape(flag.type or ""),
                default=md_escape(flag.default or ""),
                desc=md_escape(flag.description or ""),
            )
        )
    return "\n".join(lines) + "\n"


def render_markdown(
    docs: list[CommandDoc],
    version: str,
    generated_at: str,
    acli_path: str,
    detailed: bool = False,
) -> str:
    detail_docs = docs if detailed else [d for d in docs if tuple(d.words) in DETAIL_ALLOWLIST]
    command_count = len(docs)
    jira_count = sum(1 for doc in docs if doc.words and doc.words[0] == "jira")
    non_jira_count = command_count - jira_count
    lines: list[str] = [
        "# Atlassian CLI Jira Command Reference",
        "",
        f"Generated from `{acli_path}` using read-only `--help` invocations only.",
        "",
        f"- **acli version:** `{version}`",
        f"- **Generated at:** `{generated_at}`",
        f"- **Commands discovered:** `{command_count}` (`{jira_count}` Jira, `{non_jira_count}` top-level/non-Jira inventory)",
        f"- **Commands documented in detail:** `{len(detail_docs)}`",
        "- **Safety invariant:** generator refuses to run anything except `acli --version`, `acli --help`, and `acli ... --help`.",
        "",
        "## Scope",
        "",
        "The command tree below lists everything the installed acli exposes. Detailed flag",
        "tables are included only for the commands we use regularly.",
        "",
        "**For any command not detailed here, run `acli <command> --help`.** That is the",
        "authoritative source and it cannot go stale. Do not guess a flag, and do not assume",
        "a flag that works on one subcommand works on its neighbour — several do not.",
        "",
        "To regenerate with every command detailed: `python3 gen_acli_reference.py --all`.",
        "",
        "## Command tree",
        "",
    ]

    def tree_line(doc: CommandDoc) -> str:
        indent = "  " * len(doc.words)
        status = "" if doc.returncode == 0 else f" _(help exited {doc.returncode})_"
        marker = " ✱" if tuple(doc.words) in DETAIL_ALLOWLIST and not detailed else ""
        return f"{indent}- `{doc.command}` — {doc.purpose}{status}{marker}"

    for doc in docs:
        lines.append(tree_line(doc))
    if not detailed:
        lines.extend(["", "✱ documented in detail below. For the rest, use `--help`.", ""])
    lines.extend(["", "## Detailed reference", ""])

    for doc in detail_docs:
        level = min(6, 2 + len(doc.words))
        lines.append(f"{'#' * level} `{doc.command}`")
        lines.append("")
        if doc.purpose:
            lines.append(f"**Purpose:** {doc.purpose}")
            lines.append("")
        if doc.returncode != 0:
            lines.append(f"**Help status:** exited `{doc.returncode}`.")
            lines.append("")
        if doc.usage:
            lines.append("**Usage:**")
            lines.append("")
            lines.append("```text")
            lines.append(doc.usage)
            lines.append("```")
            lines.append("")
        if doc.children:
            lines.append("**Subcommands:**")
            lines.append("")
            for child, desc in doc.children:
                lines.append(f"- `{doc.command} {child}` — {desc}")
            lines.append("")
        if doc.examples:
            lines.append("**Official examples:**")
            lines.append("")
            lines.append("```text")
            lines.append(doc.examples)
            lines.append("```")
            lines.append("")
        lines.append("**Flags:**")
        lines.append("")
        lines.append(render_flags(doc.flags))
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a markdown acli Jira reference from installed --help output.")
    parser.add_argument("--acli", default=os.environ.get("ACLI", DEFAULT_ACLI), help="Path to acli binary")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="Markdown output path")
    parser.add_argument("--all", dest="detailed", action="store_true",
                        help="Render detailed flag tables for every discovered command, not just the allowlist")
    args = parser.parse_args(argv)

    version_rc, version_out = run_readonly(args.acli, ["--version"])
    if version_rc != 0:
        raise SystemExit(f"Failed to read acli version: {version_out}")
    version = version_out.strip().replace("acli version ", "")
    generated_at = dt.datetime.now(dt.timezone.utc).astimezone().isoformat(timespec="seconds")
    docs = discover(args.acli)
    md = render_markdown(docs, version, generated_at, args.acli, detailed=args.detailed)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(md, encoding="utf-8")
    print(f"Wrote {args.output}")
    print(f"Commands documented: {len(docs)}")
    print(f"Bytes: {args.output.stat().st_size}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
