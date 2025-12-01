# Git Command

Manage Git repositories for research projects.

## Purpose

Version control for research:

- Track code and document changes
- View project history
- Manage branches and versions
- Ensure reproducibility

## Usage

```bash
/git [action] [arguments] [options]
```

**Actions:**

- `status` - Show repository status
- `log` - View commit history
- `diff` - Show changes
- `branch` - List/manage branches
- `show` - Show commit details

## Status Examples

### Check Repository Status

```bash
/git status
```

Shows modified, staged, and untracked files.

## Log Examples

### View Recent Commits

```bash
/git log
```

Shows recent commit history.

### View Specific Number of Commits

```bash
/git log --limit 10
```

Shows last 10 commits.

### Search Commit Messages

```bash
/git log --search "experiment"
```

Finds commits mentioning "experiment".

## Diff Examples

### Show Unstaged Changes

```bash
/git diff
```

Shows all uncommitted changes.

### Compare Branches

```bash
/git diff main..feature/experiment
```

Shows differences between branches.

### Diff Specific File

```bash
/git diff analysis.py
```

Shows changes in specific file.

## Branch Examples

### List All Branches

```bash
/git branch
```

Shows local branches.

### Show Current Branch

```bash
/git branch --current
```

Shows active branch name.

## Show Examples

### Show Commit Details

```bash
/git show abc123
```

Shows full commit information.

### Show Latest Commit

```bash
/git show HEAD
```

Shows most recent commit.

## Options

| Option | Description | Example |
|--------|-------------|---------|
| `--limit` | Number of results | `--limit 20` |
| `--search` | Search in messages | `--search "fix"` |
| `--author` | Filter by author | `--author "John"` |
| `--file` | Specific file | `--file src/model.py` |

## Research Workflows

### Before Starting Work

```bash
# Check current state
/git status

# See recent changes
/git log --limit 5
```

### Track Experiment Progress

```bash
# Check what's changed
/git diff

# View experiment branch
/git log --search "experiment"
```

### Prepare for Publication

```bash
# Review all changes
/git diff main..submission

# Check commit history
/git log --limit 20
```

## Output Format

### Status Output

```
Branch: main
Modified: 3 files
Staged: 1 file
Untracked: 2 files
```

### Log Output

For each commit:

- Commit hash
- Author
- Date
- Message

### Diff Output

- File paths
- Line changes (+/-)
- Context lines

## Common Patterns

### Daily Research Workflow

1. `/git status` - Check state
2. Make changes
3. `/git diff` - Review changes
4. Commit work

### Experiment Tracking

1. `/git branch` - List experiments
2. `/git log --search "exp"` - Find experiment commits
3. `/git show <hash>` - View details

### Paper Submission

1. `/git log --limit 50` - Review history
2. `/git diff submission-v1..HEAD` - See changes since submission
3. Tag new version

## Environment Setup

Set repository path (optional):

```bash
export RESEARCH_GIT_PATH=/path/to/repo
```

Default: Current directory

## Requirements

- `uv` tool installed
- Git repository initialized
- Repository path configured
