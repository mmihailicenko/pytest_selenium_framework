import pytest

from framework.pages.kniga_lv.header import Header


@pytest.fixture(scope="function")
def website(driver):
    driver.get("https://www.kniga.lv")


@pytest.fixture(scope="function")
def header(driver):
    return Header(driver)
