import bibtexparser
import os
import re
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode
from bibtexparser.bibdatabase import BibDatabase

def clean_author(author):
    authors = []
    for part in author.split(' and '):
        names = part.split(', ')
        if len(names) == 2:
            formatted_name = f"{names[1].strip()} {names[0].strip()}"
        else:
            formatted_name = names[0]
        authors.append(formatted_name)
    return '; '.join(authors)

def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '', filename)

def create_markdown_file(entry):
    title = entry.get('title', '').replace('{', '').replace('}', '')
    author = clean_author(entry.get('author', ''))
    year = entry.get('year', '')
    doi = entry.get('doi', '')
    journal = entry.get('journal', '')

    # Create a BibDatabase object
    db = BibDatabase()
    db.entries = [entry]
    entry_text = bibtexparser.dumps(db)

    safe_title = sanitize_filename(title.replace(' ', '-'))
    issue_date = f"{year}-01-01"  # Simplified issue date, adjust as needed

    permalink = f"{issue_date}-{safe_title}"
    if len(permalink) > 50:
        permalink = permalink[:50]  # Truncate to 30 characters

    markdown_content = f"""---
title: "{title}"
author: "{author}"
collection: publications
category: {year}
permalink: /publication/{permalink}
date: {issue_date}
paperurl: 'https://doi.org/{doi}'
{f"journal: '{journal}'" if journal else ''}
---
```bibtex
{entry_text.strip()}
```
"""
    filename = f"result/{permalink}.md"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(markdown_content)

def parse_bibtex_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as bibtex_file:
        parser = BibTexParser(common_strings=True)
        parser.customization = convert_to_unicode
        bib_database = bibtexparser.load(bibtex_file, parser=parser)
        for entry in bib_database.entries:
            create_markdown_file(entry)

# Example usage
parse_bibtex_file('pub_all.bib')