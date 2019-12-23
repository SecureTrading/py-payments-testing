from locators.animated_card_locators import AnimatedCardLocators
from pages.base_page import BasePage


class AnimatedCardPage(BasePage, AnimatedCardLocators):

    def get_page_title(self):
        page_title = self._executor.get_page_title()
        return page_title

    def get_page_url(self):
        return self._executor.get_page_url()
