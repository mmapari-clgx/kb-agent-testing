# python_test.py

This script generates a multi-language programming reference guide in both HTML and PDF formats. It embeds code snippets for Python, SQL, Perl, and Shell Scripting into an HTML template and compiles it into a styled PDF document using the `weasyprint` library.

## Dependencies

The script relies on the following libraries:
* `os` (standard library)
* `weasyprint` (specifically the `HTML` class for PDF generation)

## Execution Flow and Behavior

When executed, the script performs the following steps:

1. **Console Initialization**:
   Prints initialization messages to the console:
   ```text
   Hello World
   Getting start with KB Agent
   ```

2. **HTML Content Definition**:
   Defines a structured HTML document (`html_content`) containing:
   * Embedded CSS styling for print layout (A4 size, margins, page numbering, and syntax highlighting colors).
   * **Python Sample**: A script demonstrating JSON parsing, file I/O, and error handling.
   * **SQL Sample**: A query demonstrating window functions (`SUM() OVER`, `RANK() OVER`), filtering, and sorting.
   * **Perl Sample**: A script demonstrating regular expression matching for IPv4 addresses in log files.
   * **Shell Script Sample**: A Bash script demonstrating automated directory backup, tar archiving, and log rotation.

3. **File Generation**:
   * **HTML Output**: Writes the HTML content to a local file named `multi_language_samples.html` using UTF-8 encoding.
   * **PDF Compilation**: Uses `weasyprint.HTML` to read `multi_language_samples.html` and render it to a PDF file named `multi_language_samples.pdf`.

4. **Completion Message**:
   Prints a success message to the console:
   ```text
   PDF generated successfully.
   ```

## Generated Artifacts

* **`multi_language_samples.html`**: The raw HTML document containing the styled reference guide.
* **`multi_language_samples.pdf`**: The compiled, print-ready PDF document formatted to A4 specifications.
