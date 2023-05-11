from selenium.webdriver.common.by import By

from framework.pages.base_page import BasePage


class HomePage(BasePage):
    random_book = (By.CSS_SELECTOR, "li.mega-menu-item-62106")

    def go_to_random_book(self):
        self.click(*self.random_book)

    def is_on_profile_page(self):
        return "Profile" in self.driver.page_source
