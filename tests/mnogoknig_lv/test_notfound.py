import time

from framework.pages.mnogoknig_lv.homepage import HomePage


def test_notfound(driver, website):
    homepage = HomePage(driver)
    homepage.go_to_notfound()
    time.sleep(5)
