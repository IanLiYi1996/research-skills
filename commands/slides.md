# Slides Command

Create, manage, and export presentations using Slidev or python-pptx.

## Purpose

Streamline presentation creation workflows:

- Generate slide outlines from topics
- Create Slidev Markdown presentations
- Generate python-pptx code for PPTX files
- Export presentations to various formats
- Convert between formats

## Usage

```
/slides [action] [arguments] [options]
```

**Actions:**

- `new` - Create new presentation
- `outline` - Generate presentation outline
- `export` - Export to PDF/PPTX/PNG
- `convert` - Convert between formats
- `template` - Apply or list templates

## Create New Presentation

### Slidev Presentation

```
/slides new slides.md --format slidev
```

Creates a new Slidev Markdown presentation with default structure.

### With Topic

```
/slides new slides.md --format slidev --topic "Machine Learning Basics"
```

Generates slides with content outline for the given topic.

### From Template

```
/slides new slides.md --format slidev --template academic
```

Available templates:

| Template | Description | Use Case |
|----------|-------------|----------|
| `academic` | Academic talk structure | Conference, thesis defense |
| `technical` | Tech demo format | Code walkthrough, architecture |
| `business` | Business presentation | Reports, proposals |
| `minimal` | Clean minimal design | Quick presentations |

### python-pptx Presentation

```
/slides new presentation.py --format pptx
```

Generates Python script to create PPTX file.

### With Data Source

```
/slides new presentation.py --format pptx --data results.csv
```

Creates data-driven presentation from CSV.

## Generate Outline

### Basic Outline

```
/slides outline "Introduction to Neural Networks"
```

Generates suggested slide structure for the topic.

### Academic Outline

```
/slides outline "My Research" --type academic --slides 15
```

Creates 15-slide academic presentation outline.

### Technical Outline

```
/slides outline "System Architecture" --type technical --slides 10
```

Creates technical demo outline.

### Output Format

```
/slides outline "Topic" --output outline.md
```

Saves outline to file.

## Export Presentation

### Slidev to PDF

```
/slides export slides.md --to pdf
```

Exports Slidev presentation to PDF.

### Slidev to PPTX

```
/slides export slides.md --to pptx
```

Exports Slidev to PowerPoint format.

### Export Options

```
/slides export slides.md --to pdf --dark --output presentation.pdf
```

Options:

| Option | Description |
|--------|-------------|
| `--dark` | Use dark theme |
| `--output <path>` | Custom output path |
| `--range 1-10` | Export specific slides |
| `--scale 2` | Export scale factor |

### Build Static Site

```
/slides export slides.md --to spa --output dist/
```

Builds static web app for hosting.

## Convert Formats

### Markdown to PPTX Code

```
/slides convert slides.md --to pptx-code
```

Generates python-pptx code from Slidev Markdown.

### Outline to Slides

```
/slides convert outline.md --to slidev
```

Converts outline document to Slidev presentation.

## Templates

### List Available Templates

```
/slides template list
```

Shows all available presentation templates.

### Apply Template

```
/slides template apply academic slides.md
```

Applies academic template to existing presentation.

### Template Details

```
/slides template info academic
```

Shows template structure and options.

## Options Reference

### Global Options

| Option | Description |
|--------|-------------|
| `--format <type>` | Output format: slidev, pptx |
| `--output <path>` | Output file path |
| `--verbose` | Show detailed output |

### New Command Options

| Option | Description |
|--------|-------------|
| `--topic <text>` | Presentation topic |
| `--template <name>` | Template to use |
| `--slides <n>` | Target number of slides |
| `--data <file>` | Data source file |

### Outline Options

| Option | Description |
|--------|-------------|
| `--type <type>` | academic, technical, business |
| `--slides <n>` | Number of slides |
| `--output <path>` | Save outline to file |

### Export Options

| Option | Description |
|--------|-------------|
| `--to <format>` | pdf, pptx, png, spa |
| `--dark` | Dark theme export |
| `--range <slides>` | Slide range (e.g., 1-10) |
| `--scale <n>` | Export scale |

## Examples

### Complete Slidev Workflow

```bash
# 1. Generate outline
/slides outline "Deep Learning Tutorial" --type technical --slides 12

# 2. Create presentation from outline
/slides new deep-learning.md --format slidev --topic "Deep Learning Tutorial"

# 3. Export to PDF
/slides export deep-learning.md --to pdf --output deep-learning.pdf
```

### Academic Presentation

```bash
# 1. Create academic presentation
/slides new defense.md --format slidev --template academic --topic "My PhD Research"

# 2. Export for conference
/slides export defense.md --to pdf

# 3. Also create PPTX backup
/slides export defense.md --to pptx
```

### Data-Driven Report

```bash
# 1. Generate python-pptx script
/slides new quarterly-report.py --format pptx --data q1-data.csv

# 2. Run script to generate PPTX
python quarterly-report.py
```

### Quick Technical Demo

```bash
# Create minimal tech demo
/slides new demo.md --format slidev --template minimal --topic "API Overview"
```

## Tips

1. **Start with Outline**: Use `/slides outline` first to plan structure
2. **Choose Right Format**: Slidev for code-heavy, PPTX for formal
3. **Use Templates**: Save time with pre-built structures
4. **Export Early**: Test PDF/PPTX output before finalizing
5. **Version Control**: Track .md files in git

## Related Resources

- Skill: `slidev-presentation` - Detailed Slidev syntax
- Skill: `pptx-generation` - python-pptx code patterns
- Agent: `presentation-creator` - Interactive presentation help
