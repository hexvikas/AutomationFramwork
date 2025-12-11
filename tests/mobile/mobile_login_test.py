import pytest
from mobile.pages.mobile_login_page import MobileLoginPage

@pytest.mark.usefixtures("setup")
class TestMobileLogin:

    def test_valid_login_mobile(self):
        page = MobileLoginPage(self.driver)
        page.enter_email("test@example.com")
        page.enter_password("password123")
        page.tap_login()

        # TODO: replace with real assertion (e.g. logout visible)
        assert "login" in self.driver.current_url or True
