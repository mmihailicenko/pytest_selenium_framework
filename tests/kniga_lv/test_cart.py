import allure


@allure.title('Adding a book to cart and deleting it')
@allure.description('Navigating to a random book page, adding it to cart, deleting it, verifying cart is empty')
def test_cart_is_empty(driver, website, header):
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


@allure.title('Adding a book to cart and going to checkout')
@allure.description('Choosing a random book, adding it to cart and verifying checkout asks for login')
def test_cart_checkout_wo_login(driver, website, header):
    with allure.step("Choosing a random book and adding it to cart"):
        checkout_page = (
            header.go_to_random_book()
            .add_to_cart()
            .go_to_checkout()
        )

    with allure.step("Verifying checkout page asks for login"):
        assert checkout_page.is_login_active() is True


@allure.title('Adding a book to cart and checking out')
@allure.description('Choosing a random book, adding it to cart and verifying checkout is possible')
def test_cart_checkout_w_login(driver, website, header, login):
    with allure.step("Choosing a random book and adding it to cart"):
        checkout_page = (
            header.go_to_random_book()
            .add_to_cart()
            .go_to_checkout()
        )

    with allure.step("Verifying checkout page is possible"):
        assert checkout_page.is_login_active() is False
