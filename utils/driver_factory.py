"""This module is essential for executing our test against real web browser.
It provides 3 separated classes(SeleniumDriver, Driver and DriverFactory)
containing several functions which allow to create, manage and distribute
WebDriver instance which is responsible for direct connection and allows
to manipulate browser window thanks to its functions.
It based on singleton pattern to operate on a single instance of a driver.
"""
import abc
from enum import Enum
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.exceptions import ConfigurationError


class Drivers(Enum):
    chrome = webdriver.Chrome
    firefox = webdriver.Firefox
    ie = webdriver.Ie
    edge = webdriver.Edge
    safari = webdriver.Safari
    phantom = webdriver.PhantomJS


class DesiredCapabilities(Enum):
    chrome = webdriver.DesiredCapabilities.CHROME
    firefox = webdriver.DesiredCapabilities.FIREFOX
    ie = webdriver.DesiredCapabilities.INTERNETEXPLORER
    edge = webdriver.DesiredCapabilities.EDGE
    phantom = webdriver.DesiredCapabilities.PHANTOMJS
    safari = webdriver.DesiredCapabilities.SAFARI


class DriverFactory:
    _browser = None

    def __init__(self, config__driver):
        self._browser_name = config__driver.browser
        self._remote = config__driver.remote
        self._command_executor = config__driver.command_executor
        self._remote_capabilities = config__driver.remote_capabilities

    def _set_browser(self):
        driver = SeleniumDriver(browser_name=self._browser_name, remote=self._remote,
                                command_executor=self._command_executor,
                                remote_capabilities=self._remote_capabilities
                                )
        browser = driver.get_driver()
        DriverFactory._browser = browser

    def get_browser(self):
        if not DriverFactory._browser:
            self._set_browser()
        return DriverFactory._browser


class Driver:
    __metaclass__ = abc.ABCMeta

    def __init__(self, browser_name, remote, command_executor, remote_capabilities):
        self._browser_name = browser_name
        self._remote = remote
        self._remote_capabilities = remote_capabilities
        self._command_executor = command_executor

    @abc.abstractmethod
    def get_driver(self):
        pass

    @staticmethod
    def _get_desired_capabilities(capability):
        desired_capabilities = DesiredCapabilities[capability]
        return desired_capabilities.value.copy()

    def _check_command_executor_is_set(self):
        if not self._command_executor:
            raise ConfigurationError("Command_executor is required property!")


class SeleniumDriver(Driver):
    def get_driver(self):
        if self._remote:
            driver = self._create_remote()
        else:
            driver = self._create()
        return driver

    def _create_remote(self):
        self._check_command_executor_is_set()

        remote_driver = webdriver.Remote(command_executor=self._command_executor,
                                         desired_capabilities=self._remote_capabilities)
        return remote_driver

    def _create(self):
        driver = Drivers[self._browser_name]
        kwargs = {}
        if self._browser_name == "chrome":
            kwargs['chrome_options'] = Options()
            # kwargs['chrome_options'].headless = True
            kwargs['chrome_options'].add_argument('--no-sandbox')
            kwargs['chrome_options'].add_argument('--disable-dev-shm-usage')
            kwargs['chrome_options'].add_argument('--ignore-certificate-errors')
        return driver.value(**kwargs)
