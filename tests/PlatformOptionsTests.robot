*** Settings ***
Documentation   Platform Options Tests
Library     PlatformOptions     ${ENVFILE}     ${BROWSER}      ${URL}
Default Tags    Smoke

*** Test Cases ***
Verify the ability to toggle between Domino Contributor and Admin using the Set Org Admin and Remove Admin role
    log in   superusername     superpassword
    select qa test organization
    click users tab
    choose user option
    verify options
    select remove set org admin option
    choose user option
    verify options
    select remove set org admin option

Verify the ability to disable/enable a user from CSAdmin
    log in   superusername     superpassword
    select qa test organization
    click users tab
    choose user option
    verify options
    select disable enable option
    choose user option
    verify options
    select disable enable option

Verify the ability to resend an invitation to a user in an organization
    log in   superusername     superpassword
    select qa test organization
    click users tab
    choose user option
    verify options
    select resend invite option

Verify the ability to cancel from moving a user to a different organization
    log in   superusername     superpassword
    select qa test organization
    click users tab
    choose user option
    verify options
    cancel change organization option

Verify CSAdmin can move user to a different organization
    log in   superusername     superpassword
    select qa test organization
    click users tab
    choose user option
    verify options
    select change organization option   a-move-org
    navigate to organization
    select move test organization
    click users tab
    choose user option
    verify options
    select change organization option   a-smoke-csadmin-org
