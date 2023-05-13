import allure


@allure.title('Cart page is empty')
@allure.description('Navigating to the cart, verifying it is empty')
def test_add_random_book_to_cart(driver, website, header):
    with allure.step("Navigating to the cart"):
        cart_page = (
            header.go_to_cart()
        )

    with allure.step("Verifying cart is empty"):
        assert cart_page.is_cart_empty() is True
