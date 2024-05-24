from selenium.webdriver import Chrome

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver import Edge
from selenium.webdriver.support.wait import WebDriverWait
from pyjavaproperties import Properties
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver import Remote

class Base_Setup:
    CONFIG_PATH = "config.properties"
    XL_PATH = "test_data/input.xlsx"
    @pytest.fixture(autouse=True)
    def precondition(self):
        ppt_obt = Properties()
        ppt_obt.load(open(self.CONFIG_PATH))
        browser = ppt_obt["BROWSER"]
        grid = ppt_obt["GRID"]
        grid_url = ppt_obt["GRID_URL"]
        ito=ppt_obt["ITO"]
        eto=ppt_obt["ETO"]
        app_url=ppt_obt["APP_URL"]

        if grid.lower() == "yes":
            print("Execute script on Remote System")
            if browser.lower() == "chrome":
                options = ChromeOptions()
            elif browser.lower() == "firefox":
                options = FirefoxOptions()
            else:
                options = EdgeOptions()
            print("Open browser", browser)
            self.driver = Remote(command_executor=grid_url, options=options)

        else:
            print("Execute script on Local System")
            print("Open browser", browser)
            if browser.lower() == "chrome":
                self.driver = Chrome()
            elif browser.lower() == "firefox":
                self.driver = Firefox()
            else:
                self.driver = Edge()

        print("Implicitly timeout", ito, "seconds")
        self.driver.implicitly_wait(ito)
        self.driver.maximize_window()
        self.driver.get(app_url)
        print("Explicitly timeout", eto, "seconds")
        self.wait = WebDriverWait(self.driver, eto)

    @pytest.fixture(autouse=True)
    def postcondition(self):
        yield
        print("Close the driver")
        self.driver.close()