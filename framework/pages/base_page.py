from typing import Callable, Tuple

from selenium.common.exceptions import NoSuchElementException
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

    def click(self, identifier: tuple) -> None:
        self.find_element(identifier).click()

    @staticmethod
    def click_element(element: WebElement) -> None:
        element.click()

    def find_element(self, identifier: tuple) -> WebElement:
        return self.driver.find_element(*identifier)

    def find_elements(self, identifier: tuple) -> list:
        return self.driver.find_elements(*identifier)

    def is_element_present(self, identifier: tuple) -> bool:
        try:
            self.find_element(identifier)
        except NoSuchElementException:
            return False
        return True

    def set_text(self, identifier: tuple, value: str) -> None:
        element = self.find_element(identifier)
        element.send_keys(value)
