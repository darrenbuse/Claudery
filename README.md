# Claudery

Personal AI collaboration preferences and skills for Claude Code and GitHub Copilot CLI.

## What is this?

A managed instructions file containing personal preferences for working with AI assistants, plus custom skills. Symlinked to `~/.claude/CLAUDE.md` and `~/.copilot/AGENTS.md`, these preferences apply across all your projects in both agents. Skills are symlinked into each agent's global skills directory.

## What's included

- **Behavioral expectations** - AI proposes before implementing, waits for confirmation
- **Critical collaboration** - Push back on ideas, challenge assumptions, offer alternatives
- **Simplicity principle** - Minimal changes, avoid over-engineering
- **Communication style** - Lead with the answer, no filler or throat-clearing, bullets-to-sentences drafting; structured question format for complex decisions
- **Safety guardrails** - Never delete files or run destructive commands without confirmation
- **No attribution** - Disables commit/PR attribution messages

## Install

Requires `jq` for settings configuration: `brew install jq`

```bash
./install.sh
```

This:
- Creates symlinks from `~/.claude/CLAUDE.md` and `~/.copilot/AGENTS.md` to this repo's `CLAUDE.md`
- Merges `settings.json` into `~/.claude/settings.json` (repo settings take precedence)
- Symlinks every skill in `skills/` into `~/.claude/skills/` and `~/.copilot/skills/`

## Customization

Fork this repo and edit `CLAUDE.md` to match your preferences. The install script will symlink your customized version.

## Project-specific overrides

These are global defaults. Add a `CLAUDE.md` to any project root to override or extend for that specific project.

## Skills

Skills in `skills/` are symlinked by `install.sh` into both agents' global skills directories, so they trigger in any repo. (`install-plugin.sh` remains for the older plugin-based route in Claude Code; the symlinks are the supported path.)

### `writing-style`

Kill AI slop in chat responses, commit messages, PR descriptions and status updates: open with the point, no announcements or filler, positive form, concrete language, draft as bullets then convert each to one simple sentence. Includes a banned-phrase taxonomy and before/after rewrite examples. Softened fork of [stop-slop](https://github.com/hardikpandya/stop-slop) with Strunk composition rules.

### `writing-docs`

Write documentation with the Diataxis framework: classify every doc into one quadrant (tutorial, how-to, reference, explanation), keep the boundaries, match voice to quadrant, plain language throughout. Includes doc templates and an anti-patterns review checklist. Condensed from [developer-docs-framework](https://github.com/anivar/developer-docs-framework).

### `session-summary`

Summarise a working session at a high level: achieved outcomes grouped by workstream with their artifacts (PRs, commits, paths), then open items split into blocked-on-you versus future backlog. For wrap-ups, handoffs and progress reports.

### `create-repo`

Create a new private GitHub repository from the `darrenbuse/claude-template` template.

Claude will ask for:
- **Repository name** - kebab-case (e.g., `my-project`)
- **Avatar emoji** - single emoji (e.g., 🚀)
- **Description** - brief project description
- **Prerequisites** - setup requirements (e.g., "Node.js 20+")

Creates a private repo with customized README, git hooks (husky), and conventional commits.

### `generate-install-app`

Generate an install script that symlinks a repo's main executable to `~/.local/bin/`.

Examines the repo to identify the entry point, handles multiple languages (Shell, Node.js, Python), and creates an idempotent `install.sh` (or `install-bin.sh` if `install.sh` already exists).

### `generate-plugin-install`

Generate an install script for a Claude Code plugin repo.

Creates `install-plugin.sh` that registers the repo as a local marketplace and installs the plugin into Claude Code's plugin system. Requires `.claude-plugin/plugin.json` and `jq`.

### `acli-jira`

Operate Jira from the terminal with the Atlassian CLI (`acli`): authentication, work-item create/search/edit/transition/comment, parent linking, ADF descriptions, bulk operations and destructive-command guardrails, backed by a generated command reference. Both this skill and `writing-tickets` read a per-repo `.atlassian.yaml` for the site URL, project key and organisation name, and ask for them when the file is absent.

### `acli-confluence`

Operate Confluence from the terminal with the Atlassian CLI (`acli`): authentication, viewing pages, listing and managing spaces, creating blog posts, and guardrails for the commands that publish or overwrite, backed by a generated command reference. Reads the same per-repo `.atlassian.yaml` as `acli-jira` for the Confluence site URL and space keys, and asks for them when the file is absent. Derived from the CLI's `--help` surface and honest about what has not yet been exercised against a live site.

### `writing-tickets`

Write and challenge Jira epics and stories: business-first context, tiered outcome discipline, testable acceptance criteria, and templates with worked before/after examples. Reads the same per-repo `.atlassian.yaml` as `acli-jira` for the organisation name and project key, and asks for them when the file is absent.

## License

MIT
