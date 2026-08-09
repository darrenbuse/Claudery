# Atlassian CLI Jira Command Reference

Generated from `/opt/homebrew/bin/acli` using read-only `--help` invocations only.

- **acli version:** `1.3.22-stable`
- **Generated at:** `2026-08-01T16:47:47+01:00`
- **Commands discovered:** `85` (`77` Jira, `8` top-level/non-Jira inventory)
- **Commands documented in detail:** `20`
- **Safety invariant:** generator refuses to run anything except `acli --version`, `acli --help`, and `acli ... --help`.

## Scope

The command tree below lists everything the installed acli exposes. Detailed flag
tables are included only for the commands we use regularly.

**For any command not detailed here, run `acli <command> --help`.** That is the
authoritative source and it cannot go stale. Do not guess a flag, and do not assume
a flag that works on one subcommand works on its neighbour — several do not.

To regenerate with every command detailed: `python3 gen_acli_reference.py --all`.

## Command tree

- `acli` — Work seamlessly with Atlassian from the command line. ✱
  - `acli admin` — Admin commands.
  - `acli auth` — Authenticate to multiple Atlassian accounts with OAuth.
  - `acli confluence` — Confluence Cloud commands.
  - `acli guard` — ✗ Error: Plugin guard not found _(help exited 1)_
  - `acli jira` — Jira Cloud commands. ✱
    - `acli jira auth` — Authenticate to use Jira with OAuth or API token. ✱
      - `acli jira auth login` — Authenticate to Jira with OAuth or API token.
      - `acli jira auth logout` — Logout from current Jira account.
      - `acli jira auth status` — Show Jira account status. ✱
      - `acli jira auth switch` — Switch between Jira accounts.
    - `acli jira board` — Jira board commands.
      - `acli jira board create` — Create a new Jira board.
      - `acli jira board delete` — Deletes one or more Jira boards.
      - `acli jira board get` — DEPRECATED: this command is deprecated and will be removed in a future release. It will be removed on 2026-12-01. Deprecated since 2026-05-13.
      - `acli jira board list-projects` — List projects associated with a board.
      - `acli jira board list-sprints` — Get all sprints
      - `acli jira board search` — Search through all the boards
      - `acli jira board view` — View details of a Jira board.
    - `acli jira dashboard` — Jira dashboard commands.
      - `acli jira dashboard search` — Searches for the Jira dashboards. When multiple search parameters are present, the search ensures that all the parameters are satisfied.
    - `acli jira field` — Jira field commands.
      - `acli jira field cancel-delete` — DEPRECATED: this command is deprecated and will be removed in a future release. It will be removed on 2026-12-01. Deprecated since 2026-05-13.
      - `acli jira field create` — Create a custom field in Jira.
      - `acli jira field delete` — Moves a custom field to trash.
      - `acli jira field restore` — Restores the field from the trash.
      - `acli jira field update` — Update a custom field in Jira.
    - `acli jira filter` — Jira filter commands.
      - `acli jira filter add-favourite` — Add a filter as favourite.
      - `acli jira filter change-owner` — Change the owner of the provided filters.
      - `acli jira filter get` — DEPRECATED: this command is deprecated and will be removed in a future release. It will be removed on 2026-12-01. Deprecated since 2026-05-13.
      - `acli jira filter get-columns` — DEPRECATED: this command is deprecated and will be removed in a future release. It will be removed on 2026-12-01. Deprecated since 2026-05-13.
      - `acli jira filter list` — List filter that are either my or favourite.
      - `acli jira filter list-columns` — List configured columns for a filter.
      - `acli jira filter reset-columns` — Reset configured columns for a filter.
      - `acli jira filter search` — Searches for Jira filters. When multiple search parameters are present, the search ensures that all the parameters are satisfied.
      - `acli jira filter update` — Update an existing Jira filter.
      - `acli jira filter view` — View a Jira filter by its ID.
    - `acli jira project` — Jira project commands. ✱
      - `acli jira project archive` — Archives a Jira project.
      - `acli jira project create` — Create a Jira project which is a collection of work items (stories, bugs, tasks, etc). You would typically use a project to represent the development work for a product, project, or service in Jira.
      - `acli jira project delete` — Deletes a Jira project.
      - `acli jira project list` — List of projects visible to the user.
      - `acli jira project restore` — Restore a Jira project.
      - `acli jira project update` — Update a Jira project.
      - `acli jira project view` — Fetches a Jira project. ✱
    - `acli jira sprint` — Jira sprint commands.
      - `acli jira sprint create` — Create a new sprint on the board.
      - `acli jira sprint delete` — Deletes one or more Jira sprints.
      - `acli jira sprint list-workitems` — List work items in a sprint.
      - `acli jira sprint update` — Update an existing Jira sprint.
      - `acli jira sprint view` — View details of a Jira sprint.
    - `acli jira workitem` — Jira work item commands. ✱
      - `acli jira workitem archive` — Archives a work item or multiple work items. Archive a work item if you want to remove it from your project without deleting it. If you archive a work item, it will only appear in Archived work items and can no longer be edited. You can restore an archived work item if you need it in the future.
      - `acli jira workitem assign` — Assign a work item to an assignee or multiple work items to multiple assignees. ✱
      - `acli jira workitem attachment` — Work item attachments commands.
        - `acli jira workitem attachment delete` — Delete an attachment from a workitem.
        - `acli jira workitem attachment list` — List all the attachments of a workitem.
      - `acli jira workitem clone` — Create a duplicate of a work item or multiple work items by cloning within the same project or site, copying over most information from a work item like the Summary and Description fields and more.
      - `acli jira workitem comment` — Work item comments commands. ✱
        - `acli jira workitem comment create` — Add a comment to a work item or multiple work items using the default visibility for the project. ✱
        - `acli jira workitem comment delete` — Delete a comment for a given workitem
        - `acli jira workitem comment list` — List comments for a work item. ✱
        - `acli jira workitem comment update` — Update a comment on a work item. ✱
        - `acli jira workitem comment visibility` — Get visibility options for work item comments.
      - `acli jira workitem create` — Create a Jira work item to track individual pieces of work that must be completed. ✱
      - `acli jira workitem create-bulk` — Bulk create Jira issues.
      - `acli jira workitem delete` — Delete a work item or multiple work items. ✱
      - `acli jira workitem edit` — Edit a Jira work item or multiple work items. ✱
      - `acli jira workitem link` — Link work items commands. ✱
        - `acli jira workitem link create` — Create links between work items. ✱
        - `acli jira workitem link delete` — Delete links between work items.
        - `acli jira workitem link list` — List all the links of a workitem.
        - `acli jira workitem link type` — Get available workitem link types.
      - `acli jira workitem list-watchers` — List watchers of an issue
      - `acli jira workitem search` — Searches for work item or multiple work items. ✱
      - `acli jira workitem transition` — Transitioning a work item can mean moving it to another status, or performing a looped transition where the transition allows you to perform an action but keep the work item in its current status. ✱
      - `acli jira workitem unarchive` — Unarchives work item or multiple work items.
      - `acli jira workitem view` — Retrieve information about Jira work items. ✱
      - `acli jira workitem watcher` — Work item watcher commands.
        - `acli jira workitem watcher list` — DEPRECATED: this command is deprecated and will be removed in a future release. It will be removed on 2026-12-01. Deprecated since 2026-05-13.
        - `acli jira workitem watcher remove` — Remove a watcher from an issue
  - `acli rovodev` — ✗ Error: to get started, authenticate your Atlassian account: 1. Create a Rovo Dev scoped API token: <redacted-url> 2. Authenticate with: 'acli rovodev auth login' 3. Start using 'acli rovodev run' _(help exited 1)_
  - `acli config` — Commands for changing configuration settings.
  - `acli feedback` — Submit a request or report a problem.

