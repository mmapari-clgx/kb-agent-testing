# python_test.py

This script generates a styled, multi-language programming reference guide in both HTML and PDF formats. It serves as a utility to produce documentation templates covering code snippets for Python, SQL, Perl, and Shell Scripting.

## Overview

The script defines a structured HTML document containing syntax-highlighted code blocks and uses the `weasyprint` library to compile this HTML into a print-ready PDF document.

## Dependencies

The script relies on the following libraries:
*   `os` (Standard library, imported but not explicitly used in the generation logic)
*   `weasyprint` (External library used for HTML-to-PDF compilation)

## Execution Flow and Behavior

When executed, the script performs the following steps sequentially:

1.  **Initialization Message**: Prints `"Getting start with KB Agent"` to the standard output.
2.  **HTML Content Definition**: Defines a multi-line string (`html_content`) containing:
    *   CSS styling optimized for A4 page layout, margins, page numbering, and code syntax highlighting.
    *   **Section 1: Python Sample (`.py`)**: A sample script demonstrating JSON parsing, file I/O, and exception handling.
    *   **Section 2: SQL Sample (`.sql`)**: A relational query demonstrating window functions (`SUM() OVER`, `RANK() OVER`), filtering, and sorting.
    *   **Section 3: Perl Sample (`.pl`)**: A text-processing script demonstrating regular expressions for parsing IP addresses from a log file.
    *   **Section 4: Shell Script Sample (`.sh`)**: A Bash script demonstrating directory creation, tarball archiving, and automated file rotation based on modification time.
3.  **File Writing**: Writes the HTML content to a local file named `multi_language_samples.html` using `utf-8` encoding.
4.  **PDF Compilation**: Instantiates a `weasyprint.HTML` object pointing to the generated HTML file and calls `.write_pdf()` to compile it into `multi_language_samples.pdf`.
5.  **Completion Message**: Prints `"PDF generated successfully."` to the standard output.

## Output Artifacts

The execution of this script produces two files in the working directory:

| File Name | Format | Description |
| :--- | :--- | :--- |
| `multi_language_samples.html` | HTML | The raw HTML document containing the styled reference guide. |
| `multi_language_samples.pdf` | PDF | The compiled, print-ready PDF version of the reference guide. |
