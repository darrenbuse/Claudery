#!/bin/bash

# Claudery Install Script
# Creates symlink from ~/.claude/CLAUDE.md to this repo's CLAUDE.md
# Configures attribution settings in settings.json

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_FILE="$SCRIPT_DIR/CLAUDE.md"
TARGET_DIR="$HOME/.claude"
TARGET_FILE="$TARGET_DIR/CLAUDE.md"
SETTINGS_FILE="$TARGET_DIR/settings.json"

echo "Claudery Installer"
echo "=================="
echo ""

# Check source exists
if [ ! -f "$SOURCE_FILE" ]; then
    echo "Error: CLAUDE.md not found at $SOURCE_FILE"
    exit 1
fi

# Check jq is available
if ! command -v jq &> /dev/null; then
    echo "Error: jq is required but not installed."
    echo "Install with: brew install jq"
    exit 1
fi

# Create ~/.claude if it doesn't exist
if [ ! -d "$TARGET_DIR" ]; then
    echo "Creating $TARGET_DIR..."
    mkdir -p "$TARGET_DIR"
fi

# Handle existing CLAUDE.md
if [ -e "$TARGET_FILE" ] || [ -L "$TARGET_FILE" ]; then
    if [ -L "$TARGET_FILE" ]; then
        CURRENT_TARGET="$(readlink "$TARGET_FILE")"
        if [ "$CURRENT_TARGET" = "$SOURCE_FILE" ]; then
            echo "CLAUDE.md symlink already correct."
        else
            echo "Existing symlink found pointing to: $CURRENT_TARGET"
            read -p "Replace it? [y/N] " -n 1 -r
            echo ""
            if [[ ! $REPLY =~ ^[Yy]$ ]]; then
                echo "Aborted."
                exit 1
            fi
            BACKUP="$TARGET_FILE.backup.$(date +%Y%m%d%H%M%S)"
            echo "Backing up to $BACKUP..."
            mv "$TARGET_FILE" "$BACKUP"
            ln -s "$SOURCE_FILE" "$TARGET_FILE"
            echo "Created symlink: $TARGET_FILE -> $SOURCE_FILE"
        fi
    else
        echo "Existing CLAUDE.md found at $TARGET_FILE"
        read -p "Replace it? [y/N] " -n 1 -r
        echo ""
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo "Aborted."
            exit 1
        fi
        BACKUP="$TARGET_FILE.backup.$(date +%Y%m%d%H%M%S)"
        echo "Backing up to $BACKUP..."
        mv "$TARGET_FILE" "$BACKUP"
        ln -s "$SOURCE_FILE" "$TARGET_FILE"
        echo "Created symlink: $TARGET_FILE -> $SOURCE_FILE"
    fi
else
    ln -s "$SOURCE_FILE" "$TARGET_FILE"
    echo "Created symlink: $TARGET_FILE -> $SOURCE_FILE"
fi

# Merge settings.json
echo ""
echo "Configuring settings..."

SOURCE_SETTINGS="$SCRIPT_DIR/settings.json"

if [ -f "$SOURCE_SETTINGS" ]; then
    if [ -f "$SETTINGS_FILE" ]; then
        # Merge: existing settings + repo settings (repo wins), remove deprecated keys
        jq -s '.[0] * .[1] | del(.includeCoAuthoredBy)' "$SETTINGS_FILE" "$SOURCE_SETTINGS" > "$SETTINGS_FILE.tmp"
        mv "$SETTINGS_FILE.tmp" "$SETTINGS_FILE"
        echo "Merged settings from $SOURCE_SETTINGS into $SETTINGS_FILE"
    else
        # No existing settings, just copy
        cp "$SOURCE_SETTINGS" "$SETTINGS_FILE"
        echo "Created $SETTINGS_FILE from $SOURCE_SETTINGS"
    fi
else
    echo "No settings.json in repo, skipping settings configuration"
fi

# Install plugin
echo ""
"$SCRIPT_DIR/install-plugin.sh"

echo ""
echo "Done! Your personal AI preferences and plugins are now active for Claude Code."
echo ""
echo "Available skills:"
for skill_file in "$SCRIPT_DIR"/skills/*/SKILL.md; do
    [ -f "$skill_file" ] || continue
    skill_name="$(basename "$(dirname "$skill_file")")"
    skill_desc="$(sed -n 's/^description: *//p' "$skill_file" | head -1)"
    printf "  /%-28s %s\n" "$skill_name" "- ${skill_desc%%.*}."
done
