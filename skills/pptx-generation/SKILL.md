---
name: pptx-generation
description: Python-pptx presentation generation skill for programmatically creating PowerPoint files. Use when generating PPTX slides from data, creating templated reports, batch processing presentations, or requiring fine-grained control over slide layout. Keywords include python-pptx, PowerPoint, PPTX generation, automated slides, batch presentation, programmatic slides.
---

# Python-pptx Generation Skill

This skill enables programmatic creation of PowerPoint presentations using the python-pptx library, ideal for automated report generation and data-driven slides.

## Core Capabilities

### 1. Slide Creation

- Create presentations from scratch
- Add slides with various layouts
- Insert text, images, tables, charts
- Control positioning and sizing

### 2. Template Support

- Use existing PPTX templates
- Apply master slides
- Maintain corporate branding
- Reuse slide layouts

### 3. Batch Processing

- Generate multiple presentations
- Data-driven slide content
- Automated report creation
- Loop-based slide generation

### 4. Fine-Grained Control

- Precise positioning (inches/cm)
- Font and color customization
- Shape and object manipulation
- Paragraph and run formatting

## Installation

```bash
pip install python-pptx
```

## Basic Usage

### Create Empty Presentation

```python
from pptx import Presentation

# Create new presentation
prs = Presentation()

# Add title slide
slide_layout = prs.slide_layouts[0]  # Title Slide layout
slide = prs.slides.add_slide(slide_layout)

title = slide.shapes.title
subtitle = slide.placeholders[1]

title.text = "My Presentation"
subtitle.text = "Created with python-pptx"

# Save
prs.save('presentation.pptx')
```

### Use Existing Template

```python
from pptx import Presentation

# Load template
prs = Presentation('template.pptx')

# Add slide using template layout
slide_layout = prs.slide_layouts[1]  # Title and Content
slide = prs.slides.add_slide(slide_layout)

# Save as new file
prs.save('new_presentation.pptx')
```

## Slide Layouts

Standard PowerPoint layouts (indices may vary by template):

| Index | Layout Name | Description |
|-------|-------------|-------------|
| 0 | Title Slide | Title and subtitle |
| 1 | Title and Content | Title with body |
| 2 | Section Header | Section divider |
| 3 | Two Content | Two column content |
| 4 | Comparison | Side-by-side comparison |
| 5 | Title Only | Title without content |
| 6 | Blank | Empty slide |
| 7 | Content with Caption | Content and caption |
| 8 | Picture with Caption | Image and caption |

## Working with Text

### Add Text Box

```python
from pptx.util import Inches, Pt
from pptx.dml.color import RgbColor

slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank

# Add text box
left = Inches(1)
top = Inches(1)
width = Inches(8)
height = Inches(1)

txBox = slide.shapes.add_textbox(left, top, width, height)
tf = txBox.text_frame

# Add paragraph
p = tf.paragraphs[0]
p.text = "Hello, World!"
p.font.size = Pt(24)
p.font.bold = True
p.font.color.rgb = RgbColor(0x00, 0x66, 0xCC)
```

### Multiple Paragraphs

```python
from pptx.enum.text import PP_ALIGN

tf = txBox.text_frame
tf.word_wrap = True

p = tf.paragraphs[0]
p.text = "First paragraph"
p.alignment = PP_ALIGN.LEFT

p = tf.add_paragraph()
p.text = "Second paragraph"
p.level = 1  # Indentation level
```

## Working with Images

### Add Image

```python
from pptx.util import Inches

slide = prs.slides.add_slide(prs.slide_layouts[6])

# Add image with position and size
left = Inches(1)
top = Inches(2)
width = Inches(4)
# Height auto-calculated to maintain aspect ratio

slide.shapes.add_picture('image.png', left, top, width=width)
```

### Add Image from URL

```python
import requests
from io import BytesIO
from pptx.util import Inches

# Download image
response = requests.get('https://example.com/image.png')
image_stream = BytesIO(response.content)

# Add to slide
slide.shapes.add_picture(image_stream, Inches(1), Inches(1), width=Inches(4))
```

## Working with Tables

### Create Table

```python
from pptx.util import Inches, Pt

slide = prs.slides.add_slide(prs.slide_layouts[6])

# Define table dimensions
rows = 4
cols = 3
left = Inches(1)
top = Inches(2)
width = Inches(8)
height = Inches(2)

table = slide.shapes.add_table(rows, cols, left, top, width, height).table

# Set column widths
table.columns[0].width = Inches(2)
table.columns[1].width = Inches(3)
table.columns[2].width = Inches(3)

# Add header row
table.cell(0, 0).text = "Name"
table.cell(0, 1).text = "Value"
table.cell(0, 2).text = "Description"

# Add data rows
data = [
    ("Item 1", "100", "First item"),
    ("Item 2", "200", "Second item"),
    ("Item 3", "300", "Third item"),
]

for row_idx, (name, value, desc) in enumerate(data, start=1):
    table.cell(row_idx, 0).text = name
    table.cell(row_idx, 1).text = value
    table.cell(row_idx, 2).text = desc
```

### Style Table Cells

