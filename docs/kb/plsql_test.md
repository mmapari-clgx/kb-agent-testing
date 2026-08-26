# plsql_test.pkb

The `plsql_test.pkb` file implements the package body for `pkg_github_demo`. This package provides basic utility subprograms to print a welcome message and retrieve a static repository status.

## Package Information
* **Package Body Name:** `pkg_github_demo`
* **Language:** PL/SQL (Oracle)

---

## Subprograms

### `print_welcome` (Procedure)

This procedure prints a welcome message to the standard DBMS output.

#### Syntax
```sql
PROCEDURE print_welcome (p_user_name IN VARCHAR2);
```

#### Parameters
| Parameter Name | Mode | Data Type | Description |
| :--- | :--- | :--- | :--- |
| `p_user_name` | `IN` | `VARCHAR2` | The name of the user to welcome. |

#### Behavior and Implementation Details
* The procedure uses `DBMS_OUTPUT.PUT_LINE` to output the welcome message.
* It evaluates the input parameter `p_user_name` using the `NVL` function. If `p_user_name` is `NULL`, it defaults to `'Developer'`.
* **Output Format:** `Welcome to GitHub, <p_user_name or 'Developer'>!`

---

### `get_repo_status` (Function)

This function returns a status message indicating the current state of the repository.

#### Syntax
```sql
FUNCTION get_repo_status RETURN VARCHAR2;
```

#### Return Value
* **Data Type:** `VARCHAR2`
* **Returned Value:** `'Repository is active, and code is ready for commits.'`

#### Behavior and Implementation Details
* The function does not accept any parameters.
* It returns a hardcoded string indicating that the repository is active and ready.
