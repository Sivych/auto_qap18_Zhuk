from diplom_demowebshop.pages import BasePage
from diplom_demowebshop.helpers import BASE_URL
from diplom_demowebshop.locators import NewsletterLocators
from selenium.webdriver.common.by import By


class NewsletterPage(BasePage, NewsletterLocators):

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(BASE_URL)

    def assert_elements_visible(self):
        assert self.driver.find_element(By.CSS_SELECTOR, self.BLOCK_NEWSLETTER)
        assert self.driver.find_element(By.CSS_SELECTOR, self.NEWSLETTER_EMAIL)

        self.save_screenshot('assert_elements_visible.png')