```python
from pptx.dml.color import RgbColor
from pptx.enum.text import PP_ALIGN

cell = table.cell(0, 0)
cell.text = "Header"

# Access paragraph
paragraph = cell.text_frame.paragraphs[0]
paragraph.font.bold = True
paragraph.font.size = Pt(14)
paragraph.alignment = PP_ALIGN.CENTER

# Cell background
cell.fill.solid()
cell.fill.fore_color.rgb = RgbColor(0x00, 0x66, 0xCC)
```

## Working with Charts

### Add Column Chart

```python
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE
from pptx.util import Inches

slide = prs.slides.add_slide(prs.slide_layouts[6])

# Prepare data
chart_data = CategoryChartData()
chart_data.categories = ['Q1', 'Q2', 'Q3', 'Q4']
chart_data.add_series('Revenue', (100, 150, 200, 180))
chart_data.add_series('Profit', (20, 35, 50, 40))

# Add chart
x, y, cx, cy = Inches(1), Inches(2), Inches(8), Inches(4)
chart = slide.shapes.add_chart(
    XL_CHART_TYPE.COLUMN_CLUSTERED, x, y, cx, cy, chart_data
).chart

# Customize
chart.has_legend = True
chart.legend.include_in_layout = False
```

### Chart Types

| Type | Constant |
|------|----------|
| Column | `XL_CHART_TYPE.COLUMN_CLUSTERED` |
| Bar | `XL_CHART_TYPE.BAR_CLUSTERED` |
| Line | `XL_CHART_TYPE.LINE` |
| Pie | `XL_CHART_TYPE.PIE` |
| Area | `XL_CHART_TYPE.AREA` |
| Scatter | `XL_CHART_TYPE.XY_SCATTER` |

## Shapes and Objects

### Add Shape

```python
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches

slide = prs.slides.add_slide(prs.slide_layouts[6])

# Add rectangle
shape = slide.shapes.add_shape(
    MSO_SHAPE.RECTANGLE,
    Inches(1), Inches(1),  # left, top
    Inches(3), Inches(1)   # width, height
)

# Customize
shape.fill.solid()
shape.fill.fore_color.rgb = RgbColor(0xFF, 0x99, 0x00)
shape.line.color.rgb = RgbColor(0x00, 0x00, 0x00)

# Add text to shape
shape.text = "Important!"
```

## Batch Generation Example

### Generate Reports from Data

```python
from pptx import Presentation
from pptx.util import Inches, Pt
import pandas as pd

def create_report(data: dict, template_path: str, output_path: str):
    """Generate presentation from data dictionary."""
    prs = Presentation(template_path)

    # Title slide
    slide = prs.slides[0]
    slide.shapes.title.text = data['title']
    slide.placeholders[1].text = data['date']

    # Add content slides
    for section in data['sections']:
        slide = prs.slides.add_slide(prs.slide_layouts[1])
        slide.shapes.title.text = section['title']

        body = slide.shapes.placeholders[1].text_frame
        for point in section['points']:
            p = body.add_paragraph()
            p.text = point
            p.level = 0

    prs.save(output_path)

# Usage
reports_data = [
    {
        'title': 'Q1 Report',
        'date': 'March 2024',
        'sections': [
            {'title': 'Summary', 'points': ['Revenue up 15%', 'New clients: 12']},
            {'title': 'Challenges', 'points': ['Supply chain delays', 'Hiring']},
        ]
    },
    # More reports...
]

for i, data in enumerate(reports_data):
    create_report(data, 'template.pptx', f'report_{i+1}.pptx')
```

## Best Practices

1. **Use Templates**: Start with a branded template
2. **Consistent Units**: Stick to Inches or Emu throughout
3. **Error Handling**: Wrap file operations in try/except
4. **Memory Management**: Close presentations when done
5. **Test Output**: Open generated files to verify
6. **Version Control**: Track template and script separately

## Common Patterns

### Slide Factory Function

```python
def add_title_content_slide(prs, title: str, bullets: list) -> None:
    """Add a standard title + bullet points slide."""
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = title

    body = slide.shapes.placeholders[1].text_frame
    body.paragraphs[0].text = bullets[0]

    for bullet in bullets[1:]:
        p = body.add_paragraph()
        p.text = bullet
        p.level = 0
```

### Data Table from DataFrame

```python
def add_dataframe_table(slide, df: pd.DataFrame, position: tuple) -> None:
    """Add pandas DataFrame as table."""
    rows, cols = df.shape
    rows += 1  # Header row

    left, top, width, height = position
    table = slide.shapes.add_table(rows, cols, left, top, width, height).table

    # Headers
    for col_idx, col_name in enumerate(df.columns):
        table.cell(0, col_idx).text = str(col_name)

    # Data
    for row_idx, row in enumerate(df.itertuples(index=False), start=1):
        for col_idx, value in enumerate(row):
            table.cell(row_idx, col_idx).text = str(value)
```

## Integration with Other Skills

- **data-visualization**: Generate charts for slides
- **academic-research**: Create literature review presentations
- **experiment-tracking**: Auto-generate experiment reports
- **presentation-creator**: Use agent for content planning
