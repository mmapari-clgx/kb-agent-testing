# shell_test.sh

The `shell_test.sh` script (internally documented as `sys_utility.sh`) is a utility script designed to perform a system disk space check on the root partition and simulate a file backup process for text files within a specified target directory.

---

## Usage

```bash
./shell_test.sh [target_directory]
```

### Parameters

*   **`target_directory`** *(Optional)*: The path to the directory containing the text files to be backed up. If not provided, the script defaults to `$HOME/Documents`.

---

## Configuration and Environment

### Shell Options
*   **`set -e`**: The script is configured to exit immediately if any command exits with a non-zero status.

### Color Codes
The script defines several ANSI escape codes for color-coded console output:
*   `GREEN` (`\033[0;32m`): Used for successful operations and safe status messages.
*   `YELLOW` (`\103[1;33m`): Used for section headers and script boundaries.
*   `RED` (`\033[0;31m`): Used for errors and critical warnings.
*   `NC` (`\033[0m`): Resets the console color.

---

## Execution Flow

### 1. Target Directory Resolution and Validation
1. The script assigns the target directory path to the variable `TARGET_DIR`. It uses the first command-line argument (`$1`) if provided; otherwise, it defaults to `$HOME/Documents`.
2. It checks if the resolved `TARGET_DIR` exists and is a directory (`[ ! -d "$TARGET_DIR" ]`).
3. If the directory does not exist, the script prints an error message in red and exits with status `1`.

### 2. Disk Space Check
1. The script queries the disk usage of the root file system (`/`) using the `df -h /` command.
2. It parses the output using `awk 'NR==2 {print $5}'` to extract the capacity percentage from the second line, and strips the `%` symbol using `sed 's/%//'`.
3. The resulting integer is stored in the `DISK_USAGE` variable.
4. The script evaluates the usage:
    *   If `DISK_USAGE` is strictly greater than `85`, it prints a critical warning in red.
    *   Otherwise, it prints a message in green indicating that disk usage is within safe limits.

### 3. Simulated Backup Process
1. The script initializes a counter variable `FILE_COUNT` to `0`.
2. It iterates over all files matching the glob pattern `"$TARGET_DIR"/*.txt`.
3. For each match, it verifies if the file actually exists (`[ -e "$file" ]`) to handle cases where the glob pattern does not match any files.
4. If a valid `.txt` file is found:
    *   It prints a message indicating the file is being backed up (using `basename` to display only the filename).
    *   It increments the `FILE_COUNT` counter.
5. After completing the loop:
    *   If `FILE_COUNT` is `0`, it prints a message stating that no `.txt` files were found.
    *   Otherwise, it prints a success message in green displaying the total number of processed files.

---

## Exit Codes

*   **`0`**: The script completed successfully.
*   **`1`**: The specified target directory does not exist.
*   **Other Non-Zero Codes**: Any command failure during execution will trigger an immediate exit with that command's exit status due to `set -e`.
