# Atlassian CLI Confluence Command Reference

Generated from `/opt/homebrew/bin/acli` using read-only `--help` invocations only.

- **acli version:** `1.3.22-stable`
- **Generated at:** `2026-08-09T17:15:55+01:00`
- **Commands discovered:** `27` (`19` Confluence, `8` top-level/non-Confluence inventory)
- **Commands documented in detail:** `16`
- **Safety invariant:** generator refuses to run anything except `acli --version`, `acli --help`, and `acli ... --help`.

## Scope

The command tree below lists everything the installed acli exposes. Detailed flag
tables are included only for the commands we expect to use regularly.

**For any command not detailed here, run `acli <command> --help`.** That is the
authoritative source and it cannot go stale. Do not guess a flag, and do not assume
a flag that works on one subcommand works on its neighbour — several do not.

To regenerate with every command detailed: `python3 gen_acli_confluence_reference.py --all`.

## Command tree

- `acli` — Work seamlessly with Atlassian from the command line. ✱
  - `acli admin` — Admin commands.
  - `acli auth` — Authenticate to multiple Atlassian accounts with OAuth.
  - `acli confluence` — Confluence Cloud commands. ✱
    - `acli confluence auth` — Authenticate to use Confluence with OAuth or API token. ✱
      - `acli confluence auth login` — Authenticate to Confluence with OAuth or API token. ✱
      - `acli confluence auth logout` — Logout from current Confluence account.
      - `acli confluence auth status` — Show Confluence account status. ✱
      - `acli confluence auth switch` — Switch between Confluence accounts.
    - `acli confluence blog` — Confluence blog commands. ✱
      - `acli confluence blog create` — Create a new Confluence blog post in the specified space. ✱
      - `acli confluence blog list` — List Confluence blog posts. ✱
      - `acli confluence blog view` — View details of a Confluence blog post. ✱
    - `acli confluence page` — Confluence page commands. ✱
      - `acli confluence page view` — View details of a Confluence page. ✱
    - `acli confluence space` — Confluence space commands. ✱
      - `acli confluence space archive` — Archive a Confluence space by key.
      - `acli confluence space create` — Create a Confluence space. ✱
      - `acli confluence space list` — List Confluence spaces. ✱
      - `acli confluence space restore` — Restore a Confluence space from the trash or archive by key.
      - `acli confluence space update` — Update details of a Confluence space, such as name, description, status, or settings by key. ✱
      - `acli confluence space view` — View details of a Confluence space. ✱
  - `acli guard` — ✗ Error: Plugin guard not found _(help exited 1)_
  - `acli jira` — Jira Cloud commands.
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


### `acli confluence`

**Purpose:** Confluence Cloud commands.

**Usage:**

```text
  acli confluence [command]
```

**Subcommands:**

- `acli confluence auth` — Authenticate to use Confluence with OAuth or API token.
- `acli confluence blog` — Confluence blog commands.
- `acli confluence page` — Confluence page commands.
- `acli confluence space` — Confluence space commands.

**Flags:**

| Flag | Short | Type | Default | Description |
|---|---|---|---|---|
| --help | -h |  |  | Show help for command |


#### `acli confluence auth`

**Purpose:** Authenticate to use Confluence with OAuth or API token.

**Usage:**

```text
  acli confluence auth [command]
```

**Subcommands:**

- `acli confluence auth login` — Authenticate to Confluence with OAuth or API token.
- `acli confluence auth logout` — Logout from current Confluence account.
- `acli confluence auth status` — Show Confluence account status.
- `acli confluence auth switch` — Switch between Confluence accounts.

**Flags:**

| Flag | Short | Type | Default | Description |
|---|---|---|---|---|
| --help | -h |  |  | Show help for command |


##### `acli confluence auth login`

**Purpose:** Authenticate to Confluence with OAuth or API token.

**Usage:**

```text
  acli confluence auth login [flags]
```

**Official examples:**

```text
# Authenticate using web browser (OAuth)
$ acli confluence auth login --web

# Authenticate with your email, site name and API token without scopes
$ acli confluence auth login --site "<redacted-site>" --email "<redacted-email>" --token < token.txt
OR
$ echo <token> | acli confluence auth login --site "<redacted-site>" --email "<redacted-email>" --token
	
# Authenticate with your email, site name and API token without scopes on Windows
$ Get-Content token.txt | .\acli.exe confluence auth login --site "<redacted-site>" --email "<redacted-email>" --token
```

