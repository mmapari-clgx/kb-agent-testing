# lite_llm_test.py

This file contains a simple utility script that prints a greeting message, defines a function to generate a Fibonacci sequence, and provides an interactive command-line interface (CLI) to run the generator.

## Overview

Upon loading or execution, the script immediately prints a greeting message:
```text
hi aruna im agent
```

It contains a single utility function, `fibonacci`, and an execution block that allows users to input a number of terms and view the generated sequence.

---

## Functions

### `fibonacci(n)`

Generates the first `n` terms of the Fibonacci sequence.

#### Parameters
* **`n`** (`int`): The number of terms to generate. Must be a non-negative integer.

#### Returns
* **`list`**: A list of integers containing the generated Fibonacci sequence.

#### Exceptions Raised
* **`ValueError`**: Raised if `n` is not an instance of `int` or is less than `0` (with the message `"Number of terms must be a non-negative integer."`).

#### Behavior and Logic
1. Validates that the input `n` is a non-negative integer.
2. Initializes an empty list `sequence` and the first two Fibonacci numbers (`a = 0`, `b = 1`).
3. Iterates `n` times, appending the current value of `a` to the sequence and updating the values such that `a` becomes `b` and `b` becomes `a + b`.
4. Returns the populated `sequence` list.

---

## Execution Flow (`__main__`)

When the script is executed directly, it runs an interactive loop within a `try-except` block:

1. **User Input**: Prompts the user to enter the number of Fibonacci terms via standard input:
   ```text
   Enter the number of Fibonacci terms: 
   ```
2. **Generation**: Converts the input to an integer and calls `fibonacci(n_terms)`.
3. **Output**: Prints the resulting sequence:
   ```text
   Fibonacci sequence (<n_terms> terms): <fib_sequence>
   ```
4. **Error Handling**: If a `ValueError` is raised (either from invalid integer conversion or from the `fibonacci` function validation), it catches the exception and prints:
   ```text
   Error: <error_message>
   ```
