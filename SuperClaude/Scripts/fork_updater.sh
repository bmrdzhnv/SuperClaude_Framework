#!/usr/bin/env bash

# SuperClaude Fork Updater Script
# Synchronizes fork with upstream and updates feature branches

set -euo pipefail

# Configuration
SUPERCLAUDE_FRAMEWORK_PATH="${SUPERCLAUDE_FRAMEWORK_PATH:-/Users/bm/Projects/GitHub/Sources/SuperClaude_Framework}"
UPSTREAM_REPO="SuperClaude-Org/SuperClaude_Framework"
FORK_REPO="bmrdzhnv/SuperClaude_Framework"
DEFAULT_BRANCH="master"
FEATURE_BRANCH="feature/comprehensive-documentation"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Parse arguments
DRY_RUN=false
USE_REBASE=false
FORCE_RESET=false
CUSTOM_PATH=""

while [[ $# -gt 0 ]]; do
    case $1 in
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --rebase)
            USE_REBASE=true
            shift
            ;;
        --force-reset)
            FORCE_RESET=true
            shift
            ;;
        --path)
            CUSTOM_PATH="$2"
            shift 2
            ;;
        *)
            echo -e "${RED}Unknown option: $1${NC}"
            exit 1
            ;;
    esac
done

# Override path if provided
if [[ -n "$CUSTOM_PATH" ]]; then
    SUPERCLAUDE_FRAMEWORK_PATH="$CUSTOM_PATH"
fi

# Functions
log_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

log_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

log_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

log_error() {
    echo -e "${RED}❌ $1${NC}"
}

run_command() {
    local cmd="$1"
    local description="${2:-Running command}"

    if [[ "$DRY_RUN" == true ]]; then
        echo -e "${YELLOW}[DRY RUN]${NC} Would execute: $cmd"
        return 0
    fi

    log_info "$description"
    if eval "$cmd"; then
        return 0
    else
        return $?
    fi
}

check_git_status() {
    if [[ -n "$(git status --porcelain)" ]]; then
        return 1
    else
        return 0
    fi
}

