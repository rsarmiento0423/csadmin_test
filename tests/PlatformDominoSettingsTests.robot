*** Settings ***
Documentation   Platform Domino Settings Tests
Library     PlatformDominoSettingsPage     ${ENVFILE}     ${BROWSER}      ${URL}
Default Tags    Smoke

*** Test Cases ***
As Domino super user, verify accessing Upload Locations
    log in   superusername     superpassword
    click upload locations tab

As Domino super user, verify default search for Upload Locations
    log in   superusername     superpassword
    click upload locations tab
    click search upload locations

As Domino super user, verify accessing Mising Building Request
    log in   superusername     superpassword
    click upload locations tab
    click missing buildings requests tab
