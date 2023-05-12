from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class WebDriver(webdriver.Remote):
    def __init__(self):
        super().__init__(
            command_executor='http://selenium-hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME
        )
        self.implicitly_wait(5)
        self.set_page_load_timeout(30)
        self.maximize_window()
