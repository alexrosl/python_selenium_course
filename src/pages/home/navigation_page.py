import src.utilities.custom_logger as cl
import logging
from src.base.basepage import BasePage


class NavigationPage(BasePage):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _main_page_logo = "//a[@class='navbar-brand header-logo']"
    _login_link = "Login"
    _my_courses = "My Courses"
    _all_courses = "All Courses"
    _practice = "Practice"
    _user_settings_icon = "//div[@id='navbar']//li[@class='dropdown']"
    _successful_login = "//a[contains(@class, 'open-my-profile-dropdown')]"

    def go_to_main_page(self):
        self.web_scroll(direction="up")
        self.element_click_(self._main_page_logo, locator_type="xpath")

    def navigate_to_all_courses(self):
        self.element_click_(locator=self._all_courses, locator_type="link")

    def navigate_to_my_courses(self):
        self.element_click_(locator=self._my_courses, locator_type="link")

    def navigate_to_practice(self):
        self.element_click_(locator=self._practice, locator_type="link")

    def navigate_to_user_settings(self):
        user_settings_element = self.wait_for_element_(locator=self._user_settings_icon,
                                      locator_type="xpath", poll_frequency=1)
        # self.elementClick(element=user_settings_element)
        self.element_click_(locator=self._user_settings_icon, locator_type="xpath")

    def logout(self):
        self.element_click_(locator="_successful_login", locator_type="xpath")
        self.element_click_(locator=".user-signout", locator_type="css")
        self.wait_for_element_(locator=self._login_link, locator_type='link')
