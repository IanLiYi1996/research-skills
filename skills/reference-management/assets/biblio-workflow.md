# Bibliography Workflow Template

Step-by-step guide for creating and managing bibliographies using DBLP and reference management tools.

## Pre-Search Preparation

### 1. Define Scope

**Questions to Answer:**
- [ ] What is the main research question?
- [ ] What are the key topics to cover?
- [ ] What time period is relevant?
- [ ] Which research areas to include?
- [ ] How many references are needed?

**Topic List:**
```
Main Topic: _________________________________
Subtopic 1: _________________________________
Subtopic 2: _________________________________
Subtopic 3: _________________________________
Related Areas: ______________________________
```

### 2. Identify Key Venues

**Conferences:**
- [ ] _____________________ (e.g., NeurIPS, ICML)
- [ ] _____________________
- [ ] _____________________

**Journals:**
- [ ] _____________________ (e.g., JMLR, TPAMI)
- [ ] _____________________
- [ ] _____________________

### 3. Key Researchers

**Must-include Authors:**
- [ ] _____________________ (e.g., Yoshua Bengio)
- [ ] _____________________
- [ ] _____________________
- [ ] _____________________

## Search Phase

### Step 1: Broad Keyword Search

**For each major topic:**

Topic: _____________________

```
Search query: _____________________________
Results found: ____
Relevant papers: ____
Papers to add: ____
```

**Selected Papers:**
- [ ] _____________________ (DBLP key: ________________)
- [ ] _____________________ (DBLP key: ________________)
- [ ] _____________________ (DBLP key: ________________)

### Step 2: Author-Specific Search

**For each key researcher:**

Author: _____________________

```
Total publications: ____
Relevant papers: ____
Papers to add: ____
```

**Selected Papers:**
- [ ] _____________________ (DBLP key: ________________)
- [ ] _____________________ (DBLP key: ________________)
- [ ] _____________________ (DBLP key: ________________)

### Step 3: Venue-Specific Search

**For each venue:**

Venue: _____________________

```
Years searched: _________ to _________
Papers found: ____
Papers to add: ____
```

**Selected Papers:**
- [ ] _____________________ (DBLP key: ________________)
- [ ] _____________________ (DBLP key: ________________)
- [ ] _____________________ (DBLP key: ________________)

### Step 4: Citation Network

**Follow-up searches:**

Seminal Paper: _____________________

```
Cited by search: _____________________________
References search: ___________________________
Papers to add: ____
```

**Selected Papers:**
- [ ] _____________________ (DBLP key: ________________)
- [ ] _____________________ (DBLP key: ________________)

## Collection Phase

### Step 5: Organize Papers by Category

**Category 1: _____________________ (e.g., Foundational Work)**
- [ ] Paper 1: _________________ (Key: ___________)
- [ ] Paper 2: _________________ (Key: ___________)
- [ ] Paper 3: _________________ (Key: ___________)

**Category 2: _____________________ (e.g., Recent Advances)**
- [ ] Paper 1: _________________ (Key: ___________)
- [ ] Paper 2: _________________ (Key: ___________)
- [ ] Paper 3: _________________ (Key: ___________)

**Category 3: _____________________ (e.g., Related Work)**
- [ ] Paper 1: _________________ (Key: ___________)
- [ ] Paper 2: _________________ (Key: ___________)
- [ ] Paper 3: _________________ (Key: ___________)

### Step 6: Create Citation Keys

**Convention Used:**
- [ ] Author2024 (single author)
- [ ] AuthorAuthor2024 (two authors)
- [ ] Author2024Topic (author + topic)
- [ ] Venue24Author (venue-based)
- [ ] Custom: _____________________

**Citation Key List:**
```
Paper Title                    | DBLP Key              | Citation Key
------------------------------|----------------------|---------------
_____________________________| ____________________ | _____________
_____________________________| ____________________ | _____________
_____________________________| ____________________ | _____________
```

### Step 7: Batch Add to Bibliography

**Add Command Template:**
```bash
/references add <dblp-key> <citation-key>
```

