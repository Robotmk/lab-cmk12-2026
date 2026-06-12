*** Settings ***
Library           Browser    run_on_failure=Take A Screenshot


*** Keywords ***

Take A Screenshot
    [Arguments]  ${selector}=${None}
    
    Browser.Take Screenshot  EMBED  ${selector}