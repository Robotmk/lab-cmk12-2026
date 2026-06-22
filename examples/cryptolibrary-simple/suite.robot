*** Settings ***
Documentation       A minimalistic example of how to use the **CryptoLibrary**, without bells and whistles.

Library     CryptoLibrary
...             key_path=${CURDIR}/keys
...             password=%{RMKCRYPTPW=rmksecret}


*** Variables ***

${PASSWORD_CRYPT}   crypt:+88hq/fgSuQZPUEj/qOwjGdpp+JRHKvJ5xpIXo1HYXM0JepeaZJrPwbw6m6Ndcn2vo+iv3aYeMDiXo8h2zc=

*** Test Cases ***
Test Password Equality
    [Documentation]    Tests whether the decrypted text matches the expected value.
    ${pass}   Get Decrypted Text  ${PASSWORD_CRYPT}
    Should Be Equal As Strings  ${pass}  password123456
