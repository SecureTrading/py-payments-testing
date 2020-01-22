"""BasePage is a parent class for each page class then this way of implementation allow us
to use his self attributes inside typical page."""


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
