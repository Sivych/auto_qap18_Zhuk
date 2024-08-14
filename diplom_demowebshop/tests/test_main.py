import allure

from diplom_demowebshop.elements import HeaderLinks
from diplom_demowebshop.pages.main_page import MainPage
from diplom_demowebshop.pages.cart_page import CartPage


@allure.title("MAIN TITLE")
@allure.feature("MAIN feature")
def test_that_main_is_opened(driver):
    main_page = MainPage(driver)
    main_page.open()

    main_page.assert_that_main_is_opened()


def test_open_shopping_cart(driver):
    main_page = MainPage(driver)
    main_page.open()

    main_page.assert_that_main_is_opened()

    main_page.click_on_shopping_cart()

    cart_page = CartPage(driver)
    cart_page.assert_that_page_is_opened()
