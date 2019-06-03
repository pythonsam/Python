*** Settings ***
Resource        myResource.robot    # Import reaource filed with Resource keyword
Resource        myResource2.robot
Library         py_mod1.py          # Import python modules with Library keyword
Variables       var.py              # Import variables

*** Variables ***
${sv1}      1                       # Scalar variable

*** Test Cases ***
TestCase2
    # Same keyword is available in myResource and myResource2. So use resource name dot to access and avoid name collision
    myResource2.My IF Keyword       
    Nested Loop
    py_mod1.f1
    py_mod1.f2
    ${lv1}=     Set Variable        ${3000}         # Create local variable
    Log     ${VAR1} ${VAR3} ${sv1}
    Set Global Variable     ${gv1}   ${10000}       # Create global variable
    ${ret}=     Retrun from key1    50      2000    # Pass args to keyword and assign retuen value to a variable

TestCase3
    #Log     ${lv1}
    Log     ${gv1}


*** Keywords ***
Retrun from key1
    [Arguments]     ${v1}   ${v2}                   # Keyword defined to accept arguments
    Log     ${v1} ${v2}
    [return]    abc                                 # Return a value from keyword
    

