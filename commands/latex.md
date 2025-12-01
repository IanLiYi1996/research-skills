# LaTeX Paper Command

Create, format, and manage LaTeX documents for academic paper writing.

## Purpose

Assist with LaTeX document preparation:
- Create new papers from templates
- Format mathematical equations
- Generate tables and figures
- Manage bibliography entries
- Troubleshoot compilation errors

## Usage

```
/latex [action] [arguments] [options]
```

**Actions:**
- `new` - Create new document from template
- `equation` - Generate mathematical equations
- `table` - Create formatted tables
- `figure` - Generate figure environments
- `bib` - Create bibliography entries
- `check` - Check document for common issues

## Create New Document

### From Generic Template
```
/latex new paper.tex
```
Creates a new paper using the generic article template.

### From IEEE Template
```
/latex new paper.tex --template ieee
```
Creates IEEE conference/journal paper.

### From ACM Template
```
/latex new paper.tex --template acm
```
Creates ACM publication format paper.

### Available Templates

| Template | Description | Use Case |
|----------|-------------|----------|
| `generic` | Standard article format | General papers, preprints |
| `ieee` | IEEE two-column format | IEEE transactions, conferences |
| `acm` | ACM publication format | ACM conferences, journals |

## Generate Equations

### Inline Equation
```
/latex equation "E = mc^2" --inline
```
Output: `$E = mc^2$`

### Display Equation
```
/latex equation "E = mc^2" --display
```
Output:
```latex
\begin{equation}
    E = mc^2
    \label{eq:einstein}
\end{equation}
```

### Multi-line Aligned
```
/latex equation "a = b + c, d = e + f" --align
```
Output:
```latex
\begin{align}
    a &= b + c \\
    d &= e + f
\end{align}
```

### Matrix
```
/latex equation --matrix 2x2 "a,b,c,d"
```
Output:
```latex
\begin{bmatrix}
    a & b \\
    c & d
\end{bmatrix}
```

## Generate Tables

### Basic Table
```
/latex table --cols 3 --rows 4 --header "Method,Accuracy,Time"
```
Creates a 3-column, 4-row table with headers.

### From CSV
```
/latex table data.csv --booktabs
```
Converts CSV to LaTeX table with booktabs formatting.

### With Caption
```
/latex table --cols 2 --caption "Results comparison" --label tab:results
```

## Generate Figures

### Single Figure
```
/latex figure image.pdf --width 0.8 --caption "Results" --label fig:results
```
Output:
```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.8\textwidth]{image.pdf}
    \caption{Results}
    \label{fig:results}
\end{figure}
```

### Subfigures
```
/latex figure img1.pdf img2.pdf --subfigures --caption "Comparison"
```

## Bibliography Entries

### Create BibTeX Entry
```
/latex bib --type article --author "Smith, John" --title "Paper Title" --year 2024 --journal "Nature"
```
Output:
```bibtex
@article{smith2024paper,
    author = {Smith, John},
    title = {Paper Title},
    journal = {Nature},
    year = {2024}
}
```

### Entry Types
- `article` - Journal article
- `inproceedings` - Conference paper
- `book` - Book
- `incollection` - Book chapter
- `techreport` - Technical report
- `misc` - Other

## Check Document

### Check for Common Issues
```
/latex check paper.tex
```
Checks for:
- Missing labels
- Undefined references
- Common syntax errors
- Package conflicts
- Overfull/underfull boxes

### Verbose Check
```
/latex check paper.tex --verbose
```
Shows detailed diagnostics.

## Options Reference

### Template Options
| Option | Description |
|--------|-------------|
| `--template <type>` | Template: generic, ieee, acm |
| `--output <path>` | Output file path |

### Equation Options
| Option | Description |
|--------|-------------|
| `--inline` | Inline math mode |
| `--display` | Display equation |
| `--align` | Aligned equations |
| `--matrix <size>` | Matrix (e.g., 2x2, 3x3) |
| `--label <name>` | Equation label |

### Table Options
| Option | Description |
|--------|-------------|
| `--cols <n>` | Number of columns |
| `--rows <n>` | Number of rows |
| `--header <text>` | Column headers (comma-separated) |
| `--booktabs` | Use booktabs style |
| `--caption <text>` | Table caption |
| `--label <name>` | Table label |

### Figure Options
| Option | Description |
|--------|-------------|
| `--width <ratio>` | Width relative to textwidth |
| `--caption <text>` | Figure caption |
| `--label <name>` | Figure label |
| `--subfigures` | Create subfigure layout |
| `--placement <spec>` | Float placement (htbp) |

### Bibliography Options
| Option | Description |
|--------|-------------|
| `--type <type>` | Entry type |
| `--author <name>` | Author(s) |
| `--title <text>` | Title |
| `--year <year>` | Publication year |
| `--journal <name>` | Journal name |
| `--booktitle <name>` | Conference/book name |

## Examples

### Complete Workflow
```bash
# 1. Create new IEEE paper
/latex new my-paper.tex --template ieee

# 2. Add an equation
/latex equation "\sum_{i=1}^n x_i = \mu n" --display --label eq:sum

# 3. Create results table
/latex table results.csv --booktabs --caption "Experimental Results" --label tab:results

# 4. Add figure
/latex figure results.pdf --width 0.9 --caption "Performance comparison" --label fig:perf

# 5. Generate bibliography entry
/latex bib --type inproceedings --author "Doe, Jane" --title "My Paper" --booktitle "ICML 2024" --year 2024

# 6. Check document
/latex check my-paper.tex
```

## Tips

1. **Use templates** - Start with appropriate publisher template
2. **Label everything** - Add labels to equations, figures, tables
3. **Compile often** - Check for errors incrementally
4. **Use booktabs** - For professional-looking tables
5. **Vector graphics** - Prefer PDF/EPS over PNG/JPG for figures

## Related Resources

- Templates: `skills/latex-writing/assets/`
- Cheatsheet: `skills/latex-writing/references/latex-cheatsheet.md`
- Agent: Use `latex-expert` for interactive help
