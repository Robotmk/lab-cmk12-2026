*** Settings ***
Library     Browser
...             enable_playwright_debug=disabled
...             auto_delete_passed_tracing=True
...             run_on_failure=Take A Screenshot


*** Keywords ***

Browser Init
    # If there is no env var ROBOTMK_HEADLESS_HOST, always show the UI
    New Browser  headless=%{ROBOTMK_HEADLESS_HOST=false}  slowMo=750ms

Session Init
    [Arguments]  ${url}
    New Context    locale=en-US
    New Page    ${url}

Take A Screenshot
    Take Screenshot  EMBED  fileType=jpeg  quality=80