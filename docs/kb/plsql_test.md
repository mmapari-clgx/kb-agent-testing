# plsql_test.pkb

The `plsql_test.pkb` file contains the package body implementation for `pkg_github_demo`. This package provides basic utility subprograms to print a welcome message and retrieve a repository status string.

## Package Details

* **Package Name:** `pkg_github_demo`
* **Language:** PL/SQL (Oracle)

---

## Subprograms

### `print_welcome`

This procedure prints a welcome message to the standard output using `DBMS_OUTPUT`.

#### Syntax
```sql
PROCEDURE print_welcome (p_user_name IN VARCHAR2);
```

#### Parameters
| Parameter Name | Data Type | Mode | Description |
| :--- | :--- | :--- | :--- |
| `p_user_name` | `VARCHAR2` | `IN` | The name of the user to welcome. |

#### Behavior
* Constructs a welcome message in the format: `Welcome to GitHub, <p_user_name>!`
* Uses the `NVL` function to default the username to `'Developer'` if `p_user_name` is `NULL`.
* Outputs the message using `DBMS_OUTPUT.PUT_LINE`.

---

### `get_repo_status`

This function returns a static status message indicating the state of the repository.

#### Syntax
```sql
FUNCTION get_repo_status RETURN VARCHAR2;
```

#### Return Value
* **Type:** `VARCHAR2`
* **Value:** `'Repository is active, and code is ready for commits.'`
