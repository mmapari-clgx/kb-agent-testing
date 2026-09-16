<!-- kb-agent:source-sha256=1d5186ce44e80a8b84d9e5a2ce341a22319252bd6b3dab1b1af3e869c250aba2 -->
# plsql_test.pkb

The `plsql_test.pkb` file implements the package body for `pkg_github_demo`. This package provides basic utility subprograms to print a welcome message and retrieve a repository status string.

## Package Overview

- **Package Name:** `pkg_github_demo`
- **Language:** PL/SQL (Oracle)
- **Purpose:** Demonstration and utility functions for GitHub repository status and user greeting.

---

## Subprograms

### `print_welcome`

This procedure prints a welcome message to the standard output using the `DBMS_OUTPUT` package.

#### Syntax
```sql
PROCEDURE print_welcome (p_user_name IN VARCHAR2);
```

#### Parameters
| Parameter Name | Type | Mode | Description |
| :--- | :--- | :--- | :--- |
| `p_user_name` | `VARCHAR2` | `IN` | The name of the user to welcome. |

#### Behavior
- Constructs a greeting message: `Welcome to GitHub, <p_user_name>!`
- If `p_user_name` is `NULL`, the procedure defaults the name to `'Developer'` using the `NVL` function.
- Outputs the final string using `DBMS_OUTPUT.PUT_LINE`.

---

### `get_repo_status`

This function returns a static status message indicating the state of the repository.

#### Syntax
```sql
FUNCTION get_repo_status RETURN VARCHAR2;
```

#### Return Value
- **Type:** `VARCHAR2`
- **Value:** `'Repository is active, and code is ready for commits.'`

#### Behavior
- Returns a hardcoded string indicating that the repository is active and ready for commits. No database tables are queried.
