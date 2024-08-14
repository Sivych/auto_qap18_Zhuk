import allure

from diplom_demowebshop.elements import HeaderLinks
from diplom_demowebshop.helpers import BASE_URL
from diplom_demowebshop.locators.cart_locators import CartLocators
from diplom_demowebshop.locators import HeaderLinksLocators
from diplom_demowebshop.pages import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage, CartLocators, HeaderLinks):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Open page demowebshop.tricentis.com")
    def open(self):
        self.driver.get(BASE_URL)

    # def click_on_shopping_cart(self):
    #     assert self.click(self.SHOPPING_CART)

    @allure.step("Assert that page is opened")
    def assert_that_page_is_opened(self):
        assert self.get_element(By.CSS_SELECTOR, self.TEXT_SHOPPING_CART)
        assert self.get_element(By.CSS_SELECTOR, self.CONTINUE_SHOPPING)
        assert self.get_element(By.CSS_SELECTOR, self.TABLE)

        self.save_screenshot('assert_that_page_is_opened.png')




