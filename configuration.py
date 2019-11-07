""" Please configure you solution here
"""
import pprint
from distutils.util import strtobool
from attrdict import AttrDict
from utils.logger import _get_logger
from utils.read_configuration import get_path_from_env, get_from_env


def load_config():
    """
    Set config env variables
    """
    config = {

        'URL': AttrDict({"BASE_URL": "http://www.google.com"}),
        'REPORTS_PATH': get_path_from_env('AUTOMATION_REPORTS', 'reports'),
        'BROWSER': get_from_env('AUTOMATION_BROWSER', 'chrome'),
        'TIMEOUT': get_from_env('AUTOMATION_TIMEOUT', 10),
        'REMOTE': get_from_env('AUTOMATION_REMOTE', 'false'),
        'COMMAND_EXECUTOR': get_from_env('AUTOMATION_COMMAND_EXECUTOR',
                                         "https://BROWSERSTACK_USERNAME:BROWSERSTACK_KEY@hub.browserstack.com/wd/hub"),
    }

    return AttrDict(config)


def print_properties(config):
    """
    Printing all configuration data before starting the tests
    """
    logger = _get_logger()
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
        self.browser = CONFIGURATION.BROWSER.lower()
        remote = strtobool(CONFIGURATION.REMOTE)
        self.remote = bool(remote)
        self.command_executor = CONFIGURATION.COMMAND_EXECUTOR


class TestExecutorConfig:
    """
    reports_path - path, where tests artifacts should be stored
    timeout - max time before continuing with the next step
    """

    def __init__(self):
        self.timeout = int(CONFIGURATION.TIMEOUT)
        self.reports_path = CONFIGURATION.REPORTS_PATH