✱ documented in detail below. For the rest, use `--help`.


## Detailed reference

## `acli`

**Purpose:** Work seamlessly with Atlassian from the command line.

**Usage:**

```text
  acli [command]
```

**Subcommands:**

- `acli admin` — Admin commands.
- `acli auth` — Authenticate to multiple Atlassian accounts with OAuth.
- `acli confluence` — Confluence Cloud commands.
- `acli guard` — Atlassian Guard CLI.
- `acli jira` — Jira Cloud commands.
- `acli rovodev` — Atlassian’s AI coding agent: Rovo Dev (Beta).
- `acli config` — Commands for changing configuration settings.
- `acli feedback` — Submit a request or report a problem.

**Flags:**

| Flag | Short | Type | Default | Description |
|---|---|---|---|---|
| --help | -h |  |  | Show help for command |
| --version | -v |  |  | version for acli |


### `acli jira`

**Purpose:** Jira Cloud commands.

**Usage:**

```text
  acli jira [command]
```

**Subcommands:**

- `acli jira auth` — Authenticate to use Jira with OAuth or API token.
- `acli jira board` — Jira board commands.
- `acli jira dashboard` — Jira dashboard commands.
- `acli jira field` — Jira field commands.
- `acli jira filter` — Jira filter commands.
- `acli jira project` — Jira project commands.
- `acli jira sprint` — Jira sprint commands.
- `acli jira workitem` — Jira work item commands.

