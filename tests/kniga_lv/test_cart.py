import allure


@allure.title('Adding random book to cart')
@allure.description('Choosing a random book, adding it to cart and verifying cart is not empty')
def test_add_random_book_to_cart(driver, website, header):
    with allure.step("Choosing a random book and adding it to cart"):
        cart_page = (
            header.go_to_random_book()
            .add_to_cart()
            .go_to_cart()
        )

    with allure.step("Verifying cart is not empty"):
        assert cart_page.is_cart_empty() is False


@allure.title('Adding random book to cart and deleting it')
@allure.description('Navigating to a random book page and adding it to cart')
def test_cart_is_empty(driver, website, header, login):
    with allure.step("Clicking on 'Add to Cart' button for a random book"):
        cart_page = (
            header.go_to_random_book()
            .add_to_cart()
            .go_to_cart()
        )

    with allure.step("Verifying cart is not empty"):
        assert cart_page.is_cart_empty() is False

    with allure.step("removing cart item"):
        cart_page.remove_cart_item()

    with allure.step("Verifying cart is empty"):
        assert cart_page.is_cart_empty() is True
