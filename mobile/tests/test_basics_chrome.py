import time
from appium import webdriver

def test_open_google():
    desired_caps = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "deviceName": "Android",
        "browserName": "Chrome",
        "chromedriverExecutableDir": r"C:\\chromedriver",
        "newCommandTimeout": 300,
    }

    driver = webdriver.Remote("http://127.0.0.1:4723", desired_caps)

    driver.get("https://google.com")
    time.sleep(3)
    assert "Google" in driver.title

    driver.quit()
