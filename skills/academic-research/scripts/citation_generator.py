#!/usr/bin/env python3
"""
Citation Generator Script
Converts paper metadata to formatted citations in various academic styles.

Supports: APA, MLA, Chicago, Harvard, IEEE
"""

import json
import argparse
import sys
from datetime import datetime
from typing import Dict, List, Optional


def format_authors_apa(authors: List[str]) -> str:
    """Format authors according to APA 7th edition style."""
    if not authors:
        return ""

    if len(authors) == 1:
        return authors[0]
    elif len(authors) == 2:
        return f"{authors[0]}, & {authors[1]}"
    elif len(authors) <= 20:
        formatted = ", ".join(authors[:-1])
        return f"{formatted}, & {authors[-1]}"
    else:
        # For 21+ authors, list first 19, ellipsis, then last author
        formatted = ", ".join(authors[:19])
        return f"{formatted}, ... {authors[-1]}"


def format_authors_mla(authors: List[str]) -> str:
    """Format authors according to MLA 9th edition style."""
    if not authors:
        return ""

    if len(authors) == 1:
        return authors[0]
    elif len(authors) == 2:
        return f"{authors[0]}, and {authors[1]}"
    else:
        return f"{authors[0]}, et al."


def generate_apa_citation(metadata: Dict) -> str:
    """Generate APA 7th edition citation."""
    authors = metadata.get('authors', [])
    year = metadata.get('year', datetime.now().year)
    title = metadata.get('title', 'Untitled')
    journal = metadata.get('journal', '')
    volume = metadata.get('volume', '')
    issue = metadata.get('issue', '')
    pages = metadata.get('pages', '')
    doi = metadata.get('doi', '')
    url = metadata.get('url', '')

    # Format authors
    author_str = format_authors_apa(authors)
    if not author_str:
        author_str = "Unknown Author"

    # Build citation
    citation = f"{author_str} ({year}). {title}. "

    if journal:
        citation += f"*{journal}*"
        if volume:
            citation += f", *{volume}*"
        if issue:
            citation += f"({issue})"
        if pages:
            citation += f", {pages}"
        citation += "."

    # Add DOI or URL
    if doi:
        citation += f" https://doi.org/{doi}"
    elif url:
        citation += f" {url}"

    return citation


def generate_mla_citation(metadata: Dict) -> str:
    """Generate MLA 9th edition citation."""
    authors = metadata.get('authors', [])
    title = metadata.get('title', 'Untitled')
    journal = metadata.get('journal', '')
    volume = metadata.get('volume', '')
    issue = metadata.get('issue', '')
    year = metadata.get('year', datetime.now().year)
    pages = metadata.get('pages', '')
    doi = metadata.get('doi', '')

    # Format authors
    author_str = format_authors_mla(authors)
    if not author_str:
        author_str = "Unknown Author"

    # Build citation
    citation = f'{author_str}. "{title}." '

    if journal:
        citation += f"*{journal}*"
        if volume:
            citation += f", vol. {volume}"
        if issue:
            citation += f", no. {issue}"
        citation += f", {year}"
        if pages:
            citation += f", pp. {pages}"
        citation += "."

    # Add DOI
    if doi:
        citation += f" https://doi.org/{doi}."

    return citation


def generate_chicago_citation(metadata: Dict) -> str:
    """Generate Chicago 17th edition citation (notes-bibliography)."""
    authors = metadata.get('authors', [])
    title = metadata.get('title', 'Untitled')
    journal = metadata.get('journal', '')
    volume = metadata.get('volume', '')
    issue = metadata.get('issue', '')
    year = metadata.get('year', datetime.now().year)
    pages = metadata.get('pages', '')
    doi = metadata.get('doi', '')

    # Format authors (first author: Last, First; others: First Last)
    if not authors:
        author_str = "Unknown Author"
    elif len(authors) == 1:
        author_str = authors[0]
    elif len(authors) == 2:
        # Assuming format "Last, First" already
        author_str = f"{authors[0]} and {authors[1]}"
    else:
        author_str = f"{authors[0]} et al."

    # Build citation
    citation = f'{author_str}. "{title}." '

    if journal:
        citation += f"*{journal}*"
        if volume:
            citation += f" {volume}"
        if issue:
            citation += f", no. {issue}"
        citation += f" ({year})"
        if pages:
            citation += f": {pages}"
        citation += "."

    # Add DOI
    if doi:
        citation += f" https://doi.org/{doi}."

    return citation


