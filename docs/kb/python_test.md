# `python_test.py`

This script generates a PDF document (`multi_language_samples.pdf`) that serves as a multi-language code reference guide. The content, including code snippets for Python, SQL, Perl, and Shell Script, is hardcoded within an HTML string in the script.

The script first writes this HTML content to an intermediate file, `multi_language_samples.html`. It then uses the `weasyprint` library to convert the HTML file into the final PDF.

## Script Behavior

When executed, the script performs the following actions:
1.  Defines a multi-line string `html_content` containing a styled HTML5 document. This document includes formatted code samples for Python, SQL, Perl, and Shell Script.
2.  Writes the content of `html_content` to a new file named `multi_language_samples.html` in the current working directory.
3.  Uses the `weasyprint.HTML` class to read and parse `multi_language_samples.html`.
4.  Calls the `write_pdf` method to render the parsed HTML into a PDF file named `multi_language_samples.pdf` in the current working directory.
5.  Prints the message "PDF generated successfully." to standard output upon successful completion.

This script has an external dependency on the `weasyprint` library.
