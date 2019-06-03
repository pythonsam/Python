*** Settings ***
Documentation  Addition and Substraction Using Scalar Variables
*** Variables ***
${NUM1}     5
${NUM2}     30
*** Test Cases ***
Test Case1 : Addition
    ${Result} =   Evaluate  ${NUM1} + 10
    Log to Console      \n SUM is :: ${Result}
Test Case2 : Substraction
    ${Result} =   Evaluate  ${NUM2} - 20
    Log to Console      \n  SUB is :: ${Result}

*** Keywords ***
