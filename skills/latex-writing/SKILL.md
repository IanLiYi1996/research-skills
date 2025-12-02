---
name: latex-writing
description: LaTeX academic writing skill for creating professionally formatted research papers, theses, and scientific documents. Use when writing LaTeX documents, formatting journal submissions, typesetting mathematical equations, creating tables and figures, managing bibliographies, or preparing camera-ready papers. Keywords include LaTeX, TeX, typesetting, paper formatting, journal template, IEEE, ACM, Springer, BibTeX, equations, thesis.
---

# LaTeX Writing Skill

This skill provides comprehensive tools and templates for LaTeX document preparation and academic paper formatting.

## Core Capabilities

### 1. Document Preparation
Create professionally formatted academic documents:
- Research papers and journal articles
- Conference submissions
- Theses and dissertations
- Technical reports
- Preprints for arXiv

### 2. Mathematical Typesetting
Expert-level mathematical equation formatting:
- Inline and display equations
- Multi-line equation environments
- Matrices, vectors, and arrays
- Custom mathematical operators
- Theorem environments

### 3. Journal Formatting
Format papers for major publishers:
- IEEE (transactions, conferences, letters)
- ACM (SIGPLAN, SIGCHI, etc.)
- Springer (LNCS, journals)
- Elsevier journals
- Nature and Science family

### 4. Bibliography Management
Professional reference management:
- BibTeX database creation
- Multiple citation styles
- Author-year and numeric formats
- Bibliography customization

## Bundled Resources

### Templates

Use templates in `assets/` for quick start:

#### Generic Paper Template
```bash
# Copy generic template
cp skills/latex-writing/assets/paper-template-generic.tex my-paper.tex
```
Basic article structure with common packages and examples.

#### IEEE Template
```bash
cp skills/latex-writing/assets/paper-template-ieee.tex ieee-paper.tex
```
IEEE two-column format for transactions and conferences.

#### ACM Template
```bash
cp skills/latex-writing/assets/paper-template-acm.tex acm-paper.tex
```
ACM publication format.

### References

Consult `references/latex-cheatsheet.md` for:
- Mathematical notation standards (scalar, vector, matrix conventions)
- Common LaTeX commands and symbols
- Non-breaking spaces and quotation marks
- Citation commands (cite, citep, citet)
- Three-line tables with booktabs
- Pre-submission checklist

Consult `references/paper-writing-tips.md` for:
- Comprehensive mathematical symbol conventions
- Formula best practices (brackets, alignment, numbering)
- Table and figure design guidelines
- Writing style rules (avoiding contractions, absolute statements)
- Latin expressions usage (e.g., i.e., et al.)
- Pre-submission checklist (detailed)
- External tools and resources

## Workflow Patterns

### New Paper Workflow

1. **Choose Template**: Select appropriate template for target venue
2. **Set Up Structure**: Define sections and create outline
3. **Write Content**: Fill in sections with text and equations
4. **Add Figures/Tables**: Include visualizations
5. **Manage References**: Build BibTeX database
6. **Format and Polish**: Adjust formatting, fix warnings
7. **Final Review**: Check compilation, output quality

### Journal Submission Workflow

1. **Download Official Template**: Get publisher's template
2. **Adapt Content**: Transfer content to template
3. **Format Figures**: Ensure resolution and format requirements
4. **Check References**: Verify citation format
5. **Run Checks**: Compile multiple times for references
6. **Generate Output**: Create camera-ready PDF

## Best Practices

1. **Use Version Control**: Track changes with Git
2. **Modular Files**: Split large documents into sections
3. **Compile Frequently**: Catch errors early
4. **Comment Code**: Document complex LaTeX constructs
5. **Backup BibTeX**: Keep bibliography files safe
6. **Test Output**: Check PDF on multiple viewers

## Common Commands

### Document Structure
```latex
\documentclass[options]{class}
\usepackage{package}
\begin{document}
\maketitle
\section{Title}
\end{document}
```

### Mathematics
```latex
% Inline
$E = mc^2$

% Display
\begin{equation}
    \int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}
\end{equation}

% Aligned equations
\begin{align}
    a &= b + c \\
    d &= e + f
\end{align}
```

### Figures
```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.8\textwidth]{figure.pdf}
    \caption{Figure caption.}
    \label{fig:example}
\end{figure}
```

### Tables
```latex
\begin{table}[htbp]
    \centering
    \caption{Table caption.}
    \begin{tabular}{lcc}
        \toprule
        Header 1 & Header 2 & Header 3 \\
        \midrule
        Data 1 & Data 2 & Data 3 \\
        \bottomrule
    \end{tabular}
    \label{tab:example}
\end{table}
```

### Citations
```latex
\cite{key}      % Basic citation
\citep{key}     % Parenthetical (natbib)
\citet{key}     % Textual (natbib)
```

## Integration with Other Skills

- **academic-research**: Use literature review outputs as paper content
- **academic-writing**: Combine writing guidance with LaTeX formatting
- **data-visualization**: Export figures for LaTeX inclusion

## Requirements

- LaTeX distribution (TeX Live, MiKTeX, or MacTeX)
- PDF viewer for output review
- Text editor with LaTeX support (recommended)
