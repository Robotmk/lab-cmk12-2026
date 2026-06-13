<!-- First include the example/template's partial. Examples include the exmaple-intro.partial in turn. -->

# web-todomvc

<!-- Common intro injected after H1 in every example README.
     Edit this file in _dev/_shared/ — do not edit the generated copy. -->

This repository provides a **working example** to learn and test [Robot Framework](https://robotframework.org/) automation - the test scripting language used by [Robotmk](https://www.robotmk.org) for *Synthetic Monitoring* in [Checkmk](https://checkmk.com).

## How to Run the example

### Run online in a VS Code Devcontainer (recommended)

This is the easiest way to run the example — no local installation needed. Just click the button below:

[![Run this Robot in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/robotmk/example-web-todomvc)

→ [How to run the example in Codespace](https://github.com/elabit/robotmk-starter/blob/main/docs/example-guide.md)

> **What is a GitHub Codespace?**  
> A Codespace is a browser-based development environment (VS Code) hosted by GitHub — no local installation needed.  

### Manually with RCC

To run Robot Framework suites manually, refer to the Robotmk blog post with the step-by-step instructions for RCC:
   
→ [How to Run Robot Framework Examples with RCC](https://www.robotmk.org/en/blog/rcc-efficient-python-integration/)  
→ [Troubleshooting RCC](https://www.robotmk.org/en/blog/rcctrouble/)


## About this Robot Framework test

A focused web automation example using [robotframework-browser](https://robotframework-browser.org) (Playwright),
testing the well-known [TodoMVC](https://todomvc.com) application.

The suite deliberately emphasises **assertion after every action** — each keyword verifies
the expected DOM state before returning, rather than relying on implicit waits alone.
XPath is used to target elements by their visible text, which keeps selectors readable
and resilient to minor markup changes.

## Test Cases

| Test Case | Description |
| --- | --- |
| `Todo Can Be Created` | Adds a new todo item and verifies it appears in the list |
| `Todo Can Be Deleted` | Adds a todo, deletes it via hover → click, and asserts it is gone |
| `Todo Can Be Checked Off` | Adds a todo and marks it as completed; checks the checkbox state |
| `Show Only Active Items` | Adds multiple todos, checks one off, activates the Active filter, and verifies the completed item is hidden |

## Key Files

- `suite.robot` — all test cases and keywords in one file
- `Resources/BrowserCommon.resource` — shared `Browser Init` keyword (headless-aware via `ROBOTMK_HEADLESS_HOST`)

## Links

### General links & Documentation

- [TodoMVC — Vue.js demo](https://todomvc.com/examples/vue/dist/)
- [robotframework-browser](https://robotframework-browser.org)
- [Robotmk Homepage](https://robotmk.org)



## Libraries and Versions used in this example

| Library | Version |
|---|---|
| Python | `3.12` |
| Node.js | `22.11.0` |
| Robot Framework | `7.4` |
| robotframework-browser | `19.14.2` |


## About

Also try the other [RF example suites](https://github.com/elabit/robotmk-starter#content), they all work in the Codespace environment.  

🪲 Found a bug or have a suggestion?  
→ [Open an issue](https://github.com/robotmk/robotmk-starter/issues) or submit a [pull request](https://github.com/robotmk/robotmk-starter/pulls) — contributions are welcome.

📖 Want to go deeper? Want ot get a certified professional?  
→ I offer [Synthetic Monitoring Trainings](https://lp.robotmk.org/robotmk-masterclass-4d-en) or book a free [call](https://meet.brevo.com/simon-meggle).

**Simon Meggle** — Founder of Robotmk, Product Manager Synthetic Monitoring at Checkmk
