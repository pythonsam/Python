*** Settings ***
Documentation   To know how to do list operations
Library    Collections

*** Variables ***
@{list_1}    sriram chowdary
@{list_2}    ${list_1}    nagesh


*** Test Cases ***
List Operations
    Log    ${list_1}       ERROR
    Log    @{list_2}[0]    ERROR
    ${type} =    Evaluate    type($list_1).__name__
    Log    TYPE IS ::: ${TYPE}    WARN

