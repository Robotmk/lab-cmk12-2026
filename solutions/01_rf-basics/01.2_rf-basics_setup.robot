*** Settings ***
Documentation  Connects to the Checkmk login page and verifies that the page contains "login"
Library    RequestsLibrary
Suite Setup  Suite Initialization

*** Test Cases ***

Checkmk Successful Login
    Login Page Is Reachable

*** Keywords ***

Login Page Is Reachable
    ${resp}=    GET On Session    cmk    check_mk/login.py
    Should Be Equal As Integers    ${resp.status_code}    200
    Should Contain    ${resp.text}    Login

Suite Initialization
    Create Session    cmk    http://127.0.0.1:5000/cmk
