# Research Summarization Command

Extract key insights and generate structured summaries from research papers and academic documents.

## Purpose

Generate structured summaries of academic papers:
- Extract main findings and contributions
- Identify research methodology
- Summarize results and conclusions
- Generate formatted citations
- Highlight limitations and future work

## Usage

```
/summarize [document-path] [options]
```

**Parameters:**
- `document-path`: Path to document file (PDF, DOCX, TXT, or Markdown)

**Options:**
- `--template <type>`: Template type - `brief`, `standard`, `detailed` (default: standard)
- `--output <path>`: Save summary to specified markdown file
- `--citation <style>`: Citation style - `apa`, `mla`, `chicago`, `harvard`, `ieee` (default: apa)
- `--length <type>`: Summary length - `brief`, `standard`, `comprehensive`
- `--focus <sections>`: Focus on specific sections (comma-separated)
- `--batch`: Process multiple files
- `--format <type>`: Output format - `markdown`, `json`, `txt` (default: markdown)

## Workflow

1. **Document Loading**: Read and parse the document content
2. **Section Detection**: Identify abstract, introduction, methods, results, discussion, conclusions
3. **Key Point Extraction**: Identify main findings, research questions, hypotheses
4. **Summary Generation**: Create structured summary with key sections
5. **Citation Formatting**: Generate bibliography entry in requested style
6. **Output Creation**: Produce markdown-formatted summary document

## Output

The summarization generates:

### Executive Summary
- Concise overview (150-250 words)
- Research question and objectives
- Main methodology approach
- Key findings and implications

### Structured Breakdown

#### Research Question
What problem does this paper address?

#### Methodology
- Study design and approach
- Data collection methods
- Analysis techniques
- Sample size and characteristics

#### Key Findings
- Main results (bullet points)
- Statistical significance
- Supporting evidence

#### Contributions
- Novel insights
- Theoretical contributions
- Practical applications

#### Limitations
- Study limitations acknowledged by authors
- Potential biases
- Scope constraints

#### Future Work
- Recommended next steps
- Open questions
- Research gaps identified

### Citation
Formatted bibliography entry in specified style (APA, MLA, Chicago, Harvard)

## Examples

### Basic Summarization
```
/summarize papers/smith-2024-ml-research.pdf
```
Creates comprehensive summary with default APA citation.

### Custom Length Summary
```
/summarize articles/climate-study.docx --length brief --citation mla
```
Generates brief summary with MLA citation format.

### Focus on Methodology
```
/summarize documents/experiment-report.pdf --focus methodology,results
```
Emphasizes methodology and results sections.

### Multiple Documents
```
/summarize papers/*.pdf --batch --output literature-review.md
```
Summarizes multiple papers and compiles into single document.

### Using Templates
```
/summarize paper.pdf --template brief --output summaries/quick-summary.md
```
Uses brief template for a quick overview.

```
/summarize paper.pdf --template detailed --output summaries/full-analysis.md
```
Uses detailed template for comprehensive analysis.

### Batch with Template
```
/summarize papers/*.pdf --batch --template standard --output summaries/
```
Processes multiple papers using standard template, saving to summaries folder.

## Templates

Three summary templates are available in `skills/academic-research/assets/`:

| Template | Description | Use Case |
|----------|-------------|----------|
| `brief` | Metadata, core summary, key findings, citation | Quick reference, initial screening |
| `standard` | Executive summary, research question, methodology, findings, conclusions | Regular literature review |
| `detailed` | Full analysis with contributions, limitations, future work, critical evaluation | In-depth analysis, thesis research |

## Requirements

- **File Format**: PDF, DOCX, TXT, MD
- **Document Structure**: Works best with structured academic papers
- **Language**: English primary (other languages with reduced accuracy)
- **Length**: Papers 3+ pages recommended for meaningful summaries

## Citation Styles

Supported citation formats:
- **APA** (7th edition): Default style
- **MLA** (9th edition): Humanities focus
- **Chicago** (17th edition): Notes and bibliography
- **Harvard**: British academic standard
- **IEEE**: Technical and engineering papers

## Best Practices

1. **Verify Source**: Ensure document is complete and readable
2. **Review Output**: Always review AI-generated summaries for accuracy
3. **Cite Properly**: Use generated citations as starting point, verify details
4. **Context Matters**: Add your own insights and connections to other work
5. **Save Summaries**: Keep organized library of summaries for literature reviews
