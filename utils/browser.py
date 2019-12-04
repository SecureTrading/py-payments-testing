""" This class consist all methods related with browser activities"""
from utils.waits import Waits


class Browser(Waits):

    def __init__(self, config):
        self.config = config

    def open_page(self, page_url):
        self._browser.get(page_url)
        self.fullscreen()

    def close_browser(self):
        self._browser.quit()

    def clear_cookies(self):
        self._browser.delete_all_cookies()

    def get_cookie_by_name(self, cookie_name):
        return self._browser.get_cookie(cookie_name)

    def is_cookie_exist(self, cookie_name):
        return bool(self.get_cookie_by_name(cookie_name))

    def switch_to_alert(self):
        self.wait_until_alert_is_presented()
        alert = self._browser.switch_to_alert()
        return alert

    def accept_alert(self):
        alert = self.switch_to_alert()
        alert.accept()

    def dismiss_alert(self):
        alert = self.switch_to_alert()
        alert.dismiss()

    def get_alert_text(self):
        alert = self.switch_to_alert()
        return alert.text

    def get_page_url(self):
        return self._browser.current_url

    def get_page_title(self):
        title = self._browser.title
        return title

    def scroll_horizontally(self):
        self._browser.execute_script("window.scrollBy(100,0)")  # Scroll 100px to the right

    def fullscreen(self):
        if not(self.config.REMOTE_DEVICE.startswith('iPhone')):
            self._browser.maximize_window()

    def scroll_into_view(self, element):
        self._browser.execute_script("arguments[0].scrollIntoView();", element)
