import allure

from diplom_demowebshop.pages.newsletter_page import NewsletterPage


@allure.title("Test Authentication")
def test_open_page(driver):
    page = NewsletterPage(driver)
    page.open()

    page.assert_elements_visible()
