*** Settings ***
Documentation   To know how to do IF Else
...             Conditons
*** Variables ***
${One}  8
*** Test Cases ***
Condtional Statements
    Run Keyword If   2 == 2    Add   ${ONE}    5

    Run Keyword If   2 == 4    Log    if block      WARN
    #...   ELSE IF    3 == 3    Log    first elif    ERROR
    #...   ELSE IF    3 == 6    Log    Second elif   WARN
    ...   ELSE    Log   Else block is     ERROR

***Keywords***
Add    [arguments]    ${a}    ${b}
    ${r} =   Evaluate   ${a} - ${b}
    Log    ${r}    WARN




