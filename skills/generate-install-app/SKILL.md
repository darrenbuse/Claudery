---
name: generate-install-app
description: This skill should be used when the user wants to create an install script for a repo, install a CLI tool, make a script globally available, make a command available on PATH, add to PATH, or create a symlink wrapper for an executable. Generates install.sh that symlinks the repo's main executable into ~/.local/bin/.
allowed-tools: Bash(*), AskUserQuestion, Read, Edit, Write, Glob, Grep
---

# Create App Install Script

Create an install script that symlinks a repo's main executable to `~/.local/bin/` so it's available on the user's PATH.

## Steps

1. **Identify the main executable** by examining the repo:
   - Look for common entry points: `bin/`, `cli.*`, `main.*`, `app.*`, `index.*`, shebang lines, `package.json` `bin` field, Python `entry_points`, etc.
   - If multiple candidates or unclear, ask the user which file is the entry point using AskUserQuestion.
   - Ask the user what the command name should be (the name of the symlink in `~/.local/bin/`). Default suggestion: the repo directory name.

2. **Check for existing install scripts**:
   - Look for `install.sh` in the repo root.
   - If one exists, read it and check whether it already symlinks to `~/.local/bin/`.
     - If it already handles this: inform the user, no action needed.
     - If it does something else: name the new script `install-bin.sh` instead.
   - If no `install.sh` exists, create `install.sh`.

3. **Generate the install script** with this structure:
   ```bash
   #!/bin/bash
   set -e

   SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
   BIN_DIR="$HOME/.local/bin"
   COMMAND_NAME="<command-name>"
   TARGET="$SCRIPT_DIR/<path-to-executable>"

   echo "Installing $COMMAND_NAME..."

   # Create ~/.local/bin if needed
   if [ ! -d "$BIN_DIR" ]; then
       mkdir -p "$BIN_DIR"
       echo "Created $BIN_DIR"
   fi

   # Make executable
   chmod +x "$TARGET"

   # Handle existing symlink or file
   LINK="$BIN_DIR/$COMMAND_NAME"
   if [ -L "$LINK" ]; then
       CURRENT="$(readlink "$LINK")"
       if [ "$CURRENT" = "$TARGET" ]; then
           echo "$COMMAND_NAME already installed."
           exit 0
       fi
       echo "Updating existing symlink..."
       rm "$LINK"
   elif [ -e "$LINK" ]; then
       echo "Warning: $LINK exists and is not a symlink. Skipping."
       exit 1
   fi

   ln -s "$TARGET" "$LINK"
   echo "Installed: $COMMAND_NAME -> $TARGET"
   ```

4. **Adapt for the language/runtime** if needed:
   - **Shell scripts**: Symlink directly.
   - **Node.js**: If there's a `package.json` with a `bin` field, symlink that entry. If it needs `node` to run and has no shebang, create a small wrapper script in the repo (e.g., `bin/<name>`) with `#!/usr/bin/env node` and symlink that.
   - **Python**: If no shebang, create a wrapper with `#!/usr/bin/env python3` and symlink that.
   - **Other**: Ensure appropriate shebang is present or create a wrapper.

5. **Make the install script executable**:
   ```bash
   chmod +x install.sh  # or install-bin.sh
   ```

6. **Report** what was created and how to use it:
   ```
   Created: install.sh
   Run: ./install.sh
   Command will be available as: <command-name>
   ```
