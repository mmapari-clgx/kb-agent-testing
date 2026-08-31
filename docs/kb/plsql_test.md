# plsql_test.pkb

The `plsql_test.pkb` file defines the package body for `pkg_github_demo`. This package provides basic utility subprograms to print a welcome message and retrieve a repository status string.

## Package Details

* **Package Name:** `pkg_github_demo`
* **Language:** PL/SQL (Oracle)

---

## Subprograms

### `print_welcome`

This procedure prints a welcome message to the standard output (`DBMS_OUTPUT`).

#### Syntax
```sql
PROCEDURE print_welcome (p_user_name IN VARCHAR2);
```

#### Parameters
| Parameter Name | Type | Mode | Description |
| :--- | :--- | :--- | :--- |
| `p_user_name` | `VARCHAR2` | `IN` | The name of the user to welcome. If `NULL`, defaults to `'Developer'`. |

#### Behavior
* Constructs a welcome message using the formula: `'Welcome to GitHub, ' || NVL(p_user_name, 'Developer') || '!'`
* Outputs the message using `DBMS_OUTPUT.PUT_LINE`.

---

### `get_repo_status`

This function returns a static string indicating the current status of the repository.

#### Syntax
```sql
FUNCTION get_repo_status RETURN VARCHAR2;
```

#### Return Value
* **Type:** `VARCHAR2`
* **Value:** `'Repository is active, and code is ready for commits.'`