**Flags:**

| Flag | Short | Type | Default | Description |
|---|---|---|---|---|
| --help | -h |  |  | Show help for command |


#### `acli jira auth`

**Purpose:** Authenticate to use Jira with OAuth or API token.

**Usage:**

```text
  acli jira auth [command]
```

**Subcommands:**

- `acli jira auth login` — Authenticate to Jira with OAuth or API token.
- `acli jira auth logout` — Logout from current Jira account.
- `acli jira auth status` — Show Jira account status.
- `acli jira auth switch` — Switch between Jira accounts.

**Flags:**

| Flag | Short | Type | Default | Description |
|---|---|---|---|---|
| --help | -h |  |  | Show help for command |


##### `acli jira auth status`

**Purpose:** Show Jira account status.

**Usage:**

```text
  acli jira auth status [flags]
```

**Official examples:**

```text
$ acli jira auth status
```

**Flags:**

| Flag | Short | Type | Default | Description |
|---|---|---|---|---|
| --help | -h |  |  | Show help for command |


#### `acli jira project`

**Purpose:** Jira project commands.

**Usage:**

```text
  acli jira project [command]
```

**Subcommands:**

- `acli jira project archive` — Archives a Jira project.
- `acli jira project create` — Create a Jira project – a collection of work items.
- `acli jira project delete` — Deletes a Jira project.
- `acli jira project list` — List of projects visible to the user.
- `acli jira project restore` — Restore a Jira project.
- `acli jira project update` — Update a Jira project.
- `acli jira project view` — Fetches a Jira project.

**Flags:**

| Flag | Short | Type | Default | Description |
|---|---|---|---|---|
| --help | -h |  |  | Show help for command |


##### `acli jira project view`

**Purpose:** Fetches a Jira project.

**Usage:**

```text
  acli jira project view [flags]
```

**Official examples:**

```text
# Fetches a project details with given key
$ acli jira project view --key "TEAM"
$ acli jira project view --key "TEAM" --json
```

**Flags:**

| Flag | Short | Type | Default | Description |
|---|---|---|---|---|
| --help | -h |  |  | Show help for command |
| --json | -j |  |  | Output in JSON format |
| --key |  | string |  | Key of the project to be fetched |


#### `acli jira workitem`

**Purpose:** Jira work item commands.

**Usage:**

```text
  acli jira workitem [command]
```

**Subcommands:**

- `acli jira workitem archive` — Archives a work item or multiple work items.
- `acli jira workitem assign` — Assign a work item(s) to an assignee(s).
- `acli jira workitem attachment` — Work item attachments commands.
- `acli jira workitem clone` — Create a duplicate work item(s).
- `acli jira workitem comment` — Work item comments commands.
- `acli jira workitem create` — Create a Jira work item.
- `acli jira workitem create-bulk` — Bulk create Jira issues.
- `acli jira workitem delete` — Delete a work item or multiple work items.
- `acli jira workitem edit` — Edit a Jira work item or multiple work items.
- `acli jira workitem link` — Link work items commands.
- `acli jira workitem list-watchers` — List watchers of an issue
- `acli jira workitem search` — Searches for work item or multiple work items.
- `acli jira workitem transition` — Transitioning a work item.
- `acli jira workitem unarchive` — Unarchives work item or multiple work items.
- `acli jira workitem view` — Retrieve information about Jira work items.
- `acli jira workitem watcher` — Work item watcher commands.

