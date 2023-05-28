import allure
from selenium.webdriver.common.by import By

from framework.pages.base_page import BasePage


class CheckoutPage(BasePage):
    customer_login = (By.ID, "customer_login")

    def is_login_active(self) -> bool:
        with allure.step('checking if login form exists'):
            return self.is_element_present(self.customer_login)
