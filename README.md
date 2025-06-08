## About

---
This is a simple example of a test automation project for testing [saucedemo](https://www.saucedemo.com/), using [Pytest](https://docs.pytest.org/en/stable/), 
[selenium](https://www.selenium.dev/) and [allure](https://allurereport.org/docs/) for reporting.
Repository have a general structure to help you organize and create frameworks from scratch.

Made by Siarhei Stamal for Python Test Automation course.

## Project structure

---
```
/pytest-framework
├── .github
│   ├── workflows
│   │   ├── flake8.yaml
│   │   ├── ...
├── source
│   ├── pages
│   │   ├── base.py
│   │   ├── ...
│   ├── calculator.py
├── test_data
│   ├── constants.py
│   ├── ...
├── tests
│   ├── api
│   ├── unit
│   │   ├── test_calculator.py
│   ├── ui
│   │   ├── test_login.py
│   │   ├── ...
├── test-reports
│   ├── Test_report_xxxx-xx-xx xx:xx:xx.html
├── .gitignore
├── pytest.ini
├── README.md
├── requirements.txt
└── LICENSE
```

## Usage

---
### How to install

1. Clone this repository
```bash
    $ git clone <URL>
```
2. Create virtual environment, activate it:
```bash
    $ pip install virtualenv
    $ cd ~/projects/pytest-framework
    $ virtualenv venv
    $ source venv/bin/activate
```
3. Install dependencies
```bash
    $ pip install -r requirements.txt
```

### How to run tests
1. To execute ALL tests w/ DEBUG log level
```bash
    $ pytest . --log-level=DEBUG
```
2. To execute ALL UI test cases
```bash
    $ pytest . -m uitests
```
3. To execute smoke suite 
```bash
    $ pytest . -m smoke
```
4. To execute UI tests in Firefox, headless mode 
```bash
    $ pytest . -m uitests --browser=firefox --headless
```

### Available markers:
   + UI tests
     - `add_cart - Tests adding products to the cart`
     - `login - All login tests`
     - `login_success - Login tests with a user who is not locked out`
     - `login_incorrect - Login tests with incorrect login credentials`
     - `product_page - All product page related tests`
     - `product_sort - All product page tests related to sorting`
     - `uitests - Run ALL UI tests`
   + Common
     - `regression - Run the regression test suite`
     - `smoke - Run the smoke test suite`

### Additional arguments
```shell
Options:

  --browser=<browser>          To run UI tests on specific browser: chrome\firefox
  --headless                   To run browser in headless mode
```