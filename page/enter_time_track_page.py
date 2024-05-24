from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

class EnterTimeTrackPage:
    __logout = (By.ID,"logoutLink")

    def __init__(self,driver):
        self.driver = driver

    def verify_home_page_displayed(self, wait):
        try:
            wait.until(expected_conditions.visibility_of_element_located(self.__logout))
            print("Home page displayed")
            return True
        except:
            print("Home page NOT displayed")
            return False

    def click_logoutLink(self):
        self.driver.find_element(*self.__logout).click()

