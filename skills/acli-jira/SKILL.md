---
name: acli-jira
description: Operating Jira from the terminal with the Atlassian CLI (acli) — authentication, work-item create/search/edit/transition/comment, parent linking, ADF descriptions, bulk operations and destructive-command guardrails. WHEN creating, querying, transitioning or commenting on Jira work items with the `acli` command.
kind: reference
---

# Operating Jira with acli

## Overview

`acli` is Atlassian's official CLI. This skill covers the Jira commands only.

Everything here is verified against a specific installed version. Do not trust
remembered syntax, and do not copy examples from public acli guides — two widely
shared ones were checked and both contained flags that do not exist. When in doubt,
run `--help` or consult the generated reference.

- Scoped reference for the commands we use: [ACLI-REFERENCE.md](ACLI-REFERENCE.md)
- **For anything not in it, run `acli <command> --help`.** That is authoritative and
  cannot go stale. The reference deliberately covers only the ~20 commands we run
  regularly; it lists the whole command tree so you can see what exists, but does not
  document flags for the rest.
- Regenerate after an acli upgrade: `python3 gen_acli_reference.py`
  (add `--all` to document every command, which is about ten times the size)

The reference is generated from the installed binary's own `--help` output and is
stamped with the acli version. If the installed version does not match the stamp,
regenerate before relying on it.

## Repo context

Atlassian details for a repository live in `.atlassian.yaml` at its root. Read it before
running a Jira command or naming a project key. Never hardcode a project key, site URL or
organisation name in this skill or in your working notes.

Look in the repository root only — `git rev-parse --show-toplevel` when inside a git
repository, otherwise the current directory. Do not search parent directories.

**Present.** Use its values: `jira_base_url` as the site, `default_project` for a new item
unless the requester names another, `projects[].use_for` to choose between projects, and
`organisation` wherever this skill's text says "the organisation". Where two projects could
both fit, ask rather than guess.

**Absent.** Say the repository has no `.atlassian.yaml`, then ask for the project key and
site URL and work from the answers for the rest of the session. Offer once to write the
file. Never write it unasked, and never in a repository that has nothing to do with
Atlassian. Schema and scaffold: [ATLASSIAN-YAML.md](ATLASSIAN-YAML.md).

**Malformed or incomplete.** Name the key that is missing or would not parse, then continue
as though the file were absent. Do not repair it silently.

**Personal notes.** If `~/.atlassian-notes/` exists, read its `NOTES.md` before asking the
user for page links, conventions or context — it holds their personal notes for the
organisations they work with. It is optional and machine-local: when it is absent, skip
this step silently. Treat its content as context for you, not text to paste into shared
documents unless the user asks.

## Check authentication first — and use the right command

```bash
acli jira auth status
```

**Not `acli auth status`.** The top-level `auth` command covers global OAuth only. On
an API-token session it exits non-zero with "unauthorized" while Jira access is
working perfectly. Advice to run `acli auth status` before Jira work is wrong and
will send you into a pointless re-login. When `acli jira auth status` reports no session,
tell the caller to run `acli jira auth login` and give them the site from `jira_base_url`.
Do not guess the site.

Each product authenticates separately: `acli jira auth`, `acli admin auth`,
`acli confluence auth`. Being authenticated to one says nothing about the others.

## Command structure

```
acli <product> <entity> <action> [flags]
```

There is no `--action` flag. Almost every value is passed by named flag, including
where you would expect a positional (`acli jira sprint view --id 123`, not
`acli jira sprint view 123`).

**`workitem view` is the exception, and it is the one you will use most.** It takes the
key positionally and has no `--key` flag at all. Its neighbour `workitem edit` is the
opposite. Getting these two the wrong way round is the most common mistake with this
tool.

### How each command takes a work item key

Verified against acli 1.3.22-stable.

| Command | How the key is passed |
| --- | --- |
| `workitem view` | **positional** — `workitem view PROJ-1`. No `--key` flag exists |
| `workitem edit` | `--key` / `-k` |
| `workitem delete` | `--key` / `-k`, or `--jql`, `--filter`, `--from-file` |
| `workitem transition` | `--key` / `-k` |
| `workitem assign` | `--key` / `-k` |
| `workitem comment create` | `--key` / `-k`, or `--jql`, `--filter` |
| `workitem comment update` | `--key` **and** `--id` — both required. `--id` is the comment ID, not the work item |
| `workitem link create` | neither — uses `--out`, `--in` and `--type`, or `--from-json` / `--from-csv` |
| `workitem create` | no key; identified by `--project`, `--type`, `--summary` |

To find a comment ID for `comment update`, list the comments first:
`acli jira workitem view PROJ-1 --fields comment --json`.

## Common operations

```bash
# Search
acli jira workitem search --jql "project = PROJ AND assignee = currentUser()" --json
acli jira workitem search --jql "project = PROJ" --fields "key,summary,status" --csv
acli jira workitem search --jql "project = PROJ" --count

# View
acli jira workitem view PROJ-1
acli jira workitem view PROJ-1 --json

# Create
acli jira workitem create --project PROJ --type Story --summary "..." --assignee @me
acli jira workitem create --project PROJ --type Story --summary "..." \
  --description-file description.json --parent PROJ-1

# Edit, transition, assign, comment
acli jira workitem edit --key PROJ-1 --summary "..."
acli jira workitem transition --key PROJ-1 --status "In Progress"
acli jira workitem assign --key PROJ-1 --assignee @me
acli jira workitem comment create --key PROJ-1 --body "..."

# Projects, boards, sprints
acli jira project view --key PROJ --json
acli jira board list-sprints --id 123 --state active
acli jira sprint view --id 42
```

`--assignee` accepts an email, an account ID, `@me`, or `default` for the project
default assignee.