**Papers Added:**
- [ ] ___________________ (✓ Added | ✗ Failed)
- [ ] ___________________ (✓ Added | ✗ Failed)
- [ ] ___________________ (✓ Added | ✗ Failed)

**Total Papers in Collection: ___________**

## Export Phase

### Step 8: Export to BibTeX

**Export Details:**
```
Output file: _________________________________
Number of entries: ____
File location: __________________________________
```

**Export Command:**
```bash
/references export /path/to/references.bib
```

**Export Status:**
- [ ] Export successful
- [ ] File verified
- [ ] No errors

### Step 9: Verify BibTeX File

**Verification Checklist:**
- [ ] All entries present (count matches)
- [ ] No duplicate keys
- [ ] Author names formatted correctly
- [ ] Titles properly capitalized
- [ ] Years are correct
- [ ] Venues are accurate
- [ ] Special characters handled

**Issues Found:**
- _____________________________________
- _____________________________________

**Corrections Made:**
- _____________________________________
- _____________________________________

## Integration Phase

### Step 10: Test in LaTeX

**Test Document:**
```latex
\documentclass{article}
\usepackage{natbib}

\begin{document}
Test citation: \cite{TestKey2024}

\bibliographystyle{plain}
\bibliography{references}
\end{document}
```

**Compilation Test:**
- [ ] pdflatex runs without errors
- [ ] bibtex runs successfully
- [ ] Citations appear correctly
- [ ] Bibliography formatted properly

**Errors Encountered:**
- _____________________________________
- _____________________________________

### Step 11: Download Papers (Optional)

**Papers to Download from arXiv:**

| Paper Title | DBLP Key | arXiv ID | Status |
|-------------|----------|----------|--------|
| ___________ | ________ | ________ | ☐ Done |
| ___________ | ________ | ________ | ☐ Done |
| ___________ | ________ | ________ | ☐ Done |

**Download Command:**
```bash
/arxiv download <arxiv-id>
```

### Step 12: Organize Local Files

**File Structure:**
```
papers/
├── foundational/
│   ├── Author2024_paper.pdf
│   └── ...
├── recent/
│   ├── Author2024_paper.pdf
│   └── ...
└── related/
    ├── Author2024_paper.pdf
    └── ...
```

**Organization Status:**
- [ ] Folders created
- [ ] Papers sorted by category
- [ ] Naming convention applied
- [ ] README created

## Quality Control Phase

### Step 13: Review and Validate

**Coverage Check:**
- [ ] All major topics covered
- [ ] Key authors included
- [ ] Important venues represented
- [ ] Recent work included
- [ ] Foundational work included
- [ ] Diverse perspectives

**Quality Check:**
- [ ] High-quality venues
- [ ] Peer-reviewed papers
- [ ] Adequate citation counts
- [ ] Reputable authors
- [ ] Complete metadata

**Balance Check:**
- [ ] Not too many from one author
- [ ] Not too many from one venue
- [ ] Good time distribution
- [ ] Mix of surveys and research
- [ ] Theory and practice balanced

### Step 14: Gap Analysis

**Potential Gaps:**
- Topic not covered: _____________________
- Missing perspective: ___________________
- Time period gap: _______________________
- Venue underrepresented: _______________

**Additional Searches Needed:**
- [ ] _____________________________________
- [ ] _____________________________________
- [ ] _____________________________________

### Step 15: Final Statistics

**Bibliography Metrics:**
```
Total papers: ____
Date range: _______ to _______
Number of authors: ____
Number of venues: ____
Top venue: _________________
Most cited author: _____________
```

**Citation Statistics:**
```
/references stats

Output:
- Papers per year: _________________
- Top authors: ____________________
- Top venues: _____________________
- Research trends: ________________
```

## Maintenance Phase

### Step 16: Version Control

**Git Tracking:**
```bash
git add references.bib
git commit -m "Add bibliography for [project]"
git tag v1.0-bibliography
```

**Version History:**
- [ ] v1.0: Initial bibliography (Date: _________)
- [ ] v1.1: Added recent papers (Date: _________)
- [ ] v2.0: Major update (Date: _________)

### Step 17: Documentation

