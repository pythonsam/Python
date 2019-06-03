*** Settings ***
Documentation    This file is used to do Loop operations

*** Variables ***
${ONE}     88

*** Test Cases ***
Test For Loop
    : FOR    ${INDEX}    IN RANGE    10
    \   ${INDEX}    Evaluate    ${INDEX} + 1
    \  Continue For Loop If    ${INDEX} == 5
    \  log    ${INDEX}    WARN
    \  Exit For Loop If    ${INDEX} == 5
