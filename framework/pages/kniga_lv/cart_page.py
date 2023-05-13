import allure
from selenium.webdriver.common.by import By

from framework.pages.base_page import BasePage


class CartPage(BasePage):
    checkout_btn = (By.CSS_SELECTOR, ".checkout-button")
    product_remove_btn = (By.CSS_SELECTOR, "a.remove")
    cart_empty = (By.CSS_SELECTOR, ".cart-empty")

    @BasePage.wait_for_element(checkout_btn)
    def go_to_checkout(self, element):
        with allure.step("clicking on the 'Go to Checkout' button in the cart page"):
            self.click_element(element)

    def is_cart_empty(self) -> bool:
        with allure.step('checking if cart element exists'):
            return self.is_element_present(self.cart_empty)

    @BasePage.wait_for_element(product_remove_btn)
    def remove_cart_item(self, element):
        with allure.step('removing first single book from cart'):
            self.click_element(element)