**Flags:**

| Flag | Short | Type | Default | Description |
|---|---|---|---|---|
| --email | -e | string |  | User email is required for authentication |
| --help | -h |  |  | Show help for command |
| --site | -s | string |  | Site of the Atlassian instance is required for authentication |
| --token |  |  |  | Read token from standard input |
| --web | -w |  |  | Authenticate using web browser |


##### `acli confluence auth status`

**Purpose:** Show Confluence account status.

**Usage:**

```text
  acli confluence auth status [flags]
```

**Official examples:**

```text
$ acli confluence auth status
```

**Flags:**

| Flag | Short | Type | Default | Description |
|---|---|---|---|---|
| --help | -h |  |  | Show help for command |


#### `acli confluence blog`

**Purpose:** Confluence blog commands.

**Usage:**

```text
  acli confluence blog [command]
```

**Subcommands:**

- `acli confluence blog create` — Create a new Confluence blog post in the specified space.
- `acli confluence blog list` — List Confluence blog posts.
- `acli confluence blog view` — View details of a Confluence blog post.

**Flags:**

| Flag | Short | Type | Default | Description |
|---|---|---|---|---|
| --help | -h |  |  | Show help for command |


##### `acli confluence blog create`

**Purpose:** Create a new Confluence blog post in the specified space.

**Usage:**

```text
  acli confluence blog create [flags]
```

**Official examples:**

```text
# Create a published blog post in a space
$ acli confluence blog create --space-id 12345 --title "Release Notes" --body "<p>Content here</p>"

# Create a draft blog post
$ acli confluence blog create --space-id 12345 --title "Work in progress" --status draft --body "<p>Draft content</p>"

# Create a private published blog post
$ acli confluence blog create --space-id 12345 --title "Private announcement" --private --body "<p>Private content</p>"

# Create a blog post with custom creation timestamp
$ acli confluence blog create --space-id 12345 --title "Backdated blog" --created-at "2026-01-16T10:20:30.000Z" --body "<p>Content</p>" --json

# Create a blog post from a file
$ acli confluence blog create --space-id 12345 --title "From file" --from-file ./blog_content.html

# Create a blog post from JSON
$ acli confluence blog create --from-json ./blog_payload.json

# Generate example JSON structure
$ acli confluence blog create --generate-json
```

**Flags:**

| Flag | Short | Type | Default | Description |
|---|---|---|---|---|
| --body |  | string |  | Blog post content in Confluence storage format (XHTML) |
| --created-at |  | string |  | ISO 8601 timestamp for when the blog post is created (optional) |
| --from-file |  | string |  | Read blog post content from a file (plain text or HTML) |
| --from-json |  | string |  | Read blog post payload from a JSON file |
| --generate-json |  |  |  | Generate example JSON structure for use with --from-json |
| --help | -h |  |  | Show help for command |
| --json | -j |  |  | Output result in JSON format |
| --private |  |  |  | Create the blog post as private |
| --space-id |  | string |  | ID of the space where the blog post will be created |
| --status |  | string | "current" | Status of the blog post (current for published or draft) |
| --title |  | string |  | Title of the blog post |


##### `acli confluence blog list`

**Purpose:** List Confluence blog posts.

**Usage:**

```text
  acli confluence blog list [flags]
```

**Official examples:**

```text
# Get latest blog posts from a space with default limit
$ acli confluence blog list --space-id 12345

# Get a specific blog post by ID
$ acli confluence blog list --id 98765 -j

# Get current (published) blog posts from multiple spaces
$ acli confluence blog list --space-id 12345,67890 --status current,deleted --limit 25

# Get blog posts matching a title filter
$ acli confluence blog list --space-id 12345 --title "Release Notes"

# Get blog posts with body in storage format
$ acli confluence blog list --space-id 12345 --body-format storage -l 10

# Paginate using cursor from a previous response
$ acli confluence blog list --cursor "<cursor-from-previous-call>" --limit 25 -j
```

**Flags:**

