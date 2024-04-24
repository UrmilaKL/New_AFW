from generic.base_setup import Base_Setup
from generic.excel import Excel
from page.login_page import LoginPage

class Test_InValidLogin(Base_Setup):
    def test_invalid_login(self):
        # 1. Enter invalid UN
        loginpage = LoginPage(self.driver)
        loginpage.set_username("urmilaklbhat@kkkk.com")
        # 2. Enter invalid PW
        loginpage.set_password("abcdef")
        # 3. Click on login button
        loginpage.click_loginButton()
        # 4. Verify the error msg is displayed
        status = loginpage.verify_err_msg_displayed(self.wait)
        assert status
