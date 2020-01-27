""" Please configure you solution here
"""
import pprint
from datetime import date
from distutils.util import strtobool
from attrdict import AttrDict

from utils.logger import _get_logger
from utils.read_configuration import get_path_from_env, get_from_env


def load_config():
    """
    Set config env variables
    """
    config = {
        'URL': AttrDict({"BASE_URL": get_from_env("BASE_URL", "https://merchant.example.com:8443")}),
        'REPORTS_PATH': get_path_from_env('AUTOMATION_REPORTS', 'reports'),
        'BROWSER': get_from_env('AUTOMATION_BROWSER', 'chrome'),
        'TIMEOUT': get_from_env('AUTOMATION_TIMEOUT', 10),
        'REMOTE': strtobool(get_from_env('AUTOMATION_REMOTE', 'false')),
        'COMMAND_EXECUTOR': get_from_env('AUTOMATION_COMMAND_EXECUTOR',
                                "https://"+str(get_from_env('BROWSERSTACK_USERNAME'))+":"+
                                 str(get_from_env('BROWSERSTACK_ACCESS_KEY'))+"@hub.browserstack.com/wd/hub"),
        'REMOTE_OS': get_from_env('AUTOMATION_REMOTE_OS', ''),
        'REMOTE_OS_VERSION': get_from_env('AUTOMATION_REMOTE_OS_VERSION', ''),
        'REMOTE_BROWSER': get_from_env('AUTOMATION_REMOTE_BROWSER', ''),
        'REMOTE_BROWSER_VERSION': get_from_env('AUTOMATION_REMOTE_BROWSER_VERSION', ''),
        'REMOTE_DEVICE': get_from_env('AUTOMATION_REMOTE_DEVICE', ''),
        'REMOTE_REAL_MOBILE': get_from_env('AUTOMATION_REMOTE_REAL_MOBILE', ''),
        'BROWSERSTACK_LOCAL': get_from_env('LOCAL', 'true'),
        'BROWSERSTACK_LOCAL_IDENTIFIER': get_from_env('BROWSERSTACK_LOCAL_IDENTIFIER'),
        'ACCEPT_SSL_CERTS': get_from_env('ACCEPT_SSL_CERTS', 'true'),
        'PROJECT_NAME': get_from_env('PROJECT_NAME', 'JS Payments Interface'),
        'BUILD_NAME': get_from_env('BUILD_NAME', 'Behavioral test: ' + str(date.today())),
        'BROWSERSTACK_DEBUG': get_from_env('BROWSERSTACK_DEBUG', 'true'),
    }

    return AttrDict(config)


def print_properties(config):
    """
    Printing all configuration data before starting the tests
    """
    logger = _get_logger()
    config.pop('COMMAND_EXECUTOR')
    logger.info(f'CONFIGURATION: \n{pprint.pformat(config, indent=4)}')


CONFIGURATION = load_config()
print_properties(CONFIGURATION)


class TestConfig:
    """ Url section"""
    def __init__(self):

        self.base_page = CONFIGURATION.URL.BASE_URL


class DriverConfig:
    """
    Webdriver configuration:
    browser name - one of: chrome, firefox, ie, edge, safari, phantom
    if remote = True, command_executor (selenium server) endpoint must be set
    """

    def __init__(self):
        self.remote = CONFIGURATION.REMOTE
        if self.remote:
            if CONFIGURATION.REMOTE_BROWSER:
                self.browser = CONFIGURATION.REMOTE_BROWSER.lower()
            else:
                self.browser = CONFIGURATION.REMOTE_DEVICE.lower()
            self.remote_capabilities = self.get_remote_capabilities(CONFIGURATION)
            self.command_executor = CONFIGURATION.COMMAND_EXECUTOR
        else:
            self.browser = CONFIGURATION.BROWSER.lower()
            self.remote_capabilities = {}
            self.command_executor = ""

    @staticmethod
    def get_remote_capabilities(config):
        possible_caps = {"os": config.REMOTE_OS,
                         "os_version": config.REMOTE_OS_VERSION,
                         "browserName": config.REMOTE_BROWSER,
                         "browserVersion": config.REMOTE_BROWSER_VERSION,
                         "browserstack.local": config.BROWSERSTACK_LOCAL,
                         "browserstack.localIdentifier": config.BROWSERSTACK_LOCAL_IDENTIFIER,
                         "device": config.REMOTE_DEVICE,
                         "real_mobile": config.REMOTE_REAL_MOBILE,
                         "acceptSslCerts": config.ACCEPT_SSL_CERTS,
                         "project": config.PROJECT_NAME,
                         "build": config.BUILD_NAME,
                         "browserstack.debug": config.BROWSERSTACK_DEBUG,
                         # "browserstack.networkLogs": "true",
                         # "ie.ensureCleanSession": 'true',
                         # "ie.forceCreateProcessApi": 'true',
                         # "ignoreProtectedModeSettings": "true",
                         }
        capabilities = {}
        for key, value in possible_caps.items():
            if value:
                capabilities[key] = value
        return capabilities


class TestExecutorConfig:
    """
    reports_path - path, where tests artifacts should be stored
    timeout - max time before continuing with the next step
    """

    def __init__(self):
        self.timeout = int(CONFIGURATION.TIMEOUT)
        self.reports_path = CONFIGURATION.REPORTS_PATH
