# shell_test.sh

The `shell_test.sh` script (internally referred to as `sys_utility.sh`) is a utility script designed to perform a system disk space check on the root partition and simulate a backup process for text files within a specified target directory.

## Usage

```bash
./shell_test.sh [target_directory]
```

### Parameters

| Parameter | Position | Type | Required | Default Value | Description |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `target_directory` | `$1` | String | No | `$HOME/Documents` | The directory containing the `.txt` files to be processed during the simulated backup. |

---

## Script Configuration

*   **Fail-Fast Behavior**: The script executes `set -e`, meaning it will exit immediately if any command returns a non-zero exit status.
*   **Colorized Output**: The script defines ANSI escape codes for colorized terminal output:
    *   `GREEN` (`\033[0;32m`): Used for success messages.
    *   `YELLOW` (`\033[1;33m`): Used for headers and section dividers.
    *   `RED` (`\033[0;31m`): Used for errors and warning messages.
    *   `NC` (`\033[0m`): Resets the terminal color.

---

## Execution Flow and Behavior

### 1. Directory Validation
The script checks if the resolved `TARGET_DIR` exists and is a directory:
*   If the directory **does not exist**, it prints an error message in red and terminates execution with an exit code of `1`.
*   If the directory exists, execution continues.

### 2. Disk Space Check
The script checks the disk usage of the root file system (`/`):
1.  It extracts the usage percentage using the command:
    ```bash
    df -h / | awk 'NR==2 {print $5}' | sed 's/%//'
    ```
2.  The resulting integer is stored in the `DISK_USAGE` variable.
3.  The script evaluates the usage:
    *   If `DISK_USAGE` is **greater than 85%**, it prints a warning: `Warning: Disk usage is critically high!` in red.
    *   Otherwise, it prints: `Disk usage is within safe limits.` in green.

### 3. Simulated Backup Process
The script simulates a backup of text files within the `TARGET_DIR`:
1.  It iterates over all files matching the glob pattern `"$TARGET_DIR"/*.txt`.
2.  For each match, it verifies if the file actually exists (to handle cases where the glob pattern does not resolve to any files).
3.  If a valid `.txt` file is found:
    *   It prints `Backing up: <filename>...` (using `basename` to extract the file name).
    *   It increments the `FILE_COUNT` counter.
4.  After completing the loop:
    *   If `FILE_COUNT` is `0`, it prints: `No .txt files found to back up in <TARGET_DIR>.`
    *   If files were processed, it prints: `Successfully processed <FILE_COUNT> file(s).` in green.

### 4. Completion
Upon successful completion of all steps, the script prints a final completion message and exits with status `0`.
