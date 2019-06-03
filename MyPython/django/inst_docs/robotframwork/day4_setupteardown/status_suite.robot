

*** Settings ***
Library         py_mod1.py

*** Test Cases ***
Test Case1

    # Run Keyword And Continue On Failure:
    # This keyword will let the whole testcase be execeuted irrespective of
    # what happens in the executed keyword(py_mod1.f1). But this will alter the 
    # test case status after its execution to fail if the keyword(py_mod1.f1) fails

    Run Keyword And Continue On Failure     py_mod1.f1
    py_mod1.f2
    Log     Test case finished execution

Test Case2

    # Run Keyword And Return Status:
    # This kyword will not change the staus of the testcase if the provided keyword 
    # fails. It ignores errors. This will return the execution status as 'True'
    # or 'False' which one can capture in to a variable and use as necessary

    ${status}=      Run Keyword And Return Status           py_mod1.f1   
    py_mod1.f2
    Log     Test case finished execution

Test Case3

    # Run Keyword And Ignore Error
    # This keyword too will not alter the status and is similar to above keyword.
    # But additionaly this gives the return value of executed keyword along with status
    # i.e, returns 2 variables as output. First is status 'PASS' or 'FAIL' and the next
    # is return value which contains the return value of executed keyword(py_mod1.f1) if
    # it passes else it contains the error message if it fails

    ${status}   ${retval}=       Run Keyword And Ignore Error        py_mod1.f1
    py_mod1.f2
    Log     Test case finished execution

