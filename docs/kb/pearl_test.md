# pearl_test.pl

This document provides an overview of the `pearl_test.pl` script, detailing its purpose, execution flow, and behavior.

## Overview

`pearl_test.pl` is a simple, interactive Perl script designed to demonstrate basic input/output operations, string sanitization, conditional logic, and loop structures. It does not define any custom classes, objects, or functions.

## Execution and Dependencies

The script is executed using a standard Perl interpreter. It enforces strict coding standards and warnings:

```perl
use strict;
use warnings;
```

### Inputs
* **Standard Input (`STDIN`)**: The script prompts the user to enter their name interactively during execution.

### Outputs
* **Standard Output (`STDOUT`)**: The script prints greeting messages, prompts, and a sequential count to the console.

---

## Behavior and Logic Flow

The script executes sequentially from top to bottom through the following steps:

### 1. Welcome Message
The script prints an initial greeting to the console:
```
Hello, World!
```

### 2. User Input and Sanitization
The script prompts the user for their name and reads the input from standard input (`STDIN`). It then uses `chomp` to remove any trailing newline character from the input:
```perl
print "Please enter your name: ";
my $name = <STDIN>;
chomp($name);
```

### 3. Conditional Greeting
The script evaluates the sanitized input:
* **If the input is empty** (`$name eq ""`), it prints:
  ```
  Hello, stranger!
  ```
* **If the input is not empty**, it prints a personalized greeting:
  ```
  Nice to meet you, <name>!
  ```

### 4. Loop Demonstration
Finally, the script prints a header and executes a `foreach` loop to count from 1 to 3, printing each iteration:
```
Counting to 3:
Count: 1
Count: 2
Count: 3
```

---

## Functions and Procedures

There are no user-defined functions, subroutines, or procedures in this script. All logic is executed inline.
