Selenium Automation Framework (Python + Pytest + POM)

Project Overview
This project is a modular and scalable Selenium Automation Framework built using:

Python

Selenium WebDriver

Pytest

Page Object Model (POM)

Custom Logging

Fixtures

HTML Reports

It follows a clean structure suitable for professional automation projects.

Project Structure

project_root/
│
├── pages/
│ └── contact_page.py
│
├── tests/
│ └── user/
│ └── test_contact.py
│
├── utilities/
│ ├── custom_logger.py
│ └── driver_setup.py (optional)
│
├── reports/
│ └── screenshots/
│
├── conftest.py
├── requirements.txt
└── README.md

How to Run Tests

Run a specific test:
pytest tests/user/test_contact.py -v

Run all tests:
pytest -v

Generate HTML report:
pytest --html=reports/report.html -v

How the Contact Test Works

WebDriver is initialized through the pytest fixture in conftest.py.

A temporary file is created for upload.

The Contact Us page is opened.

The form fields (name, email, subject, message) are filled.

The file is uploaded.

The form is submitted.

The success message is captured and validated.

The temporary file is deleted after the test run.

Installation

Install all dependencies:
pip install -r requirements.txt

Sample requirements.txt:
selenium
pytest
pytest-html
webdriver-manager

Browser Support

If browser selection is implemented in conftest.py, tests can be executed as:
pytest --browser chrome
pytest --browser firefox

Page Object Model (POM)

Each webpage has a dedicated class under the pages/ directory.
All locators and related actions are defined inside these classes to keep testing code clean and readable.
Example: ContactPage handles operations related to the Contact Us form.

Logging

custom_logger.py implements a timestamp-based logger.
All major steps such as navigation, form filling, submission and validation are logged for debugging purposes.

Screenshots on Failure

If a test fails, a screenshot is captured and saved under:
reports/screenshots/

Future Enhancements

Add Allure reporting

Add parallel test execution

Integrate with Jenkins CI/CD

Add data-driven testing (JSON / Excel)

Add API layer integration
