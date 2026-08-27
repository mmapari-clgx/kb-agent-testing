# lite_llm_test.py

This file is a utility script that provides a function to generate the Fibonacci sequence and includes an interactive command-line interface (CLI) for testing.

Upon initial import or execution, the script prints a greeting message to the console:
```text
hi aruna im agent
```

---

## Functions

### `fibonacci`

Generates the first `n` terms of the Fibonacci sequence.

#### Syntax
```python
fibonacci(n)
```

#### Parameters
* **`n`** (*int*): The number of terms to generate. Must be a non-negative integer.

#### Exceptions Raised
* **`ValueError`**: Raised if `n` is not an instance of `int` or is less than `0`. The error message is:
  `"Number of terms must be a non-negative integer."`

#### Returns
* **`list`**: A list of integers containing the first `n` terms of the Fibonacci sequence.

#### Implementation Details
The function initializes the sequence with `a, b = 0, 1` and iteratively appends `a` to the sequence list while updating the values to `a, b = b, a + b` for `n` iterations.

---

## Execution Flow (CLI Usage)

When the script is executed directly (`__name__ == "__main__"`), it runs an interactive loop:

1. **User Input**: Prompts the user to enter the number of terms:
   ```text
   Enter the number of Fibonacci terms: 
   ```
2. **Generation**: Converts the input to an integer and calls `fibonacci(n_terms)`.
3. **Output**: Prints the resulting sequence:
   ```text
   Fibonacci sequence (<n_terms> terms): <sequence>
   ```
4. **Error Handling**: If a `ValueError` occurs (either from invalid integer conversion or from the `fibonacci` function's validation), the script catches the exception and prints:
   ```text
   Error: <error_message>
   ```
