# Fetch Command

Fetch and retrieve content from web URLs.

## Purpose

Access online content for research:

- Fetch web pages and articles
- Download online resources
- Extract text from URLs
- Access API endpoints

## Usage

```bash
/fetch [action] [url] [options]
```

**Actions:**

- `url` - Fetch content from URL (default)
- `html` - Get raw HTML content
- `markdown` - Get content as markdown
- `text` - Get plain text only

## Fetch Examples

### Basic URL Fetch

```bash
/fetch https://example.com/research-paper
```

Fetches and displays the page content.

### Fetch as Markdown

```bash
/fetch markdown https://docs.python.org/3/tutorial/
```

Converts the page to readable markdown.

### Fetch Raw HTML

```bash
/fetch html https://arxiv.org/abs/2301.07041
```

Gets the raw HTML for parsing.

### Fetch Text Only

```bash
/fetch text https://en.wikipedia.org/wiki/Machine_learning
```

Extracts plain text without formatting.

## Options

| Option | Description | Example |
|--------|-------------|---------|
| `--timeout` | Request timeout in seconds | `--timeout 30` |
| `--headers` | Custom HTTP headers | `--headers "Auth: token"` |
| `--output` | Save to file | `--output page.md` |

## Common Use Cases

### Research Paper Access

```bash
# Fetch paper abstract page
/fetch https://arxiv.org/abs/2301.07041

# Fetch documentation
/fetch markdown https://pytorch.org/docs/stable/
```

### Data Repository Access

```bash
# Fetch dataset description
/fetch https://huggingface.co/datasets/imdb

# Fetch GitHub README
/fetch markdown https://github.com/user/repo
```

### API Data Retrieval

```bash
# Fetch JSON API
/fetch https://api.example.com/data.json
```

## Output Format

### Default Output

Returns formatted content with:

- Page title
- Main content
- Extracted links (if relevant)

### Markdown Output

Clean markdown with:

- Preserved headings
- Formatted lists
- Code blocks
- Links

### Text Output

Plain text with:

- No HTML tags
- Readable paragraphs
- Preserved structure

## Workflow Tips

1. **Use Markdown**: Best for documentation and articles
2. **Use Text**: Best for analysis and extraction
3. **Use HTML**: When you need to parse structure
4. **Check Status**: Verify successful fetch before processing

## Error Handling

Common errors and solutions:

| Error | Cause | Solution |
|-------|-------|----------|
| 404 | Page not found | Verify URL |
| 403 | Access denied | Check permissions |
| Timeout | Slow server | Increase timeout |
| SSL Error | Certificate issue | Verify HTTPS |

## Requirements

- `uv` tool installed
- Internet connection
- Target URL must be accessible
