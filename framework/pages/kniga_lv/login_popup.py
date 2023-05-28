import allure
from selenium.webdriver.common.by import By

from framework.pages.base_page import BasePage


class LoginPopup(BasePage):
    username = (By.ID, "username")
    password = (By.ID, "password")
    submit_btn = (By.CSS_SELECTOR, ".woocommerce-form-login__submit")

    @BasePage.wait_for_element(username)
    def fill_in_username(self, element, username: str):
        with allure.step("clicking on the 'View Cart' button in the cart popup"):
            self.set_text(element, username)
        return LoginPopup(self.driver)

    @BasePage.wait_for_element(password)
    def fill_in_password(self, element, password: str):
        with allure.step("clicking on the 'View Cart' button in the cart popup"):
            self.set_text(element, password)
        return LoginPopup(self.driver)

    @BasePage.wait_for_element(submit_btn)
    def submit(self, element):
        with allure.step("clicking on the 'Random Book' link in the header"):
            self.click_element(element)
