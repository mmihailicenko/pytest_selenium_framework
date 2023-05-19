import pytest

from framework.core.webdriver import WebDriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox"],
                     help="Browser to run the tests on")


@pytest.fixture(scope="function")
def driver(browser):
    with WebDriver(browser) as driver:
        yield driver


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
