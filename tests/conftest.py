import pytest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # 1. Logic for Toda's date (Format: DDMMYY e.g., 031225)
    today_date = datetime.now().strftime("%d%m%y")
    
    # 2. Counter Reading logic (Sequential Logic)
    counter_file = "run_counter.txt"
    
    if os.path.exists(counter_file):
        with open(counter_file, "r") as f:
            try:
                last_count = int(f.read().strip())
                new_count = last_count + 1
            except:
                new_count = 1
    else:
        new_count = 1
        
    # Counter save 
    with open(counter_file, "w") as f:
        f.write(str(new_count))
    
    # 3. FINAL ID making: Date + Counter (e.g., 031225_15)
    full_run_id = f"{today_date}_{new_count}"
    
    # 4. Environment Variable mein set  (Taaki Screenshot isse use kare)
    os.environ["CURRENT_RUN_ID"] = full_run_id
    
    # 5. Report Name Setting
    # Example: Report_031225_15.html
    report_name = f"Report_{full_run_id}.html"
    
    if not os.path.exists("reports"):
        os.makedirs("reports")
        
    config.option.htmlpath = os.path.join("reports", report_name)

@pytest.fixture(scope="function")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()