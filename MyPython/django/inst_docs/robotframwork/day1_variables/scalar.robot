*** Settings ***
Documentation   To know how to do scalar operations
Library    Collections

*** Variables ***
${name}     Sriram
${NO} =   98

*** Test Cases ***
Scalar Operations
    ${R}     Catenate    ${name}    chowdary
    ${R}    Evaluate    ${NO} + 7
    Log    ${R}    WARN
