""" This class consist all necessary web elements extensions methods
"""
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from utils.waits import Waits


class WebElementsExtensions(Waits):

    def send_keys(self, locator, string):
        element = self.find_element(locator)
        element.send_keys(string)

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def click_with_wait(self, locator):
        self.wait_for_ajax()
        element = self.wait_for_element(locator)
        element.click()

    def find_element(self, locator):
        self.wait_for_ajax()
        element = self._browser.find_element(*locator)
        # * collects all the positional arguments in a tuple
        return element

    def find_elements(self, locator):
        self.wait_for_ajax()
        elements = self._browser.find_elements(*locator)
        return elements

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text

    def clear_input(self, locator):
        element = self.find_element(locator)
        element.clear()

    def is_checkbox_selected(self, locator):
        element = self.find_element(locator)
        return element.is_selected()

    def get_element_attribute(self, locator, attribute_name):
        element = self.find_element(locator)
        return element.get_attribute(attribute_name)

    def is_element_enabled(self, locator):
        element = self.find_element(locator)
        is_enabled = element.is_enabled()
        return is_enabled

    def scroll_directly_to_element(self, locator):
        element = self.find_element(locator)
        self._browser.execute_script("arguments[0].scrollIntoView();", element)

    def enter(self, locator):
        element = self.find_element(locator)
        element.send_keys(Keys.RETURN)

    def select_element_from_list(self, locator, element_number):
        select = Select(self._browser.find_elements(*locator))
        select.select_by_index(element_number)
