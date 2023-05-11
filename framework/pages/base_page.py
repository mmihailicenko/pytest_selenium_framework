from typing import Callable, Tuple

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def wait_for_element(identifier: Tuple, timeout: int = 10) -> Callable:
        def wrapper(func: Callable):
            def inner(self, *args, **kwargs):
                element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(identifier))
                return func(self, element, *args, **kwargs)
            return inner
        return wrapper

    def click(self, how: By, what: str) -> None:
        element = self.find_element(how, what)
        element.click()

    @staticmethod
    def click_element(element: WebElement) -> None:
        element.click()

    def find_element(self, how: By, what: str) -> WebElement:
        return self.driver.find_element(how, what)

    def find_elements(self, how: By, what: str) -> list:
        return self.driver.find_elements(how, what)

    def is_element_present(self, how: By, what: str) -> bool:
        try:
            self.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def set_text(self, how: By, what: str, value: str) -> None:
        element = self.find_element(how, what)
        element.send_keys(value)
