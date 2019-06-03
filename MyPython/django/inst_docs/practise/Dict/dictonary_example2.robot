*** Settings ***
Documentation  Dictonary Operations
Library  Collections
*** Variables ***
&{DICT1}    name=Roger  Dept=IT
*** Test Cases ***
Dictonary Operations
    ${D}    create dictionary  name=SHYAM
    LOG     Dict Items are:: ${D}    WARN
    ${v}    Get From Dictionary  ${D}   name
    LOG     Name is :: ${v}     WARN
    ${K}    get dictionary keys  ${D}
    LOG     Key is :: ${K}      WARN
    Remove From Dictionary    ${D}    name
    Log     Dict values are :: ${D}    WARN