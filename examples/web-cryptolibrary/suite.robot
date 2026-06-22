*** Settings ***
Documentation       A example of how to use the **CryptoLibrary** in a web test (**BrowserLibrary**).

Library     Browser
...             enable_playwright_debug=disabled
...             auto_delete_passed_tracing=True
Library     CryptoLibrary
...             key_path=${CURDIR}/keys
...             password=%{RMKCRYPTPW=rmksecret}
...             variable_decryption=True

Suite Setup     Suite Initialization
Test Setup      Test Initialization

*** Variables ***
${URL}              https://testpages.eviltester.com/apps/simulated-login/
${USERNAME}         Admin
# BAD: Never store clear-text passwords in production suites. Instead use CryptoLibrary to encrypt secrets: https://github.com/Snooz82/robotframework-crypto
${PASSWORD_CLEAR}   AdminPass
# GOOD: Encrypted with the private key in keys/private_key.json:
${PASSWORD_CRYPT}   crypt:VEM3Q3ggAVXybUf5yoBHxO/7LhheyMBhOwoOUMWGb2qcV00spV/DgGQkvGAFW8pEgVt7lc5AZC9X

*** Test Cases ***

Login With Clear Text Password
    # BAD example!
    [Documentation]    Demonstrates a login using a clear-text password.
    ...                This is intentionally shown as a negative example — never do this
    ...                in production. Use CryptoLibrary (see next test case) instead.
    Fill Text    id=username    ${USERNAME}
    Fill Text    id=password    ${PASSWORD_CLEAR}
    Click        id=login
    Wait For Condition    Text    h2#adminh    ==    You are Admin

Login With CryptoLibrary
    # GOOD example!
    [Documentation]    Demonstrates a login using a CryptoLibrary-encrypted password.
    ...                The encrypted value is decrypted at runtime using the private key.
    Fill Text    id=username    ${USERNAME}
    # Fill the cryptographic cipher text (encrypted by the CryptoLibrary)
    # It is NOT allowed to pass a regular RF variable to "Fill Secret". 
    # Instead, we omit the curly brackets: the keyword resolves the variable then internally to avoid the secret being leaked into the logs. 
    Fill Secret    id=password    $PASSWORD_CRYPT
    Click        id=login
    Wait For Condition    Text    h2#adminh    ==    You are Admin

*** Keywords ***
Suite Initialization
    # ROBOTMK_HEADLESS_HOST is set by Robotmk; default to false (show browser) locally.
    New Browser    chromium    headless=%{ROBOTMK_HEADLESS_HOST=false}    slowMo=1s

Test Initialization
    New Context
    New Page    url=${URL}
