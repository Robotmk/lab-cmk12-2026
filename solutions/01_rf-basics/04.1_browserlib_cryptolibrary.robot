*** Settings ***

Documentation   Uses BrowserLibrary to login into a Checkmk site.
Resource  Resources/BrowserCommon.resource
Resource  Resources/Checkmk.resource

Library  CryptoLibrary
...    key_path=${CURDIR}/keys
...    password=rmksecret
...    variable_decryption=True 

# Load Configuration Data from a Variables Resource
Resource  Data/Variables.resource

Suite Setup  BrowserCommon.Browser Init

*** Test Cases ***

Checkmk Monitors Host
    [Documentation]  Verifies that there is a monitored host "127.0.0.1"
    [Setup]  BrowserCommon.Session Init  url=${CMK_URL}
    Checkmk.Login  username=${CMK_USER}  password=${CMK_PASSWORD}
    Checkmk.Open All Hosts
    Checkmk.Verify Monitored Host  host=${EXPECT_HOST}
