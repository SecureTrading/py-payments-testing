from locators.sample_test_locators import SamplePageLocators
from pages.base_page import BasePage


class SamplePage(BasePage, SamplePageLocators):

    def get_page_title(self):
        page_title = self._executor.get_page_title()
        return page_title

    def get_page_url(self):
        return self._executor.get_page_url()
