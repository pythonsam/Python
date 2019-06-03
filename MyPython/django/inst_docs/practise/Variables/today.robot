*** Settings ***
Documentation    Today test cases

*** Variables ***
${ONE}    23
${NAME}    sriram

*** Test Cases ***
Test Case1: Add
    ${R} =   Evaluate  ${ONE} + 3
    Log to console    \n SUM IS :: ${R}
Test Case2: Sub
    ${R} =   Evaluate  ${ONE} - 3
    Log to console    \n SUB IS :: ${R}

