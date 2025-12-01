---
name: academic-research
description: Comprehensive academic research skill for literature review, paper analysis, citation management, and research synthesis. Use when conducting systematic literature reviews, analyzing academic papers, managing citations and bibliographies, synthesizing research findings, identifying research gaps, or performing scholarly research tasks. Keywords include literature review, citation, bibliography, paper analysis, systematic review, research synthesis, academic writing, scholarly research.
---

# Academic Research Skill

This skill provides comprehensive tools and workflows for academic research tasks.

## Core Capabilities

### 1. Literature Review
Conduct systematic literature reviews following established protocols:
- Design effective search strategies with boolean operators
- Search across multiple academic databases (PubMed, IEEE, ACM, arXiv)
- Screen papers for relevance using inclusion/exclusion criteria
- Extract key information using structured forms
- Synthesize findings across multiple papers
- Identify themes, patterns, and research gaps

### 2. Paper Analysis
Extract and analyze key information from academic papers:
- Identify research questions and hypotheses
- Examine methodology and study design
- Evaluate data collection and analysis methods
- Assess validity and reliability of findings
- Identify limitations and biases
- Extract key contributions and implications
- Compare with existing literature

### 3. Citation Management
Generate and format citations in multiple academic styles:
- APA (7th edition) - Social sciences standard
- MLA (9th edition) - Humanities focus
- Chicago (17th edition) - History and humanities
- Harvard - British academic standard
- IEEE - Engineering and technical papers
- Build annotated bibliographies
- Track sources and references
- Avoid citation duplication

### 4. Research Synthesis
Combine findings from multiple papers systematically:
- Identify common themes and patterns
- Compare methodologies and results across studies
- Conduct gap analysis to find unexplored areas
- Generate research recommendations
- Create evidence-based summaries
- Map research landscape

## Bundled Resources

### Scripts

Use `scripts/citation_generator.py` for automated citation formatting:

```bash
python skills/academic-research/scripts/citation_generator.py \
  --input paper-metadata.json \
  --format apa \
  --output citations.txt
```

This script converts paper metadata (JSON format) into formatted citations. Supports APA, MLA, Chicago, Harvard, and IEEE styles.

Input format example:
```json
{
  "authors": ["Smith, J.", "Johnson, A."],
  "year": 2024,
  "title": "Machine Learning in Climate Science",
  "journal": "Nature Climate Change",
  "volume": "14",
  "pages": "123-135",
  "doi": "10.1038/s41558-024-12345-6"
}
```

### References

Consult `references/research-methodology.md` for:
- PRISMA guidelines for systematic reviews
- Quality assessment criteria for papers
- Bias assessment frameworks (selection, performance, detection, attrition, reporting)
- Study design evaluation methods
- Research quality checklists

Consult `references/citation-formats.md` for:
- Detailed APA 7th edition formatting rules
- MLA 9th edition guidelines
- Chicago 17th edition style
- Harvard referencing system
- IEEE citation format
- Common citation patterns and examples

### Assets

Use `assets/literature-review-template.md` for conducting structured literature reviews. This template includes:
- Research question definition section
- Search strategy documentation
- Inclusion/exclusion criteria
- Paper screening workflow
- Key themes and findings organization
- Gap analysis section
- Conclusion and recommendations

Use `assets/annotation-template.md` for creating annotated bibliographies. Each annotation includes:
- Full citation in chosen format
- Paper summary (150-200 words)
- Methodology overview
- Key findings
- Relevance to your research
- Critical evaluation

## Workflow Patterns

### Systematic Literature Review

Follow this structured approach:

1. **Define Research Question**: Formulate specific, answerable research question using PICO framework (Population, Intervention, Comparison, Outcome)

2. **Develop Search Strategy**:
   - Identify key concepts and synonyms
   - Construct boolean search queries
   - Select appropriate databases
   - Document search strategy in template

3. **Execute Searches**: Run searches across selected databases and document results

4. **Screen Papers**:
   - Title and abstract screening first
   - Full-text review for remaining papers
   - Apply inclusion/exclusion criteria consistently
   - Document reasons for exclusion

5. **Extract Data**: Use structured form to extract:
   - Study characteristics
   - Methodology details
   - Main findings
   - Quality indicators

6. **Synthesize Findings**:
   - Group papers by theme or methodology
   - Compare and contrast findings
   - Identify patterns and contradictions
   - Assess overall evidence quality

7. **Write Review**: Follow literature review template structure

### Paper Analysis Workflow

1. **First Pass - Skim**: Read abstract, introduction, and conclusion to understand main contribution

2. **Second Pass - Deep Read**:
   - Examine methodology section carefully
   - Review results with attention to tables and figures
   - Assess discussion and interpretation

3. **Evaluation**:
   - Use quality assessment checklist from references
   - Identify strengths and limitations
   - Assess generalizability

4. **Annotation**: Create structured annotation using template

5. **Citation**: Generate formatted citation using citation generator script

## Best Practices

1. **Systematic Approach**: Follow established protocols and document all decisions

2. **Documentation**: Keep detailed records of:
   - Search strategies and dates
   - Databases searched
   - Number of results at each stage
   - Inclusion/exclusion decisions
   - Quality assessment scores

3. **Quality Assessment**: Evaluate each paper rigorously using standardized criteria

4. **Proper Attribution**: Always cite sources correctly and avoid plagiarism

5. **Version Control**: Track iterations of your review as it evolves

6. **Transparency**: Document limitations and potential biases in your review process

7. **Up-to-Date**: Regularly update searches for ongoing research areas

## Integration with Other Tools

- **MCP Search Server**: Use for finding recent papers online
- **MCP Filesystem**: Organize papers and notes systematically
- **MCP Database**: Store paper metadata and annotations in structured format
- **Git**: Version control for your literature review documents

## Example Usage

When user requests: "Help me conduct a systematic review on renewable energy adoption"

Process:
1. Load systematic review protocol from `references/research-methodology.md`
2. Help define specific research question (e.g., "What factors influence residential solar panel adoption?")
3. Develop search terms: (renewable energy OR solar OR wind) AND (adoption OR uptake OR implementation) AND (residential OR household)
4. Guide database selection (IEEE, ACM for technical, ScienceDirect for interdisciplinary)
5. Document strategy in `assets/literature-review-template.md`
6. Execute searches using MCP search server
7. Screen results using inclusion/exclusion criteria
8. Extract data from selected papers
9. Synthesize findings by theme (economic factors, policy influence, social factors, etc.)
10. Generate citations using `scripts/citation_generator.py`
11. Write structured review following template

Always maintain academic rigor and ensure reproducibility of the review process.
