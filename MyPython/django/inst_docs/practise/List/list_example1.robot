*** Settings ***
Documentation  List Operations
Library  Collections

*** Variables ***
@{list_1}    SHYAM EMMADI
@{list_2}   @{list_1}   pythonist

*** Test Cases ***
List Operations
    log  ${list_1}      WARN
    log  @{list_2}[1]      WARN
    ${type} =    Evaluate    type($list_1).__name__
    Log    TYPE IS ::: ${TYPE}    WARN
    LOG TO CONSOLE  \n list items:: @{list_1}
    log to console  \n list items ::@{list_2}

*** Keywords ***
