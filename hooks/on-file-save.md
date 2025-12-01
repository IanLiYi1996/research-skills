---
event: file.save
name: auto-formatter
description: Automatically format and validate files on save
---

# Auto-Formatter Hook

Automatically format code and research files when saved.

## Trigger Event
- **Event**: file.save
- **File Types**: .py, .js, .ts, .md, .tex, .r

## Actions

### Python Files (.py)
1. Format with Black (if available)
2. Sort imports with isort (if available)
3. Check basic syntax
4. Update file timestamp

### JavaScript/TypeScript (.js, .ts)
1. Format with Prettier (if available)
2. Check basic syntax
3. Update file timestamp

### Markdown Files (.md)
1. Format with Prettier (if available)
2. Check for broken links (warn only)
3. Update table of contents (if markers present)

### LaTeX Files (.tex)
1. Check for common syntax errors
2. Validate citation references
3. Check for unclosed environments

### R Files (.r, .R)
1. Format with styler (if available)
2. Check basic syntax

## Configuration

Enable/disable formatting in plugin settings:
```json
{
  "hooks": {
    "auto-formatter": {
      "enabled": true,
      "python": true,
      "javascript": true,
      "markdown": true,
      "latex": true,
      "r": true
    }
  }
}
```

## Error Handling

If formatting fails:
1. Show error notification
2. Do not prevent file save
3. Log error for debugging
4. Allow user to fix manually

## Notes

- Formatting tools must be installed on system
- Non-blocking - won't prevent saves
- Can be disabled per file type
- Respects existing formatter configs (.black, .prettierrc, etc.)
