# shell_test.sh

This Bash script performs a system utility check consisting of a root partition disk space verification and a simulated backup of text files from a specified target directory.

## Overview

The script is configured to exit immediately if any command fails (`set -e`). It utilizes ANSI color codes (`GREEN`, `YELLOW`, `RED`, and `NC`) to format console output for readability.

## Usage

```bash
./shell_test.sh [target_directory]
```

### Parameters

| Parameter | Position | Type | Description | Default Value |
| :--- | :--- | :--- | :--- | :--- |
| `target_directory` | `$1` | String | The path to the directory containing `.txt` files to be backed up. | `$HOME/Documents` |

---

## Execution Flow and Behavior

### 1. Directory Verification
The script checks if the resolved `TARGET_DIR` exists as a directory:
* If the directory **does not exist**, it prints an error message in red and exits with status `1`.
* If the directory **exists**, execution continues.

### 2. Disk Space Check
The script evaluates the disk usage of the root file system (`/`):
* It extracts the usage percentage using `df -h /`, `awk`, and `sed`.
* If the root partition disk usage is strictly greater than **85%**, it prints a critical warning in red: `Warning: Disk usage is critically high!`.
* Otherwise, it prints a success message in green: `Disk usage is within safe limits.`.

### 3. Simulated Backup Process
The script simulates backing up text files within the `TARGET_DIR`:
* It iterates over all files matching the glob pattern `"$TARGET_DIR"/*.txt`.
* For each matching file, it verifies the file's existence (to handle cases where the glob pattern does not match any files).
* If files are found, it prints `Backing up: <filename>...` for each file and increments the `FILE_COUNT` tracker.
* **Outcome**:
  * If no `.txt` files are found, it prints: `No .txt files found to back up in <TARGET_DIR>.`
  * If `.txt` files are processed, it prints a success message in green indicating the total number of files processed.

### 4. Completion
Upon successful execution of all steps, the script prints a completion message in yellow and exits with status `0`.
