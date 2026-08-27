# plsql_test.pkb

The `plsql_test.pkb` file implements the package body for `pkg_github_demo`. This package provides basic utility functions and procedures designed to demonstrate PL/SQL integration and repository status reporting.

## Package Information
* **Package Name:** `pkg_github_demo`
* **Language:** PL/SQL (Oracle)

---

## Procedures and Functions

### `print_welcome`
This procedure prints a welcome message to the standard output (`DBMS_OUTPUT`).

#### Syntax
```sql
PROCEDURE print_welcome (p_user_name IN VARCHAR2);
```

#### Parameters
| Parameter Name | Type | Mode | Description |
| :--- | :--- | :--- | :--- |
| `p_user_name` | `VARCHAR2` | `IN` | The name of the user to welcome. |

#### Behavior
* The procedure outputs a message using `DBMS_OUTPUT.PUT_LINE`.
* It uses the `NVL` function to handle null inputs. If `p_user_name` is `NULL`, it defaults to `'Developer'`.
* **Output Format:** `Welcome to GitHub, <p_user_name or 'Developer'>!`

---

### `get_repo_status`
This function returns a static string indicating the current status of the repository.

#### Syntax
```sql
FUNCTION get_repo_status RETURN VARCHAR2;
```

#### Parameters
This function does not accept any parameters.

#### Return Value
* **Type:** `VARCHAR2`
* **Value:** `'Repository is active, and code is ready for commits.'`
