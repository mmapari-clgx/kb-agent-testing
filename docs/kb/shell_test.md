<!-- kb-agent:source-sha256=247aa523c663360d25d87fa657ea12ce7442a03344a94d946b6b75a112a7ef65 -->
# shell_test.sh

The `shell_test.sh` script (internally referred to in comments as `sys_utility.sh`) is a utility script designed to perform a system disk space check and simulate a file backup process for text files within a specified directory.

## Usage

```bash
./shell_test.sh [target_directory]
```

### Arguments

| Argument | Type | Description | Default Value |
| :--- | :--- | :--- | :--- |
| `target_directory` | String (Path) | *Optional.* The directory containing the `.txt` files to be backed up. | `$HOME/Documents` |

---

## Configuration and Environment

*   **Shell Options**: The script executes with `set -e` enabled, meaning it will exit immediately if any command returns a non-zero exit status.
*   **Colorized Output**: The script defines ANSI escape codes for color-coded terminal output:
    *   `GREEN` (`\033[0;32m`): Used for successful operations.
    *   `YELLOW` (`\033[1;33m`): Used for section headers and status updates.
    *   `RED` (`\033[0;31m`): Used for warnings and errors.
    *   `NC` (`\033[0m`): Resets the terminal color.

---

## Execution Flow

### 1. Target Directory Validation
The script assigns the target directory from the first command-line argument. If no argument is provided, it defaults to `$HOME/Documents`. 

It then verifies if the directory exists:
*   If the directory **does not exist**, it prints an error message in red and exits with status `1`.
*   If the directory **exists**, execution continues.

### 2. Disk Space Check
The script checks the disk usage of the root partition (`/`):
1.  It runs `df -h /` to get disk space statistics.
2.  It parses the output using `awk` to extract the capacity percentage (column 5 of the second row).
3.  It strips the `%` symbol using `sed` to isolate the integer value, storing it in `DISK_USAGE`.
4.  It evaluates the usage:
    *   If `DISK_USAGE` is **greater than 85**, it prints a critical warning in red.
    *   If `DISK_USAGE` is **85 or lower**, it prints a safe limit confirmation in green.

### 3. Simulated Backup Process
The script simulates backing up `.txt` files located directly inside the target directory:
1.  It initializes a counter `FILE_COUNT` to `0`.
2.  It loops through all files matching the glob pattern `"$TARGET_DIR"/*.txt`.
3.  For each match, it verifies if the file actually exists (to handle cases where the glob pattern does not resolve to any files).
4.  If a valid `.txt` file is found, it prints the base name of the file and increments `FILE_COUNT`.
5.  After the loop completes:
    *   If `FILE_COUNT` is `0`, it prints a message stating no `.txt` files were found.
    *   If `FILE_COUNT` is greater than `0`, it prints a success message in green indicating the total number of files processed.

---

## Exit Codes

| Exit Code | Description |
| :--- | :--- |
| `0` | Script completed successfully. |
| `1` | The specified `target_directory` does not exist. |
| *Non-zero* | Any command failure during execution (due to `set -e`). |
