from logic.helpers.config_helper import get_base_url as base_url
from logic.pages.locators.my_account_signed_out_locator import MyAccountSignedOutLocator
from logic.pages.selenuim_extended import SeleniumExtended
import logging as logger


class MyAccountSignedOut(MyAccountSignedOutLocator):

    endpoint = '/my-account/'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_my_account(self):
        my_account_url = base_url() + self.endpoint
        logger.info(f"Going to {my_account_url}")
        self.driver.get(my_account_url)

    def input_login_username(self, username):
        self.sl.wait_and_input_text(self.LOGIN_USER_NAME, username)

    def input_login_password(self, password):
        self.sl.wait_and_input_text(self.LOGIN_PASSWORD, password)

    def click_login_button(self):
        logger.info(f"Clicking login button")
        self.sl.wait_and_click(self.LOGIN_BTN)

    def get_error_ul(self) -> str:
        return self.sl.wait_until_element_contain_text(self.ERRORS_UL)

    def input_register_email(self, email):
        self.sl.wait_and_input_text(self.REGISTER_EMAIL, email)

    def input_register_password(self, password):
        self.sl.wait_and_input_text(self.REGISTER_PASSWORD, password)

    def click_register_button(self):
        logger.info(f"Clicking register button")
        self.sl.wait_and_click(self.REGISTER_BTN)
