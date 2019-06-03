*** Settings ***
Documentation   To know how to do list operations
Library    Collections

*** Variables ***
${ONE}    5
${TWO}    sriram

*** Test Cases ***
List Operations
    ${L}    Create List
    Append To List    ${L}   one   2   3   ${TWO}
    log    List values are :: ${L}    WARN
    ${R} =    Get From List   ${L}    -3
    log    Second index value :: ${R}    WARN
    Remove From List  ${L}   0
    log    After removing based on index :: @{L}    ERROR
    Remove Values From List   ${L}   sriram
    log    After removing based on value ==> ${L}    WARN
