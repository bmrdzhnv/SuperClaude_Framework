---
name: update-superclaude-fork
description: "Automated fork synchronization with upstream and conflict detection"
category: utility
complexity: advanced
mcp-servers: []
personas: [devops-architect]
depends: [git, gh]
---

# /sc:update-superclaude-fork - Fork Synchronization

## Purpose
Automatically synchronize your SuperClaude fork with upstream changes while preserving your feature branch work and detecting conflicts. Provides safe, intelligent fork management with comprehensive logging and dry-run capabilities.

## Current Situation Analysis
**If you run the command now** with the existing Deep Research System conflicts:

**✅ WILL HAPPEN:**
- Successfully stash your `update-superclaude-fork.md` changes
- Update master to v4.2.0 (Deep Research System)
- Push updated master to your fork

**⚠️ CONFLICT DETECTION:**
The enhanced command will detect and categorize these conflicts:
- **🟡 Version Conflict**: VERSION file (4.2.0 vs your version) - *Interactive resolution required*
- **🔴 Feature Conflict**: Research command implementations - *Integration decision needed*
- **🟢 Documentation**: README/docs updates - *Auto-resolvable with smart merging*
- **🟢 MCP Configuration**: Tavily server addition - *Auto-resolvable (additive)*

**🎯 ENHANCED BEHAVIOR:**
- **Interactive mode** will present version options with context
- **Smart merging** will auto-resolve documentation conflicts
- **Integration guidance** for overlapping research features
- **No manual git conflict resolution** - the command handles technical merging

**📋 YOU WILL BE ASKED:**
1. Version strategy choice (use 4.2.0, increment to 4.2.1, or custom)
2. Research feature integration decision (merge, rename, or separate)
3. Confirmation for auto-resolved conflicts

## Core Features
- **Intelligent Remote Detection**: Automatically handles both 'origin' and 'myfork' remote configurations
- **Safe Synchronization**: Never proceeds past conflicts, automatic stashing of uncommitted work
- **Enhanced Conflict Resolution**: Categorizes and intelligently handles different conflict types
- **Interactive Version Management**: Smart handling of version number conflicts with context
- **Color-Coded Logging**: Clear visual feedback with INFO (blue), SUCCESS (green), WARNING (yellow), ERROR (red)
- **Dry-Run Mode**: Preview all operations before execution with detailed summary
- **Pre-Merge Conflict Analysis**: Identify potential issues before attempting merge

## Enhanced Workflow
1. **Pre-Analysis** (if `--preview-conflicts`): Analyze potential conflicts before merge
2. **Stash** uncommitted changes (if any)
3. **Fetch** from upstream (origin: SuperClaude-Org/SuperClaude_Framework)
4. **Update** master branch with upstream changes
5. **Intelligent Merge**: Apply conflict resolution strategy
   - **Auto-resolve** structural conflicts (docs, imports, formatting)
   - **Interactive resolution** for semantic conflicts (versions, logic)
   - **Integration guidance** for feature conflicts (commands, agents)
6. **Validation** and consistency checks
7. **Restore** stashed changes after successful sync

## Usage
```bash
/sc:update-superclaude-fork                    # Standard update with interactive conflict resolution
/sc:update-superclaude-fork --dry-run          # Preview changes without executing
/sc:update-superclaude-fork --preview-conflicts # Analyze potential conflicts before merge
/sc:update-superclaude-fork --conflict-strategy auto # Auto-resolve safe conflicts
/sc:update-superclaude-fork --version-strategy upstream # Use upstream version numbers
/sc:update-superclaude-fork --auto-resolve docs,imports # Auto-resolve documentation and import conflicts
/sc:update-superclaude-fork --rebase           # Use rebase instead of merge
/sc:update-superclaude-fork --force-reset      # Force reset master to upstream (caution!)
/sc:update-superclaude-fork --path <path>      # Use custom repository path
```

## Parameters
| Parameter | Description | Default |
|-----------|-------------|---------|
| `--dry-run` | Preview operations without executing | false |
| `--rebase` | Use rebase strategy for feature branch | false (merge) |
| `--force-reset` | Force reset master to upstream (destructive) | false |
| `--path <path>` | Override repository path | `$SUPERCLAUDE_FRAMEWORK_PATH` |
| `--conflict-strategy <mode>` | Conflict resolution approach: `auto`, `interactive`, `manual` | interactive |
| `--version-strategy <mode>` | Version conflict handling: `upstream`, `increment`, `custom` | interactive |
| `--preview-conflicts` | Analyze conflicts before attempting merge | false |
| `--auto-resolve <types>` | Auto-resolve conflict types: `docs`, `imports`, `structure` | none |

