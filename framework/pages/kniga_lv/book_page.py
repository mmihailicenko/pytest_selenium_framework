import allure
from selenium.webdriver.common.by import By

from framework.pages.base_page import BasePage
from framework.pages.kniga_lv.cart_popup import CartPopup


class BookPage(BasePage):
    btn_add_to_cart = (By.CSS_SELECTOR, ".sticky-add-to-cart")

    def add_to_cart(self):
        with allure.step("clicking on the 'Add to Cart' button in the book page"):
            self.click(self.btn_add_to_cart)
        return CartPopup(self.driver)
