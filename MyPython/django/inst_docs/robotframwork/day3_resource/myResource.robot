
*** Keywords ***
My IF Keyword
    Log     If executed
    Log     Second ine executed

Nested Loop
    :FOR    ${j}  IN RANGE      4
    \       Log     ${j}
    