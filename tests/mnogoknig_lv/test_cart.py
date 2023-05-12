import allure


@allure.title('Adding random book to cart')
@allure.description('Navigating to a random book page and adding it to cart')
def test_add_random_book_to_cart(driver, website, header):
    with allure.step("Clicking on 'Add to Cart' button for a random book"):
        cart_page = (
            header.go_to_cart()
        )

    with allure.step("Verifying cart is empty"):
        assert cart_page.is_cart_empty() is True
