*** Settings ***
Documentation  Dictionary Opeartions
Library  Collections
*** Variables ***
&{DICT1}    name=Roger  Dept=IT
*** Test Cases ***
Dictionary Operations
    LOG     Dictionary::&{DICT1}  WARN  # To print entire dictionary
    LOG     &{DICT1}[name]  WARN        # TO get value based on key
    ${type} =    Evaluate    type($DICT1).__name__
    Log    TYPE IS ::: ${TYPE}    WARN