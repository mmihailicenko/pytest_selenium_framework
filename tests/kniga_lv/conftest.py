import os

import pytest

from framework.pages.kniga_lv.header import Header


@pytest.fixture(scope="function")
def website(driver):
    driver.get("https://www.kniga.lv")


@pytest.fixture(scope="function")
def header(driver):
    return Header(driver)


username = 'mikhail.mihailicenko@gmail.com'#os.environ.get("USERNAME")
password = 'Jer87ich0'#os.environ.get("PASSWORD")


@pytest.fixture(scope="function")
def login(driver, header):
    return {
        header.go_to_login()
        .fill_in_username(username)
        .fill_in_password(password)
        .submit()
    }
