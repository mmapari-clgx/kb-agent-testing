# pearl_test.pl

This document provides an overview of the `pearl_test.pl` script, a basic interactive Perl utility.

## Overview

The `pearl_test.pl` script is a simple command-line utility designed to demonstrate basic Perl syntax, including standard input/output (I/O), string sanitization, conditional branching, and basic looping. 

The script enforces strict variable declarations and warnings using:
* `use strict;`
* `use warnings;`

---

## Execution Flow

When executed, the script performs the following steps sequentially:

1. **Welcome Message**
   Prints a standard greeting to the console:
   ```text
   Hello, World!
   ```

2. **User Input Collection**
   Prompts the user with the message `Please enter your name: ` and waits for input from standard input (`STDIN`).

3. **Input Sanitization**
   Applies the `chomp` function to the input variable `$name` to remove any trailing newline character.

4. **Conditional Greeting**
   * **If the input is empty** (the user pressed Enter without typing a name):
     Prints `Hello, stranger!`.
   * **If the input is not empty**:
     Prints `Nice to meet you, <name>!` (where `<name>` is the sanitized user input).

5. **Counting Loop**
   Prints a header `Counting to 3:` and executes a `foreach` loop iterating through the range `1..3`. For each iteration, it prints:
   ```text
   Count: <index>
   ```

---

## Functions and Procedures

This script does not define any custom packages, classes, functions, or subroutines. All logic is executed sequentially in the main body of the script.
