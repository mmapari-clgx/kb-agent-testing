# `shell_test.sh`

## Overview

This shell script performs two main system utility tasks: it checks the disk space usage of the root filesystem and simulates a backup process for text files in a specified directory. The script provides color-coded console output to indicate status, warnings, and errors.

## Usage

The script can be executed with an optional command-line argument to specify the target directory.

```shell
./shell_test.sh [target_directory]
```

## Parameters

| Parameter | Type | Description | Default |
| :--- | :--- | :--- | :--- |
| `[target_directory]` | String | The absolute or relative path to the directory for the backup simulation. The script will look for `.txt` files within this directory. | `$HOME/Documents` |

This is a positional parameter (`$1`). If it is not provided, the script defaults to using the current user's `Documents` directory.

## Behavior

The script executes the following steps in order:

1.  **Initialization**:
    *   Sets the `-e` option, which causes the script to exit immediately if any command fails.
    *   Defines shell variables for `GREEN`, `YELLOW`, `RED`, and `NC` (No Color) to format console output.
    *   Assigns the `TARGET_DIR` variable. It uses the first positional argument (`$1`) if provided; otherwise, it defaults to `$HOME/Documents`.

2.  **Directory Validation**:
    *   It verifies that the `TARGET_DIR` exists using `if [ ! -d "$TARGET_DIR" ]`.
    *   If the directory does not exist, the script prints a red error message and exits with a status code of `1`.

3.  **Disk Usage Check**:
    *   The script checks the disk usage of the root filesystem (`/`).
    *   It uses `df -h / | awk 'NR==2 {print $5}' | sed 's/%//'` to extract the usage percentage as an integer.
    *   It prints the current usage percentage.
    *   If the usage is greater than 85%, it prints a "critically high" warning in red.
    *   Otherwise, it prints a confirmation that usage is within safe limits in green.

4.  **Backup Simulation**:
    *   The script announces the start of the backup simulation.
    *   It iterates through all files matching the pattern `"$TARGET_DIR"/*.txt`.
    *   For each potential match, it first confirms the file exists with `if [ -e "$file" ]`. This correctly handles the case where no `.txt` files are found.
    *   For each existing `.txt` file, it prints a "Backing up..." message with the file's base name and increments a `FILE_COUNT` counter.

5.  **Completion Summary**:
    *   After the loop, it checks the value of `FILE_COUNT`.
    *   If `FILE_COUNT` is `0`, it reports that no `.txt` files were found in the target directory.
    *   If one or more files were processed, it prints a green success message indicating the total number of files.
    *   Finally, it prints a "Script Completed Successfully" message and exits.