**Flags:**

| Flag | Short | Type | Default | Description |
|---|---|---|---|---|
| --help | -h |  |  | Show help for command |


##### `acli jira workitem assign`

**Purpose:** Assign a work item to an assignee or multiple work items to multiple assignees.

**Usage:**

```text
  acli jira workitem assign [flags]
```

**Official examples:**

```text
# Assign work item with work item key
$ acli jira workitem assign --key "KEY-1" --assignee "@me"

# Assign work item with JQL query
$ acli jira workitem assign --jql "project = TEAM" --assignee "<redacted-email>"

# Assign work item with filter ID
$ acli jira workitem assign --filter 10001 --assignee "default"

# Assign work item from file
$ acli jira workitem assign --from-file "issues.txt" --remove-assignee --json
```

**Flags:**

| Flag | Short | Type | Default | Description |
|---|---|---|---|---|
| --assignee | -a | string |  | Assign work item with email or account ID. Use '@me' to self-assign, 'default' to assign to the project's default assignee |
| --filter |  | string |  | Filter ID of work items to be assigned |
| --from-file | -f | string |  | Reads the work items to be assigned from the file. The file may contain work items IDs or keys separated by commas, white spaces, or new lines |
| --help | -h |  |  | Show help for command |
| --ignore-errors |  |  |  | Ignore the errors and continue |
| --jql |  | string |  | JQL query for work items to be assigned |
| --json |  |  |  | Generate a JSON output |
| --key | -k | string |  | A list of work item keys to be assigned |
| --remove-assignee |  |  |  | Remove assignee |
| --yes | -y |  |  | Confirm assign without prompting |


##### `acli jira workitem comment`

**Purpose:** Work item comments commands.

**Usage:**

```text
  acli jira workitem comment [command]
```

**Subcommands:**

- `acli jira workitem comment create` — Create a comment on work items
- `acli jira workitem comment delete` — Delete a comment for a given workitem
- `acli jira workitem comment list` — List comments for a work item.
- `acli jira workitem comment update` — Update a comment on a work item.
- `acli jira workitem comment visibility` — Get visibility options for work item comments.

**Flags:**

| Flag | Short | Type | Default | Description |
|---|---|---|---|---|
| --help | -h |  |  | Show help for command |


###### `acli jira workitem comment create`

**Purpose:** Add a comment to a work item or multiple work items using the default visibility for the project.

**Usage:**

```text
  acli jira workitem comment create [flags]
```

**Official examples:**

```text
# Comment on work item with work item keys
$ acli jira workitem comment --key "KEY-1" --body "This is a comment"

# Comment on work item with JQL query and plain text file 
$ acli jira workitem comment --jql "project = TEAM" --body-file "comment.txt" --edit-last

# Comment on work item with JQL query
$ acli jira workitem comment --jql "project = TEAM" --editor
```

**Flags:**

| Flag | Short | Type | Default | Description |
|---|---|---|---|---|
| --body | -b | string |  | Comment body in plain text or Atlassian Document Format (ADF) |
| --body-file | -F | string |  | Plain text file with text or Atlassian Document Format (ADF) |
| --edit-last | -e |  |  | Edit the last comment from the same author |
| --editor |  |  |  | Skip prompts and open the text editor to write the body |
| --filter |  | string |  | Filter ID of work items to comment |
| --help | -h |  |  | Show help for command |
| --ignore-errors |  |  |  | Ignore the errors and continue |
| --jql |  | string |  | JQL query for work items to comment |
| --json |  |  |  | Generate a JSON output |
| --key | -k | string |  | A list of work item keys to comment |


###### `acli jira workitem comment list`

**Purpose:** List comments for a work item.

**Usage:**

```text
  acli jira workitem comment list [flags]
```

**Official examples:**

```text
# List work item comments
$ acli jira workitem comment list --key TEST-123
```

**Flags:**

