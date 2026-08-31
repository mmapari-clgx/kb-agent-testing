# shell_test.sh

The `shell_test.sh` script (internally referred to as `sys_utility.sh` in its header) is a utility script designed to perform a system disk space check and simulate a file backup process for text files within a specified directory.

## System Behavior & Settings

- **Strict Error Handling**: The script executes with `set -e` enabled, meaning it will exit immediately if any command returns a non-zero exit status.
- **Visual Feedback**: The script defines ANSI color codes (`GREEN`, `YELLOW`, `RED`, and `NC` for reset) to format console output for warnings, errors, and success messages.

---

## Usage

```bash
./shell_test.sh [target_directory]
```

### Parameters

| Parameter | Position | Type | Description | Default Value |
| :--- | :--- | :--- | :--- | :--- |
| `target_directory` | `$1` (Optional) | String | The path to the directory containing `.txt` files to process. | `$HOME/Documents` |

---

## Execution Flow

### 1. Target Directory Validation
The script checks if the resolved `TARGET_DIR` exists as a directory:
- If the directory **does not exist**, it prints an error message in red and terminates immediately with an exit status of `1`.
- If the directory **exists**, execution continues.

### 2. Disk Space Check
The script checks the disk usage of the root partition (`/`):
1. It extracts the usage percentage using the command:
   ```bash
   df -h / | awk 'NR==2 {print $5}' | sed 's/%//'
   ```
2. It compares the resulting integer value against a threshold of **85%**:
   - **Usage > 85%**: Prints a warning message in red: `Warning: Disk usage is critically high!`.
   - **Usage ≤ 85%**: Prints a success message in green: `Disk usage is within safe limits.`.

### 3. Simulated Backup Process
The script simulates backing up all `.txt` files in the `TARGET_DIR`:
1. It iterates through all files matching the glob pattern `"$TARGET_DIR"/*.txt`.
2. For each matched item, it verifies that the file actually exists (to handle cases where no `.txt` files exist and the glob pattern remains unexpanded).
3. If a valid file is found:
   - It prints `Backing up: <filename>...` to the console.
   - It increments a counter (`FILE_COUNT`).
4. After the loop completes:
   - If **no files** were processed (`FILE_COUNT` is `0`), it prints: `No .txt files found to back up in <TARGET_DIR>.`
   - If **one or more files** were processed, it prints a success message in green: `Successfully processed <FILE_COUNT> file(s).`

### 4. Completion
Upon successful execution of all steps, the script prints a completion message and exits with status `0`.
