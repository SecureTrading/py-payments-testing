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
        'URL': AttrDict({"BASE_URL": get_from_env("BASE_URL", "https://merchant.securetrading.net"), "REACT_APP": get_from_env("REACT_APP", "https://localhost:3000")}),
        'REPORTS_PATH': get_path_from_env('AUTOMATION_REPORTS', 'reports'),
        'BROWSER': get_from_env('AUTOMATION_BROWSER', 'chrome'),
        'TIMEOUT': get_from_env('AUTOMATION_TIMEOUT', 200), # TODO change after test to 20
        'REMOTE': strtobool(get_from_env('REMOTE', 'false')),
        'COMMAND_EXECUTOR': get_from_env('AUTOMATION_COMMAND_EXECUTOR',
                                "https://"+str(get_from_env('BS_USERNAME'))+":"+
                                 str(get_from_env('BS_ACCESS_KEY'))+"@hub.browserstack.com/wd/hub"),
        'REMOTE_OS': get_from_env('OS', ''),
        'REMOTE_OS_VERSION': get_from_env('OS_VERSION', ''),
        'REMOTE_BROWSER': get_from_env('BROWSER', ''),
        'REMOTE_BROWSER_VERSION': get_from_env('BROWSER_VERSION', ''),
        'REMOTE_DEVICE': get_from_env('DEVICE', ''),
        'REMOTE_REAL_MOBILE': get_from_env('REAL_MOBILE', ''),
        'BROWSERSTACK_LOCAL': get_from_env('LOCAL', 'true'),
        'BROWSERSTACK_LOCAL_IDENTIFIER': get_from_env('BS_LOCAL_IDENTIFIER', 'local_id'),
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
    config_to_print = config.copy()
    config_to_print.pop('COMMAND_EXECUTOR')
    logger.info(f'CONFIGURATION: \n{pprint.pformat(config_to_print, indent=4)}')


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
        network_logs = 'true'
        send_keys = 'false'
        if 'Safari' in config.REMOTE_BROWSER:
            network_logs = 'false'
        # if 'IE' in config.REMOTE_BROWSER:
        #     send_keys = 'true'
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
                         "browserstack.networkLogs": network_logs,
                         "browserstack.console": "errors",
                         "ie.ensureCleanSession": 'true',
                         "ie.forceCreateProcessApi": 'true',
                         # "browserstack.sendKeys": send_keys,
                         # "browserstack.idleTimeout": 300
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
