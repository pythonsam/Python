*** Settings ***
Documentation  Scalaor Variable
*** Variables ***
${Name}     SHYAM
${Num}      10
*** Test Cases ***
Test Case1 : Scalar Operation Concatiante the String
    ${Result}   Catenate  ${Name}   Emmadi
    Log     ${Result}
    LOG TO CONSOLE  \n Concatination is :: ${Result}
Test Case2 : Scalor Operation
    ${Result}   catenate  ${Name}   Pythonionst
    LOG  ${Result}
    LOG TO CONSOLE  \n Concatination is :: ${Result}
*** Keywords ***
