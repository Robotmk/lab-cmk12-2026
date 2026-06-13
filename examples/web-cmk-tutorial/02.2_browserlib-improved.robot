*** Settings ***

Documentation   Uses BrowserLibrary to login into a Checkmk site.
# Load common keywords from a shared file
Resource  Resources/BrowserCommon.resource
# Load Checkmk-specific keywords
Resource  Resources/Checkmk.resource
# Create a Browser instance across all test cases
Suite Setup  BrowserCommon.Browser Init

*** Variables ***

${CMK_URL}    http://127.0.0.1:5000/cmk

*** Test Cases ***

Checkmk Monitors 127.0.0.1
    [Documentation]  Verifies that there is a monitored host "127.0.0.1"
    # Use the keyword from BrowserCommon.resource
    [Setup]  BrowserCommon.Session Init  url=${CMK_URL}
    Checkmk.Login
    Checkmk.Open All Hosts
    Checkmk.Verify Monitored Host
