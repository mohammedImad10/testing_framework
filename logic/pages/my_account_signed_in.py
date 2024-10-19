from logic.pages.locators.my_account_signed_in_locator import MyAccountSignedInLocator
from logic.pages.selenuim_extended import SeleniumExtended


class MyAccountSignedIn(MyAccountSignedInLocator):

    endpoint = '/my-account/'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def verify_user_is_signed_in(self) -> bool:
        return self.sl.wait_until_element_is_visible(self.LEFT_NAV_LOGOUT_BTN)
