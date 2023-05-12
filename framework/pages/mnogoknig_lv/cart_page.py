import allure
from selenium.webdriver.common.by import By

from framework.pages.base_page import BasePage


class CartPage(BasePage):
    checkout_btn = (By.CSS_SELECTOR, "a.btn.btn-primary")
    product_remove_btn = (By.CSS_SELECTOR, ".fa.fa-remove")
    cart_empty = (By.CSS_SELECTOR, ".text-center")

    def go_to_checkout(self):
        with allure.step("clicking on the 'Go to Checkout' button in the cart page"):
            self.click(self.checkout_btn)

    def is_cart_empty(self) -> bool:
        with allure.step('checking if cart element exists'):
            return self.is_element_present(self.cart_empty)

    def remove_cart_item(self):
        with allure.step('removing first single book from cart'):
            self.click(self.cart_empty)