**Bibliography Notes:**
```markdown
# Bibliography Notes

## Search Strategy
- Keywords used: _________________________
- Date range: ____________________________
- Venues searched: _______________________

## Selection Criteria
- Minimum citation count: _______________
- Venue requirements: ___________________
- Time period: __________________________

## Known Limitations
- _____________________________________
- _____________________________________

## Future Updates
- Check for new papers: [Date]
- Update with latest ICML: [Date]
- Add journal versions: [Date]
```

### Step 18: Backup and Share

**Backup Locations:**
- [ ] Local backup: _______________________
- [ ] Cloud storage: ______________________
- [ ] Git repository: _____________________
- [ ] Reference manager: __________________

**Sharing:**
- [ ] Team shared folder
- [ ] Collaborator access
- [ ] Public repository
- [ ] Supplementary material

## Citation Key Conventions

### Recommended Formats

**Single Author:**
```
Smith2024
Smith2024ML
Smith2024Attention
```

**Two Authors:**
```
SmithJones2024
SmithJones2024Survey
```

**Three or More Authors:**
```
Smith2024              # First author only
SmithEtAl2024
ICML24Smith            # Venue-based
```

### Special Cases

**Same Author, Same Year:**
```
Smith2024a
Smith2024b
Smith2024c
```

**Common Names:**
```
SmithJohn2024          # Add first name
JSmith2024             # Add initial
SmithNLP2024           # Add area
```

**Preprint vs Publication:**
```
Smith2024arxiv         # Preprint
Smith2024              # Published version
```

## Quality Control Checklist

### Pre-Export Checks

- [ ] All DBLP keys valid
- [ ] No duplicate papers
- [ ] Citation keys follow convention
- [ ] Papers properly categorized
- [ ] Collection size appropriate

### Post-Export Checks

- [ ] .bib file syntax valid
- [ ] All entries exported
- [ ] No formatting errors
- [ ] Special characters correct
- [ ] URLs and DOIs present

### Integration Checks

- [ ] LaTeX compilation successful
- [ ] Citations render correctly
- [ ] Bibliography formatted properly
- [ ] No missing references
- [ ] Consistent style applied

## Common Issues and Solutions

### Issue 1: Too Many Results

**Solution:**
- Add more specific keywords
- Use venue filters
- Narrow date range
- Focus on top venues
- Add author constraints

### Issue 2: Too Few Results

**Solution:**
- Broaden keywords
- Try synonyms
- Remove filters
- Expand date range
- Check spelling

### Issue 3: Citation Key Conflicts

**Solution:**
- Add topic suffix
- Include venue code
- Add letter (a, b, c)
- Use more specific names
- Check naming convention

### Issue 4: Export Failures

**Solution:**
- Verify DBLP keys
- Check permissions
- Try different path
- Reduce batch size
- Retry individually

### Issue 5: LaTeX Errors

**Solution:**
- Check BibTeX syntax
- Verify citation keys
- Escape special characters
- Update LaTeX packages
- Check file encoding

## Templates

### Minimal Workflow

For small bibliographies (< 20 papers):

1. Search DBLP
2. Collect DBLP keys
3. Add all papers
4. Export to .bib
5. Verify in LaTeX

### Standard Workflow

For medium bibliographies (20-50 papers):

1. Define scope and topics
2. Search by keywords
3. Search by authors
4. Organize by category
5. Create citation keys
6. Batch add papers
7. Export and verify
8. Test in LaTeX

### Comprehensive Workflow

For large bibliographies (> 50 papers):

1. Full scope definition
2. Multi-faceted searches
3. Citation network exploration
4. Detailed organization
5. Statistical analysis
6. Batch operations
7. Quality control
8. Documentation
9. Version control
10. Team coordination

## Final Checklist

**Before Submission/Publication:**

- [ ] All cited papers in .bib
- [ ] All .bib entries cited or removed
- [ ] Citation keys consistent
- [ ] Author names verified
- [ ] Publication years correct
- [ ] Venue names accurate
- [ ] DOIs included where available
- [ ] LaTeX compiles cleanly
- [ ] Bibliography style correct
- [ ] No duplicate entries
- [ ] Backup created
- [ ] Documentation complete

**Project Complete:** ☐

**Date:** ___________________
