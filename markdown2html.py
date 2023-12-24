#!/usr/bin/python3
''' Write a script markdown2html.py that takes an argument 2 strings:

    First argument is the name of the Markdown file
    Second argument is the output file name
'''
import sys
import os

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



    exit(0)

if __name__ == "__main__":
    main()
