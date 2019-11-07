""" This module consist all methods related with reporting
"""
import os
import time


class Reporter:

    def __init__(self, driver__browser, config__executor):
        self._browser = driver__browser.get_browser()
        self._reports_path = config__executor.reports_path

    def _create_reports_dir(self):
        if not os.path.exists(self._reports_path):
            os.makedirs(self._reports_path)

    def save_screenshot_and_page_source(self, filename):
        sreenshot_filename = f'{filename}.png'
        screenshot_filepath = os.path.join(self._reports_path, sreenshot_filename)
        source_filename = f'{filename}.html'
        source_filepath = os.path.join(self._reports_path, source_filename)

        self.save_screenshot(screenshot_filepath)
        self._create_reports_dir()
        self.save_page_source(source_filepath)

    def save_screenshot(self, filepath):
        self._browser.save_screenshot(filepath)

    def save_instant_screenshot(self):
        filename = time.strftime("%Y%m%d-%H%M%S.png")
        filepath = os.path.join(self._reports_path, filename)
        self._browser.save_screenshot(filepath)

    def save_page_source(self, filepath):
        source = self._browser.page_source
        with open(filepath, 'a', encoding='utf-8') as path:
            path.write(source)
