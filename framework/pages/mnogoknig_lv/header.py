import allure
from selenium.webdriver.common.by import By

from framework.pages.base_page import BasePage
from framework.pages.mnogoknig_lv.cart_page import CartPage


class Header(BasePage):
    cart_icon = (By.ID, "cart")

    def go_to_cart(self):
        with allure.step("clicking on the 'My Cart' link in the header"):
            self.click(self.cart_icon)
        return CartPage(self.driver)
