# LaTeX Cheatsheet

Quick reference for common LaTeX commands and patterns.

## Mathematical Notation Standards

### Symbol Conventions

| Type | Convention | Example |
|------|------------|---------|
| Scalar | lowercase italic | $x$, $y$, `\ell` (not `l`) |
| Vector | lowercase bold | `\mathbf{x}`, `\boldsymbol{\theta}` |
| Matrix | uppercase bold | `\mathbf{A}`, `\mathbf{W}` |
| Set | calligraphic | `\mathcal{D}`, `\mathcal{X}` |
| Number field | blackboard | `\mathbb{R}`, `\mathbb{E}`, `\mathbb{N}` |

### Multi-letter Operators

```latex
% Use upright font for multi-letter names
\textrm{softmax}(x)
\textrm{ReLU}(x)

% Or define custom operators
\DeclareMathOperator{\softmax}{softmax}
```

### Bracket Matching

```latex
% Auto-sized brackets
\left( \sum_{i=1}^n x_i \right)
\left\{ x \middle| x > 0 \right\}
```

---

## Document Structure

```latex
\documentclass[options]{class}   % article, report, book, beamer
\usepackage{package}             % Load packages
\begin{document}
    Content here
\end{document}
```

### Common Document Classes

| Class | Use Case |
|-------|----------|
| `article` | Short documents, papers |
| `report` | Longer documents with chapters |
| `book` | Books, theses |
| `beamer` | Presentations |
| `IEEEtran` | IEEE papers |
| `acmart` | ACM papers |

## Text Formatting

```latex
\textbf{bold}           % Bold
\textit{italic}         % Italic
\underline{underlined}  % Underlined
\texttt{monospace}      % Typewriter/code
\textsf{sans serif}     % Sans serif
\textsc{Small Caps}     % Small capitals
```

## Sectioning

```latex
\part{Part Title}           % (book, report)
\chapter{Chapter Title}     % (book, report)
\section{Section}
\subsection{Subsection}
\subsubsection{Subsubsection}
\paragraph{Paragraph}
\subparagraph{Subparagraph}
```

## Lists

```latex
% Bulleted list
\begin{itemize}
    \item First item
    \item Second item
\end{itemize}

% Numbered list
\begin{enumerate}
    \item First item
    \item Second item
\end{enumerate}

% Description list
\begin{description}
    \item[Term 1] Definition 1
    \item[Term 2] Definition 2
\end{description}
```

## Mathematics

### Inline vs Display

```latex
Inline math: $E = mc^2$

Display math:
\[ E = mc^2 \]

% or
\begin{equation}
    E = mc^2
    \label{eq:einstein}
\end{equation}
```

### Common Symbols

| Symbol | Code | Symbol | Code |
|--------|------|--------|------|
| $\alpha$ | `\alpha` | $\beta$ | `\beta` |
| $\gamma$ | `\gamma` | $\delta$ | `\delta` |
| $\epsilon$ | `\epsilon` | $\theta$ | `\theta` |
| $\lambda$ | `\lambda` | $\mu$ | `\mu` |
| $\pi$ | `\pi` | $\sigma$ | `\sigma` |
| $\phi$ | `\phi` | $\omega$ | `\omega` |
| $\infty$ | `\infty` | $\partial$ | `\partial` |
| $\nabla$ | `\nabla` | $\sum$ | `\sum` |
| $\prod$ | `\prod` | $\int$ | `\int` |
| $\sqrt{x}$ | `\sqrt{x}` | $\frac{a}{b}$ | `\frac{a}{b}` |

### Relations and Operators

| Symbol | Code | Symbol | Code |
|--------|------|--------|------|
| $\leq$ | `\leq` | $\geq$ | `\geq` |
| $\neq$ | `\neq` | $\approx$ | `\approx` |
| $\equiv$ | `\equiv` | $\sim$ | `\sim` |
| $\subset$ | `\subset` | $\supset$ | `\supset` |
| $\in$ | `\in` | $\notin$ | `\notin` |
| $\cup$ | `\cup` | $\cap$ | `\cap` |
| $\times$ | `\times` | $\cdot$ | `\cdot` |
| $\pm$ | `\pm` | $\mp$ | `\mp` |

### Fractions and Roots

```latex
\frac{numerator}{denominator}   % Fraction
\dfrac{a}{b}                    % Display-style fraction
\tfrac{a}{b}                    % Text-style fraction
\sqrt{x}                        % Square root
\sqrt[n]{x}                     % n-th root
```

### Subscripts and Superscripts

```latex
x^2         % Superscript
x_i         % Subscript
x_i^2       % Both
x_{ij}      % Multi-character subscript
x^{n+1}     % Multi-character superscript
```

### Sums, Products, Integrals

```latex
\sum_{i=1}^{n} x_i              % Sum
\prod_{i=1}^{n} x_i             % Product
\int_a^b f(x) dx                % Integral
\iint, \iiint, \oint            % Double, triple, contour
\lim_{x \to \infty} f(x)        % Limit
```

### Matrices

```latex
\begin{pmatrix}                 % Parentheses
    a & b \\
    c & d
\end{pmatrix}

\begin{bmatrix}                 % Brackets
    a & b \\
    c & d
\end{bmatrix}

\begin{vmatrix}                 % Vertical bars (determinant)
    a & b \\
    c & d
\end{vmatrix}
```

### Multi-line Equations

```latex
% Aligned at &
\begin{align}
    a &= b + c \\
    d &= e + f
\end{align}

% No alignment
\begin{gather}
    a = b + c \\
    d = e + f
\end{gather}

% Split single equation
\begin{equation}
\begin{split}
    a &= b + c \\
      &= d + e
\end{split}
\end{equation}
```

