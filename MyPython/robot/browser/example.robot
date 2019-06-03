*** Settings ***
Documentation    Example using the space separated plain text format.
Library          OperatingSystem

*** Variables ***
${MESSAGE}    Hello, world!
${MESSAGE1}    HELLO PYTHON

*** Test Cases ***
My Test
    [Documentation]    Example test
    Log    ${MESSAGE}
    Log    ${MESSAGE1}
    My Keyword    /tmp

Another Test
    Should Be Equal    ${MESSAGE}    Hello, world!
	Should Be Equal    ${MESSAGE1}    HELLO PYTHON

*** Keywords ***
My Keyword
    [Arguments]    ${path}
    Directory Should Exist    ${path}