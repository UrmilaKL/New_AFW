import pytest

from generic.base_setup import Base_Setup
from generic.excel import Excel
from page.login_page import LoginPage
from generic.excel import Excel
from page.enter_time_track_page import EnterTimeTrackPage
class Test_ValidLogin(Base_Setup):
    @pytest.mark.run(order=1)
    def test_valid_login(self):
        un = Excel.get_cell_data(self.XL_PATH,"valid_login",2, 1)
        pw = Excel.get_cell_data(self.XL_PATH,"valid_login",2,2)
        # 1. Enter valid UN
        loginpage = LoginPage(self.driver)
        loginpage.set_username(un)
        # 2. Enter valid PW
        loginpage.set_password(pw)
        # 3. Click on login button
        loginpage.click_loginButton()
        # 4. Verify the home page is displayed
        homepage = EnterTimeTrackPage(self.driver)
        status = homepage.verify_home_page_displayed(self.wait)
        assert status