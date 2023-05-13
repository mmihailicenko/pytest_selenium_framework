import allure
from selenium.webdriver.common.by import By

from framework.pages.base_page import BasePage
from framework.pages.mnogoknig_lv.cart_page import CartPage


class Header(BasePage):
    cart_icon = (By.ID, "cart")

    @BasePage.wait_for_element(cart_icon)
    def go_to_cart(self, element):
        with allure.step("clicking on the 'My Cart' link in the header"):
            self.click_element(element)
        return CartPage(self.driver)
