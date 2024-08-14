from lesson21.pages.newsletter_page import NewsletterPage


def test_open_page(driver):
    page = NewsletterPage(driver)
    page.open()

    page.assert_elements_visible()
