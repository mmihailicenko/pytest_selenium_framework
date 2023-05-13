import allure
from selenium.webdriver.common.by import By

from framework.pages.base_page import BasePage
from framework.pages.kniga_lv.cart_page import CartPage
from framework.pages.kniga_lv.checkout_page import CheckoutPage


class CartPopup(BasePage):
    cart_btn = (By.CSS_SELECTOR, "a.button.wc-forward")
    checkout_btn = (By.CSS_SELECTOR, "a.button.checkout.wc-forward")

    @BasePage.wait_for_element(cart_btn)
    def go_to_cart(self, element):
        with allure.step("clicking on the 'View Cart' button in the cart popup"):
            self.click_element(element)
        return CartPage(self.driver)

    @BasePage.wait_for_element(checkout_btn)
    def go_to_checkout(self, element):
        with allure.step("clicking on the 'View Cart' button in the cart popup"):
            self.click_element(element)
        return CheckoutPage(self.driver)
