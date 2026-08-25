# `pearl_test.pl`

This document outlines the functionality of the `pearl_test.pl` script.

## Purpose

This script serves as a basic demonstration of Perl syntax and interactive command-line behavior. It is not part of a larger ETL process but rather a standalone example.

The script performs the following actions in sequence:
1.  Prints a static "Hello, World!" message.
2.  Prompts the user to enter their name and reads the input from standard input.
3.  Prints a personalized greeting based on the user's input.
4.  Executes a simple `foreach` loop, printing a count from 1 to 3.

## Public Functions/Procedures

This script does not define any public functions or procedures. It consists of a single, top-level sequence of executable statements.

## Execution Behavior

When executed from the command line, the script will:

1.  Immediately print the line `Hello, World!` to standard output.
2.  Print the prompt `Please enter your name: ` without a trailing newline.
3.  Wait for the user to provide input via `STDIN` and press Enter. The input is stored in the `$name` variable. The `chomp` function is used to remove the trailing newline character from the input.
4.  Evaluate the `$name` variable:
    *   If the user provided no input (i.e., `$name` is an empty string `""`), the script prints `Hello, stranger!`.
    *   Otherwise, it prints `Nice to meet you, $name!`, where `$name` is the value provided by the user.
5.  Print a blank line, followed by the line `Counting to 3:`.
6.  Iterate through the numbers 1, 2, and 3, printing `Count: 1`, `Count: 2`, and `Count: 3` on successive lines.
