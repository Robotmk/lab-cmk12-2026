*** Settings ***
Documentation     A **BrowserLibrary** suite running against a demo web shop, showing a full user journey: login → add items to cart → checkout.

Library           Browser    run_on_failure=Take A Screenshot
Library           CryptoLibrary
...                 key_path=${CURDIR}/keys
...                 password=%{RMKCRYPTPW=secret}
...                 variable_decryption=True
Resource          Resources/authentication.resource
Resource          Resources/catalog.resource
Resource          Resources/cart.resource
Resource          Resources/checkout.resource

Suite Setup       Open Webshop

*** Variables ***
# https://github.com/testsmith-io/practice-software-testing
${BASE_URL}       https://practicesoftwaretesting.com
${USER_EMAIL}     customer3@practicesoftwaretesting.com
# pass123
${USER_PASSWORD}  crypt:y4/mHOmQTOJIWy/eJsOwUei+3AGv1OJwox5BoU9eOUvhJz0Lb/7EesIru4vUOX8j4KQuqfbLoA==
${USER_NAME}      Bob Smith
${ITEMS_IN_CART}  0
@{ITEMS_TO_ADD}   Ear Protection    Safety Goggles

*** Test Cases ***
User Can Reach Checkout Page
    [Documentation]    Logs in as a user, adds items to the cart, and reaches checkout.
    authentication.Login As User    ${USER_EMAIL}    ${USER_PASSWORD}    ${USER_NAME}
    catalog.Add Items To Cart       @{ITEMS_TO_ADD}
    cart.Open Cart
    checkout.Checkout

*** Keywords ***
Open Webshop
    # ROBOTMK_HEADLESS_HOST is set by Robotmk; default to false (show browser) locally.
    New Browser    chromium    headless=%{ROBOTMK_HEADLESS_HOST=false}
    New Context    locale=en-US    viewport={'width': 1280, 'height': 1024}
    New Page       ${BASE_URL}
