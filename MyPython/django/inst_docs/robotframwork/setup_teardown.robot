*** Settings ***
Library            py_mod1.py

# Test setup and teardown will be generally applied to all available testcases
# in the suite which reduces the code from being duplicated
Test Setup          MyTestSetup
Test Teardown       MyTestTeardown

# Suite setup will be executed before any test case starts and teardown
# will be executed after all the testcases ends in a test suite
Suite Setup         MySuiteSetup
Suite Teardown      MySuiteTeardown

*** Test Cases ***
Test Case1

    [Setup]     MySetup

    py_mod1.f1
    py_mod1.f2
    Log     Test case finished execution

    [Teardown]  MyTeardown

Test Case2
    py_mod1.f2
    Log     Test case finished execution

Test Case3
    py_mod1.f2
    Log     Test case finished execution

Test Case4
    py_mod1.f2
    Log     Test case finished execution

*** Keywords ***
MySetup
    Log         Setup started

MyTeardown
    Log         Teardown started

MyTestSetup
    Log         MyTestSetup started

MyTestTeardown
    Log         MyTestTeardown started

MySuiteSetup
    Log         Suite setup started

MySuiteTeardown
    Log         Suite teardown started
