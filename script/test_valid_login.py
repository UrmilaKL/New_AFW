from generic.base_setup import Base_Setup
from generic.excel import Excel
from page.login_page import LoginPage
from page.enter_time_track_page import EnterTimeTrackPage
class Test_ValidLogin(Base_Setup):
    def test_valid_login(self):
        # 1. Enter valid UN
        loginpage = LoginPage(self.driver)
        loginpage.set_username("urmilaklbhat@gmail.com")
        # 2. Enter valid PW
        loginpage.set_password("b4@p8A@b")
        # 3. Click on login button
        loginpage.click_loginButton()
        # 4. Verify the home page is displayed
        homepage = EnterTimeTrackPage(self.driver)
        status = homepage.verify_home_page_displayed(self.wait)
        assert status