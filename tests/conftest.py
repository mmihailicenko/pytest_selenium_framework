import pytest
from framework.core.webdriver import WebDriver


@pytest.fixture(scope="function")
def driver():
    driver = WebDriver()
    yield driver
    driver.quit()
