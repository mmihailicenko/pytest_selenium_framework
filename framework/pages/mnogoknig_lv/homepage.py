from selenium.webdriver.common.by import By

from framework.pages.base_page import BasePage


class HomePage(BasePage):
    notfound = (By.ID, "notfound")

    def go_to_notfound(self):
        self.click(*self.notfound)
