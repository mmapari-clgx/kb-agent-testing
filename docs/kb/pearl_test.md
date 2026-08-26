# pearl_test.pl

This document provides technical documentation for the `pearl_test.pl` script. 

The script is a simple, procedural Perl program designed to demonstrate basic interactive input/output (I/O), conditional logic, and loop control.

## Overview

The script runs sequentially from top to bottom. It enforces strict variable declarations and warnings to ensure code quality and safety.

### Environment Requirements
* **Interpreter:** Perl (configured via `#!/usr/bin/env perl`)
* **Pragmas Enabled:**
  * `use strict;` — Restricts unsafe constructs (forces variable declaration).
  * `use warnings;` — Enables detailed compile-time and run-time warnings.

---

## Code Structure & Entities

* **Classes/Objects:** None
* **Functions/Procedures:** None (procedural execution flow)

---

## Execution Flow and Behavior

The script executes the following steps in order:

1. **Welcome Message**
   Prints the string `"Hello, World!\n"` to standard output.

2. **User Input Collection**
   * Prompts the user with `"Please enter your name: "`.
   * Reads a line of input from standard input (`<STDIN>`) and assigns it to the scalar variable `$name`.
   * Calls `chomp($name)` to remove any trailing newline character from the input.

3. **Conditional Greeting**
   * **If the input is empty** (`$name eq ""`):
     Prints `"Hello, stranger!\n"`.
   * **Otherwise** (if the user entered a name):
     Prints `"Nice to meet you, [name]!\n"`, interpolating the value of `$name`.

4. **Loop Demonstration**
   * Prints a header: `"\nCounting to 3:\n"`.
   * Executes a `foreach` loop iterating through the range `1..3`.
   * For each iteration, it prints `"Count: $i\n"`, where `$i` is the current loop index (1, 2, and 3).
