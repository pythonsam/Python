*** Settings ***
Documentation  For Loop Opeartions
*** Test Cases ***
Test for loop
    : FOR     ${INDEX}   IN RANGE    5
    \   ${INDEX}   evaluate    ${INDEX} + 1
    \   continue for loop if    ${INDEX} == 2
    \   LOG     ${INDEX}    WARN
    \   exit for loop if    ${INDEX} == 5

