from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class LoginPage:
    __username = (By.ID,"username")
    __password = (By.NAME,"pwd")
    __loginButton = (By.ID,"loginButton")
    __err_msg = (By.XPATH,'//span[contains(text(),"invalid")]')

    def __init__(self,driver):
        self.driver = driver

    def set_username(self, un):
        self.driver.find_element(*self.__username).send_keys(un)

    def set_password(self, pw):
        self.driver.find_element(*self.__password).send_keys(pw)

    def click_loginButton(self):
        self.driver.find_element(*self.__loginButton).click()

    def verify_err_msg_displayed(self, wait):
        try:
            wait.until(expected_conditions.visibility_of_element_located(self.__err_msg))
            print("Error displayed")
            return True
        except:
            print("Error NOT displayed")
            return False

    def verify_login_page_displayed(self, wait):
        try:
            wait.until(expected_conditions.visibility_of_element_located(self.__loginButton))
            print("Error displayed")
            return True
        except:
            print("Error NOT displayed")
            return False




