*** Settings ***
Documentation   Platform Organization Tests
Library     PlatformOrganizationPage     ${ENVFILE}     ${BROWSER}      ${URL}
Default Tags    Smoke

*** Test Cases ***
As Domino super user, verify elements exists on Organization page
    log in   superusername     superpassword
    verify organization elements exists

As Domino super user, verify elements in New Organization page
    log in   superusername     superpassword
    click add organization
    verify new org elements_exists

As Domino super user, cancel from creating new organization
    log in   superusername     superpassword
    click add organization
    click cancel from new organization

As Domino super user, verify no organization name error
    log in   superusername     superpassword
    click add organization
    click create from new organization
    verify name required

Verify viewing and editing admin notes from an organization
    log in   superusername     superpassword
    click first organization
    get admin notes
    update admin notes
