import csv
import os
import re

def clean_author(author):
    return '; '.join(part.split('(')[0].strip() for part in author.split(';'))

def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '', filename)

def create_markdown_file(title, author, issue_date, publication_year, doi, abstract, journal):
    markdown_content = f"""---
title: "{title}"
author: "{clean_author(author)}"
collection: publications
category: {publication_year}
permalink: /publication/{issue_date}-{title.replace(' ', '-')}
date: {issue_date}
paperurl: 'https://doi.org/{doi}'
journal: '{journal}'
---

{abstract}
"""
    safe_title = sanitize_filename(title.replace(' ', '-'))
    filename = f"{issue_date}-{safe_title}.md"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(markdown_content)

with open('publications-0912.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # print(row)
        create_markdown_file(
            title=row['Title'],
            author=row['Author'],
            issue_date=row['Issue date'],
            publication_year=row['Publication year'],
            doi=row['DOI'],
            abstract=row['Abstract'],
            journal=row['Source']
        )