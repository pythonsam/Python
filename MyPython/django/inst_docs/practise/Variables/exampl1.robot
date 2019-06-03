*** Settings ***
Documentation  Simple TestCases for Addition and Substraction without Using Variables
*** Variables ***

*** Test Cases ***
Test Case1: Addition

    ${Result} =   Evaluate    2 + 3
    Log to Console  \n sum is :: ${Result}
Test Case2: Substraction

    ${Result} =   Evaluate    3 - 2
    Log to Console  \n Sub is :: ${Result}

*** Keywords ***