## Environment Variables
```bash
# Default repository path
SUPERCLAUDE_FRAMEWORK_PATH="${SUPERCLAUDE_FRAMEWORK_PATH:-/Users/bm/Projects/GitHub/Sources/SuperClaude_Framework}"
```

## Output Examples

### Dry-Run Output
```
[INFO] SuperClaude Fork Synchronization
[INFO] ================================
[INFO]
[INFO] === DRY RUN SUMMARY ===
[INFO] Repository: /Users/bm/Projects/GitHub/Sources/SuperClaude_Framework
[INFO] Current branch: feature/comprehensive-documentation
[INFO] Upstream remote: origin
[INFO] Fork remote: myfork
[INFO] Use rebase: false
[INFO] Force reset: false
[INFO]
[INFO] Operations that would be performed:
[INFO] 1. Stash uncommitted changes (if any)
[INFO] 2. Fetch from upstream (origin)
[INFO] 3. Update master branch
[INFO] 4. Update feature branch (if not on master)
[INFO] 5. Check for conflicts
[INFO] 6. Restore stashed changes
```

### Successful Sync Output
```
[INFO] SuperClaude Fork Synchronization
[INFO] ================================
[INFO] No uncommitted changes to stash
[INFO] Fetching from upstream...
[INFO] Executing: git fetch origin
[INFO] Updating master branch...
[INFO] Executing: git checkout master
[INFO] Executing: git merge --ff-only origin/master
[INFO] Executing: git push myfork master
[INFO] Executing: git checkout feature/comprehensive-documentation
[INFO] Updating feature branch 'feature/comprehensive-documentation'...
[INFO] Executing: git merge master
[SUCCESS] Fork synchronization completed successfully!
```

### Conflict Detection Output
```
[INFO] Updating feature branch 'feature/comprehensive-documentation'...
[INFO] Executing: git merge master
[ERROR] Conflicts detected! Manual resolution required.
[INFO] Resolution steps:
[INFO] 1. cd /Users/bm/Projects/GitHub/Sources/SuperClaude_Framework
[INFO] 2. git status  # Review conflicts
[INFO] 3. Resolve conflicts manually in your editor
[INFO] 4. git add .  # Stage resolved files
[INFO] 5. git commit  # Complete merge
[INFO] 6. git push myfork feature/comprehensive-documentation
```

## Safety Features
- **Automatic Stashing**: Preserves uncommitted work before operations
- **Intelligent Conflict Detection**: Categorizes conflicts by type and complexity
- **Non-Destructive Default**: Merge strategy preserves commit history
- **Dry-Run Validation**: Preview all operations before execution
- **Clear Rollback Path**: Stashed changes can be recovered if needed
- **Intelligent Remote Handling**: Works with various remote configurations

## Enhanced Conflict Resolution

### Conflict Classification System
The enhanced command categorizes conflicts into three types:

**🟢 Structural Conflicts (Auto-resolvable)**
- Import statements and dependency additions
- Documentation formatting and markdown structure
- Non-semantic code organization changes
- *Strategy*: Automatically resolved with intelligent merge algorithms

**🟡 Semantic Conflicts (Interactive resolution)**
- Business logic changes and API modifications
- Version numbering (strategic decisions)
- Configuration values affecting behavior
- *Strategy*: Present options with context for user decision

**🔴 Feature Conflicts (Integration decisions)**
- New commands with similar names or purposes
- MCP server configuration overlaps
- Mode or agent conflicts requiring architectural decisions
- *Strategy*: Provide integration guidance and alternatives

### Interactive Version Resolution
When version conflicts are detected, you'll see:

```
[CONFLICT] VERSION file conflict detected
  Upstream version: 4.2.0 (Deep Research System)
  Your version: 4.1.5 (Comprehensive Documentation)

Options:
  1. Use upstream version (4.2.0) - adopts new features
  2. Increment from upstream (4.2.1) - your work follows theirs
  3. Use semantic increment (4.3.0) - major feature addition
  4. Custom version: [input field]

Choice [1-4]: _
```

### Conflict Strategy Modes

**Auto Mode** (`--conflict-strategy auto`)
- Automatically resolves structural conflicts
- Stops on semantic/feature conflicts for user input
- Fastest for experienced users with predictable conflicts

