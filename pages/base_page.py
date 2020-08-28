"""BasePage is a parent class for each page class then this way of implementation allow us
to use his self attributes inside typical page."""
from configuration import CONFIGURATION
from locators.payment_methods_locators import PaymentMethodsLocators
from utils.enums.field_type import FieldType


class BasePage:
    def __init__(self, executor__test, extensions__test, reporter__test, config__test, waits__test):
        self._executor = executor__test
        self._action = extensions__test
        self._waits = waits__test
        self._reporter = reporter__test
        self._page_url = config__test.base_page

    def open_self_page(self):
        self._executor.open_page(self._page_url)

    def open_page(self, url):
        self._executor.open_page(url)

    def stop_page(self):
        self._executor.stop_browser()

    def scroll_to_bottom(self):
        self._executor.scroll_to_bottom()

    def scroll_to_top(self):
        self._executor.scroll_to_top()

    def is_connection_not_private_dispayed(self, url):
        if 'Safari' in CONFIGURATION.REMOTE_BROWSER and  \
                (len(self._action.find_elements(PaymentMethodsLocators.not_private_connection_text)) > 0):
            self.open_page(url)

    def wait_for_iframe(self):
        if 'Chrome' in CONFIGURATION.REMOTE_BROWSER:
            self._waits.wait_until_iframe_is_presented_and_switch_to_it(FieldType.SECURITY_CODE.value)
            self._waits.switch_to_default_content()
