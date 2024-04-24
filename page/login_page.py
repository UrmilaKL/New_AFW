from selenium.webdriver.common.by import By


class LoginPage:
    __username = (By.ID,"username")
    __password = (By.NAME,"pwd")
    __loginButton = (By.ID,"loginButton")

    def __init__(self,driver):
        self.driver = driver

    def set_username(self, un):
        self.driver.find_element(*self.__username).send_keys(un)

    def set_password(self, pw):
        self.driver.find_element(*self.__password).send_keys(pw)

    def click_loginButton(self):
        self.driver.find_element(*self.__loginButton).click()


