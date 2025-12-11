from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import time


class MobileUtils:

    def __init__(self, driver):
        self.driver = driver

    # ------------------------------------------------------------
    # BASIC TAP
    # ------------------------------------------------------------
    def tap(self, locator):
        element = self.driver.find_element(*locator)
        TouchAction(self.driver).tap(element).perform()

    # ------------------------------------------------------------
    # TAP ON X,Y POSITION
    # ------------------------------------------------------------
    def tap_xy(self, x, y):
        TouchAction(self.driver).tap(x=x, y=y).perform()

    # ------------------------------------------------------------
    # LONG PRESS
    # ------------------------------------------------------------
    def long_press(self, locator, duration=2000):
        element = self.driver.find_element(*locator)
        TouchAction(self.driver).long_press(el=element, duration=duration).release().perform()

    # ------------------------------------------------------------
    # SWIPE (GENERIC)
    # ------------------------------------------------------------
    def swipe(self, start_x, start_y, end_x, end_y, duration=800):
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    # ------------------------------------------------------------
    # VERTICAL SCROLL (Down or Up)
    # ------------------------------------------------------------
    def scroll_vertical(self, direction="down", distance=0.6, duration=800):
        size = self.driver.get_window_size()
        width = size["width"] / 2

        if direction == "down":
            start = size["height"] * 0.8
            end = size["height"] * (1 - distance)
        else:
            start = size["height"] * 0.3
            end = size["height"] * 0.8

        self.swipe(width, start, width, end, duration)

    # ------------------------------------------------------------
    # HIDE KEYBOARD
    # ------------------------------------------------------------
    def hide_keyboard(self):
        try:
            self.driver.hide_keyboard()
        except:
            pass

    # ------------------------------------------------------------
    # SCROLL UNTIL ELEMENT VISIBLE (Android Only)
    # ------------------------------------------------------------
    def scroll_to_text(self, text):
        """
        Uses Android UIAutomator scroll strategy.
        """
        return self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().scrollable(true)).scrollTextIntoView("{text}")'
        )

    # ------------------------------------------------------------
    # SCROLL UNTIL ELEMENT BY LOCATOR (MANUAL LOOP)
    # ------------------------------------------------------------
    def scroll_until_element(self, locator, max_swipes=5):
        """
        Scrolls down until element is found.
        Useful when UiScrollable fails.
        """
        for _ in range(max_swipes):
            try:
                element = self.driver.find_element(*locator)
                return element
            except:
                self.scroll_vertical("down")
        return None
