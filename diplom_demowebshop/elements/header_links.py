from diplom_demowebshop.locators import HeaderLinksLocators
from diplom_demowebshop.pages.base_page import BasePage
from diplom_demowebshop.helpers.urls import BASE_URL


class HeaderLinks(BasePage, HeaderLinksLocators):

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_shopping_cart(self):
        self.click(self.SHOPPING_CART)



