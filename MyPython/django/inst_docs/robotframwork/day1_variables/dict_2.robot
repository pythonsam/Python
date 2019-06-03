*** Settings ***
Documentation   To know how to do Dict operations
Library    Collections

*** Variables ***
${ONE}    5
${TWO}    sriram


*** Test Cases ***
Dict Operations
    ${D}    Create Dictionary    name=sriram    dno=34
    Log     Dict values are :: ${D}    WARN
    ${r}    Get From Dictionary    ${D}    name
    Log    Name is : ${r}     WARN
    ${K}    Get Dictionary Keys    ${D}
    Log    Keys is : ${K}     WARN
    Remove From Dictionary    ${D}    name
    Log     Dict values are :: ${D}    WARN
   
