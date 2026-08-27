# python_test.py

This script generates a multi-language programming reference guide containing code snippets for Python, SQL, Perl, and Shell Script. It outputs the guide as both an HTML file and a compiled PDF document.

## Overview

The script does not define any classes or functions. Instead, it runs a linear execution flow to write an HTML template to disk and compile it into a PDF using the `weasyprint` library.

## Dependencies

- **`weasyprint`**: Used to compile the generated HTML file into a PDF.
- **`os`**: Imported, but not explicitly used in the provided code.

## Execution Flow and Behavior

When executed, the script performs the following steps:

1. **Console Initialization**: Prints startup messages to the console:
   ```
   Hello World
   Getting start with KB Agent
   ```

2. **HTML Content Definition**: Defines a multi-line HTML string (`html_content`) containing embedded CSS styling and syntax-highlighted code blocks for four languages:
   - **Python**: A sample script demonstrating file I/O, error handling, and JSON parsing.
   - **SQL**: A query demonstrating aggregations, window functions (`SUM() OVER`, `RANK() OVER`), and filtering.
   - **Perl**: A log-parsing script using regular expressions to count IP addresses.
   - **Shell Script**: A Bash script demonstrating automated backup creation and log rotation.

3. **HTML File Generation**: Writes the HTML content to a local file named `multi_language_samples.html` using UTF-8 encoding.

4. **PDF Compilation**: Uses `weasyprint.HTML` to read `multi_language_samples.html` and render it to a PDF file named `multi_language_samples.pdf`.

5. **Completion Message**: Prints a success message to the console:
   ```
   PDF generated successfully.
   ```

## Output Files

The script produces two files in the working directory:
- `multi_language_samples.html`: The raw HTML document containing the styled reference guide.
- `multi_language_samples.pdf`: The print-ready PDF compiled from the HTML document.
