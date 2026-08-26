# python_test.py

This Python script generates a styled, multi-language programming reference guide in both HTML and PDF formats. It embeds code snippets for Python, SQL, Perl, and Shell Scripting into an HTML template and compiles it into a print-ready PDF using the `weasyprint` library.

## Overview

The script performs the following high-level tasks:
1. Prints initialization messages to the console.
2. Defines a complete HTML document string containing CSS styling (optimized for A4 page layout) and syntax-highlighted code snippets.
3. Writes the HTML content to a local file named `multi_language_samples.html`.
4. Compiles the HTML file into a PDF document named `multi_language_samples.pdf` using WeasyPrint.

## Dependencies

The script relies on the following libraries:
* **`weasyprint`**: Used to render the HTML file into a PDF (`weasyprint.HTML`).
* **`os`**: Imported, but not explicitly used in the file generation logic.

## Generated Output Files

The script writes two files to the working directory:

| File Name | Format | Description |
| :--- | :--- | :--- |
| `multi_language_samples.html` | HTML | The raw HTML document containing the embedded CSS and code snippets. |
| `multi_language_samples.pdf` | PDF | The compiled PDF document, styled for A4 paper with custom page margins and footers. |

---

## Documented Code Snippets

The generated reference guide contains four distinct code examples:

### 1. Python Sample (`.py`)
Demonstrates basic file I/O, error handling (`try-except` blocks for `FileNotFoundError` and `json.JSONDecodeError`), and JSON parsing using the standard `json` library.

### 2. SQL Sample (`.sql`)
Demonstrates a relational database query utilizing:
* Window functions (`SUM() OVER` and `RANK() OVER` partitioned by department).
* Filtering (`WHERE` clause with date and status checks).
* Sorting (`ORDER BY`).

### 3. Perl Sample (`.pl`)
Demonstrates text processing and regular expressions:
* Opens and reads an Apache-style access log (`access.log`).
* Uses a regular expression to match and extract IPv4 addresses.
* Counts occurrences of each IP address using a hash map and prints the sorted results.

### 4. Shell Script Sample (`.sh`)
A Bash script demonstrating automated backup operations:
* Uses strict error handling (`set -euo pipefail`).
* Creates a timestamped tarball archive of a source directory.
* Cleans up backup archives older than 7 days using the `find` command.

---

## Execution Flow

When executed, the script runs sequentially:

1. Prints `"Hello World"` to the standard output.
2. Prints `"Getting start with KB Agent"` to the standard output.
3. Opens `multi_language_samples.html` in write mode with `utf-8` encoding and writes the HTML markup.
4. Invokes `HTML(filename="multi_language_samples.html").write_pdf("multi_language_samples.pdf")` to generate the PDF.
5. Prints `"PDF generated successfully."` to the standard output upon completion.
