#!/usr/bin/python3
''' Write a script markdown2html.py that takes an argument 2 strings:

    First argument is the name of the Markdown file
    Second argument is the output file name
'''
import sys
import os
import re

def convert_bold(text):
    """Convert Markdown bold syntax to HTML bold tags."""
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'__(.*?)__', r'<em>\1</em>', text)
    return text

def convert_headings(line):
    """Convert Markdown headings to HTML headings."""
    for i in range(6, 0, -1):
        if line.startswith('#' * i):
            return f"<h{i}>{line[i+1:].strip()}</h{i}>"
    return None

def convert_lists(lines):
    """Convert Markdown unordered and ordered lists to HTML lists."""
    in_ul = False  # Unordered list flag
    in_ol = False  # Ordered list flag
    html_lines = []

    for line in lines:
        line = convert_bold(line)  # Convert bold syntax within the line

        if line.startswith('- '):
            if not in_ul:
                if in_ol:  # Close ordered list if open
                    html_lines.append('</ol>')
                    in_ol = False
                html_lines.append('<ul>')
                in_ul = True
            html_lines.append(f"<li>{line[2:].strip()}</li>")
        elif line.startswith('* '):
            if not in_ol:
                if in_ul:  # Close unordered list if open
                    html_lines.append('</ul>')
                    in_ul = False
                html_lines.append('<ol>')
                in_ol = True
            html_lines.append(f"<li>{line[2:].strip()}</li>")
        else:
            if in_ul or in_ol:
                html_lines.append('</ul>' if in_ul else '</ol>')
                in_ul = in_ol = False
            if line.strip():  # Avoid adding blank lines
                html_lines.append(line.strip())

    # Close any open lists at the end of file
    if in_ul or in_ol:
        html_lines.append('</ul>' if in_ul else '</ol>')

    return html_lines

def convert_paragraphs(lines):
    """Convert text blocks into HTML paragraphs."""
    html_lines = []
    paragraph = []

    for line in lines:
        line = convert_bold(line)  # Convert bold syntax within the line

        if line == '\n':
            if paragraph:
                html_lines.append('<p>')
                html_lines.append('<br/>'.join(paragraph))
                html_lines.append('</p>')
                paragraph = []
        else:
            paragraph.append(line.strip())

    # Add the last paragraph if exists
    if paragraph:
        html_lines.append('<p>')
        html_lines.append('<br/>'.join(paragraph))
        html_lines.append('</p>')

    return html_lines

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

    # Read the Markdown file and convert it to HTML
    with open(markdown_file, 'r') as md_file:
        lines = md_file.readlines()

    html_lines = []
    for line in lines:
        line = convert_bold(line)  # Convert bold syntax within the line
        heading = convert_headings(line)
        if heading is not None:
            html_lines.append(heading)
        else:
            html_lines.append(line)

    html_lines = convert_lists(html_lines)
    html_lines = convert_paragraphs(html_lines)

    # Write the HTML output
    with open(sys.argv[2], 'w') as html_file:
        for line in html_lines:
            html_file.write(line + '\n')

    exit(0)

if __name__ == "__main__":
    main()
