# python_test.py

This script generates a styled HTML reference document and compiles it into a PDF file using the `weasyprint` library. The generated document serves as a multi-language scripting reference guide containing code snippets for Python, SQL, Perl, and Shell Scripting.

## Overview

The script runs sequentially to:
1. Print initialization messages to the console.
2. Define a structured HTML document containing CSS styles and syntax-highlighted code blocks.
3. Write the HTML content to a local file.
4. Convert the HTML file into a PDF document.

## Dependencies

The script relies on the following libraries:
* `os` (imported but not explicitly used in the generation logic)
* `weasyprint` (specifically the `HTML` class for PDF compilation)

## Generated Files

The execution of this script produces two files in the working directory:
* **`multi_language_samples.html`**: The raw HTML document containing the styled code snippets.
* **`multi_language_samples.pdf`**: The compiled PDF version of the HTML document, formatted for A4 size.

## Document Content & Structure

The generated reference guide contains the following sections:

1. **Python Sample (`.py`)**: A sample script demonstrating file I/O, error handling, and JSON parsing.
2. **SQL Sample (`.sql`)**: A relational database query demonstrating aggregations, window functions (`SUM() OVER`, `RANK() OVER`), and filtering.
3. **Perl Sample (`.pl`)**: A text processing script using regular expressions to parse IP addresses from a log file.
4. **Shell Script Sample (`.sh`)**: A Bash script demonstrating automated backup creation, directory management, and file rotation.

## Execution Flow

1. **Console Output**: Prints startup messages:
   ```text
   Welcome to KB Agent
   Getting start with KB Agent
   ```
2. **HTML Generation**: Writes the hardcoded HTML string (`html_content`) to `multi_language_samples.html` using UTF-8 encoding.
3. **PDF Compilation**: Instantiates `weasyprint.HTML` with the generated HTML file and calls `.write_pdf()` to output `multi_language_samples.pdf`.
4. **Completion Output**: Prints a success message upon successful PDF generation:
   ```text
   PDF generated successfully.
   ```
