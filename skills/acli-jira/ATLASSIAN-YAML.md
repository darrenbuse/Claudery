# .atlassian.yaml

Atlassian context for a repository, read by the `acli-jira`, `acli-confluence` and
`writing-tickets` skills. Lives at the repository root, is committed, and contains no secrets —
credentials, and where they live (environment variables, token files, or otherwise),
are out of scope for this file.

## Fields

| Field | Required | Consumer |
| --- | --- | --- |
| `organisation` | yes | writing-tickets — substituted wherever skill text/templates say "the organisation" |
| `jira_base_url` | yes | acli-jira — site for `acli jira auth login` guidance; `…/browse/KEY-1` links after create/edit |
| `default_project` | optional; required when `projects` has >1 entry | `workitem create --project`; where a ticket lands without asking |
| `projects[].key` | yes | every command and JQL example |
| `projects[].name` | optional | disambiguation when asking the user to choose |
| `projects[].use_for` | yes | choosing between projects without a round trip |
| `confluence_base_url` | required for acli-confluence | acli-confluence — site for `acli confluence auth login` guidance and page links |
| `default_space` | optional; required when `confluence_spaces` has >1 entry | acli-confluence — where new content lands without asking |
| `confluence_spaces[].key` / `name` / `use_for` | key and use_for required per entry; name optional | acli-confluence — choosing between spaces without a round trip; name for disambiguation |

## Example

```yaml
# .atlassian.yaml — Atlassian context for this repository.
# Read by the acli-jira and writing-tickets skills. Committed; contains no secrets.
organisation: Example Retail Group
jira_base_url: https://example.atlassian.net
default_project: PROJ
projects:
  - key: PROJ
    name: Platform Engineering
    use_for: platform tooling, CI and developer experience work
  - key: DATA
    name: Data Services
    use_for: pipelines and warehouse data quality; file here when the change lands in the warehouse
confluence_base_url: https://example.atlassian.net/wiki
default_space: DOCS
confluence_spaces:
  - key: DOCS
    name: Engineering Docs
    use_for: runbooks, architecture notes and how-tos for the platform teams
  - key: ENG
    name: Engineering Announcements
    use_for: release notes and team-wide announcements, usually as blog posts
```

## Scaffold

Copy-paste starting point for a new repository:

```yaml
# .atlassian.yaml — Atlassian context for this repository.
# Read by the acli-jira and writing-tickets skills. Committed; contains no secrets.
organisation:
jira_base_url:
default_project:
projects:
  - key:
    name:
    use_for:
```

## Confluence

Read by the `acli-confluence` skill. Add these fields only in repositories that
actually work with Confluence; the Jira fields stand alone without them.

```yaml
confluence_base_url: https://example.atlassian.net/wiki   # required for acli-confluence
default_space: DOCS        # optional; required when confluence_spaces has >1 entry
confluence_spaces:
  - key: DOCS
    name: Engineering Docs
    use_for: one line on what lives there
```

## Credentials are out of scope

This file never holds a token, password or API key, and never records which
environment variable or token file a credential lives in. That is a matter for each
tool's own auth flow (for `acli-jira`, `acli jira auth login`), not for this file.
