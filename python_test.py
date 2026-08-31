# Let's create a comprehensive sample zip or archive containing sample files for python, sql, perl, and shell script.
# Or better yet, we can create a single nicely formatted Markdown document or a structured Python script containing all four languages, 
# or multiple files combined in a zip, or an Excel spreadsheet / PDF guide. 
# Wait, the prompt says "create a sample file with for python, sql, perl, shell script". 
# Let's create a Python script that generates a multi-tab Excel workbook or a comprehensive PDF code reference guide, or a ZIP archive with individual files (.py, .sql, .pl, .sh).
# Let's make a comprehensive PDF programming snippets cheat sheet/guide covering Python, SQL, Perl, and Shell Script.

import os
from weasyprint import HTML

print("Hello Agent")

print("Getting start with KB Agent")

html_content = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
    @page {
        size: A4;
        margin: 15mm;
        background-color: #f7f9fa;
        @bottom-right {
            content: "Page " counter(page);
            font-family: 'Courier New', monospace;
            font-size: 8pt;
            color: #666;
        }
    }
    *, *::before, *::after {
        box-sizing: border-box;
    }
    body {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        color: #333;
        margin: 0;
        padding: 0;
        font-size: 10pt;
        line-height: 1.4;
    }
    .header {
        background: #1e293b;
        color: white;
        padding: 20px 25px;
        margin: -15mm -15mm 20px -15mm;
        border-bottom: 4px solid #3b82f6;
    }
    .header h1 {
        margin: 0 0 5px 0;
        font-size: 20pt;
        font-weight: 700;
        letter-spacing: -0.5px;
    }
    .header p {
        margin: 0;
        color: #94a3b8;
        font-size: 10pt;
    }
    h2 {
        color: #1e293b;
        font-size: 13pt;
        border-left: 4px solid #3b82f6;
        padding-left: 8px;
        margin-top: 25px;
        margin-bottom: 10px;
        page-break-after: avoid;
    }
    p {
        margin: 0 0 10px 0;
    }
    pre {
        background: #0f172a;
        color: #e2e8f0;
        padding: 12px 15px;
        border-radius: 6px;
        font-family: 'Courier New', Courier, monospace;
        font-size: 9pt;
        line-height: 1.5;
        overflow-x: auto;
        margin: 0 0 15px 0;
        border: 1px solid #334155;
        page-break-inside: avoid;
    }
    .keyword { color: #93c5fd; font-weight: bold; }
    .string { color: #86efac; }
    .comment { color: #64748b; font-style: italic; }
    .function { color: #fca5a5; }
    .number { color: #fde047; }
</style>
</head>
<body>

<div class="header">
    <h1>Multi-Language Scripting Reference</h1>
    <p>Sample code snippets for Python, SQL, Perl, and Shell Scripting</p>
</div>

<h2>1. Python Sample (.py)</h2>
<p>A sample script demonstrating file I/O, error handling, and JSON parsing in Python.</p>
<pre><code><span class="keyword">import</span> json
<span class="keyword">import</span> sys

<span class="keyword">def</span> <span class="function">process_data</span>(filepath):
    <span class="keyword">try</span>:
        <span class="keyword">with</span> <span class="function">open</span>(filepath, <span class="string">'r'</span>) <span class="keyword">as</span> f:
            data = json.<span class="function">load</span>(f)
            <span class="keyword">for</span> item <span class="keyword">in</span> data.get(<span class="string">"records"</span>, []):
                <span class="function">print</span>(<span class="string">f"Processing ID: {item.get('id')} - Status: {item.get('status')}"</span>)
    <span class="keyword">except</span> FileNotFoundError:
        <span class="function">print</span>(<span class="string">f"Error: File {filepath} not found."</span>, file=sys.stderr)
    <span class="keyword">except</span> json.JSONDecodeError:
        <span class="function">print</span>(<span class="string">"Error: Invalid JSON format."</span>, file=sys.stderr)

<span class="keyword">if</span> __name__ == <span class="string">"__main__"</span>:
    <span class="function">process_data</span>(<span class="string">"config.json"</span>)</code></pre>

<h2>2. SQL Sample (.sql)</h2>
<p>A relational database query demonstrating aggregations, window functions, and filtering.</p>
<pre><code><span class="comment">-- Calculate running totals and rank employees by department salary</span>
<span class="keyword">SELECT</span> 
    department_id,
    employee_name,
    salary,
    <span class="function">SUM</span>(salary) <span class="keyword">OVER</span> (<span class="keyword">PARTITION BY</span> department_id) <span class="keyword">AS</span> dept_total_salary,
    <span class="function">RANK</span>() <span class="keyword">OVER</span> (<span class="keyword">PARTITION BY</span> department_id <span class="keyword">ORDER BY</span> salary <span class="keyword">DESC</span>) <span class="keyword">AS</span> salary_rank
<span class="keyword">FROM</span> 
    employees
<span class="keyword">WHERE</span> 
    status = <span class="string">'ACTIVE'</span>
    <span class="keyword">AND</span> hire_date >= <span class="string">'2022-01-01'</span>
<span class="keyword">ORDER BY</span> 
    department_id <span class="keyword">ASC</span>, 
    salary <span class="keyword">DESC</span>;</code></pre>

<h2>3. Perl Sample (.pl)</h2>
<p>A text processing script using Regular Expressions in Perl.</p>
<pre><code><span class="comment">#!/usr/bin/env perl</span>
<span class="keyword">use</span> strict;
<span class="keyword">use</span> warnings;

<span class="keyword">my</span> $filename = <span class="string">"access.log"</span>;
<span class="keyword">open</span>(<span class="keyword">my</span> $fh, <span class="string">'&lt;'</span>, $filename) <span class="keyword">or</span> <span class="keyword">die</span> <span class="string">"Could not open file '$filename' $!"</span>;

<span class="keyword">my</span> %ip_counts;
<span class="keyword">while</span> (<span class="keyword">my</span> $line = &lt;$fh&gt;) {
    <span class="comment"># Match standard IPv4 addresses in log lines</span>
    <span class="keyword">if</span> ($line =~ <span class="string">/^(\d{1,3}(?:\.\d{1,3}){3})/</span>) {
        $ip_counts{$1}++;
    }
}
<span class="keyword">close</span>($fh);

<span class="keyword">foreach</span> <span class="keyword">my</span> $ip (<span class="keyword">sort</span> { $ip_counts{$b} &lt;=&gt; $ip_counts{$a} } <span class="keyword">keys</span> %ip_counts) {
    <span class="keyword">print</span> <span class="string">"$ip: $ip_counts{$ip} requests\n"</span>;
}</code></pre>

<h2>4. Shell Script Sample (.sh)</h2>
<p>An automated backup and rotation script using Bash.</p>
<pre><code><span class="comment">#!/usr/bin/env bash</span>
<span class="keyword">set</span> -euo pipefail

BACKUP_DIR=<span class="string">"/var/backups/app"</span>
SOURCE_DIR=<span class="string">"/var/www/html"</span>
TIMESTAMP=\$(date +<span class="string">"%Y%m%d_%H%M%S"</span>)
ARCHIVE_NAME=<span class="string">"backup_\${TIMESTAMP}.tar.gz"</span>

<span class="keyword">mkdir</span> -p "\${BACKUP_DIR}"

echo <span class="string">"Starting backup of \${SOURCE_DIR}..."</span>
tar -czf "\${BACKUP_DIR}/\${ARCHIVE_NAME}" -C "\${SOURCE_DIR}" .

echo <span class="string">"Cleaning up backups older than 7 days..."</span>
find "\${BACKUP_DIR}" -name <span class="string">"backup_*.tar.gz"</span> -mtime +7 -delete

echo <span class="string">"Backup completed successfully: \${ARCHIVE_NAME}"</span></code></pre>

</body>
</html>
"""

html_path = "multi_language_samples.html"
pdf_path = "multi_language_samples.pdf"

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

HTML(filename=html_path).write_pdf(pdf_path)
print("PDF generated successfully.")
