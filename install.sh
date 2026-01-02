#!/bin/bash

# Claudery Install Script
# Creates symlink from ~/.claude/CLAUDE.md to this repo's CLAUDE.md

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_FILE="$SCRIPT_DIR/CLAUDE.md"
TARGET_DIR="$HOME/.claude"
TARGET_FILE="$TARGET_DIR/CLAUDE.md"

echo "Claudery Installer"
echo "=================="
echo ""

# Check source exists
if [ ! -f "$SOURCE_FILE" ]; then
    echo "Error: CLAUDE.md not found at $SOURCE_FILE"
    exit 1
fi

# Create ~/.claude if it doesn't exist
if [ ! -d "$TARGET_DIR" ]; then
    echo "Creating $TARGET_DIR..."
    mkdir -p "$TARGET_DIR"
fi

# Handle existing file
if [ -e "$TARGET_FILE" ] || [ -L "$TARGET_FILE" ]; then
    if [ -L "$TARGET_FILE" ]; then
        CURRENT_TARGET="$(readlink "$TARGET_FILE")"
        if [ "$CURRENT_TARGET" = "$SOURCE_FILE" ]; then
            echo "Already installed. Symlink exists and points to correct location."
            exit 0
        fi
        echo "Existing symlink found pointing to: $CURRENT_TARGET"
    else
        echo "Existing CLAUDE.md found at $TARGET_FILE"
    fi

    read -p "Replace it? [y/N] " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Aborted."
        exit 1
    fi

    # Backup existing file
    BACKUP="$TARGET_FILE.backup.$(date +%Y%m%d%H%M%S)"
    echo "Backing up to $BACKUP..."
    mv "$TARGET_FILE" "$BACKUP"
fi

# Create symlink
echo "Creating symlink..."
ln -s "$SOURCE_FILE" "$TARGET_FILE"

echo ""
echo "Done! $TARGET_FILE -> $SOURCE_FILE"
echo ""
echo "Your personal AI preferences are now active for Claude Code."
