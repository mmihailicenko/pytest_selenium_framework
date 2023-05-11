import pytest


@pytest.fixture(scope="module")
def website(driver):
    driver.get("https://www.mnogoknig.lv")