def generate_harvard_citation(metadata: Dict) -> str:
    """Generate Harvard citation."""
    authors = metadata.get('authors', [])
    year = metadata.get('year', datetime.now().year)
    title = metadata.get('title', 'Untitled')
    journal = metadata.get('journal', '')
    volume = metadata.get('volume', '')
    issue = metadata.get('issue', '')
    pages = metadata.get('pages', '')

    # Format authors
    if not authors:
        author_str = "Unknown Author"
    elif len(authors) == 1:
        author_str = authors[0]
    elif len(authors) == 2:
        author_str = f"{authors[0]} and {authors[1]}"
    else:
        author_str = f"{authors[0]} et al."

    # Build citation
    citation = f"{author_str} ({year}) '{title}', "

    if journal:
        citation += f"*{journal}*"
        if volume:
            citation += f", vol. {volume}"
        if issue:
            citation += f", no. {issue}"
        if pages:
            citation += f", pp. {pages}"
        citation += "."

    return citation


def generate_ieee_citation(metadata: Dict) -> str:
    """Generate IEEE citation."""
    authors = metadata.get('authors', [])
    title = metadata.get('title', 'Untitled')
    journal = metadata.get('journal', '')
    volume = metadata.get('volume', '')
    issue = metadata.get('issue', '')
    pages = metadata.get('pages', '')
    year = metadata.get('year', datetime.now().year)
    month = metadata.get('month', '')

    # Format authors (Initial. Last)
    if not authors:
        author_str = "Unknown Author"
    else:
        # Simplified - assumes format already suitable
        author_str = ", ".join(authors[:3])
        if len(authors) > 3:
            author_str += ", et al."

    # Build citation
    citation = f'{author_str}, "{title}," '

    if journal:
        citation += f"*{journal}*"
        if volume:
            citation += f", vol. {volume}"
        if issue:
            citation += f", no. {issue}"
        if pages:
            citation += f", pp. {pages}"
        if month:
            citation += f", {month}"
        citation += f", {year}."

    return citation


def main():
    parser = argparse.ArgumentParser(description='Generate formatted citations from paper metadata')
    parser.add_argument('--input', required=True, help='Input JSON file with paper metadata')
    parser.add_argument('--format', choices=['apa', 'mla', 'chicago', 'harvard', 'ieee'],
                       default='apa', help='Citation format (default: apa)')
    parser.add_argument('--output', help='Output file (default: stdout)')

    args = parser.parse_args()

    try:
        # Read input
        with open(args.input, 'r', encoding='utf-8') as f:
            metadata = json.load(f)

        # Support both single paper and list of papers
        if isinstance(metadata, list):
            papers = metadata
        else:
            papers = [metadata]

        # Generate citations
        citations = []
        for paper in papers:
            if args.format == 'apa':
                citation = generate_apa_citation(paper)
            elif args.format == 'mla':
                citation = generate_mla_citation(paper)
            elif args.format == 'chicago':
                citation = generate_chicago_citation(paper)
            elif args.format == 'harvard':
                citation = generate_harvard_citation(paper)
            elif args.format == 'ieee':
                citation = generate_ieee_citation(paper)
            else:
                citation = generate_apa_citation(paper)

            citations.append(citation)

        # Output
        output_text = '\n\n'.join(citations)

        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(output_text)
            print(f"Citations written to {args.output}")
        else:
            print(output_text)

        return 0

    except FileNotFoundError:
        print(f"Error: Input file '{args.input}' not found", file=sys.stderr)
        return 1
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in input file: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
