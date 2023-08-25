*** Settings ***
Documentation   Platform Login Tests
Library     PlatformLoginPage     ${ENVFILE}     ${BROWSER}      ${URL}
Default Tags    Smoke

*** Test Cases ***
Login as Domino super user
    log in   superusername     superpassword
    log out

Login without permission
    login with no permission    usernopermission    passwordopermission

Login with invalid password
    login negative    superusername    wrongpassword

Login with no password
    login negative    superusername    blank

Login with invalid username
    login negative    badusername@oneconcern.com   superpassword

Login with no username
    login negative    blank    superpassword

Click Forgot password link
    click forgot password
