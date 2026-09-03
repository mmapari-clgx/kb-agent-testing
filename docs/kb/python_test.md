<!-- kb-agent:source-sha256=8f1989088335800e8109f5e8f5024559a3d3071a256c3dcfea7439dacd4b35e8 -->
# python_test.py

This Python script generates a multi-language programming reference guide in both HTML and PDF formats. It compiles syntax-highlighted code snippets for Python, SQL, Perl, and Shell scripting into a styled document.

## Dependencies

The script relies on the following libraries:
*   `weasyprint` (specifically the `HTML` class for PDF generation)
*   `os` (imported but not actively used in the generation logic)

## Generated Outputs

When executed, the script writes two files to the local directory:
1.  **`multi_language_samples.html`**: An HTML document styled with CSS for print/A4 layout.
2.  **`multi_language_samples.pdf`**: A PDF document compiled from the HTML file using WeasyPrint.

---

## Execution Flow and Behavior

1.  **Initialization**: Prints the message `"Getting start with KB Agent"` to the standard output.
2.  **HTML Content Definition**: Defines a structured HTML template (`html_content`) containing CSS styling and code snippets for four languages:
    *   **Python**: A sample script demonstrating file I/O, JSON parsing, and exception handling.
    *   **SQL**: A query demonstrating window functions (`SUM() OVER`, `RANK() OVER`), filtering, and sorting.
    *   **Perl**: A log-parsing script utilizing regular expressions to count IP addresses.
    *   **Shell Script**: A Bash script demonstrating directory creation, archiving (`tar`), and file cleanup (`find ... -delete`).
3.  **File Writing**: Writes the HTML content to `multi_language_samples.html` using UTF-8 encoding.
4.  **PDF Compilation**: Instantiates `weasyprint.HTML` with the generated HTML file and calls `.write_pdf()` to render `multi_language_samples.pdf`.
5.  **Completion**: Prints `"PDF generated successfully."` to the standard output.