# Main execution
main() {
    log_info "SuperClaude Fork Updater"
    log_info "========================"

    # Change to repository directory
    if [[ ! -d "$SUPERCLAUDE_FRAMEWORK_PATH" ]]; then
        log_error "Repository path not found: $SUPERCLAUDE_FRAMEWORK_PATH"
        log_info "Set SUPERCLAUDE_FRAMEWORK_PATH environment variable or use --path option"
        exit 1
    fi

    cd "$SUPERCLAUDE_FRAMEWORK_PATH" || exit 1
    log_success "Changed to repository: $SUPERCLAUDE_FRAMEWORK_PATH"

    # Get current branch
    CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
    log_info "Current branch: $CURRENT_BRANCH"

    # Check for uncommitted changes
    STASH_CREATED=false
    if ! check_git_status; then
        log_warning "Uncommitted changes detected, stashing..."
        STASH_MSG="auto-stash for fork update $(date '+%Y-%m-%d %H:%M:%S')"
        run_command "git stash push -m '$STASH_MSG'" "Stashing changes"
        STASH_CREATED=true
    fi

    # Fetch all remotes
    log_info "Fetching remote changes..."
    run_command "git fetch --all" "Fetching all remotes"

    # Check if upstream is configured
    if ! git remote | grep -q "upstream"; then
        log_warning "Upstream remote not configured, adding..."
        run_command "git remote add upstream https://github.com/$UPSTREAM_REPO.git" "Adding upstream remote"
        run_command "git fetch upstream" "Fetching upstream"
    fi

    # Update fork's master branch
    log_info "Updating fork's $DEFAULT_BRANCH branch..."
    run_command "git checkout $DEFAULT_BRANCH" "Switching to $DEFAULT_BRANCH"

    if [[ "$FORCE_RESET" == true ]]; then
        log_warning "Force resetting $DEFAULT_BRANCH to upstream/$DEFAULT_BRANCH"
        run_command "git reset --hard upstream/$DEFAULT_BRANCH" "Resetting to upstream"

        if [[ "$DRY_RUN" == false ]]; then
            log_warning "Force pushing to origin (fork)..."
            if ! git push origin "$DEFAULT_BRANCH" --force-with-lease; then
                log_error "Failed to push to origin. You may need to use --force if --force-with-lease failed"
                exit 1
            fi
        fi
    else
        log_info "Merging upstream changes..."
        if ! run_command "git merge upstream/$DEFAULT_BRANCH --ff-only" "Fast-forward merge from upstream"; then
            log_error "Cannot fast-forward merge. You may need to use --force-reset"
            exit 1
        fi

        if [[ "$DRY_RUN" == false ]]; then
            run_command "git push origin $DEFAULT_BRANCH" "Pushing to fork"
        fi
    fi

    # Update feature branch
    log_info "Updating feature branch: $FEATURE_BRANCH"
    run_command "git checkout $FEATURE_BRANCH" "Switching to feature branch"

    # Perform merge or rebase
    if [[ "$USE_REBASE" == true ]]; then
        log_info "Rebasing onto $DEFAULT_BRANCH..."
        if [[ "$DRY_RUN" == false ]]; then
            if ! git rebase "$DEFAULT_BRANCH"; then
                log_error "Rebase conflicts detected!"
                log_warning "Resolve conflicts manually, then run:"
                echo "  git rebase --continue"
                echo "  git push origin $FEATURE_BRANCH --force-with-lease"

                # Check for open PRs
                if command -v gh &> /dev/null; then
                    PR_NUMBER=$(gh pr list --head "$FEATURE_BRANCH" --json number --jq '.[0].number' 2>/dev/null || echo "")
                    if [[ -n "$PR_NUMBER" ]]; then
                        log_warning "Open PR #$PR_NUMBER will need conflict resolution"
                    fi
                fi
                exit 1
            fi
        fi
    else
        log_info "Merging $DEFAULT_BRANCH..."
        if [[ "$DRY_RUN" == false ]]; then
            if ! git merge "$DEFAULT_BRANCH" --no-edit; then
                log_error "Merge conflicts detected!"
                log_warning "Resolve conflicts manually, then run:"
                echo "  git add ."
                echo "  git commit"
                echo "  git push origin $FEATURE_BRANCH"

                # Check for open PRs and comment
                if command -v gh &> /dev/null; then
                    PR_NUMBER=$(gh pr list --head "$FEATURE_BRANCH" --json number --jq '.[0].number' 2>/dev/null || echo "")
                    if [[ -n "$PR_NUMBER" ]]; then
                        log_warning "Commenting on PR #$PR_NUMBER about conflicts..."
                        gh pr comment "$PR_NUMBER" --body "⚠️ **Automated Fork Update Conflicts**

Fork sync from upstream detected conflicts in feature branch.
Manual resolution required before merge.

**Conflict Resolution Steps:**
1. \`cd $SUPERCLAUDE_FRAMEWORK_PATH\`
2. \`git status\` - Review conflicts
3. Resolve conflicts manually
4. \`git add . && git commit\`
5. \`git push origin $FEATURE_BRANCH\`

_Generated by /sc:update_superclaude_fork_"
                    fi
                fi
                exit 1
            fi
        fi
    fi

    # Push feature branch
    if [[ "$DRY_RUN" == false ]]; then
        log_info "Pushing feature branch..."
        if [[ "$USE_REBASE" == true ]]; then
            run_command "git push origin $FEATURE_BRANCH --force-with-lease" "Pushing rebased branch"
        else
            run_command "git push origin $FEATURE_BRANCH" "Pushing merged branch"
        fi
    fi

    # Restore stash if created
    if [[ "$STASH_CREATED" == true ]]; then
        log_info "Restoring stashed changes..."
        if [[ "$DRY_RUN" == false ]]; then
            if ! git stash pop; then
                log_error "Stash pop conflicts detected!"
                log_warning "Your changes are still in stash. To recover:"
                echo "  git stash list  # Find your stash"
                echo "  git stash pop   # Try again after resolving"
                exit 1
            fi
        fi
    fi

    # Summary
    log_success "Fork update completed successfully!"
    if [[ "$DRY_RUN" == true ]]; then
        log_warning "This was a dry run. No changes were made."
    else
        log_info "Your fork is now synchronized with upstream"
        log_info "Feature branch '$FEATURE_BRANCH' is up to date"
    fi
}

# Run main function
main