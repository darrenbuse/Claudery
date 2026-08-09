---
name: acli-confluence
description: Operating Confluence from the terminal with the Atlassian CLI (acli) — authentication, viewing pages, listing and managing spaces, creating blog posts, and guardrails for the commands that change things. WHEN viewing Confluence pages, listing spaces, or creating blog posts or spaces with the `acli` command. For writing the document content itself use writing-docs; for Jira work items use acli-jira.
kind: reference
---

# Operating Confluence with acli

## Overview

`acli` is Atlassian's official CLI. This skill covers the Confluence commands only —
for Jira work items use the `acli-jira` skill, and for how a document should be
structured and worded use `writing-docs`.

**Provenance, honestly stated.** The `acli-jira` skill's behavioural notes were earned
through real use against a live site. This skill is younger: it is derived from the
installed CLI's own `--help` surface, and its commands have not yet been exercised
against a live Confluence site. Syntax and flags below are accurate for the stamped
version; behavioural claims beyond what `--help` states are deliberately absent. Do
not trust remembered syntax, and do not copy examples from public acli guides — when
in doubt, run `--help` or consult the generated reference.

- Scoped reference for the commands we expect to use: [ACLI-CONFLUENCE-REFERENCE.md](ACLI-CONFLUENCE-REFERENCE.md)
- **For anything not in it, run `acli <command> --help`.** That is authoritative and
  cannot go stale. The reference lists the whole `acli confluence` command tree but
  documents flags only for the read, create and update commands people actually reach for.
- Regenerate after an acli upgrade: `python3 gen_acli_confluence_reference.py`
  (add `--all` to document every command)

The reference is generated from the installed binary's own `--help` output and is
stamped with the acli version. If the installed version does not match the stamp,
regenerate before relying on it.

## Repo context

Atlassian details for a repository live in `.atlassian.yaml` at its root — the same
file the `acli-jira` and `writing-tickets` skills read. Read it before running a
Confluence command or naming a space key. Never hardcode a space key, site URL or
organisation name in this skill or in your working notes.

Look in the repository root only — `git rev-parse --show-toplevel` when inside a git
repository, otherwise the current directory. Do not search parent directories.

**Present.** Use its values: `confluence_base_url` as the site, `default_space` for new
content unless the requester names another space, and `confluence_spaces[].use_for` to
choose between spaces. Where two spaces could both fit, ask rather than guess.

**Absent.** Say the repository has no `.atlassian.yaml`, then ask for the space key and
site URL and work from the answers for the rest of the session. Offer once to write the
file. Never write it unasked, and never in a repository that has nothing to do with
Atlassian. Schema and scaffold: [../acli-jira/ATLASSIAN-YAML.md](../acli-jira/ATLASSIAN-YAML.md).

**Malformed or incomplete.** Name the key that is missing or would not parse, then continue
as though the file were absent. Do not repair it silently.

**Personal notes.** If `~/.atlassian-notes/` exists, read its `NOTES.md` before asking the
user for page links, conventions or context — it holds their personal notes for the
organisations they work with. It is optional and machine-local: when it is absent, skip
this step silently. Treat its content as context for you, not text to paste into shared
documents unless the user asks.

## Check authentication first — and use the right command

```bash
acli confluence auth status
```

**Not `acli auth status`.** The top-level `auth` command covers global OAuth only; the
`acli-jira` skill verified that on an API-token session it exits non-zero with
"unauthorized" while product access is working perfectly. When
`acli confluence auth status` reports no session, tell the caller to run
`acli confluence auth login` and give them the site from `confluence_base_url`. Do not
guess the site.

Each product authenticates separately: `acli jira auth`, `acli admin auth`,
`acli confluence auth`. Being authenticated to one says nothing about the others.

## Command structure

```
acli confluence <entity> <action> [flags]
```

Every value is passed by named flag — `--help` shows no positional arguments anywhere
in the confluence group, unlike Jira's `workitem view`.

The surface is small in acli 1.3.22-stable, and lopsided in ways worth knowing before
you promise anything:

- **`page` has only `view`.** There is no `page create`, `page edit` or `page delete`
  in this version. The CLI cannot write a Confluence page; the only content-creation
  command in the group is `blog create`.
