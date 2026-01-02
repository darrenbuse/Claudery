# Claudery

Personal AI collaboration preferences for Claude Code.

## What is this?

A managed `CLAUDE.md` file containing personal preferences for working with AI assistants. Symlinked to `~/.claude/CLAUDE.md`, these preferences apply across all your projects.

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

## License

MIT
