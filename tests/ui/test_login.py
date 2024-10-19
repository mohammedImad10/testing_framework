import time

import pytest
from logic.pages.my_account_signed_out import MyAccountSignedOut


@pytest.mark.usefixtures("init_driver")
class TestLogin:

    @pytest.mark.tcid1
    def test_login_none_existing_user_negative(self):
        username = 'wrongname'
        password = 'wrongpass'
        expected_error = f'Error: The username {username} is not registered on this site'
        my_account = MyAccountSignedOut(self.driver)
        my_account.go_to_my_account()
        my_account.input_login_username(username)
        my_account.input_login_password(password)
        my_account.click_login_button()
        error = my_account.get_error_ul()
        assert expected_error in error, f"expected to get error {expected_error} but got {error}"


