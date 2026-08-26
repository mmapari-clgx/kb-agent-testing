# lite_llm_test.py

The `lite_llm_test.py` script is a utility file containing a Fibonacci sequence generator and an interactive command-line interface (CLI) execution block. Upon loading or execution, the script immediately prints a greeting message: `"hi aruna im agent"`.

---

## Functions

### `fibonacci`

Generates a list containing the first `n` terms of the Fibonacci sequence.

#### Parameters
* **`n`** (`int`): The number of terms to generate. Must be a non-negative integer.

#### Returns
* **`list`**: A list of integers representing the generated Fibonacci sequence.

#### Exceptions Raised
* **`ValueError`**: Raised if `n` is not an instance of `int` or is less than `0`. The exception message is: `"Number of terms must be a non-negative integer."`

#### Behavior
The function initializes an empty list and starts the sequence with `a = 0` and `b = 1`. It loops `n` times, appending the current value of `a` to the sequence and updating the values to `a, b = b, a + b` at each iteration.

---

## Execution Flow (`__main__`)

When the script is executed directly, it runs an interactive loop within a `try-except` block:

1. **User Input**: Prompts the user to enter the number of terms:
   ```text
   Enter the number of Fibonacci terms: 
   ```
2. **Generation**: Converts the input to an integer and calls the `fibonacci` function.
3. **Output**: Prints the resulting sequence:
   ```text
   Fibonacci sequence (<n_terms> terms): <sequence>
   ```
4. **Error Handling**: Catches any `ValueError` (either from an invalid integer conversion during input or from the validation inside the `fibonacci` function) and prints the error message:
   ```text
   Error: <error_message>
   ```
