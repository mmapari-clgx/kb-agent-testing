<!-- kb-agent:source-sha256=0d45d5a2da8d2810749bf9e4223ec5895f7fa423628e91d4c276877d75bfaeca -->
# pearl_test.pl

This document provides an overview of the `pearl_test.pl` script, detailing its purpose, execution flow, and behavior.

## Overview

`pearl_test.pl` is a basic, interactive Perl script. It serves as a simple demonstration or test script within the codebase to verify the Perl runtime environment, basic standard input/output (I/O) operations, conditional branching, and loop execution.

## Execution and Usage

The script is designed to be executed from the command line:

```bash
perl pearl_test.pl
```

Or, if the file has executable permissions:

```bash
./pearl_test.pl
```

## Code Behavior and Logic Flow

The script executes sequentially as follows:

1. **Environment Initialization**:
   * Uses the `#!/usr/bin/env perl` shebang to locate the Perl interpreter.
   * Enables strict code references and safety checks with `use strict;`.
   * Enables compile-time and run-time warnings with `use warnings;`.

2. **Initial Greeting**:
   * Prints `Hello, World!` followed by a newline to the standard output.

3. **User Input Processing**:
   * Prints the prompt `Please enter your name: ` (without a trailing newline).
   * Reads a line of input from standard input (`<STDIN>`) and assigns it to the scalar variable `$name`.
   * Calls `chomp($name)` to remove any trailing newline character from the input.

4. **Conditional Greeting**:
   * **If the input is empty** (`$name eq ""`):
     * Prints `Hello, stranger!` to standard output.
   * **If the input is not empty**:
     * Prints `Nice to meet you, <name>!` (where `<name>` is the value entered by the user).

5. **Loop Demonstration**:
   * Prints a section header: `Counting to 3:` preceded by a newline.
   * Executes a `foreach` loop iterating through the range `1..3`.
   * During each iteration, prints `Count: <i>` (where `<i>` is the current integer from 1 to 3).

## Functions and Procedures

There are no custom classes, packages, functions, or subroutines defined in this script. All logic is executed inline within the main body of the script.
