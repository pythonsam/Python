*** Settings ***
Suite Setup       GoToHomePage
Suite Teardown    Close Browser
Library           SeleniumLibrary

*** Variables ***
${url}            https://opensource-demo.orangehrmlive.com/index.php/auth/validateCredentials
@{CRDENTIALS}     Admin    admin123
&{LOGIN}          Username=Admin    Password=admin123

*** Test Cases ***
Test1
    [Tags]    Test1
    Open Browser    ${url}    chrome
    Close Browser
    Log To Console    Completed Successfully

Test2
    [Tags]    Test2
    Open Browser    ${url}    chrome
    Input Text    id=txtUsername    @{CRDENTIALS}[0]
    Input Password    id=txtPassword    &{LOGIN}[Password]
    Click Button    id=btnLogin
    Close Browser

Test3
    [Tags]    Test3
    [Setup]    Log To Console    Test Case Started
    Login
    [Teardown]    Log To Console    Test Case Ended

Test4
    [Tags]    Sanity
    Log To Console    Test4 Started
    Open Browser    http://google.com
    Close Browser
    Log To Console    Test Ended
    Set Tags    SmokeTest

Test5
    [Tags]    Sanity
    Log To Consol

*** Keywords ***
Login
    Input Text    id=txtUsername    Admin
    Input Password    id=txtPassword    admin123
    Click Button    id=btnLogin

GoToHomePage
    Open Browser    ${url}    chrome
