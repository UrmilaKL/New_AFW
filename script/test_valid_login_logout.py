import time

import pytest

from generic.base_setup import Base_Setup
from generic.excel import Excel
from page.login_page import LoginPage
from generic.excel import Excel
from page.enter_time_track_page import EnterTimeTrackPage
class Test_ValidLoginLogout(Base_Setup):
    @pytest.mark.run(order=3)
    def test_valid_login_logout(self):
        un = Excel.get_cell_data(self.XL_PATH,"valid_login",2, 1)
        pw = Excel.get_cell_data(self.XL_PATH,"valid_login",2,2)
        # 1. Enter valid UN
        loginlogoutpage = LoginPage(self.driver)
        loginlogoutpage.set_username(un)
        # 2. Enter valid PW
        loginlogoutpage.set_password(pw)
        # 3. Click on login button
        loginlogoutpage.click_loginButton()
        # 4. Verify the home page is displayed
        # Click Logout Button, Verify login page is displayed
        #time.sleep(2)
        logoutpage = EnterTimeTrackPage(self.driver)
        logoutpage.click_logoutLink()
        status = loginlogoutpage.verify_login_page_displayed(self.wait)
        assert status
