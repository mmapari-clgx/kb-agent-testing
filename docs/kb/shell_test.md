# shell_test.sh

## Overview

The `shell_test.sh` script is a system utility that performs two main functions: it checks the disk space usage of the root filesystem and simulates a backup process for text files within a specified directory. The script provides color-coded console output to indicate status and warnings.

## Usage

The script can be executed directly from the shell. It accepts an optional command-line argument to specify the target directory for the simulated backup.

```shell
./shell_test.sh [target_directory]
```

## Parameters

| Parameter | Type | Description | Default |
| :--- | :--- | :--- | :--- |
| `[target_directory]` | String | The absolute or relative path to the directory for the backup simulation. The script will look for `.txt` files in this location. | `$HOME/Documents` |

The script uses the first positional parameter (`$1`) as the target directory. If no parameter is provided, it defaults to the current user's `Documents` directory, as defined by `TARGET_DIR="${1:-$HOME/Documents}"`.

## Behavior

The script executes the following steps in order:

1.  **Initialization**:
    *   Sets the `-e` option, which causes the script to exit immediately if any command fails.
    *   Defines shell variables for color-coded output (Green, Yellow, Red).

2.  **Target Directory Resolution**:
    *   Assigns the `TARGET_DIR` variable based on the first positional argument. If no argument is supplied, it defaults to `$HOME/Documents`.

3.  **Directory Validation**:
    *   It verifies that the `TARGET_DIR` exists using `if [ ! -d "$TARGET_DIR" ]`.
    *   If the directory does not exist, it prints a red error message and exits with a status code of `1`.

4.  **Disk Usage Check**:
    *   The script checks the disk usage of the root filesystem (`/`).
    *   It extracts the percentage value using the command `df -h / | awk 'NR==2 {print $5}' | sed 's/%//'`.
    *   If the usage is greater than 85% (`if [ "$DISK_USAGE" -gt 85 ]`), it prints a critical warning message in red.
    *   Otherwise, it prints a confirmation that disk usage is within safe limits in green.

5.  **Simulated Backup**:
    *   The script iterates through all files ending with the `.txt` extension within the `TARGET_DIR` (`for file in "$TARGET_DIR"/*.txt`).
    *   A check `if [ -e "$file" ]` is performed to handle cases where no `.txt` files match the glob pattern.
    *   For each `.txt` file found, it prints a "Backing up..." message and increments a file counter.
    *   After the loop, if the file count is zero, it reports that no `.txt` files were found.
    *   If one or more files were processed, it prints a success message indicating the total number of files handled.

6.  **Completion**:
    *   The script concludes by printing a "Script Completed Successfully" message.

## Exit Codes

*   **1**: The specified `target_directory` does not exist.
