# python_test.py

This script generates a multi-language programming reference guide in both HTML and PDF formats. It embeds code snippets for Python, SQL, Perl, and Shell Scripting into a styled HTML template and compiles it into a PDF document using the `weasyprint` library.

## Overview

The script performs the following tasks:
1. Prints initialization messages to the console.
2. Defines a comprehensive HTML document containing CSS styling and code snippets for four different languages.
3. Writes the HTML content to a local file.
4. Compiles the HTML file into a styled PDF document.

## Dependencies

The script requires the following external library:
* **WeasyPrint**: Used to render the HTML file into a PDF document (`from weasyprint import HTML`).

## Execution Flow and Behavior

1. **Console Initialization**:
   The script prints the following startup messages:
   ```text
   Hello Agent
   Getting start with KB Agent
   ```

2. **HTML Generation**:
   The script defines a string variable `html_content` containing a complete HTML5 document. The document includes:
   * **CSS Styling**: Custom print styles (`@page` size A4, margins, page numbering), color schemes, and syntax highlighting classes (`.keyword`, `.string`, `.comment`, `.function`, `.number`).
   * **Python Sample**: A snippet demonstrating JSON parsing and file I/O error handling.
   * **SQL Sample**: A query demonstrating window functions (`SUM() OVER`, `RANK() OVER`) and filtering.
   * **Perl Sample**: A script demonstrating regular expression matching for IPv4 addresses in log files.
   * **Shell Script Sample**: A Bash script demonstrating directory creation, archiving (`tar`), and file rotation (`find ... -delete`).

3. **File Writing**:
   The HTML content is written to a file named `multi_language_samples.html` using UTF-8 encoding.

4. **PDF Compilation**:
   The script instantiates `weasyprint.HTML` with the generated HTML file and calls `.write_pdf()` to output `multi_language_samples.pdf`.

5. **Completion Message**:
   Upon successful PDF generation, the script prints:
   ```text
   PDF generated successfully.
   ```

## Output Files

The script produces two output files in the working directory:
* **`multi_language_samples.html`**: The raw HTML document containing the styled code snippets.
* **`multi_language_samples.pdf`**: The compiled, print-ready PDF version of the reference guide.
