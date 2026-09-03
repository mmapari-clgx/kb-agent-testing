<!-- kb-agent:source-sha256=1d5186ce44e80a8b84d9e5a2ce341a22319252bd6b3dab1b1af3e869c250aba2 -->
# plsql_test.pkb

The `plsql_test.pkb` file implements the package body for `pkg_github_demo`. This package provides basic utility subprograms to print a welcome message and retrieve a repository status string.

## Package Details
* **Package Name:** `pkg_github_demo`
* **Language:** PL/SQL (Oracle)

---

## Procedures and Functions

### print_welcome
This procedure prints a standardized welcome message to the standard output (`DBMS_OUTPUT`).

#### Syntax
```sql
PROCEDURE print_welcome (p_user_name IN VARCHAR2)
```

#### Parameters
| Parameter Name | Mode | Data Type | Description |
| :--- | :--- | :--- | :--- |
| `p_user_name` | `IN` | `VARCHAR2` | The name of the user to include in the welcome message. |

#### Behavior
* Constructs a welcome message in the format: `Welcome to GitHub, <p_user_name>!`
* Uses `NVL(p_user_name, 'Developer')` to default the username to `'Developer'` if `p_user_name` is passed as `NULL`.
* Outputs the message using `DBMS_OUTPUT.PUT_LINE`.

---

### get_repo_status
This function returns a static status message indicating the state of the repository.

#### Syntax
```sql
FUNCTION get_repo_status RETURN VARCHAR2
```

#### Parameters
This function does not accept any parameters.

#### Return Value
* **Data Type:** `VARCHAR2`
* **Value:** `'Repository is active, and code is ready for commits.'`
