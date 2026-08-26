# `plsql_test.pkb`

This file provides the implementation (body) for the `pkg_github_demo` PL/SQL package.

---

## Public Functions/Procedures

### `print_welcome`

This procedure prints a welcome message to the DBMS output stream.

**Signature**
```plsql
PROCEDURE print_welcome (p_user_name IN VARCHAR2)
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `p_user_name` | `IN VARCHAR2` | The name of the user to include in the welcome message. |

**Behavior**

*   The procedure constructs a welcome message string: `'Welcome to GitHub, '`.
*   It appends the value of `p_user_name`.
*   If `p_user_name` is `NULL`, it uses the default value `'Developer'` in its place, as handled by the `NVL` function.
*   The resulting string is printed using `DBMS_OUTPUT.PUT_LINE`.

---

### `get_repo_status`

This function returns a static string indicating the repository status.

**Signature**
```plsql
FUNCTION get_repo_status RETURN VARCHAR2
```

**Parameters**

This function does not accept any parameters.

**Returns**

*   `VARCHAR2`: A string describing the repository status.

**Behavior**

*   The function always returns the hardcoded string literal `'Repository is active, and code is ready for commits.'`.
