#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PLUGINS_DIR="$HOME/.claude/plugins"
PLUGIN_NAME="claudery"
MARKETPLACE_NAME="claudery-marketplace"
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
