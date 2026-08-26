# `python_test.py`

## File Purpose

This script generates a multi-page PDF document (`multi_language_samples.pdf`) containing formatted code snippets for Python, SQL, Perl, and Shell Script. It first defines the content and styling for the document within an HTML string, writes this string to an HTML file, and then uses the `weasyprint` library to convert the HTML file into a PDF.

## Behavior

Upon execution, the script performs the following actions:
1.  Prints `"Hello World"` to standard output.
2.  Defines a multi-line string `html_content` which contains the complete HTML and CSS for a "Multi-Language Scripting Reference" document. The document is styled and includes sample code for:
    *   Python: A script for file I/O and JSON parsing.
    *   SQL: A query using window functions and aggregations.
    *   Perl: A script for parsing log files with regular expressions.
    *   Shell Script: A Bash script for creating and rotating backups.
3.  Writes the content of the `html_content` variable to a new file named `multi_language_samples.html` in the current directory.
4.  Uses the `weasyprint` library to read `multi_language_samples.html` and render it as a PDF.
5.  Saves the resulting PDF as `multi_language_samples.pdf` in the current directory.
6.  Prints `"PDF generated successfully."` to standard output upon successful completion.

## Public Interface

This file is a standalone script and does not expose any public functions or classes for import.
