# pearl_test.pl

This document provides an overview of the `pearl_test.pl` script, a basic interactive Perl script used to verify environment setup and demonstrate simple input/output operations.

## Overview

The `pearl_test.pl` script is a utility script written in Perl. It performs basic console I/O operations, including reading from standard input (`STDIN`), executing conditional logic, and running a simple loop. 

## Execution and Environment

- **Interpreter**: The script uses the system's default Perl interpreter via `#!/usr/bin/env perl`.
- **Pragmas**: 
  - `use strict;` - Enforces strict vars, subs, and refs.
  - `use warnings;` - Enables optional warnings for cleaner execution.

## Behavior and Logic Flow

The script executes sequentially through the following steps:

### 1. Welcome Message
The script prints a standard greeting to the console:
```
Hello, World!
```

### 2. User Input and Conditional Greeting
The script prompts the user for their name and reads the input from `STDIN`:
1. Prints: `Please enter your name: `
2. Reads the input line into the variable `$name`.
3. Trims the trailing newline character using `chomp($name)`.
4. Evaluates the input:
   - **If the input is empty** (`$name eq ""`): Prints `Hello, stranger!`
   - **Otherwise**: Prints `Nice to meet you, <name>!` (where `<name>` is the entered string).

### 3. Counting Loop
The script prints a header and executes a simple loop:
1. Prints: `Counting to 3:`
2. Iterates through the range `1..3` using a `foreach` loop.
3. For each iteration, prints: `Count: <i>` (where `<i>` is the current number in the range).

## Inputs and Outputs

### Inputs
- **Standard Input (`STDIN`)**: Expects a string representing the user's name when prompted.

### Outputs
- **Standard Output (`STDOUT`)**: Prints the welcome message, prompt, conditional greeting, and counting loop sequence.
