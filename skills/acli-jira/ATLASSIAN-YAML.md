# .atlassian.yaml

Atlassian context for a repository, read by the `acli-jira` and `writing-tickets`
skills. Lives at the repository root, is committed, and contains no secrets —
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

## Confluence (reserved, not yet used)

`confluence_base_url` and `confluence_spaces` are reserved names for a future
Confluence-reading consumer. Deliberately absent from this schema in v1 — their
shape will be agreed when a consumer exists. Do not add them speculatively.

## Credentials are out of scope

This file never holds a token, password or API key, and never records which
environment variable or token file a credential lives in. That is a matter for each
tool's own auth flow (for `acli-jira`, `acli jira auth login`), not for this file.
