---
name: generate-plugin-install
description: This skill should be used when the user wants to generate an install script for a Claude Code plugin repo, set up plugin installation, or make a plugin installable. The repo must have .claude-plugin/plugin.json. Creates install-plugin.sh that registers the plugin as a local marketplace and enables it in Claude Code.
allowed-tools: Bash(*), AskUserQuestion, Read, Edit, Write, Glob, Grep
---

# Generate Plugin Install Script

Generate an `install-plugin.sh` script for a Claude Code plugin repo. The script registers the repo as a local marketplace and installs the plugin into Claude Code's plugin system.

## Prerequisites

- The repo must have `.claude-plugin/plugin.json` with at least `name` and `version` fields.
- The repo must have `.claude-plugin/marketplace.json`. If missing, generate it (see step 2).
- `jq` must be available on the system.

## Steps

1. **Verify this is a plugin repo**:
   - Check for `.claude-plugin/plugin.json` in the repo root.
   - If not found, inform the user this doesn't appear to be a Claude Code plugin repo and suggest creating `.claude-plugin/plugin.json` first.

2. **Ensure marketplace.json exists**:
   - Check for `.claude-plugin/marketplace.json`.
   - If missing, generate it using the plugin name from `plugin.json`:
     ```json
     {
       "name": "<plugin-name>-marketplace",
       "owner": {
         "name": "<author-name or repo owner>"
       },
       "plugins": [
         {
           "name": "<plugin-name>",
           "source": "./",
           "description": "<description from plugin.json>"
         }
       ]
     }
     ```
   - Ask the user for the owner name if not available from `plugin.json` author field.

3. **Read the plugin metadata**:
   - Parse `name` and `version` from `.claude-plugin/plugin.json`.
   - Parse marketplace name from `.claude-plugin/marketplace.json`.
   - Derive the plugin key: `<plugin-name>@<marketplace-name>`.

4. **Generate `install-plugin.sh`** in the repo root with this structure:
   ```bash
   #!/bin/bash
   set -e

   SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
   PLUGINS_DIR="$HOME/.claude/plugins"
   PLUGIN_NAME="<plugin-name>"
   MARKETPLACE_NAME="<marketplace-name>"
   PLUGIN_KEY="${PLUGIN_NAME}@${MARKETPLACE_NAME}"
   SETTINGS_FILE="$HOME/.claude/settings.json"
   KNOWN_MARKETPLACES="$PLUGINS_DIR/known_marketplaces.json"
   INSTALLED_PLUGINS="$PLUGINS_DIR/installed_plugins.json"

   # Check jq is available
   if ! command -v jq &> /dev/null; then
       echo "Error: jq is required but not installed."
       echo "Install with: brew install jq"
       exit 1
   fi

   echo "Installing $PLUGIN_NAME plugin..."

   # Create ~/.claude/plugins if needed
   mkdir -p "$PLUGINS_DIR"

   # Remove old symlink if it exists (legacy install method)
   OLD_SYMLINK="$PLUGINS_DIR/$PLUGIN_NAME"
   if [ -L "$OLD_SYMLINK" ]; then
       echo "Removing legacy symlink..."
       rm "$OLD_SYMLINK"
   fi

   NOW="$(date -u +%Y-%m-%dT%H:%M:%S.000Z)"
   VERSION=$(jq -r '.version // "1.0.0"' "$SCRIPT_DIR/.claude-plugin/plugin.json")

   # 1. Register marketplace in known_marketplaces.json
   echo "Registering marketplace..."
   if [ ! -f "$KNOWN_MARKETPLACES" ]; then
       echo '{}' > "$KNOWN_MARKETPLACES"
   fi

   jq --arg name "$MARKETPLACE_NAME" \
      --arg path "$SCRIPT_DIR" \
      --arg now "$NOW" \
      '.[$name] = {
        "source": {"source": "directory", "path": $path},
        "installLocation": $path,
        "lastUpdated": $now
      }' "$KNOWN_MARKETPLACES" > "$KNOWN_MARKETPLACES.tmp"
   mv "$KNOWN_MARKETPLACES.tmp" "$KNOWN_MARKETPLACES"

   # 2. Register plugin in installed_plugins.json
   echo "Registering plugin..."
   if [ ! -f "$INSTALLED_PLUGINS" ]; then
       echo '{"version": 2, "plugins": {}}' > "$INSTALLED_PLUGINS"
   fi

   jq --arg key "$PLUGIN_KEY" \
      --arg path "$SCRIPT_DIR" \
      --arg version "$VERSION" \
      --arg now "$NOW" \
      '.plugins[$key] = [{
        "scope": "user",
        "installPath": $path,
        "version": $version,
        "installedAt": $now,
        "lastUpdated": $now
      }]' "$INSTALLED_PLUGINS" > "$INSTALLED_PLUGINS.tmp"
   mv "$INSTALLED_PLUGINS.tmp" "$INSTALLED_PLUGINS"

   # 3. Enable plugin in settings.json
   echo "Enabling plugin..."
   if [ ! -f "$SETTINGS_FILE" ]; then
       echo '{}' > "$SETTINGS_FILE"
   fi

   jq --arg key "$PLUGIN_KEY" \
      '.enabledPlugins[$key] = true' "$SETTINGS_FILE" > "$SETTINGS_FILE.tmp"
   mv "$SETTINGS_FILE.tmp" "$SETTINGS_FILE"

   echo "Installed: $PLUGIN_KEY (v$VERSION)"
   echo "Restart Claude Code to load the plugin."
   ```

5. **Make the script executable**:
   ```bash
   chmod +x install-plugin.sh
   ```

6. **Report** what was created and how to use it:
   ```
   Created: install-plugin.sh
   Run: ./install-plugin.sh
   Plugin will be registered as: <plugin-name>@<marketplace-name>
   Requires: jq (brew install jq)
   ```
