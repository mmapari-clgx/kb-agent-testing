# lite_llm_test.py

This file is a utility script that provides a function to generate the Fibonacci sequence and includes an interactive command-line interface (CLI) for testing the generator.

Upon initial import or execution, the script prints a greeting message:
```text
hi aruna im agent
```

---

## Functions

### `fibonacci(n)`

Generates the first `n` terms of the Fibonacci sequence.

#### Parameters
* **`n`** (`int`): The number of terms to generate. Must be a non-negative integer.

#### Returns
* **`list`**: A list of integers representing the Fibonacci sequence up to `n` terms.

#### Exceptions Raised
* **`ValueError`**: Raised if `n` is not an instance of `int` or if `n` is less than `0`. The error message is:
  `"Number of terms must be a non-negative integer."`

#### Behavior and Implementation
The function initializes the sequence with an empty list and sets the starting values of the sequence (`a = 0`, `b = 1`). It then iterates `n` times, appending the current value of `a` to the sequence and updating the values to the next terms in the sequence (`a, b = b, a + b`).

---

## Execution Flow (CLI Usage)

When the script is executed directly (`python lite_llm_test.py`), it runs an interactive loop in the terminal:

1. **User Input**: Prompts the user with `"Enter the number of Fibonacci terms: "` and attempts to cast the input to an integer.
2. **Generation**: Calls the `fibonacci` function with the provided integer.
3. **Output**: 
   * On success, prints the generated sequence: `Fibonacci sequence (<n_terms> terms): <sequence>`
   * On failure (e.g., if the input is not an integer or is a negative integer), catches the `ValueError` and prints: `Error: <error_message>`
