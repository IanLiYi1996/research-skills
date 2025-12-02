# Paper Check Command

Pre-submission checklist and automated checks for academic papers.

## Purpose

Perform comprehensive checks on LaTeX papers before submission:
- Content and anonymity verification
- LaTeX formatting best practices
- Citation and reference checks
- Figure and table quality checks

## Usage

```
/paper-check [file.tex] [options]
```

**Options:**
- `--full` - Run all checks (default)
- `--anonymity` - Check only anonymity
- `--latex` - Check only LaTeX formatting
- `--citations` - Check only citations
- `--figures` - Check only figures/tables
- `--verbose` - Show detailed output

## Check Categories

### 1. Anonymity Check (`--anonymity`)

Scans for potential anonymity violations:

```
/paper-check paper.tex --anonymity
```

Checks for:
- [ ] Author names in text
- [ ] Institution names
- [ ] Personal file paths (e.g., `/home/username/`)
- [ ] Email addresses
- [ ] GitHub/GitLab URLs with usernames
- [ ] Acknowledgment sections
- [ ] Self-citations with identifying info

### 2. LaTeX Formatting Check (`--latex`)

Verifies LaTeX best practices:

```
/paper-check paper.tex --latex
```

Checks for:
- [ ] Non-breaking spaces before `\ref`, `\cite` (should use `~`)
- [ ] English quotation marks (`` ` `` and `'` vs `"`)
- [ ] Contractions (don't, it's, can't)
- [ ] Bracket matching (`\left`/`\right` pairs)
- [ ] Equation numbering consistency
- [ ] Missing `\label` for figures/tables
- [ ] Booktabs usage (vs `\hline`)
- [ ] Vector graphics (PDF vs PNG/JPG)

### 3. Citation Check (`--citations`)

Validates references and citations:

```
/paper-check paper.tex --citations
```

Checks for:
- [ ] Citation style consistency (`\cite` vs `\citep` vs `\citet`)
- [ ] Undefined references
- [ ] Unused bibliography entries
- [ ] arXiv vs published version preference
- [ ] Conference name abbreviation consistency
- [ ] Missing fields in BibTeX entries

### 4. Figure/Table Check (`--figures`)

Reviews visual elements:

```
/paper-check paper.tex --figures
```

Checks for:
- [ ] All figures/tables have captions
- [ ] All figures/tables are referenced in text
- [ ] Image file format (PDF preferred)
- [ ] Excessive whitespace in figures
- [ ] Caption vs body text redundancy

### 5. Content Check

General content quality:

```
/paper-check paper.tex --content
```

Checks for:
- [ ] Page limit compliance
- [ ] Abstract word count
- [ ] Short final paragraph lines (< 1/4 width)
- [ ] Missing sections (Abstract, Introduction, Conclusion)

## Full Check Example

```
/paper-check paper.tex --full --verbose
```

Output:
```
Paper Check Report for paper.tex
================================

[PASS] Anonymity Check
  - No author names found
  - No personal paths detected
  - No email addresses found

[WARN] LaTeX Formatting
  - Line 45: Missing ~ before \ref{fig:model}
  - Line 89: Straight quotes found, use ``...''
  - Line 123: Contraction "don't" found

[PASS] Citation Check
  - All citations defined
  - Citation style consistent

[WARN] Figure/Table Check
  - figures/result.png: Consider using PDF format
  - Table 2: Not referenced in text

Summary: 2 warnings, 0 errors
```

## Interactive Mode

Run interactive check with suggestions:

```
/paper-check paper.tex --interactive
```

Prompts for each issue:
```
Line 45: Missing non-breaking space before \ref
  Current:  Figure \ref{fig:model}
  Suggested: Figure~\ref{fig:model}

  [a]pply  [s]kip  [A]pply all  [q]uit
```

## Pre-submission Workflow

Recommended usage before submission:

```bash
# 1. Run full check
/paper-check paper.tex --full

# 2. Fix reported issues

# 3. Run again to verify
/paper-check paper.tex --full

# 4. Final anonymity check
/paper-check paper.tex --anonymity --verbose
```

## Common Patterns Checked

### Non-breaking Spaces

```latex
# Should be:
Figure~\ref{fig:1}
Table~\ref{tab:1}
Section~\ref{sec:intro}
BERT~\cite{bert}

# Not:
Figure \ref{fig:1}
Table \ref{tab:1}
```

### Quotation Marks

```latex
# Should be:
``quoted text''

# Not:
"quoted text"
```

### Citation Style

```latex
# As sentence subject:
\citet{author2020} propose a method.

# Parenthetical:
This has been studied~\citep{author2020}.

# Not mixed:
Author et al. \cite{author2020} propose...  # Wrong
```

### Table Format

```latex
# Should use booktabs:
\toprule
\midrule
\bottomrule

# Not:
\hline
|c|c|c|  # vertical lines
```

## Integration

Works with:
- **latex-expert agent**: For fixing reported issues
- **latex-writing skill**: For templates and best practices
- **writing-assistant agent**: For content improvements

## Related Resources

- Checklist reference: `skills/latex-writing/references/paper-writing-tips.md`
- LaTeX cheatsheet: `skills/latex-writing/references/latex-cheatsheet.md`
- External tools:
  - [aclpubcheck](https://github.com/acl-org/aclpubcheck) - ACL paper checker
  - [Grammarly](https://grammarly.com) - Grammar check
  - [Writefull](https://writefull.com) - Academic writing check
