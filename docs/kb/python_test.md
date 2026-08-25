# `python_test.py`

## Overview

This script generates a PDF document named `multi_language_samples.pdf` that serves as a formatted code reference guide. The guide contains sample code snippets for Python, SQL, Perl, and Shell Script.

The script's functionality is self-contained. It defines the entire content of the guide as a static HTML string, writes this string to a temporary HTML file, and then uses the `weasyprint` library to convert the HTML file into a polished PDF.

## Execution Behavior

This script is intended to be executed directly. It does not define any functions or classes for external use. Upon execution, it performs the following actions sequentially:

1.  **Define Content**: A multi-line string variable, `html_content`, is defined. This string contains a complete HTML5 document with embedded CSS for styling and syntax highlighting. The body of the HTML includes pre-formatted code blocks for Python, SQL, Perl, and a Shell Script.
2.  **Write HTML File**: The script writes the contents of the `html_content` variable to a file named `multi_language_samples.html` in the current directory. This file is encoded in UTF-8.
3.  **Generate PDF**: It uses the `weasyprint` library to read and render the `multi_language_samples.html` file.
4.  **Write PDF File**: The rendered content is written to a new file named `multi_language_samples.pdf` in the current directory.
5.  **Log Success**: After the PDF is successfully created, the script prints the message `PDF generated successfully.` to standard output.

## Dependencies

-   **`weasyprint`**: This third-party library is required for converting the HTML content to a PDF.
-   **`os`**: This standard library is imported but not explicitly used in the provided source.

## Generated Files

-   **`multi_language_samples.html`**: An intermediate HTML file created in the script's working directory. It contains the raw, styled content that is used to generate the PDF.
-   **`multi_language_samples.pdf`**: The final output. A multi-page PDF document containing the formatted code snippets.
