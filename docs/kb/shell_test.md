<!-- kb-agent:source-sha256=247aa523c663360d25d87fa657ea12ce7442a03344a94d946b6b75a112a7ef65 -->
# shell_test.sh

The `shell_test.sh` script (internally referred to as `sys_utility.sh`) is a utility script designed to perform a system disk space check on the root partition and simulate a backup process for text files within a specified directory.

## Execution Settings

The script begins with the following shell configuration:
*   `set -e`: Instructs the shell to exit immediately if any command exits with a non-zero status.

It also defines ANSI color codes for formatted terminal output:
*   `GREEN` (`\033[0;32m`)
*   `YELLOW` (`\033[1;33m`)
*   `RED` (`\033[0;31m`)
*   `NC` (No Color / Reset)

---

## Usage and Parameters

The script accepts a single optional positional parameter:

```bash
./shell_test.sh [target_directory]
```

| Parameter | Position | Type | Description | Default Value |
| :--- | :--- | :--- | :--- | :--- |
| `target_directory` | `$1` | String | The path to the directory containing `.txt` files to process. | `$HOME/Documents` |

---

## Detailed Behavior and Logic Flow

### 1. Target Directory Validation
*   The script assigns the target directory to the variable `TARGET_DIR`. If no argument is provided, it defaults to `$HOME/Documents`.
*   It checks if the directory exists using the `[ ! -d "$TARGET_DIR" ]` condition.
*   If the directory does not exist, the script prints an error message in red and exits with status `1`.

### 2. Disk Usage Check
*   The script checks the disk usage of the root file system (`/`) using the command:
    ```bash
    df -h / | awk 'NR==2 {print $5}' | sed 's/%//'
    ```
    This extracts the usage percentage as an integer and stores it in `DISK_USAGE`.
*   It compares `DISK_USAGE` against a threshold of **85%**:
    *   **Usage > 85%**: Prints a warning message in red: `Warning: Disk usage is critically high!`.
    *   **Usage ≤ 85%**: Prints a confirmation message in green: `Disk usage is within safe limits.`.

### 3. Simulated Backup Process
*   The script initializes a counter `FILE_COUNT` to `0`.
*   It iterates over all files matching the glob pattern `"$TARGET_DIR"/*.txt`.
*   For each match, it verifies if the file actually exists using `[ -e "$file" ]` (to safely handle cases where the glob pattern does not match any files).
*   If a valid `.txt` file is found:
    *   It prints `Backing up: <filename>...` using the `basename` of the file.
    *   It increments `FILE_COUNT` by 1.
*   After completing the loop:
    *   If `FILE_COUNT` is `0`, it prints: `No .txt files found to back up in <TARGET_DIR>.`
    *   If `FILE_COUNT` is greater than `0`, it prints a success message in green indicating the total number of processed files.

### 4. Completion
*   If all steps complete without encountering a non-zero exit status, the script prints a success message and exits.