| Flag | Short | Type | Default | Description |
|---|---|---|---|---|
| --help | -h |  |  | Show help for command |
| --json |  |  |  | Output in JSON format |
| --key |  | string |  | Work item key to list comments for |
| --limit |  | int | 50 | Maximum number of comments to return per page |
| --order |  | string | "+created" | Order comments by field (created, updated) |
| --paginate |  |  |  | Continue paginating to fetch all pages of results. The --limit is ignored |


###### `acli jira workitem comment update`

**Purpose:** Update a comment on a work item.

**Usage:**

```text
  acli jira workitem comment update [flags]
```

**Official examples:**

```text
# Update comment body
$ acli jira workitem comment update --key TEST-123 --id 10001 --body "Updated comment text"

# Update comment from file
$ acli jira workitem comment update --key TEST-123 --id 10001 --body-file comment.txt

# Update comment with ADF format
$ acli jira workitem comment update --key TEST-123 --id 10001 --body-adf comment.json

# Update comment with role visibility
$ acli jira workitem comment update --key TEST-123 --id 10001 --body "Internal comment" --visibility-role "Administrators"

# Update comment with group visibility and notifications
$ acli jira workitem comment update --key TEST-123 --id 10001 --body "Team update" --visibility-group "dev-team" --notify
```

**Flags:**

| Flag | Short | Type | Default | Description |
|---|---|---|---|---|
| --body | -b | string |  | Comment body text |
| --body-adf |  | string |  | Body in Atlassian Document Format (JSON file) |
| --body-file | -F | string |  | Plain text file containing comment body |
| --help | -h |  |  | Show help for command |
| --id |  | string |  | The work item comment ID to be updated |
| --key |  | string |  | The work item key to be updated |
| --notify |  |  |  | Notifies users about the change |
| --visibility-group |  | string |  | Set comment visibility to a specific group |
| --visibility-role |  | string |  | Set comment visibility to a specific role |


##### `acli jira workitem create`

**Purpose:** Create a Jira work item to track individual pieces of work that must be completed.

**Usage:**

```text
  acli jira workitem create [flags]
```

**Official examples:**

```text
# Create work item by supplying a summary, project name and work item type
$ acli jira workitem create --summary "New Task" --project "TEAM" --type "Task"

# Create work item from file and supplying all work item details
$ acli jira workitem create --from-file "workitem.txt" --project "PROJ" --type "Bug" --assignee "<redacted-email>" --label "bug,cli"

# Generate a JSON file that could be used for workitem creation via --from-json flag
$ acli jira workitem create --generate-json

# Create work item from a JSON file
$ acli jira workitem create --from-json "workitem.json"
```

**Flags:**

| Flag | Short | Type | Default | Description |
|---|---|---|---|---|
| --assignee | -a | string |  | Assign people by their email or account ID. Use '@me' to self-assign, 'default' to assign to the project's default assignee |
| --description | -d | string |  | Supply a description in plain text or Atlassian Document Format (ADF) |
| --description-file |  | string |  | Read the description in plain text or Atlassian Document Format (ADF) from the file |
| --editor | -e |  |  | Open a text editor to specify the summary and description |
| --from-file | -f | string |  | Read the work item summary, description from a file |
| --from-json |  | string |  | Read the work item definition from a JSON file |
| --generate-json |  |  |  | Generates a JSON file that could be used for work item creation |
| --help | -h |  |  | Show help for command |
| --json |  |  |  | Output in JSON |
| --label | -l | strings |  | Add labels by name and comma-separated |
| --parent |  | string |  | Parent work item ID |
| --project | -p | string |  | Add the work item to projects by project key |
| --summary | -s | string |  | Supply a summary for the work item |
| --type | -t | string |  | Defines the work item type of the created work item. For example, Epic, Story, Task, Bug |


##### `acli jira workitem delete`

**Purpose:** Delete a work item or multiple work items.

**Usage:**

```text
  acli jira workitem delete [flags]
```

**Official examples:**

```text
# Delete work item with work item keys
$ acli jira workitem delete --key "KEY-1,KEY-2"

# Delete work item with JQL query
$ acli jira workitem delete --jql "project = TEAM"

# Delete work item with Filter ID
$ acli jira workitem delete --filter 10001

# Delete work item by reading from a file
$ acli jira workitem delete --from-file "issues.txt" --yes
```

