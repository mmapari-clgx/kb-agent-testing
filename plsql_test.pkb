-- -------------------------------------------------------------------
-- Script Name: pkg_github_demo.pkb
-- Description: Oracle PL/SQL Package Body
-- -------------------------------------------------------------------
CREATE OR REPLACE PACKAGE BODY pkg_github_demo AS

    -- Implementation of the procedure
    PROCEDURE print_welcome (p_user_name IN VARCHAR2) IS
    BEGIN
        DBMS_OUTPUT.PUT_LINE('Welcome to GitHub, ' || NVL(p_user_name, 'Developer') || '!');
    END print_welcome;

    -- Implementation of the function
    FUNCTION get_repo_status RETURN VARCHAR2 IS
    BEGIN
        RETURN 'Repository is active, and code is ready for commits.';
    END get_repo_status;

END pkg_github_demo;
/
