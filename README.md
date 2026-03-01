# Claudery

Personal AI collaboration preferences and plugins for Claude Code.

## What is this?

A managed `CLAUDE.md` file containing personal preferences for working with AI assistants, plus custom skills/plugins. Symlinked to `~/.claude/CLAUDE.md`, these preferences apply across all your projects.

## What's included

- **Behavioral expectations** - AI proposes before implementing, waits for confirmation
- **Critical collaboration** - Push back on ideas, challenge assumptions, offer alternatives
- **Simplicity principle** - Minimal changes, avoid over-engineering
- **Communication style** - Structured question format for complex decisions
- **Safety guardrails** - Never delete files or run destructive commands without confirmation
- **No attribution** - Disables commit/PR attribution messages

## Install

Requires `jq` for settings configuration: `brew install jq`

```bash
./install.sh
```

This:
- Creates a symlink from `~/.claude/CLAUDE.md` to this repo's `CLAUDE.md`
- Merges `settings.json` into `~/.claude/settings.json` (repo settings take precedence)

## Customization

Fork this repo and edit `CLAUDE.md` to match your preferences. The install script will symlink your customized version.

## Project-specific overrides

These are global defaults. Add a `CLAUDE.md` to any project root to override or extend for that specific project.

## Skills

Skills are installed as a Claude Code plugin registered as a local marketplace. The `install-plugin.sh` script registers the plugin in Claude Code's plugin system. Skills in the `skills/` directory are auto-discovered.

### `/claudery:create-repo`

Create a new private GitHub repository from the `darrenbuse/claude-template` template.

Claude will ask for:
- **Repository name** - kebab-case (e.g., `my-project`)
- **Avatar emoji** - single emoji (e.g., 🚀)
- **Description** - brief project description
- **Prerequisites** - setup requirements (e.g., "Node.js 20+")

Creates a private repo with customized README, git hooks (husky), and conventional commits.

### `/claudery:generate-install-app`

Generate an install script that symlinks a repo's main executable to `~/.local/bin/`.

Examines the repo to identify the entry point, handles multiple languages (Shell, Node.js, Python), and creates an idempotent `install.sh` (or `install-bin.sh` if `install.sh` already exists).

### `/claudery:generate-plugin-install`

Generate an install script for a Claude Code plugin repo.

Creates `install-plugin.sh` that registers the repo as a local marketplace and installs the plugin into Claude Code's plugin system. Requires `.claude-plugin/plugin.json` and `jq`.

## License

MIT
