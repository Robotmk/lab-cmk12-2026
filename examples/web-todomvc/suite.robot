*** Settings ***
Documentation       A simple web test on the famous todoMVC web application, with a 
...  special emphasis on the assertion after actions.

# Load common keywords from a shared file
Resource  Resources/BrowserCommon.resource

Suite Setup     BrowserCommon.Browser Init
Test Setup      Test Initialization

*** Variables ***
${URL}              https://todomvc.com/examples/vue/dist/
${TODO}             Buy Butter
@{TODOS}            Feed the dog
...                 Change tires
...                 Water the plants


*** Test Cases ***

Todo Can Be Created
    [Documentation]    Adds a new Todo to the list. 
    Add Todo  ${TODO}

Todo Can Be Deleted
    [Documentation]    Adds and Deletes a todo from the list
    Add Todo  ${TODO}
    Delete Todo  ${TODO}

Todo Can Be Checked Off
    [Documentation]    Checks if a Todo can be checked off.
    Add Todo  ${TODO}
    Check Todo  ${TODO}

Show Only Active Items
    [Documentation]   Tests if the filter hides checked items.
    Add Todos   ${TODOS}
    Check Todo  ${TODOS}[1]
    Set Filter  Active  notexpect=${TODOS}[1]

*** Keywords ***

Test Initialization
    New Context
    New Page    url=${URL}

Add Todo
    [Arguments]  ${item}
    Fill Text  input.new-todo  ${item}
    Keyboard Key  press  Enter
    Get Text  ul.todo-list  contains  ${item}  msg=Todo-list does not contain {expected}!

Check Todo
    [Arguments]  ${item}
    Click   //label[text()='${item}']/preceding-sibling::input
    Get Element States   //label[text()='${item}']/preceding-sibling::input  contains  checked

Delete Todo
    [Arguments]  ${item}
    # The "X" button cannot be clicked directly, because it is hidden by default. 
    # Solution: first hover over the item => make the X visible. 
    Hover   //label[text()='${item}']
    Click   //label[text()='${item}']/following-sibling::button
    Get Text  ul.todo-list  not contains  ${item}  msg=Could not delete {expected} from the list!

Add Todos
    [Arguments]  ${items}
    FOR  ${item}  IN  @{items}
        Add Todo  ${item}
    END
    
Set Filter
    [Arguments]   ${type}    ${expect}=${EMPTY}    ${notexpect}=${EMPTY}
    [Documentation]  Activates and verifies the filter
    Click  text="${type}"
    IF  "${expect}"
        Get Text  ul.todo-list  contains  ${expect}  msg=Todo-list does NOT contain {expected}!
    END
    IF  "${notexpect}"
        Get Text  ul.todo-list  not contains  ${notexpect}  msg=Todo-list DOES contain {expected}!
    END