**Flags:**

| Flag | Short | Type | Default | Description |
|---|---|---|---|---|
| --filter |  | string |  | Filter ID of work items to be deleted |
| --from-file | -f | string |  | Reads the work items to be deleted from the file. The file may contain work item IDs or keys separated by commas, white spaces, or new lines |
| --help | -h |  |  | Show help for command |
| --ignore-errors |  |  |  | Ignore the errors and continue |
| --jql |  | string |  | JQL query for work items to be deleted |
| --json |  |  |  | Generate a JSON output |
| --key | -k | string |  | A list of work item keys to be deleted |
| --yes | -y |  |  | Confirm delete without prompting |


##### `acli jira workitem edit`

**Purpose:** Edit a Jira work item or multiple work items.

**Usage:**

```text
  acli jira workitem edit [flags]
```

**Official examples:**

```text
# Edit work item with work item keys
$ acli jira workitem edit --key "KEY-1,KEY-2" --summary "New Summary"

# Edit work item with JQL query
$ acli jira workitem edit --jql "project = TEAM" --assignee "<redacted-email>"

# Edit work item with Filter ID
$ acli jira workitem edit --filter 10001 --description "Updated description" --yes

# Generate a JSON file that could be used for workitem edit via --from-json flag
$ acli jira workitem edit --generate-json

# Edit work item from a JSON file
$ acli jira workitem edit --from-json "workitem.json"
```

**Flags:**

| Flag | Short | Type | Default | Description |
|---|---|---|---|---|
| --assignee | -a | string |  | Assign work item with email or account ID. Use '@me' to self-assign, 'default' to assign to the project's default assignee |
| --description | -d | string |  | Edit the description in plain text or Atlassian Document Format (ADF) |
| --description-file |  | string |  | Read the description in plain text or Atlassian Document Format (ADF) from the file |
| --filter |  | string |  | Filter ID of work items to be edited |
| --from-json |  | string |  | Read the work item definition from a JSON file |
| --generate-json |  |  |  | Generates a JSON file that could be used for work item editing |
| --help | -h |  |  | Show help for command |
| --ignore-errors |  |  |  | Ignore the errors and continue |
| --jql |  | string |  | JQL query for work items to be edited |
| --json |  |  |  | Generate a JSON output |
| --key | -k | string |  | A list of work item keys to be edited |
| --labels | -l | string |  | Edit the labels |
| --remove-assignee |  |  |  | Remove the assignee |
| --remove-labels |  | string |  | Remove the labels |
| --summary | -s | string |  | Edit the summary |
| --type | -t | string |  | Edit the work item type |
| --yes | -y |  |  | Confirm edit without prompting |


##### `acli jira workitem link`

**Purpose:** Link work items commands.

**Usage:**

```text
  acli jira workitem link [command]
```

**Subcommands:**

- `acli jira workitem link create` — Create links between work items.
- `acli jira workitem link delete` — Delete links between work items.
- `acli jira workitem link list` — List all the links of a workitem.
- `acli jira workitem link type` — Get available workitem link types.

**Flags:**

| Flag | Short | Type | Default | Description |
|---|---|---|---|---|
| --help | -h |  |  | Show help for command |


###### `acli jira workitem link create`

**Purpose:** Create links between work items.

**Usage:**

```text
  acli jira workitem link create [flags]
```

**Official examples:**

```text
# Create a link between two work items
$ acli jira workitem link create --out KEY-123 --in KEY-456 --type Blocks

# Create multiple links from a JSON file
$ acli jira workitem link create --from-json links.json

# Generate an example JSON input structure
$ acli jira workitem link create --generate-json
```

**Flags:**

| Flag | Short | Type | Default | Description |
|---|---|---|---|---|
| --from-csv |  | string |  | Provide the input as a comma-separated table, where the first column is outward work item IDs, the second column is inward work item IDs, and the third column is linking type. The first row is ignored being the description. |
| --from-json |  | string |  | Read a JSON file for mapping work items, linking work items, and linking types |
| --generate-json |  |  |  | Prints an example JSON structure to be used with --from-json |
| --help | -h |  |  | Show help for command |
| --ignore-errors |  |  |  | Ignore the errors and continue with the next work item |
| --in |  | string |  | Inward work item ID. |
| --out |  | string |  | Outward work item ID. |
| --type |  | string |  | Work items linking type. Accepts outward descriptions |
| --yes |  |  |  | Confirm link creation without prompting |


