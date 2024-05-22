import pytest

from generic.base_setup import Base_Setup
from generic.excel import Excel
from page.login_page import LoginPage

class Test_InValidLogin(Base_Setup):
    @pytest.mark.run(order=2)
    def test_invalid_login(self):
        un = Excel.get_cell_data(self.XL_PATH,"invalid_login",2, 1)
        pw = Excel.get_cell_data(self.XL_PATH,"invalid_login",2,2)
        # 1. Enter invalid UN
        loginpage = LoginPage(self.driver)
        loginpage.set_username(un)
        # 2. Enter invalid PW
        loginpage.set_password(pw)
        # 3. Click on login button
        loginpage.click_loginButton()
        # 4. Verify the error msg is displayed
        status = loginpage.verify_err_msg_displayed(self.wait)
        assert status
