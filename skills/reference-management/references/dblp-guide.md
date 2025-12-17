# DBLP Database Guide

Complete reference for using the Digital Bibliography & Library Project (DBLP) for computer science research.

## What is DBLP?

DBLP is the premier bibliography database for computer science publications, providing:

- **Comprehensive Coverage**: Over 6 million publications
- **Computer Science Focus**: CS conferences, journals, workshops
- **Author Tracking**: Complete publication lists per researcher
- **Venue Information**: Conference and journal metadata
- **Free Access**: Open database with no subscription required
- **Regular Updates**: Daily additions of new publications

## Database Scope

### Included Publications

DBLP primarily indexes:
- Conference papers from major CS venues
- Journal articles from CS journals
- Workshop papers (co-located with conferences)
- PhD theses and dissertations
- Technical reports and preprints
- Book chapters in edited volumes

### Geographic Coverage

- Worldwide computer science publications
- All major CS conferences and journals
- Regional conferences with international participation
- Publications in multiple languages (titles/abstracts)

### Time Coverage

- Historical: Papers dating back to 1950s
- Current: New papers added within days/weeks
- Comprehensive: Complete proceedings for major venues

## Search Strategies

### Keyword Search

**Boolean Operators:**
```
transformer AND attention              # Both required
neural OR deep                        # Either term
"machine learning"                    # Exact phrase
(ML OR AI) AND healthcare            # Grouped operators
```

**Search Tips:**
- Use quotes for exact phrases
- Combine multiple terms with AND
- Use OR for synonyms
- Avoid too many terms (3-5 optimal)
- Try variations of technical terms

### Author Search

**Name Formats:**
```
"Yoshua Bengio"          # Full name
"Y. Bengio"              # With initial
"Bengio"                 # Last name only
"Geoffrey E. Hinton"     # With middle initial
```

**Common Issues:**
- Name spelling variations (François vs Francois)
- Different name orders (Western vs Eastern)
- Married name changes
- Common surnames (use initials)
- Diacritical marks (ö, é, ñ, etc.)

**Best Practices:**
- Try multiple name formats
- Use fuzzy matching for uncertainty
- Check author disambiguation
- Verify with known publications

### Title Search

**Fuzzy Matching:**
- **Threshold 0.9-1.0**: Very similar titles
- **Threshold 0.8-0.9**: Good match with minor differences
- **Threshold 0.7-0.8**: Moderate similarity
- **Threshold 0.6-0.7**: Loose matching

**When to Use:**
- Remember approximate title
- Uncertain about exact wording
- Different versions (preprint vs final)
- Title changes between versions

### Venue Search

**Venue Types:**
- **Conferences**: ICML, NeurIPS, CVPR, etc.
- **Journals**: JMLR, TPAMI, TACL, etc.
- **Workshops**: Co-located with conferences
- **Symposiums**: SOSP, VLDB, etc.

**Finding Venue Abbreviations:**
1. Search a known paper from venue
2. Check venue field in results
3. Use get_venue_info tool
4. Reference common venue lists

## DBLP Key Format

### Understanding DBLP Keys

Format: `type/venue/AuthorsYear[letter]`

**Type Prefix:**
- `conf/` - Conference paper
- `journals/` - Journal article
- `phd/` - PhD thesis
- `books/` - Book or chapter
- `tr/` - Technical report

**Venue:**
- Short name: `nips`, `icml`, `cvpr`
- Journal abbreviation: `jmlr`, `corr`
- Institution: `us/Stanford`, `de/Munich`

**Authors + Year:**
- Last names concatenated
- 2-digit or 4-digit year
- Optional letter for disambiguation

**Examples:**
```
conf/nips/VaswaniSPUJGKP17        # Attention paper at NeurIPS 2017
journals/jmlr/BengioCV13          # Representation learning in JMLR
conf/acl/DevlinCLT19              # BERT paper at ACL 2019
conf/iclr/BrownMRSKDNSSAA20       # GPT-3 at ICLR 2020
```

### Using DBLP Keys

**For BibTeX Export:**
1. Search and identify paper
2. Copy exact DBLP key from results
3. Use `add_bibtex_entry` with key
4. Provide custom citation key
5. Export to .bib file

**Key Benefits:**
- Unique identifier for each publication
- Stable across database updates
- Direct access to full metadata
- Enables batch operations

## Common Venues

### Machine Learning

**Top Conferences:**
- **NeurIPS** (nips): Neural Information Processing Systems
- **ICML** (icml): International Conference on Machine Learning
- **ICLR** (iclr): International Conference on Learning Representations
- **AISTATS** (aistats): Artificial Intelligence and Statistics

**Journals:**
- **JMLR** (jmlr): Journal of Machine Learning Research
- **MLJ** (mlj): Machine Learning Journal

### Natural Language Processing

**Top Conferences:**
- **ACL** (acl): Association for Computational Linguistics
- **EMNLP** (emnlp): Empirical Methods in NLP
- **NAACL** (naacl): North American Chapter of ACL
- **COLING** (coling): International Conference on Computational Linguistics

**Journals:**
- **TACL** (tacl): Transactions of ACL
- **CL** (cl): Computational Linguistics

### Computer Vision

**Top Conferences:**
- **CVPR** (cvpr): Computer Vision and Pattern Recognition
- **ICCV** (iccv): International Conference on Computer Vision
- **ECCV** (eccv): European Conference on Computer Vision