- **There are no `delete` commands at all** in the confluence group. The closest is
  `space archive`, which has a matching `space restore`.
- **Identifiers are inconsistent.** `page view` and `blog` commands take numeric IDs
  (`--id`, `--space-id`); `space create/update/archive/restore` take the space key
  (`--key`); `space view` takes `--id`. Find a numeric space ID with
  `acli confluence space list --keys DOCS --json`.
- **Body content is Confluence storage format (XHTML)**, not markdown and not ADF.
  `blog create --body` wants `<p>…</p>` markup; `--from-file` reads plain text or HTML.
  Markdown will arrive as literal text, exactly as it does in Jira descriptions.

## Common operations

All examples use the fictional site `https://example.atlassian.net/wiki` and spaces
`DOCS` and `ENG` — substitute values from `.atlassian.yaml`.

```bash
# Spaces
acli confluence space list
acli confluence space list --type global --json
acli confluence space list --keys DOCS,ENG --json
acli confluence space view --id 123456 --json

# Pages (read-only in this acli version)
acli confluence page view --id 123456789
acli confluence page view --id 123456789 --json
acli confluence page view --id 123456789 --body-format storage
acli confluence page view --id 123456789 --include-direct-children --include-labels

# Blog posts
acli confluence blog list --space-id 12345
acli confluence blog list --space-id 12345 --title "Release Notes" --json
acli confluence blog view --id 98765 --body-format storage
acli confluence blog create --space-id 12345 --title "Release Notes" \
  --body "<p>Content here</p>"
acli confluence blog create --space-id 12345 --title "Draft post" --status draft \
  --from-file post.html

# Space administration
acli confluence space create --key ENG --name "Engineering" --description "…"
acli confluence space update --key ENG --name "Engineering Platform"
```

`blog create --generate-json` produces a template payload for `--from-json`, mirroring
the pattern `acli-jira` uses for bulk creates.

## Guardrails

Nothing in the confluence group is a hard delete, but several commands change what
other people see, and two are easy to fire with wider effect than intended.

**Never run these unattended:**

- `space archive` — removes a space from normal view for everyone. Reversible via
  `space restore`, but disruptive; confirm the key and show the command first.
- `space update` — replaces the name, description or status outright. A description
  update does not merge; show the current value and the replacement before running it.
- `blog create` with `--status current` — publishes immediately and is visible to the
  whole space. Prefer `--status draft` unless the caller explicitly wants it live.

**Rules**

1. Get explicit confirmation before any command that archives, publishes or overwrites.
   Show the exact command and wait.
2. Before `blog create`, render the full body content on screen and get it approved.
   Content approval and command approval are separate, and a summary of what the post
   says is neither.
3. Before `space update`, fetch and show the current values
   (`acli confluence space view`) alongside the replacements.
4. Resolve numeric IDs to names before acting — confirm "space 12345 is DOCS
   (Engineering Docs)" rather than acting on a bare ID.
5. Treat `acli admin` as org-wide blast radius. Out of scope for this skill.

## Unverified

acli is not authenticated to a Confluence site on this machine, so nothing below the
`--help` surface has been exercised live. Specifically unverified: output shapes of
`--json` responses, whether `space view --id` accepts a key in practice, pagination
behaviour of `blog list --cursor`, how `page view --body-format atlas_doc_format`
renders, and any quirk of the kind the `acli-jira` skill documents (asymmetric flags,
fields missing from JSON output). When these commands get real use, record what is
learned here — that is how the Jira skill earned its quirk tables, and this skill
should earn its own the same way rather than inheriting guesses.

## Secrets

Never inline a token. Use an environment variable or file input — `auth login --token`
reads from standard input for exactly this reason — and never echo, log or print a
token or API key. A site URL read from `.atlassian.yaml` is committed configuration,
not a secret, and may be shown.

## Scope

Confluence only. `acli` also has `jira`, `admin`, `auth`, `guard`, `rovodev` and
`config` groups. Their existence is recorded in the generated reference; their
commands are not covered here. For Jira, use the `acli-jira` skill.
