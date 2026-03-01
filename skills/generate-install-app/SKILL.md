---
name: generate-install-app
description: This skill should be used when the user wants to create an install script for a repo, install a CLI tool, make a script globally available, make a command available on PATH, add to PATH, create a symlink wrapper for an executable, or update an existing install script. Generates install.sh that symlinks the repo's main executable into ~/.local/bin/ and any zsh completion files into ~/.local/share/zsh/site-functions/.
allowed-tools: Bash(*), AskUserQuestion, Read, Edit, Write, Glob, Grep
---

# Create App Install Script

Create or update an install script that symlinks a repo's main executable to `~/.local/bin/` so it's available on the user's PATH, and any zsh completion files to `~/.local/share/zsh/site-functions/`.

## Steps

1. **Identify the main executable** by examining the repo:
   - Look for common entry points: `bin/`, `cli.*`, `main.*`, `app.*`, `index.*`, shebang lines, `package.json` `bin` field, Python `entry_points`, etc.
   - If multiple candidates or unclear, ask the user which file is the entry point using AskUserQuestion.
   - Ask the user what the command name should be (the name of the symlink in `~/.local/bin/`). Default suggestion: the repo directory name.

2. **Check for existing install scripts**:
   - Look for `install.sh` in the repo root.
   - If one exists, read it and determine the appropriate action:
     - If it already handles bin symlink and completions: inform the user, no action needed.
     - If it handles bin symlink but not completions: update it to add completions support.
     - If it does something unrelated: name the new script `install-bin.sh` instead.
   - If no `install.sh` exists, create `install.sh`.

3. **Generate the install script** with this structure:
   ```bash
   #!/bin/bash
   set -e

   SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
   BIN_DIR="$HOME/.local/bin"
   COMPLETIONS_DIR="$HOME/.local/share/zsh/site-functions"
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

   # Symlink helper: creates or updates a symlink
   link_file() {
       local target="$1" link="$2" label="$3"
       if [ -L "$link" ]; then
           local current
           current="$(readlink "$link")"
           if [ "$current" = "$target" ]; then
               echo "$label already installed."
               return 0
           fi
           echo "Updating existing symlink for $label..."
           rm "$link"
       elif [ -e "$link" ]; then
           echo "Warning: $link exists and is not a symlink. Skipping $label."
           return 1
       fi
       ln -s "$target" "$link"
       echo "Installed: $label -> $target"
   }

   # Install executable
   link_file "$TARGET" "$BIN_DIR/$COMMAND_NAME" "$COMMAND_NAME"

   # Install zsh completions if present
   COMPLETION_FILE="$SCRIPT_DIR/_$COMMAND_NAME"
   if [ -f "$COMPLETION_FILE" ]; then
       mkdir -p "$COMPLETIONS_DIR"
       link_file "$COMPLETION_FILE" "$COMPLETIONS_DIR/_$COMMAND_NAME" "_$COMMAND_NAME (zsh completion)"
   fi
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

6. **Look for zsh completion files**:
   - Search the repo for files named `_<command-name>` (the underscore-prefixed completion file).
   - Common locations: repo root, `completions/`, `zsh/`, `contrib/`.
   - If found, the generated script will symlink it to `~/.local/share/zsh/site-functions/`.
   - If not found, skip completions silently (no error).

7. **Report** what was created and how to use it:
   ```
   Created: install.sh
   Run: ./install.sh
   Command will be available as: <command-name>
   ```
   - If completions were included, note that `~/.local/share/zsh/site-functions` must be on `$fpath`. Suggest adding this to `.zshrc` if needed:
     ```bash
     fpath=(~/.local/share/zsh/site-functions $fpath)
     autoload -Uz compinit && compinit
     ```
