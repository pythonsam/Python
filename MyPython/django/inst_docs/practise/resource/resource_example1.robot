
*** Settings ***
Documentation  from external resource file. Al keywords can be now accessed in this suite
Resource    myresourcefile.robot
*** Test Cases ***
TestCase1
    Log     TestCase1 started
    :FOR    ${i}    IN RANGE    10
    \       Continue FOR loop IF    ${i} == 6
    \       Exit FOR loop IF        ${i} == 4
    \       Log     ${i}    WARN
    \       Run Keyword IF      ${i} == 5
    \       ...     My IF Keywords



