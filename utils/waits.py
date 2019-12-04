""" This class consist all methods related with different waits
"""
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from utils.logger import _get_logger


class Waits:

    def __init__(self, driver__browser, config__executor):
        self._logger = _get_logger()
        self._browser = driver__browser.get_browser()
        self._logger.info(f'CAPABILITIES: \n{self._browser.capabilities}')
        self._timeout = config__executor.timeout
        self._wait = WebDriverWait(self._browser, self._timeout)

    def wait_for_element(self, locator):
        return self._wait.until(ec.presence_of_element_located(locator))

    def wait_for_element_visibility(self, locator):
        return self._wait.until(ec.visibility_of_element_located(locator))

    def wait_for_text_to_be_present_in_element(self, locator, text_):
        return self._wait.until(ec.text_to_be_present_in_element(*locator, text_))

    def wait_for_ajax(self):
        self._wait.until(lambda driver: self._browser.execute_script
                         ('return jQuery.active') == 0)
        self._wait.until(lambda driver: self._browser.execute_script
                         ('return document.readyState') == 'complete')

    def wait_until_alert_is_presented(self):
        try:
            return self._wait.until(ec.alert_is_present())
        except TimeoutException:
            print(f'Alert was not presented in {self._timeout} seconds')
