print('This code is to access litellm api key')

# Fibonacci sequence generator in Python

def fibonacci(n):
    """
    Generate the first n terms of the Fibonacci sequence.
    :param n: Number of terms (must be a non-negative integer)
    :return: List containing the Fibonacci sequence
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Number of terms must be a non-negative integer.")

    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


if __name__ == "__main__":
    try:
        # Get user input
        n_terms = int(input("Enter the number of Fibonacci terms: "))
        
        # Generate and display the sequence
        fib_sequence = fibonacci(n_terms)
        print(f"Fibonacci sequence ({n_terms} terms): {fib_sequence}")

    except ValueError as e:
        print(f"Error: {e}")


