<!-- kb-agent:source-sha256=e74961d792bf2de8d8cdf260b1c0e08c7b011e43d80c62f0599d2296b3d98152 -->
# lite_llm_test.py

This file is a utility script that prints a greeting and provides a function to generate the Fibonacci sequence. It also includes a command-line interface (CLI) block to prompt users for input and display the generated sequence.

## Overview

Upon execution, the script immediately prints `'Hello World'` to the console. It defines a single utility function, `fibonacci(n)`, and provides an interactive execution block when run directly as a script.

---

## Functions

### `fibonacci(n)`

Generates a list containing the first `n` terms of the Fibonacci sequence.

#### Parameters
* **`n`** (`int`): The number of terms to generate. Must be a non-negative integer.

#### Returns
* **`list`**: A list of integers representing the generated Fibonacci sequence.

#### Exceptions Raised
* **`ValueError`**: Raised if `n` is not an integer or is less than `0` (with the message `"Number of terms must be a non-negative integer."`).

#### Behavior
The function initializes the sequence with the starting values $a = 0$ and $b = 1$. It loops `n` times, appending the current value of $a$ to the sequence and updating the terms using the relation $a, b = b, a + b$.

---

## Execution Flow (`__main__`)

When the script is executed directly, it performs the following steps:

1. Prints `'Hello World'` to the standard output.
2. Prompts the user via the console: `"Enter the number of Fibonacci terms: "`.
3. Attempts to cast the user input to an integer (`n_terms`).
4. Calls `fibonacci(n_terms)` to generate the sequence.
5. Prints the resulting sequence to the console: `Fibonacci sequence (<n_terms> terms): <sequence>`.
6. Catches any `ValueError` (either from invalid integer casting of the user input or from the validation inside the `fibonacci` function) and prints the error message: `Error: <error_message>`.
