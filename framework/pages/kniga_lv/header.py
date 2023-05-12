import allure
from selenium.webdriver.common.by import By

from framework.pages.base_page import BasePage
from framework.pages.kniga_lv.book_page import BookPage


class Header(BasePage):
    random_book = (By.CSS_SELECTOR, ".mega-menu-item-62106")
    cart_icon = (By.CSS_SELECTOR, "a.header-cart-link")

    def go_to_random_book(self):
        with allure.step("clicking on the 'Random Book' link in the header"):
            self.click(self.random_book)
        return BookPage(self.driver)
