import allure
from selenium.webdriver.common.by import By

from framework.pages.base_page import BasePage
from framework.pages.kniga_lv.cart_page import CartPage


class CartPopup(BasePage):
    cart_btn = (By.CSS_SELECTOR, "a.button.wc-forward")
    checkout_btn = (By.CSS_SELECTOR, "a.button.checkout.wc-forward")

    def go_to_cart(self):
        with allure.step("clicking on the 'View Cart' button in the cart popup"):
            self.click(self.cart_btn)
        return CartPage(self.driver)
