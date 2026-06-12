*** Settings ***
Documentation    A suite to demonstrate how to load **variables** from **Python**, **JSON** and **YAML** variable files, including nested data structures.
Variables        Data/pyvars-simple.py
Variables        Data/pyvars-nested.py
Variables        Data/pyvars-getvariables.py  ${BROWSER}
Variables        Data/ymlvars-nested.yaml
Variables        Data/jsonvars-nested.json

*** Variables ***

${ENV}    dev
${BROWSER}   chrome

*** Test Cases ***

Test Pyvars-Simple
    [Documentation]    How to expose simple scalar values from a Python file as suite variables.
    Log   Random Number = ${RANDOM_INT}
    Log   Current time is ${CURRENT_TIME}
    Log   Is it afternoon? ${AFTERNOON}.

Test Pyvars-Nested
    [Documentation]    How to access individual values from a nested dict loaded via a Python variable file.
    Should Be Equal    ${cfg}[${ENV}][url]  https://dev.example.com
    Should Be Equal    ${cfg}[${ENV}][ssl_verify]    ${FALSE}
    Should Be Equal    ${cfg}[${ENV}][user]    dev_user
    Should Be Equal    ${cfg}[${ENV}][password]    dev_password
    

Test YML-Nested
    [Documentation]    How to load a nested data structure from a YAML variable file — same access syntax as Python dicts.
    Should Be Equal    ${cfg}[${ENV}][url]  https://dev.example.com
    Should Be Equal    ${cfg}[${ENV}][ssl_verify]    ${FALSE}
    Should Be Equal    ${cfg}[${ENV}][user]    dev_user
    Should Be Equal    ${cfg}[${ENV}][password]    dev_password

Test JSON-Nested
    [Documentation]    How to load a nested data structure from a YAML variable file — same access syntax as Python dicts.
    Should Be Equal    ${cookbook}[pasta][name]  Spaghetti Carbonara
    Should Be Equal As Integers    ${cookbook}[pasta][time_minutes]  20
    Should Contain     ${cookbook}[dessert][ingredients]   mascarpone

Test Get-Variables With Argument
    [Documentation]    How to use a get_variables() function to return different variable sets based on an argument passed at import time.
    Should Be Equal    ${BROWSER}           chrome
    Should Be Equal    ${HEADLESS}          ${FALSE}
    Should Be Equal    ${WINDOW_WIDTH}      ${1920}
    Should Be Equal    ${WINDOW_HEIGHT}     ${1080}
    Should Be Equal    ${DOWNLOAD_DIRS}[0]  /tmp/chrome-downloads



