import time
import pytest
from logic.pages.my_account_signed_out import MyAccountSignedOut
from logic.pages.my_account_signed_in import MyAccountSignedIn
from logic.data import register_data


@pytest.mark.usefixtures("init_driver")
class TestRegister:

    @pytest.mark.tcid2
    def test_register_valid_new_user(self):
        my_account_o = MyAccountSignedOut(self.driver)
        my_account_i = MyAccountSignedIn(self.driver)
        my_account_o.go_to_my_account()
        data = register_data.get_email_and_password_to_register()
        my_account_o.input_register_email(data['email'])
        my_account_o.input_register_password(data['password'])
        my_account_o.click_register_button()

        assert my_account_i.verify_user_is_signed_in()