| Flag | Short | Type | Default | Description |
|---|---|---|---|---|
| --body-format |  | string |  | Body representation of the blog post content to return (e.g. storage, atlas_doc_format) |
| --csv |  |  |  | Output in CSV format |
| --cursor |  | string |  | Pagination cursor token used to retrieve the next page of results |
| --help | -h |  |  | Show help for command |
| --id |  | string |  | Comma-separated list of blog post IDs to filter by |
| --json | -j |  |  | Output in JSON format |
| --limit | -l | int | 25 | Maximum number of blog posts to return in a single page of results |
| --sort |  | string |  | Sort order for returned blog posts |
| --space-id |  | string |  | Filter blog posts by space ID(s). Accepts comma-separated list of space IDs |
| --status |  | string |  | Filter blog posts by status. Accepts comma-separated list of statuses (e.g. current, deleted, trashed) |
| --title |  | string |  | Filter blog posts by title |


##### `acli confluence blog view`

**Purpose:** View details of a Confluence blog post.

**Usage:**

```text
  acli confluence blog view [flags]
```

**Official examples:**

```text
# View a blog post by ID
$ acli confluence blog view --id 98765

# View a blog post with body in storage format
$ acli confluence blog view --id 98765 --body-format storage

# View a blog post with body in atlas document format
$ acli confluence blog view --id 98765 --body-format atlas_doc_format

# View a specific version of a blog post
$ acli confluence blog view --id 98765 --version 2

# View a draft version of a blog post
$ acli confluence blog view --id 98765 --draft

# View a blog post with labels and properties included
$ acli confluence blog view --id 98765 --include labels,properties

# View a blog post in JSON format
$ acli confluence blog view --id 98765 --json
```

**Flags:**

| Flag | Short | Type | Default | Description |
|---|---|---|---|---|
| --body-format |  | string | "view" | The body format to return |
| --draft |  |  |  | Retrieve the draft version of this blog post |
| --help | -h |  |  | Show help for command |
| --id |  | string |  | The unique identifier of the blog post to view |
| --include |  | string |  | Comma-separated values. Possible values are labels, properties, operations, likes, versions, version, favorited, webresources, collaborators, and all to include all of the above |
| --json | -j |  |  | Output in JSON format |
| --status |  | string | "current" | Filter the blog post being retrieved by its status. Valid values are current, trashed, deleted, historical, draft |
| --version |  | int |  | Allows you to retrieve a previously published version. Specify the previous version's number to retrieve its details |


#### `acli confluence page`

**Purpose:** Confluence page commands.

**Usage:**

```text
  acli confluence page [command]
```

**Subcommands:**

- `acli confluence page view` — View details of a Confluence page.

**Flags:**

| Flag | Short | Type | Default | Description |
|---|---|---|---|---|
| --help | -h |  |  | Show help for command |


##### `acli confluence page view`

**Purpose:** View details of a Confluence page.

**Usage:**

```text
  acli confluence page view [flags]
```

**Official examples:**

```text
# View a page by ID
$ acli confluence page view --id 123456789

# View a page in JSON format
$ acli confluence page view --id 123456789 --json

# View a page requesting a specific body representation
$ acli confluence page view --id 123456789 --body-format storage
```

**Flags:**

| Flag | Short | Type | Default | Description |
|---|---|---|---|---|
| --body-format |  | string |  | Body representation to request (e.g. storage, atlas_doc_format, view) |
| --get-draft |  |  |  | When true, allows returning the draft version (if accessible) |
| --help | -h |  |  | Show help for command |
| --id |  | string |  | Page ID for the page to be displayed |
| --include-collaborators |  |  |  | Include collaborators info |
| --include-direct-children |  |  |  | Include direct child pages |
| --include-favorited-by-current-user-status |  |  |  | Include whether the page is favorited by the current user |
| --include-labels |  |  |  | Include page labels |
| --include-likes |  |  |  | Include likes / reactions info |
| --include-operations |  |  |  | Include allowed operations on the page |
| --include-properties |  |  |  | Include page content properties |
| --include-version |  |  |  | Include the detailed version object |
| --include-versions |  |  |  | Include versions list/summary |
| --include-webresources |  |  |  | Include required webresources metadata |
| --json |  |  |  | Output in JSON format |
| --status |  | string |  | Filter by page status (comma-separated list: current,draft,archived) |
| --version |  | int |  | Specific version number of the page to retrieve |


#### `acli confluence space`

**Purpose:** Confluence space commands.

**Usage:**

```text
  acli confluence space [command]
```

**Subcommands:**

