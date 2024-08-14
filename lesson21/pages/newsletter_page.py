from selenium.webdriver.common.by import By

from lesson21.pages import BasePage
from lesson21.helpers import DEMOWEBSHOP
from lesson21.locators import NewsletterLocators


class NewsletterPage(BasePage, NewsletterLocators):

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(DEMOWEBSHOP)
        return self

    def assert_elements_visible(self):
        assert self.driver.find_element(By.CSS_SELECTOR, self.BLOCK_NEWSLETTER)
        assert self.driver.find_element(By.CSS_SELECTOR, self.NEWSLETTER_EMAIL)

        self.save_screenshot('assert_elements_visible.png')
        return self

