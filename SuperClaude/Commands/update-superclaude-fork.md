---
name: update-superclaude-fork
description: "Automated fork synchronization with upstream and conflict detection"
category: utility
complexity: advanced
mcp-servers: []
personas: [devops-architect]
depends: [git, gh]
---

# /sc:update_superclaude_fork - Fork Synchronization

## Purpose
Automatically synchronize your SuperClaude fork with upstream changes while preserving your feature branch work and detecting conflicts.

## Workflow
1. **Stash** uncommitted changes
2. **Sync** fork master with upstream (SuperClaude-Org/SuperClaude_Framework)
3. **Update** feature branch with latest master
4. **Detect** conflicts and notify for manual resolution
5. **Restore** stashed changes

## Usage
```bash
/sc:update_superclaude_fork                    # Standard update
/sc:update_superclaude_fork --dry-run          # Preview changes without executing
/sc:update_superclaude_fork --rebase           # Use rebase instead of merge
/sc:update_superclaude_fork --force-reset      # Force reset master to upstream
```

## Parameters
- `--dry-run`: Show what would happen without executing
- `--rebase`: Use rebase for feature branch (default: merge)
- `--force-reset`: Force reset fork master to upstream
- `--path <path>`: Override SuperClaude repo path

## Environment Variables
```bash
SUPERCLAUDE_FRAMEWORK_PATH="${SUPERCLAUDE_FRAMEWORK_PATH:-/Users/bm/Projects/GitHub/Sources/SuperClaude_Framework}"
```

## Conflict Handling
- **Automatic stash**: Preserves uncommitted work
- **Conflict detection**: Stops on merge/rebase conflicts
- **PR notification**: Comments on open PRs if conflicts detected
- **Manual resolution**: Provides clear steps for conflict resolution

## Safety Features
- Never proceeds past conflicts
- Automatic backup before destructive operations
- Clear rollback instructions
- Detailed operation logging

## Examples

### Standard Update
```bash
/sc:update_superclaude_fork
```

### Preview Changes
```bash
/sc:update_superclaude_fork --dry-run
```

### Force Reset Fork
```bash
/sc:update_superclaude_fork --force-reset
```

## Conflict Resolution Steps
When conflicts are detected:
1. `cd $SUPERCLAUDE_FRAMEWORK_PATH`
2. `git status` - Review conflicts
3. Resolve conflicts manually in your editor
4. `git add .` - Stage resolved files
5. `git commit` - Complete merge/rebase
6. `git push origin feature/comprehensive-documentation`

## Script Location
- Command: `~/.claude/commands/sc/update-superclaude-fork.md`
- Script: `~/.claude/scripts/fork_updater.sh`