import allure
from selenium.webdriver.common.by import By

from framework.pages.base_page import BasePage
from framework.pages.kniga_lv.book_page import BookPage
from framework.pages.kniga_lv.login_popup import LoginPopup


class Header(BasePage):
    random_book = (By.CSS_SELECTOR, ".mega-menu-item-62106")
    cart_icon = (By.CSS_SELECTOR, "a.header-cart-link")
    login = (By.CSS_SELECTOR, ".nav-top-not-logged-in")

    @BasePage.wait_for_element(random_book)
    def go_to_random_book(self, element):
        with allure.step("clicking on the 'Random Book' link in the header"):
            self.click_element(element)
        return BookPage(self.driver)

    @BasePage.wait_for_element(login)
    def go_to_login(self, element):
        with allure.step("clicking on the 'Login' link in the header"):
            self.click_element(element)
        return LoginPopup(self.driver)
