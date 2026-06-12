*** Settings ***
Documentation  This suite demonstrates the use of a **custom library**, written with a simple Python class.
Library  CustomLibrary.py

*** Test Cases ***

Test Hello 
    [Documentation]  Calls the user keyword "Say Hello"
    Say Hello  Robots

Test Addition
    [Documentation]  Calls the user keyword "Add Numbers" to do a calculation
    ${result}=  Add Numbers  44  11
    Log  ${result}