## Flags that are commonly got wrong

| Wrong | Correct | Command |
| --- | --- | --- |
| `workitem view --key PROJ-1` | `workitem view PROJ-1` (positional) | `workitem view` |
| `workitem edit PROJ-1` (positional) | `workitem edit --key PROJ-1` | `workitem edit` |
| `--comment` | `--body` / `-b` | `workitem comment create` |
| `--board 42` | `--id 42` | `board list-sprints` |
| `sprint view 123` | `sprint view --id 123` | `sprint view` |
| `--columns` | `--fields` | `workitem search` |
| `--outputFormat` | `--json`, and `--csv` where the command offers it | any list command |
| `acli auth status` | `acli jira auth status` | authentication check |

## Rich descriptions: use ADF

Plain markdown passed as a description does **not** render as formatting in Jira. It
arrives as flat text. To get headings, bullets and code spans, pass Atlassian
Document Format JSON.

```bash
acli jira workitem create --project PROJ --type Story --summary "..." \
  --description-file description.json
```

Minimal ADF document:

```json
{
  "type": "doc",
  "version": 1,
  "content": [
    { "type": "heading", "attrs": { "level": 2 },
      "content": [{ "type": "text", "text": "Context" }] },
    { "type": "paragraph",
      "content": [{ "type": "text", "text": "Plain sentence." }] },
    { "type": "bulletList", "content": [
      { "type": "listItem", "content": [
        { "type": "paragraph", "content": [{ "type": "text", "text": "A point" }] }
      ]}
    ]}
  ]
}
```

Inline code uses a mark: `{"type":"text","text":"packages/","marks":[{"type":"code"}]}`.
Ordered lists use `orderedList` with `"attrs": {"order": 1}`.

### ADF support is not consistent across commands

| Command | ADF goes in |
| --- | --- |
| `workitem create` | `--description` or `--description-file` |
| `workitem edit` | `--description` or `--description-file` |
| `workitem comment create` | `--body` or `--body-file` |
| `workitem comment update` | **`--body-adf` only** — its `--body-file` is plain text |

`comment create` and `comment update` are not symmetric. Assuming they are will post
raw JSON as visible comment text.

## Verifying what you created

`workitem view --json` does not return the `parent` field, so it cannot be used to
confirm a parent link. Use JQL instead:

```bash
acli jira workitem search --jql "project = PROJ AND parent = PROJ-1"
```

`parent` is also not accepted in `--fields`.

Check the created item's status after creation — some project workflows do not open
new items in the first column.

Give the caller the item's URL — `<jira_base_url>/browse/<KEY>` — so they can open it.

## Bulk operations

Target multiple items with `--key "A-1,A-2"`, `--jql "..."`, `--filter <id>`, or
`--from-file`. `--paginate` fetches all pages. `--generate-json` produces a template
for `--from-json`; `create-bulk` accepts `--from-csv` or `--from-json`.

Prefer built-in bulk flags over shell loops.

## Guardrails

**Always preview before acting in bulk.** Run `workitem search` with the same JQL
first and show the caller what will be affected.

**Never run these unattended.** Each is destructive or irreversible:

- `workitem delete` — permanent. With `--jql --yes --ignore-errors` it deletes every
  match, silently, with errors swallowed. Highest risk command in the tool.
- `project delete` — deletes a project and its work items. No `--yes` guard shown.
- `field delete`, `sprint delete`, `board delete`
- `workitem attachment delete`, `workitem comment delete`, `workitem link delete`
- `workitem archive` — bulk removal from the active project

Impactful but reversible: `workitem archive` / `unarchive`, `project archive` /
`restore`, `field restore`.

Bulk-capable and easy to fire too widely: `workitem edit`, `transition`, `assign`,
`clone`, `comment create`, `create-bulk`, `link create`.

**Rules**

1. Get explicit confirmation before any destructive command, even where `--yes`
   exists. `--yes` suppresses the prompt; it does not represent consent.
2. Never combine `--yes` with `--ignore-errors` on a destructive bulk operation. A
   partial failure is a signal to stop, not to continue silently.
3. Resolve and show the target list before acting on `--jql`, `--filter` or
   `--from-file`.
4. Treat `acli admin` as org-wide blast radius. Out of scope for this skill.
5. Before any `workitem create` or `workitem edit` that sets a description, render the
   full text of that description on screen and get it approved. Then show the exact
   command and wait. Content approval and command approval are separate, and a summary
   of what changed is neither.
6. The same applies to `comment create` and `comment update`. A comment is visible to
   everyone watching the item and notifies them by default. `comment update` silently
   replaces the existing comment body — show both the current text and the replacement
   before running it.
7. `comment create` accepts `--jql` and `--filter`, so it can comment on many items at
   once. Resolve the list first and show it.

## Content approval before create or edit

Writing to Jira is visible to other people and is awkward to undo cleanly. The
description you are about to send must be seen before it is sent.

- Show the complete description as it will read, not a description of your changes.
  "I have reworked the outcomes" is not something anyone can approve.
- For an edit, show the whole replacement text. `workitem edit --description` replaces
  the description outright — it does not merge — so a reader who only sees the changed
  lines cannot tell what is being discarded.
- Name every key the command will touch, and state what is not changing: status,
  assignee, parent, summary.
- Wait for a clear yes. Do not propose and run in the same turn.

For how the ticket itself should be structured and worded, use the `writing-tickets`
skill.

## Secrets

Never inline a token. Use an environment variable or file input, and never echo, log
or print a token or API key. A site URL read from `.atlassian.yaml` is committed
configuration, not a secret, and may be shown.

## Scope

Jira only. `acli` also has `admin`, `auth`, `confluence`, `guard`, `rovodev` and
`config` groups. Their existence is recorded in the generated reference; their
commands are not covered here.
