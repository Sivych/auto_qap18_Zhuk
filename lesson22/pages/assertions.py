class Assertions:

    def __init__(self, driver):
        self.driver = driver

    def assert_that_text_is_visible(self, selector, text):
        el = self.driver.find_element(selector)
        assert el.text == text

    def assert_that_element_is_visible(self, selector):
        assert self.driver.find_element(*selector)

    def assert_that_attribute_is_visible(self, selector, attribute, value):
        el = self.driver.find_element(*selector)
        tmp = el.get_attribute(attribute)
        assert tmp == value, f"The value from element == {tmp}, but we want {value}"

    def assert_that_attribute_class_is_visible(self, selector, value):
        self.assert_that_attribute_is_visible(selector, 'class', value)

    def assert_that_element_checked(self, selector, value):
        self.assert_that_attribute_is_visible(selector, 'checked', value)

    def assert_that_element_containce_text(self, selector, value):
        element = self.driver.find_element(*selector)
        assert element.text == value, "Text from element, not the same"

    def assert_that_element_is_selected(self, selector):
        el = self.driver.find_element(*selector)
        assert el.is_selected()

    def assert_that_element_is_not_selected(self, selector):
        el = self.driver.find_element(*selector)
        assert el.is_selected()