- `acli confluence space archive` — Archive a Confluence space by key.
- `acli confluence space create` — Create a Confluence space.
- `acli confluence space list` — List Confluence spaces.
- `acli confluence space restore` — Restore a Confluence space from the trash or archive by key.
- `acli confluence space update` — Update details of a Confluence space, such as name, description, status, or settings by key.
- `acli confluence space view` — View details of a Confluence space.

**Flags:**

| Flag | Short | Type | Default | Description |
|---|---|---|---|---|
| --help | -h |  |  | Show help for command |


##### `acli confluence space create`

**Purpose:** Create a Confluence space.

**Usage:**

```text
  acli confluence space create [flags]
```

**Official examples:**

```text
# Create space with key and name
$ acli confluence space create --key SPACEKEY --name "Space Name"

# Create space with key, name and description
$ acli confluence space create --key SPACEKEY --name "Space Name" --description "Space description"
```

**Flags:**

| Flag | Short | Type | Default | Description |
|---|---|---|---|---|
| --alias |  | string |  | Identifier for the space in confluence page URLs |
| --description |  | string |  | The description of the new space |
| --help | -h |  |  | Show help for command |
| --json |  |  |  | Output in JSON format |
| --key |  | string |  | The key for the new space |
| --name |  | string |  | The name of the space to be created |
| --private |  |  |  | Whether to create the space as private |
| --template-key |  | string |  | The key of the template to use |


##### `acli confluence space list`

**Purpose:** List Confluence spaces.

**Usage:**

```text
  acli confluence space list [flags]
```

**Official examples:**

```text
# List all accessible spaces
$ acli confluence space list

# List only personal spaces
$ acli confluence space list --type personal

# List spaces with expanded information
$ acli confluence space list --expand description,homepage

# List spaces in JSON format
$ acli confluence space list --json
```

**Flags:**

| Flag | Short | Type | Default | Description |
|---|---|---|---|---|
| --expand |  | string |  | Comma-separated list of properties to expand (description, homepage, permissions) |
| --help | -h |  |  | Show help for command |
| --json |  |  |  | Output in JSON format |
| --keys |  | string |  | Comma-separated list of space keys to filter by |
| --limit | -l | int | 50 | Maximum number of spaces to return |
| --status |  | string | "current" | Filter spaces by status (current, archived) |
| --type |  | string |  | Filter spaces by type (global, personal) |


##### `acli confluence space update`

**Purpose:** Update details of a Confluence space, such as name, description, status, or settings by key.

**Usage:**

```text
  acli confluence space update [flags]
```

**Official examples:**

```text
# Update the name of a space
$ acli confluence space update --key SPACEKEY --name "New Team Space Name"

# Update the description of a space
$ acli confluence space update --key SPACEKEY --description "Updated description"
```

**Flags:**

| Flag | Short | Type | Default | Description |
|---|---|---|---|---|
| --description |  | string |  | New description for the space |
| --help | -h |  |  | Show help for command |
| --json |  |  |  | Output in JSON format |
| --key |  | string |  | Space key for the space to be updated |
| --name |  | string |  | New name for the space |
| --status |  | string |  | Update the status |
| --type |  | string |  | New type for the space |


##### `acli confluence space view`

**Purpose:** View details of a Confluence space.

**Usage:**

```text
  acli confluence space view [flags]
```

**Official examples:**

```text
# View a space by ID
$ acli confluence space view --id 123456

# View a space with icon and labels
$ acli confluence space view --id 123456 --icon --labels

# View a space with all additional details
$ acli confluence space view --id 123456 --include-all

# View a space in JSON format
$ acli confluence space view --id 123456 --json
```

**Flags:**

| Flag | Short | Type | Default | Description |
|---|---|---|---|---|
| --desc-format |  | string |  | The content format type to be returned in the description field (plain, view) |
| --help | -h |  |  | Show help for command |
| --icon |  |  |  | Include the icon for the space |
| --id |  | string |  | Space ID for the space to be displayed |
| --include-all |  |  |  | Include all additional details (icon, labels, role-assignments, permissions, operations, properties) |
| --json |  |  |  | Output in JSON format |
| --labels |  |  |  | Include labels associated with this space |
| --operations |  |  |  | Include operations associated with this space |
| --permissions |  |  |  | Include space permissions associated with this space |
| --properties |  |  |  | Include space properties associated with this space |
| --role-assignments |  |  |  | Include role assignments associated with this space (EAP sites only) |
