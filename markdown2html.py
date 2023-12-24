#!/usr/bin/python3
''' Write a script markdown2html.py that takes an argument 2 strings:

    First argument is the name of the Markdown file
    Second argument is the output file name
'''
import sys
import os
import re
import hashlib

def convert_md5(text):
    """Convert text within [[ ]] to its MD5 hash."""
    return re.sub(r'\[\[(.*?)\]\]', lambda match: hashlib.md5(match.group(1).encode()).hexdigest(), text)

def remove_c(text):
    """Remove all 'c' (case insensitive) from text within (( ))."""
    return re.sub(r'\(\((.*?)\)\)', lambda match: match.group(1).replace('c', '').replace('C', ''), text)

def convert_text(text):
    """Convert special text formats."""
    text = convert_md5(text)
    text = remove_c(text)
    return text

def process_markdown_line(line):
    """Process a single line of Markdown to HTML."""
    line = convert_text(line)
    # Add other conversion functions here if needed
    return line

def main():
    # Check command line arguments
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)

    markdown_file = sys.argv[1]
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        exit(1)

    # Process the Markdown file
    with open(markdown_file, 'r') as md_file, open(sys.argv[2], 'w') as html_file:
        for line in md_file:
            html_line = process_markdown_line(line)
            html_file.write(html_line)

    exit(0)

if __name__ == "__main__":
    main()