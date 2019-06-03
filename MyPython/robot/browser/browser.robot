*** Settings ***
Library           Selenium2Library

*** Variables ***
${Username}       estimatoretender1@gmail.com
${Password}       Test@123
${Browser}        Firefox
${SiteUrl}        https://etender.staging.causeway.com
${Title}    Causeway eTender
${Delay}          5s

*** Test Cases ***
LoginTest
    Open Browser to the Login Page
    Enter User Name
    Enter Password
    Click Login
    sleep    ${Delay}
    Assert Title
    [Teardown]    Close Browser

*** Keywords ***
Open Browser to the Login Page
    open browser    ${SiteUrl}    ${Browser}
    Maximize Browser Window

Enter User Name
    Input Text    LoginName    ${Username}

Enter Password
    Input Text    password    ${Password}

Click Login
    click button    submitButton

Assert Title
    Title Should be    ${Title}