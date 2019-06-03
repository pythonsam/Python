*** Settings ***
Documentation  List Opreations
Library  Collections
*** Variables ***

*** Test Cases ***
List Operations
    ${L}    create list
    LOG  created list :: ${L}   WARN
    append to list  ${L}    2   Three   4   6
    LOG  appended list :: ${L}  WARN
    ${R} =      GET FROM LIST  ${L}     1
    LOG     First Index value :: ${R}  WARN
    remove from list  ${L}      2
    LOG     After removed from lsit :: @{L}
    remove values from list  ${L}   Three
    LOG     After removed value :: ${L} WARN