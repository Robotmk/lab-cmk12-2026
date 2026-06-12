*** Settings ***

Documentation   Uses BrowserLibrary to login into a Checkmk site.
Library     Browser

*** Variables ***

${CMK_URL}    http://127.0.0.1:5000/cmk

*** Test Cases ***

Checkmk Monitors 127.0.0.1
    [Documentation]  Verifies that there is a monitored host "127.0.0.1"
    # Create a Chromium instance ("Browser"), default context ("Profile") and open first tab ("Page")
    New Browser  browser=chromium  headless=False  slowMo=0.5
    New Context
    New Page  ${CMK_URL}
    # Fill in username/password, login and verify that it was successful (Customize button is visible)
    Fill Text  id=input_user  cmkadmin
    Fill Text  id=input_pass  cmk
    Click  id=_login
    Wait For Condition  Text  body  contains  Customize
    # Open All hosts view
    Click  text="Monitor"
    Click  text="All hosts"
    # The ">>>" operator lets us access elements inside iframes
    # Verify that there is a host "127.0.0.1"
    Wait For Condition  Text  iframe[name=main] >>> body  contains  127.0.0.1


*** Keywords ***