##### `acli jira workitem search`

**Purpose:** Searches for work item or multiple work items.

**Usage:**

```text
  acli jira workitem search [flags]
```

**Official examples:**

```text
# Search for work items with JQL query
$ acli jira workitem search --jql "project = TEAM" --paginate
$ acli jira workitem search --jql "project = TEAM" --count
$ acli jira workitem search --jql "project = TEAM" --fields "key,summary,assignee" --csv
$ acli jira workitem search --jql "project = TEAM" --limit 50 --json
# Search for work items with filter ID
$ acli jira workitem search --filter 10001 --web
```

**Flags:**

| Flag | Short | Type | Default | Description |
|---|---|---|---|---|
| --count |  |  |  | Number of work items in the search |
| --csv |  |  |  | Generate a CSV output |
| --fields | -f | string | "issuetype,key,assignee,priority,status,summary" | Comma-separated list of fields to display in the output |
| --filter |  | string |  | Filter ID of work items to be searched |
| --help | -h |  |  | Show help for command |
| --jql | -j | string |  | JQL query to search for work items |
| --json |  |  |  | Generate a JSON output |
| --limit | -l | int |  | Maximum number of work items to fetch |
| --paginate |  |  |  | Fetch all work items by paginating through the results |
| --web | -w |  |  | Search for work items in the web browser |


##### `acli jira workitem transition`

**Purpose:** Transitioning a work item can mean moving it to another status, or performing a looped transition where the transition allows you to perform an action but keep the work item in its current status.

**Usage:**

```text
  acli jira workitem transition [flags]
```

**Official examples:**

```text
# Transition work item with work item keys
$ acli jira workitem transition --key "KEY-1,KEY-2" --status "Done"

# Transition work item with JQL query
$ acli jira workitem transition --jql "project = TEAM" --status "In Progress"

# Transition work item with filter ID
$ acli jira workitem transition --filter 10001 --status "To Do" --yes
```

**Flags:**

| Flag | Short | Type | Default | Description |
|---|---|---|---|---|
| --filter |  | string |  | Filter ID of work items to be transitioned |
| --help | -h |  |  | Show help for command |
| --ignore-errors |  |  |  | Ignore the errors and continue |
| --jql |  | string |  | JQL query for work items to be transitioned |
| --json |  |  |  | Generate a JSON output |
| --key | -k | string |  | A list of work item keys to be transitioned |
| --status | -s | string |  | Status to transition the work item |
| --yes | -y |  |  | Confirm transition without prompting |


##### `acli jira workitem view`

**Purpose:** Retrieve information about Jira work items.

**Usage:**

```text
  acli jira workitem view [key] [flags]
```

**Official examples:**

```text
# View work item with work item keys
$ acli jira workitem view KEY-123

# View work item by reading work item keys from a JSON file
$ acli jira workitem view KEY-123 --json

# View work item with work item keys and a list of field to return
$ acli jira workitem view KEY-123 --fields summary,comment

# View work item with work item keys and view in a web browser
$ acli jira workitem view KEY-123 --web
```

**Flags:**

| Flag | Short | Type | Default | Description |
|---|---|---|---|---|
| --fields | -f | string |  | A list of fields to return for the work item. This parameter accepts a comma-separated list. Use it to retrieve a subset of fields. Allowed values: |
|  | - | '*all' - returns all fields |  |  |
|  | - | '*navigable' - returns navigable fields |  | Any work item field, prefixed with a minus to exclude Examples: |
|  | - | 'summary |  |  |
|  | - | '-description' - returns all (default) fields except description |  |  |
|  | -comment' | '*navigable |  | (default "key,issuetype,summary,status,assignee,description") |
| --help | -h |  |  | Show help for command |
| --json |  |  |  | Generate a JSON output |
| --web | -w |  |  | View the work item in the web browser. |