**Journals:**
- **TPAMI** (tpami): IEEE Transactions on Pattern Analysis
- **IJCV** (ijcv): International Journal of Computer Vision

### Databases

**Top Conferences:**
- **SIGMOD** (sigmod): International Conference on Management of Data
- **VLDB** (vldb): Very Large Data Bases
- **ICDE** (icde): International Conference on Data Engineering

**Journals:**
- **TODS** (tods): ACM Transactions on Database Systems
- **VLDB J** (vldb): VLDB Journal

### Systems

**Top Conferences:**
- **SOSP** (sosp): Symposium on Operating Systems Principles
- **OSDI** (osdi): Operating Systems Design and Implementation
- **NSDI** (nsdi): Networked Systems Design and Implementation

**Journals:**
- **TOCS** (tocs): ACM Transactions on Computer Systems

## Advanced Search Techniques

### Temporal Filtering

**Year Ranges:**
- Recent work: 2020-2024
- Foundational work: Pre-2015
- Decade reviews: 2010-2020
- Historical: Pre-2000

**Use Cases:**
- Track research evolution
- Find seminal papers
- Survey recent advances
- Historical perspective

### Combining Filters

**Multi-dimensional Search:**
```
Keywords: "deep learning"
Author: "Bengio"
Venue: ICML
Years: 2015-2020
```

**Benefits:**
- Precise targeting
- Reduced false positives
- Comprehensive coverage
- Efficient workflow

### Citation Network Exploration

**Forward Citations:**
1. Find influential paper
2. Search papers citing it
3. Identify research branches
4. Track impact over time

**Backward Citations:**
1. Find recent paper
2. Check references
3. Find foundational work
4. Build context

## Author Name Formats

### Handling Name Variations

**Unicode Characters:**
- Try both: "François" and "Francois"
- Use wildcards if available
- Search by last name only
- Verify with known papers

**Name Order:**
- Western: Given Family
- Eastern: Family Given
- Try both orders
- Check author page

**Abbreviations:**
- "Geoffrey E. Hinton"
- "Geoffrey Hinton"
- "G. E. Hinton"
- "G. Hinton"

### Author Disambiguation

**Common Surnames:**
- Add middle initial
- Check affiliation
- Verify research area
- Cross-reference publications

**Name Changes:**
- Married names
- Name translations
- Transliterations
- Preferred names

## Best Practices

### Search Efficiency

1. **Start Specific**: Use precise keywords
2. **Broaden Gradually**: Add OR terms if needed
3. **Use Filters**: Venue and date constraints
4. **Check Variations**: Try different phrasings
5. **Verify Results**: Sample check for relevance

### Quality Control

1. **Cross-Reference**: Verify with other sources
2. **Check Metadata**: Ensure accuracy
3. **Confirm Venue**: Verify abbreviations
4. **Validate Dates**: Check publication years
5. **Review Authors**: Confirm author lists

### Batch Operations

1. **Collect Keys**: Note all DBLP keys
2. **Organize by Topic**: Group related papers
3. **Batch Add**: Add all in one session
4. **Verify Collection**: Check for duplicates
5. **Export Once**: Single .bib file

### Citation Management

1. **Consistent Keys**: Use naming convention
2. **Document Source**: Note DBLP origin
3. **Track Versions**: Note preprint vs final
4. **Backup Files**: Keep .bib backups
5. **Test LaTeX**: Verify compilation

## Common Issues and Solutions

### Paper Not Found

**Possible Reasons:**
- Too recent (not yet indexed)
- Not CS publication (out of scope)
- Workshop paper (limited coverage)
- Spelling errors in search

**Solutions:**
- Try different keywords
- Search by author
- Check venue directly
- Use arXiv for preprints

### Incorrect Metadata

**Issues:**
- Wrong author order
- Incorrect venue
- Missing information
- Outdated data

**Solutions:**
- Report to DBLP (dblp.org/faq)
- Note in bibliography
- Cross-check with DOI
- Use authoritative source

### Duplicate Entries

**Causes:**
- Preprint and final version
- Conference and journal versions
- Different venue publications
- Database inconsistencies

**Solutions:**
- Choose primary version
- Note relationship in comments
- Use most complete entry
- Cite both if relevant

### Name Disambiguation

**Problem:**
- Multiple authors with same name
- Different name formats
- Name variations

**Solutions:**
- Check affiliations
- Verify research areas
- Use author pages
- Cross-reference co-authors

## Integration Tips

### With arXiv

**Workflow:**
1. Search DBLP for CS papers
2. Note arXiv IDs in results
3. Download PDFs from arXiv
4. Collect BibTeX from DBLP
5. Combine in bibliography

### With Google Scholar

**Complementary Use:**
- DBLP: CS-specific, clean data
- Scholar: Broader coverage, citations
- Use both for comprehensive search
- Prefer DBLP for BibTeX quality

### With Reference Managers

**Export Strategy:**
1. Search and collect in DBLP
2. Export to .bib file
3. Import into manager (Zotero, Mendeley)
4. Organize and annotate
5. Export final bibliography

## Resources

### Official DBLP Links

- **Main Site**: https://dblp.org
- **FAQ**: https://dblp.org/faq
- **Author Pages**: https://dblp.org/pid/
- **Venue Pages**: https://dblp.org/db/

### Community Resources

- DBLP Blog for updates
- Research community forums
- CS conference websites
- Academic social networks

### Related Tools

- BibTeX format guide
- LaTeX bibliography packages
- Reference management software
- Citation style guides
