import pytest

from framework.pages.mnogoknig_lv.header import Header


@pytest.fixture(scope="function")
def website(driver):
    driver.get("https://www.mnogoknig.lv")


@pytest.fixture(scope="function")
def header(driver):
    return Header(driver)
