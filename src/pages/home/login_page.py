import logging

import src.utilities.custom_logger as cl
from src.base.basepage import BasePage
from src.pages.home.navigation_page import NavigationPage


class LoginPage(BasePage):

    log = cl.custom_logger(log_level=logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"
    successful_login = "//*[@id='navbar']//img[contains(@class, 'gravatar')]"
    _unsuccessful_login = "//div[contains(@class, 'alert') and contains(text(), 'Invalid email or password.')]"

    def click_login_link(self):
        self.element_click_(self._login_link, locator_type="link")

    def enter_email(self, email):
        self.send_keys_(email, self._email_field)

    def enter_password(self, password):
        self.send_keys_(password, self._password_field)

    def click_login_button(self):
        self.element_click_(self._login_button, locator_type='name')

    def login(self, email="", password=""):
        self.click_login_link()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    def verify_login_title(self):
        return self.verify_page_title("Let's Kode It")

    def verify_login_successful(self) -> bool:
        result = self.is_element_present_(self.successful_login, locator_type='xpath')
        return result

    def verify_login_failed(self):
        result = self.is_element_present_(self._unsuccessful_login, locator_type='xpath')
        return result

    def logout(self):
        self.nav.navigate_to_user_settings()
        self.element_click_(locator="//div[@id='navbar']//a[@href='/sign_out']",
                          locator_type="xpath")



