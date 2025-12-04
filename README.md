# 🚀 Hybrid Automation Framework (Selenium + Python + Pytest)

## 📌 Overview
This is a robust **End-to-End Hybrid Automation Framework** built using **Python** and **Selenium WebDriver**. It follows the industry-standard **Page Object Model (POM)** design pattern to ensure code reusability and maintainability.

The framework is designed to automate complex e-commerce workflows on [AutomationExercise.com](https://automationexercise.com), handling dynamic elements, ads, and overlays effectively.

---

## ✨ Key Features

* **🏗️ Page Object Model (POM):** Clear separation between page locators (`pages/`) and test logic (`tests/`).
* **📊 Data-Driven Testing:** Drives test scenarios using external data from Excel sheets (`test_data/`).
* **⚡ Parallel Execution:** Integrated `pytest-xdist` to run multiple tests simultaneously, reducing execution time.
* **🛡️ Robust Ad/Overlay Handling:** Custom `force_click` and `wait_for_element` methods using JavaScript Executors to bypass Google Ads and overlays.
* **🔄 Automatic Retries:** configured to automatically retry flaky tests to reduce false negatives.
* **📝 Comprehensive Logging:** Generates detailed execution logs with timestamps (`logs/automation.log`).
* **📸 Smart Reporting:** Produces HTML reports and automatically captures screenshots on test failure.
* **🆔 Traceability:** Implements unique Run IDs for tracking specific test executions across logs and reports.
* **📧 Dynamic Data Generation:** Utility to generate unique emails (`user_timestamp@gmail.com`) for testing registration flows repeatedly without data collisions.

---

## 📂 Project Structure

```text
AutomationFramework/
├── config.ini               # Global configuration (URL, Browser, Timeouts)
├── pytest.ini               # Pytest configuration (Parallel threads, Reports)
├── requirements.txt         # Project dependencies
├── run_counter.txt          # Internal counter for sequential Run IDs
│
├── pages/                   # Page Object Classes (Locators & Actions)
│   ├── base_page.py         # Parent class with generic WebDriver wrappers
│   ├── login_page.py
│   ├── signup_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   └── ...
│
├── tests/                   # Test Scripts (Business Logic & Assertions)
│   ├── conftest.py          # Fixtures for Driver Setup & Teardown
│   ├── test_login.py
│   ├── test_signup.py
│   ├── test_checkout.py
│   └── ...
│
├── test_data/               # External Data Files
│   └── login_data.xlsx      # Excel sheet for Data-Driven Testing
│
├── utilities/               # Helper Functions
│   ├── custom_logger.py     # Logging configuration
│   ├── excel_utils.py       # Excel reading logic
│   ├── read_config.py       # Config file reader
│   └── random_utils.py      # Unique email generator
│
├── reports/                 # HTML Reports & Failure Screenshots
└── logs/                    # Execution logs

⚙️ Prerequisites
Python 3.x

Chrome Browser (or Firefox/Edge)

📥 Installation
Clone the Repository

Bash

git clone [https://github.com/hexvikas/AutomationFramwork.git](https://github.com/hexvikas/AutomationFramwork.git)
cd AutomationFramwork
Create a Virtual Environment (Optional but Recommended)

Bash

python -m venv .venv
source .venv/Scripts/activate  # Windows (Git Bash)
Install Dependencies

Bash

pip install -r requirements.txt
▶️ How to Run Tests
1. Run All Tests (Parallel Mode)
Executes all tests using 3 parallel workers for speed.

Bash

python -m pytest
2. Run Specific Test Module
Example: Run only the End-to-End Checkout flow.

Bash

python -m pytest tests/test_checkout.py -n 0
3. Run Only Failed Tests
Reruns only the tests that failed in the last session.

Bash

python -m pytest --lf -n 0
🔧 Configuration (config.ini)
You can change the browser or base URL without touching the code.

Ini, TOML

[common info]
base_url = [https://automationexercise.com/login](https://automationexercise.com/login)
browser = chrome
implicit_wait = 10
📊 Reports & Logs
HTML Report: Generated in the reports/ folder (e.g., Report_041225_1.html). Contains Pass/Fail status and execution duration.

Screenshots: Captured automatically upon failure and saved in reports/ with the Test Case ID.

Logs: Detailed execution steps are saved in logs/automation.log.




