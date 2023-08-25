*** Settings ***
Documentation   Platform Audit Tests
Library     PlatformAuditPage     ${ENVFILE}     ${BROWSER}      ${URL}
Default Tags    Smoke

*** Test Cases ***
As Domino super user, verify elements exists on Audit page
    log in   superusername     superpassword
    click audit tab
    verify audit elements exists

As Domino super user, verify search with no applied filters on Audit page
    log in   superusername     superpassword
    click audit tab
    click search btn
    verify search rows returned
