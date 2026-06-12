<!-- First include the example/template's partial. Examples include the exmaple-intro.partial in turn. -->

# rf-custom-library

<!-- Common intro injected after H1 in every example README.
     Edit this file in _dev/_shared/ — do not edit the generated copy. -->

This repository provides a **working example** to learn and test [Robot Framework](https://robotframework.org/) automation - the test scripting language used by [Robotmk](https://www.robotmk.org) for *Synthetic Monitoring* in [Checkmk](https://checkmk.com).

## How to Run the example

### Run online in a VS Code Devcontainer (recommended)

This is the easiest way to run the example — no local installation needed. Just click the button below:

[![Run this Robot in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/robotmk/example-rf-custom-library)

→ [How to run the example in Codespace](https://github.com/elabit/robotmk-starter/blob/main/docs/example-guide.md)

> **What is a GitHub Codespace?**  
> A Codespace is a browser-based development environment (VS Code) hosted by GitHub — no local installation needed.  

### Manually with RCC

To run Robot Framework suites manually, refer to the Robotmk blog post with the step-by-step instructions for RCC:
   
→ [How to Run Robot Framework Examples with RCC](https://www.robotmk.org/en/blog/rcc-efficient-python-integration/)  
→ [Troubleshooting RCC](https://www.robotmk.org/en/blog/rcctrouble/)


## About this Robot Framework test

Minimal example for extending Robot Framework with a custom Python library.
Demonstrates how to write a simple Python class, expose its methods as keywords via the `@keyword` decorator, and import the library directly into a suite.


- Writing a custom Robot Framework library as a plain Python class (`CustomLibrary.py`)
- Exposing Python methods as RF keywords with `@keyword` from `robot.api.deco`
- Importing a local `.py` file as a library in a suite (`Library  CustomLibrary.py`)
- Handling type conversion for keyword arguments (string → int)

## Test Cases

| Test Case | Description |
|---|---|
| `Test Hello` | Calls the `Say Hello` keyword and logs a greeting |
| `Test Addition` | Calls `Add Numbers` with two integers and logs the result |


## Links

### Recommended links for this example
- [Robot Framework — Extending with Python](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#creating-test-libraries)

### General links & Documentation

- [Robot Framework](https://robotframework.org)
- [Robotmk Homepage](https://robotmk.org)



## Libraries and Versions used in this example

| Library | Version |
|---|---|
| Python | `3.12` |
| Robot Framework | `7.4` |


## About

Also try the other [RF example suites](https://github.com/elabit/robotmk-starter#content), they all work in the Codespace environment.  

🪲 Found a bug or have a suggestion?  
→ [Open an issue](https://github.com/robotmk/robotmk-starter/issues) or submit a [pull request](https://github.com/robotmk/robotmk-starter/pulls) — contributions are welcome.

📖 Want to go deeper? Want ot get a certified professional?  
→ I offer [Synthetic Monitoring Trainings](https://lp.robotmk.org/robotmk-masterclass-4d-en) or book a free [call](https://meet.brevo.com/simon-meggle).

**Simon Meggle** — Founder of Robotmk, Product Manager Synthetic Monitoring at Checkmk