**Interactive Mode** (`--conflict-strategy interactive`) *[Default]*
- Shows conflict analysis before attempting resolution
- Provides options and context for all conflict types
- Best balance of automation and control

**Manual Mode** (`--conflict-strategy manual`)
- Traditional behavior: stops on any conflict
- Full manual resolution using git tools
- Maximum control for complex scenarios

## Examples

### Standard Update (Most Common)
```bash
/sc:update-superclaude-fork
# Synchronizes fork with upstream using merge strategy
# Safe for daily use, preserves all commit history
```

### Preview Changes and Conflicts (Recommended First Run)
```bash
/sc:update-superclaude-fork --preview-conflicts
# Analyzes potential conflicts before attempting merge
# Shows conflict types and resolution strategies
# Perfect for understanding what needs manual attention
```

### Intelligent Conflict Resolution
```bash
/sc:update-superclaude-fork --conflict-strategy auto --auto-resolve docs,imports
# Automatically resolves documentation and import conflicts
# Interactively handles version and feature conflicts
# Optimal for most development workflows
```

### Rebase Strategy (Clean History)
```bash
/sc:update-superclaude-fork --rebase
# Uses rebase to create linear history
# Caution: May require force push if already pushed
```

### Force Reset (Recovery)
```bash
/sc:update-superclaude-fork --force-reset
# Hard resets master to match upstream exactly
# Use only when master has diverged incorrectly
```

### Version Strategy Handling
```bash
/sc:update-superclaude-fork --version-strategy increment
# Automatically increments from upstream version (4.2.0 → 4.2.1)
# Preserves your feature work as a patch-level increment
# Best for feature branches with minimal breaking changes

/sc:update-superclaude-fork --version-strategy upstream
# Uses upstream version exactly (adopts 4.2.0)
# Your feature becomes part of the upstream version
# Best when your feature integrates seamlessly
```

### Custom Repository Path
```bash
/sc:update-superclaude-fork --path /path/to/other/repo --dry-run
# Operate on a different repository
# Useful for managing multiple forks
```

## Conflict Resolution Guide

When conflicts are detected, the script stops safely and provides clear instructions:

### Step-by-Step Resolution
1. **Navigate to repository**
   ```bash
   cd $SUPERCLAUDE_FRAMEWORK_PATH
   ```

2. **Review conflict status**
   ```bash
   git status
   # Shows conflicted files in red
   ```

3. **Resolve conflicts in your editor**
   - Look for conflict markers: `<<<<<<<`, `=======`, `>>>>>>>`
   - Choose desired changes or combine them
   - Remove conflict markers

4. **Stage resolved files**
   ```bash
   git add .
   # Or stage specific files: git add path/to/file.py
   ```

5. **Complete the merge**
   ```bash
   git commit
   # Editor opens for merge commit message
   ```

6. **Push to your fork**
   ```bash
   git push myfork feature/comprehensive-documentation
   ```

## Remote Configuration

The script intelligently handles different remote configurations:

### Standard Fork Setup
```bash
origin  → SuperClaude-Org/SuperClaude_Framework (upstream)
myfork  → yourusername/SuperClaude_Framework (your fork)
```

### Alternative Setup
```bash
upstream → SuperClaude-Org/SuperClaude_Framework
origin   → yourusername/SuperClaude_Framework
```

The script automatically detects and adapts to your configuration.

## Troubleshooting

### "Upstream remote 'origin' not found"
Ensure your remotes are properly configured:
```bash
git remote add origin https://github.com/SuperClaude-Org/SuperClaude_Framework
git remote add myfork https://github.com/yourusername/SuperClaude_Framework
```

### "Not a git repository"
Ensure you're in the correct directory:
```bash
cd /Users/bm/Projects/GitHub/Sources/SuperClaude_Framework
```

### "Merge conflicts prevent automatic sync"
This is expected behavior when changes conflict. Follow the conflict resolution guide above.

### "Cannot fast-forward master"
Your master has diverged from upstream. Use force reset cautiously:
```bash
/sc:update-superclaude-fork --force-reset
```

## Script Details
- **Command**: `~/.claude/commands/sc/update-superclaude-fork.md`
- **Implementation**: `~/.claude/scripts/fork_updater.sh`
- **Log Level**: Color-coded for clarity (INFO, SUCCESS, WARNING, ERROR)
- **Error Handling**: Fails safely with clear recovery instructions