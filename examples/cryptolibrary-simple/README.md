<!-- First include the example/template's partial. Examples include the exmaple-intro.partial in turn. -->

# cryptolibrary-simple

<!-- Common intro injected after H1 in every example README.
     Edit this file in _dev/_shared/ — do not edit the generated copy. -->

This repository provides a **working example** to learn and test [Robot Framework](https://robotframework.org/) automation - the test scripting language used by [Robotmk](https://www.robotmk.org) for *Synthetic Monitoring* in [Checkmk](https://checkmk.com).

## How to Run the example

### Run online in a VS Code Devcontainer (recommended)

This is the easiest way to run the example — no local installation needed. Just click the button below:

[![Run this Robot in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/robotmk/example-cryptolibrary-simple)

→ [How to run the example in Codespace](https://github.com/elabit/robotmk-starter/blob/main/docs/example-guide.md)

> **What is a GitHub Codespace?**  
> A Codespace is a browser-based development environment (VS Code) hosted by GitHub — no local installation needed.  

### Manually with RCC

To run Robot Framework suites manually, refer to the Robotmk blog post with the step-by-step instructions for RCC:
   
→ [How to Run Robot Framework Examples with RCC](https://www.robotmk.org/en/blog/rcc-efficient-python-integration/)  
→ [Troubleshooting RCC](https://www.robotmk.org/en/blog/rcctrouble/)


## About this Robot Framework test

Minimal example for using [robotframework-crypto](https://github.com/Snooz82/robotframework-crypto) with Robotmk.  
Demonstrates how to store an encrypted secret in a Robot Framework suite and decrypt it at runtime using a private key file — no plaintext passwords anywhere in the codebase!


- Encrypting a password with `CryptoLibrary` and storing the `crypt:…` value in the suite
- Passing the key password via an environment variable (`RMKCRYPTPW`)
- Loading the private key from a file path relative to the suite

## Test Cases

| Test Case | Description |
|---|---|
| `Test Password Equality` | Decrypts an encrypted password string and asserts it equals the known plaintext |


## Links

### Recommended links for this example

- [Robotmk Blog: How to use the CryptoLibrary](https://www.robotmk.org/en/blog/cryptolibrary/)

### General links & Documentation

- [robotframework-crypto](https://github.com/Snooz82/robotframework-crypto)
- [Robot Framework](https://robotframework.org)
- [Robotmk Homepage](https://robotmk.org)



## Libraries and Versions used in this example

| Library | Version |
|---|---|
| Python | `3.12` |
| Robot Framework | `7.4` |
| robotframework-crypto | `0.3` |


## About

Also try the other [RF example suites](https://github.com/elabit/robotmk-starter#content), they all work in the Codespace environment.  

🪲 Found a bug or have a suggestion?  
→ [Open an issue](https://github.com/robotmk/robotmk-starter/issues) or submit a [pull request](https://github.com/robotmk/robotmk-starter/pulls) — contributions are welcome.

📖 Want to go deeper? Want ot get a certified professional?  
→ I offer [Synthetic Monitoring Trainings](https://lp.robotmk.org/robotmk-masterclass-4d-en) or book a free [call](https://meet.brevo.com/simon-meggle).

**Simon Meggle** — Founder of Robotmk, Product Manager Synthetic Monitoring at Checkmk
