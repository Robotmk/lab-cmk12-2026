<!-- First include the example/template's partial. Examples include the exmaple-intro.partial in turn. -->

# rf-python-varfiles

<!-- Common intro injected after H1 in every example README.
     Edit this file in _dev/_shared/ — do not edit the generated copy. -->

This repository provides a **working example** to learn and test [Robot Framework](https://robotframework.org/) automation - the test scripting language used by [Robotmk](https://www.robotmk.org) for *Synthetic Monitoring* in [Checkmk](https://checkmk.com).

## How to Run the example

### Run online in a VS Code Devcontainer (recommended)

This is the easiest way to run the example — no local installation needed. Just click the button below:

[![Run this Robot in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/robotmk/example-rf-python-varfiles)

→ [How to run the example in Codespace](https://github.com/elabit/robotmk-starter/blob/main/docs/example-guide.md)

> **What is a GitHub Codespace?**  
> A Codespace is a browser-based development environment (VS Code) hosted by GitHub — no local installation needed.  

### Manually with RCC

To run Robot Framework suites manually, refer to the Robotmk blog post with the step-by-step instructions for RCC:
   
→ [How to Run Robot Framework Examples with RCC](https://www.robotmk.org/en/blog/rcc-efficient-python-integration/)  
→ [Troubleshooting RCC](https://www.robotmk.org/en/blog/rcctrouble/)


## About this Robot Framework test

Minimal example for loading variables and configuration into a Robot Framework suite from Python and YAML files.
Demonstrates the three variable file patterns supported by RF: plain scalars, nested dicts, and the `get_variables()` function — plus YAML as a data-format alternative to Python.


- Exposing computed scalar values (e.g. current user, timestamp) from a Python variable file
- Accessing values from a nested dict loaded via a Python variable file using the `[key]` subscript syntax
- Loading a nested data structure from a YAML variable file (same access syntax as Python dicts)
- Using a `get_variables(arg)` function to return different variable sets depending on an argument passed at import time
- Selecting an environment config block at runtime by combining a suite variable with a nested dict key

## Test Cases

| Test Case | Description |
|---|---|
| `Test Pyvars-Simple` | How to expose simple scalar values from a Python file as suite variables |
| `Test Pyvars-Nested` | How to access individual values from a nested dict loaded via a Python variable file |
| `Test YML-Nested` | How to load a nested data structure from a YAML variable file |
| `Test Get-Variables With Argument` | How to use `get_variables()` to return different variable sets based on an argument passed at import time |


## Links

### Recommended links for this example
- [Robot Framework — Variable Files](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#variable-files)

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
