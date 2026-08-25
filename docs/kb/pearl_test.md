# `pearl_test.pl`

This document provides an overview of the `pearl_test.pl` script, its purpose, and its execution behavior.

## File Purpose

The `pearl_test.pl` script is a simple, interactive command-line utility written in Perl. It demonstrates basic Perl operations, including printing to the console, reading user input, conditional logic, and looping.

## Public Functions/Procedures

This script does not define any reusable functions or procedures. It consists of a single, top-to-bottom sequence of commands.

## Execution Behavior

When executed, the script performs the following actions in sequence:

1.  **Prints a Welcome Message**: The script first prints the static string `Hello, World!` to standard output, followed by a newline.

    ```perl
    # Print a welcome message
    print "Hello, World!\n";
    ```

2.  **Prompts for User Input**: It then prompts the user for their name by printing `Please enter your name: `.

    ```perl
    # Ask for the user's name
    print "Please enter your name: ";
    ```

3.  **Reads User Input**: The script waits for the user to type their name and press Enter. The input is read from `STDIN` and stored in the `$name` variable. The `chomp()` function is used to remove the trailing newline character from the input.

    ```perl
    my $name = <STDIN>;
    chomp($name); # Remove the trailing newline character
    ```

4.  **Conditional Greeting**: The script evaluates the `$name` variable.
    *   If the user provided no input (i.e., `$name` is an empty string), it prints `Hello, stranger!`.
    *   Otherwise, it prints a personalized greeting: `Nice to meet you, [name]!`, where `[name]` is the value provided by the user.

    ```perl
    # Greet the user conditionally
    if ($name eq "") {
        print "Hello, stranger!\n";
    } else {
        print "Nice to meet you, $name!\n";
    }
    ```

5.  **Loop Demonstration**: Finally, the script prints `Counting to 3:` and then executes a `foreach` loop that iterates from 1 to 3. In each iteration, it prints `Count: ` followed by the current number of the iteration (1, 2, and 3).

    ```perl
    # Simple loop example
    print "\nCounting to 3:\n";
    foreach my $i (1..3) {
        print "Count: $i\n";
    }
    ```
