---
name: create-repo
description: This skill should be used when the user wants to create a new GitHub repository, start a new project, scaffold a new codebase, set up a new project, bootstrap a repo, or initialize a project from template. Creates a private repo from the darrenbuse/claude-template template, clones it, customizes the README, and pushes.
allowed-tools: Bash(*), AskUserQuestion, Read, Edit
---

# Create Repository from Template

Create a new private GitHub repository using the `darrenbuse/claude-template` template.

## Steps

1. **Gather information** using AskUserQuestion:
   - **Repository name** (kebab-case, e.g., `my-awesome-project`)
   - **Avatar emoji** (single emoji for the project, e.g., 🚀)
   - **Description** (brief description of what this project does)
   - **Prerequisites** (e.g., "Node.js 20+, Clojure CLI" or "Python 3.11")

2. **Create the repository**:
   ```bash
   gh repo create darrenbuse/<repo-name> --template darrenbuse/claude-template --private --clone
   ```

3. **Navigate to the new repo**:
   ```bash
   cd ~/Projects/<repo-name>
   ```

4. **Update README.md** - Replace all `<REPLACE:...>` placeholders:
   - `<REPLACE: Project Name>` → repo name
   - `<REPLACE: Brief description...>` → avatar + description (e.g., "🚀 A tool for...")
   - `<REPLACE: repo URL>` → `git@github.com:darrenbuse/<repo-name>.git`
   - `<REPLACE: project-name>` → repo name
   - `<REPLACE: Other prerequisites...>` → prerequisites provided
   - Other `<REPLACE:...>` sections → remove or leave as TODOs

5. **Update package.json** if exists:
   - Set `name` to repo name
   - Set `description` to avatar + description

6. **Install dependencies and commit**:
   ```bash
   # Only if package.json exists
   [ -f package.json ] && npm install
   git add -A
   git commit -m "feat: initialize <repo-name> from template"
   git push
   ```

7. **Report success** with the repo URL and next steps.

## Example

User: "Create a new repo called data-pipeline"

Ask for:
- Avatar: 🔄
- Description: ETL pipeline for processing customer data
- Prerequisites: Python 3.11, Docker

Result: Private repo at `github.com/darrenbuse/data-pipeline` with customized README.
