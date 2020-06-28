import unittest

import pytest

from src.utilities.constants import Constants
from src.pages.home.login_page import LoginPage
from src.utilities.teststatus import TestStatus
from src.utilities.custom_logger import get_function_name


@pytest.mark.usefixtures("one_time_setup", "setup")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_setup):
        self.login_page = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.driver.get(Constants.base_url)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.login_page.login("test@email.com", "abcabc")
        self.login_page.screenshot("screenshot_test")
        result1 = self.login_page.verify_login_title()
        self.ts.mark(result1, "Title is correct")
        result2 = self.login_page.verify_login_successful()
        self.ts.mark_final(get_function_name(), result2, "Login icon is correct")

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.login_page.login()
        result = self.login_page.verify_login_failed()
        assert result is True
