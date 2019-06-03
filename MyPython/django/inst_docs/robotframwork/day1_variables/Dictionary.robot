*** Settings ***
Documentation   To know how to do Dictionary operations
Library    Collections

*** Variables ***
&{DICT_1}   name=Matti    address=xxx    phone=123
&{DICT_2}   name2=Teppo   address2=yyy   phone2=456

*** Test Cases ***
Dict Operations
    Log    ${DICT_2}    WARN           ## To print entire dictionary
    Log    &{DICT_1}[name]    WARN     ## TO get value based on key
    ${type} =    Evaluate    type($dict_1).__name__
    Log    TYPE IS ::: ${TYPE}    WARN
