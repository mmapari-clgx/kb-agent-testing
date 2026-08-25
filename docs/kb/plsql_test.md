# `plsql_test.pkb`

This file contains the package body for `pkg_github_demo`. It implements the procedures and functions declared in the corresponding package specification.

---

## Public Procedures and Functions

### `print_welcome`

A procedure that prints a welcome message to the standard output.

```plsql
PROCEDURE print_welcome (p_user_name IN VARCHAR2)
```

**Behavior:**

*   Uses `DBMS_OUTPUT.PUT_LINE` to display a welcome message.
*   If the `p_user_name` parameter is `NULL`, the procedure uses the default name 'Developer' in its place, as handled by the `NVL` function.

**Parameters:**

| Name          | Type      | Description                  |
| :------------ | :-------- | :--------------------------- |
| `p_user_name` | `VARCHAR2` | The name of the user to welcome. |

---

### `get_repo_status`

A function that returns a static string indicating the repository's status.

```plsql
FUNCTION get_repo_status RETURN VARCHAR2
```

**Behavior:**

*   This function takes no parameters.
*   It always returns the string literal `'Repository is active, and code is ready for commits.'`.

**Returns:**

| Type       | Description                               |
| :--------- | :---------------------------------------- |
| `VARCHAR2` | A hardcoded string describing repo status. |
