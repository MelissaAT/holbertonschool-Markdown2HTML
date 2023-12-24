#!/usr/bin/python3
''' Write a script markdown2html.py that takes an argument 2 strings:

    First argument is the name of the Markdown file
    Second argument is the output file name
'''
import sys
import os

def convert_headings(line):
    """Convert Markdown headings to HTML headings."""
    for i in range(6, 0, -1):
        if line.startswith('#' * i):
            return f"<h{i}>{line[i+1:].strip()}</h{i}>"
    return line

def main():
    # Check if the number of arguments is less than 2
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)

    # Check if the Markdown file exists
    markdown_file = sys.argv[1]
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        exit(1)

    # Open the Markdown file and the output HTML file
    with open(markdown_file, 'r') as md_file, open(sys.argv[2], 'w') as html_file:
        for line in md_file:
            html_line = convert_headings(line)
            html_file.write(html_line + '\n')

    exit(0)

if __name__ == "__main__":
    main()
