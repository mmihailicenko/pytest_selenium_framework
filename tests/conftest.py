import pytest
from framework.core.webdriver import WebDriver


@pytest.fixture(scope="session")
def driver():
    driver = WebDriver()
    yield driver
    driver.quit()