## Figures

```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.8\textwidth]{filename.pdf}
    \caption{Figure caption.}
    \label{fig:label}
\end{figure}

% Reference: Figure~\ref{fig:label}
```

### Placement Options

| Option | Meaning |
|--------|---------|
| `h` | Here (approximately) |
| `t` | Top of page |
| `b` | Bottom of page |
| `p` | Separate page |
| `!` | Override restrictions |
| `H` | Exactly here (float pkg) |

## Tables

```latex
\begin{table}[htbp]
    \centering
    \caption{Table caption.}
    \label{tab:label}
    \begin{tabular}{lcc}
        \toprule
        Header 1 & Header 2 & Header 3 \\
        \midrule
        Data 1 & Data 2 & Data 3 \\
        Data 4 & Data 5 & Data 6 \\
        \bottomrule
    \end{tabular}
\end{table}
```

### Column Alignment

| Specifier | Meaning |
|-----------|---------|
| `l` | Left-aligned |
| `c` | Centered |
| `r` | Right-aligned |
| `p{width}` | Paragraph with fixed width |
| `|` | Vertical line |

## Citations and References

```latex
% In preamble
\bibliographystyle{plain}       % or plainnat, ieeetr, acm, etc.

% In document
\cite{key}                      % Basic citation
\cite{key1,key2}                % Multiple citations

% With natbib
\citep{key}                     % Parenthetical (Author, Year)
\citet{key}                     % Textual: Author (Year)
\citep[p.~5]{key}               % With page number

% At end
\bibliography{references}        % references.bib file
```

## Cross-References

```latex
\label{sec:intro}               % Create label
\ref{sec:intro}                 % Reference number
\pageref{sec:intro}             % Page number
\eqref{eq:formula}              % Equation reference with parentheses

% With cleveref package
\cref{fig:example}              % "Figure 1"
\Cref{fig:example}              % "Figure 1" (capitalized)
```

## Essential Packages

```latex
% Math
\usepackage{amsmath,amssymb,amsthm}

% Graphics
\usepackage{graphicx}

% Tables
\usepackage{booktabs}           % Professional tables

% Typography
\usepackage{microtype}          % Subtle improvements

% Links
\usepackage{hyperref}           % Clickable links

% Colors
\usepackage{xcolor}

% Code listings
\usepackage{listings}

% Units
\usepackage{siunitx}

% References
\usepackage{cleveref}
```

## Common Errors and Solutions

### Error: Undefined control sequence

**Cause**: Command not defined or package not loaded

**Solution**: Check spelling, load required package

### Error: Missing $ inserted

**Cause**: Math symbol outside math mode

**Solution**: Use `$...$` or `\(...\)` around math

### Error: Overfull hbox

**Cause**: Text too wide for line

**Solution**: Reword, use `\sloppy`, or adjust hyphenation

### Error: Float specifier changed to `!htbp`

**Cause**: Invalid float specifier

**Solution**: Use valid options: h, t, b, p

### Bibliography not showing

**Cause**: Missing bibtex run or citations

**Solution**: Run: pdflatex -> bibtex -> pdflatex -> pdflatex

## Compilation Commands

```bash
# Basic compilation
pdflatex document.tex

# With bibliography
pdflatex document.tex
bibtex document
pdflatex document.tex
pdflatex document.tex

# With latexmk (recommended)
latexmk -pdf document.tex
```

## Non-breaking Spaces (~)

Use `~` to prevent unwanted line breaks:

```latex
Figure~\ref{fig:model}
Table~\ref{tab:results}
Section~\ref{sec:intro}
Equation~\eqref{eq:loss}
BERT~\cite{bert}
```

## English Quotation Marks

```latex
% Correct - use backticks and apostrophes
``double quotes''
`single quotes'

% Wrong - don't use straight quotes
"straight quotes"
```

## Citation Commands (natbib)

| Command | Usage | Output |
|---------|-------|--------|
| `\cite{key}` | Basic | [1] or (Author, 2020) |
| `\citet{key}` | In-text (subject) | Author et al. (2020) |
| `\citep{key}` | Parenthetical | (Author et al., 2020) |

```latex
% As sentence subject - use \citet
\citet{bert} propose a pre-trained model.

% Not as subject - use \citep
Pre-trained models show great success~\citep{bert}.
```

## Three-line Table (Booktabs)

```latex
% No vertical lines! Only horizontal rules.
\begin{tabular}{lcc}
    \toprule
    Method & Accuracy & F1 \\
    \midrule
    Baseline & 85.2 & 84.1 \\
    Ours & \textbf{89.3} & \textbf{88.7} \\
    \bottomrule
\end{tabular}
```

---

## Useful Tips

1. **Compile often** to catch errors early
2. **Use comments** `%` to document your code
3. **Use `~`** for non-breaking spaces before `\cite` and `\ref`
4. **Prefer vector graphics** (PDF, EPS) over raster (PNG, JPG)
5. **Use booktabs** for professional tables
6. **Use cleveref** for smart cross-references
7. **Keep backups** of your `.tex` and `.bib` files
8. **Avoid contractions** in formal writing (don't → do not)
9. **Use `\ell`** instead of `l` to avoid confusion with `1`
10. **Number only referenced equations** using `\nonumber`

## Pre-submission Checklist

- [ ] Anonymous (no personal/institution info)
- [ ] Within page limit
- [ ] All figures/tables have labels and references
- [ ] Citations format is consistent
- [ ] No compilation warnings
- [ ] Vector graphics used for figures
- [ ] Non-breaking spaces before references
