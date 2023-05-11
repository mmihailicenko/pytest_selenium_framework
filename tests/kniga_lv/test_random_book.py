import time

import allure

from framework.pages.kniga_lv.homepage import HomePage


@allure.title('Random Book')
@allure.description('Navigating to a random book page')
def test_navigation(driver, website):
    with allure.step("Opening Home Page"):
        homepage = HomePage(driver)

    with allure.step("Navigate to Random Book"):
        homepage.go_to_random_book()

    # with allure.step("Verify that the user is logged in"):
    #     assert "Welcome" in driver.page_source
    time.sleep(5)
