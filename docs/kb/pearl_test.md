<!-- kb-agent:source-sha256=0d45d5a2da8d2810749bf9e4223ec5895f7fa423628e91d4c276877d75bfaeca -->
# pearl_test.pl

This document provides technical documentation for the `pearl_test.pl` script.

## Overview

`pearl_test.pl` is a simple, interactive Perl script. It serves as a basic utility or environment verification script, demonstrating standard input/output (I/O) operations, string manipulation, conditional logic, and basic looping structures.

---

## Execution and Environment

* **Interpreter**: `/usr/bin/env perl`
* **Pragmas**: 
  * `use strict;` — Enforces strict vars, subs, and refs.
  * `use warnings;` — Enables optional warnings for debugging and code quality.

---

## Functions and Procedures

This script does not define any classes, packages, or subroutines. It executes sequentially from top to bottom.

---

## Script Behavior and Logic Flow

When executed, the script performs the following steps:

1. **Print Welcome Message**
   Outputs a standard greeting to the console:
   ```
   Hello, World!
   ```

2. **User Input Collection**
   * Prompts the user with: `Please enter your name: `
   * Reads a line of input from standard input (`STDIN`).
   * Uses `chomp` to strip the trailing newline character from the input, storing the result in the lexical variable `$name`.

3. **Conditional Greeting**
   * **If the input is empty** (`$name eq ""`):
     Prints `Hello, stranger!`
   * **If the input is not empty**:
     Prints `Nice to meet you, <name>!` (where `<name>` is the value entered by the user).

4. **Loop Demonstration**
   * Prints a header: `Counting to 3:`
   * Iterates through a range from 1 to 3 using a `foreach` loop, printing the current count on each iteration:
     ```text
     Count: 1
     Count: 2
     Count: 3
     ```
