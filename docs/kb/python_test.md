<!-- kb-agent:source-sha256=8f1989088335800e8109f5e8f5024559a3d3071a256c3dcfea7439dacd4b35e8 -->
# python_test.py

This script generates a multi-language programming reference guide in both HTML and PDF formats. It embeds syntax-highlighted code snippets for Python, SQL, Perl, and Shell Scripting into an HTML template, writes it to disk, and compiles it into a styled PDF document using the `weasyprint` library.

## Dependencies

The script relies on the following external library:
*   `weasyprint` (specifically the `HTML` class for PDF generation)

---

## Execution Flow and Behavior

When executed, the script performs the following steps:

1.  **Initialization Message**: Prints `"Getting start with KB Agent"` to the standard output.
2.  **HTML Content Definition**: Defines a multi-line string (`html_content`) containing:
    *   An embedded CSS stylesheet configured for A4 page layout, print margins, and syntax highlighting colors (e.g., keywords, strings, comments).
    *   A header titled "Multi-Language Scripting Reference".
    *   Four code snippet sections:
        *   **Python**: A sample script demonstrating JSON parsing, file I/O, and error handling.
        *   **SQL**: A query demonstrating window functions (`SUM() OVER`, `RANK() OVER`) and filtering.
        *   **Perl**: A log-parsing script using regular expressions to count IP addresses.
        *   **Shell Script**: A Bash backup script demonstrating directory creation, archiving (`tar`), and file rotation (`find ... -delete`).
3.  **HTML File Generation**: Writes the HTML content to a local file named `multi_language_samples.html` using UTF-8 encoding.
4.  **PDF Compilation**: Uses `weasyprint.HTML` to read the generated HTML file and render it to a PDF file named `multi_language_samples.pdf`.
5.  **Completion Message**: Prints `"PDF generated successfully."` to the standard output.

---

## Output Files

The script produces two files in the execution directory:

| File Name | Format | Description |
| :--- | :--- | :--- |
| `multi_language_samples.html` | HTML | The raw HTML document containing the styled reference guide. |
| `multi_language_samples.pdf` | PDF | The compiled, print-ready PDF version of the reference guide. |

---

## Classes and Functions

*   **Classes**: None
*   **Functions**: None
