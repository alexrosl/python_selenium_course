import time

import src.utilities.custom_logger as cl
import logging
from src.base.basepage import BasePage


class RegisterCoursesPage(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ############
    # Locators #
    ############
    _all_courses_navbar = "//a[contains(text(), 'All Courses')]"
    _search_box = "search-courses"
    _course = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
    _all_courses = "course-listing-title"
    _enroll_button = "enroll-button-top"
    _cc_num = "//input[@name='cardnumber']"
    _cc_exp = "//input[@name='exp-date']"
    _cc_cvv = "//input[@name='cvc']"
    _postal_code = "//input[@name='postal']"
    _agree_terms_checkbox = "agreed_to_terms_checkbox"
    _submit_enroll = "//button[@id='confirm-purchase']"
    _enroll_error_message = "//div[@id='new_card']" \
                            "//div[contains(text(),'The card number is not a valid credit card number.')]"

    ########################
    # Element Interactions #
    ########################

    def navigate_to_all_course(self):
        self.element_click_(locator=self._all_courses_navbar, locator_type="xpath")

    def enter_course_name(self, name):
        self.send_keys_(name, locator=self._search_box)

    def select_course_to_enroll(self, full_course_name):
        self.element_click_(locator=self._course.format(full_course_name), locator_type="xpath")

    def click_on_enroll_button(self):
        self.element_click_(locator=self._enroll_button)

    def enter_card_num(self, num):
        time.sleep(5)
        self.switch_frame_by_index(locator=self._cc_num, locator_type="xpath")
        self.send_keys_when_ready(num, locator=self._cc_num, locator_type="xpath")
        self.switch_to_default_content()

    def enter_card_exp(self, exp):
        self.switch_frame_by_index(self._cc_exp, locator_type="xpath")
        self.send_keys_(exp, locator=self._cc_exp, locator_type="xpath")
        self.switch_to_default_content()

    def enter_card_CVV(self, cvv):
        self.switch_frame_by_index(locator=self._cc_cvv, locator_type="xpath")
        self.send_keys_(cvv, locator=self._cc_cvv, locator_type="xpath")
        self.switch_to_default_content()

    def enter_postcode(self, postcode):
        self.switch_frame_by_index(locator=self._postal_code, locator_type="xpath")
        self.send_keys_(postcode, locator=self._postal_code, locator_type="xpath")
        self.switch_to_default_content()

    def click_agree_terms(self):
        self.element_click_(self._agree_terms_checkbox)

    def click_enroll_submit_button(self):
        self.element_click_(locator=self._submit_enroll, locator_type="xpath")

    def enter_credit_card_information(self, num, exp, cvv, postcode):
        self.enter_card_num(num)
        self.enter_card_exp(exp)
        self.enter_card_CVV(cvv)
        self.enter_postcode(postcode)

    def enroll_course(self, num="", exp="", cvv="", postcode=""):
        self.click_on_enroll_button()
        self.web_scroll(direction="down")
        self.enter_credit_card_information(num, exp, cvv, postcode)
        self.click_agree_terms()
        self.click_enroll_submit_button()

    def verify_enroll_failed(self):
        message_element = self.wait_for_element_(self._enroll_error_message, locator_type="xpath")
        result = self.is_element_displayed(element=message_element)
        return result
