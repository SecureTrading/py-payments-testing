"""This module consist Behave hooks which allows us to better manage the code workflow"""
# -*- coding: utf-8 -*-

# -- FILE: features/environment.py
# USE: behave -D BEHAVE_DEBUG_ON_ERROR         (to enable  debug-on-error)
# USE: behave -D BEHAVE_DEBUG_ON_ERROR=yes     (to enable  debug-on-error)
# USE: behave -D BEHAVE_DEBUG_ON_ERROR=no      (to disable debug-on-error)
import ioc_config

from page_factory import PageFactory
from utils.mock_handler import start_mock_server

BEHAVE_DEBUG_ON_ERROR = False


def setup_debug_on_error(userdata):
    """Debug-on-Error(in case of step failures) providing, by using after_step() hook.
    The debugger starts when step definition fails"""
    global BEHAVE_DEBUG_ON_ERROR
    BEHAVE_DEBUG_ON_ERROR = userdata.getbool('BEHAVE_DEBUG_ON_ERROR')


def before_all(context):
    """Run before the whole shooting match"""
    context.config = ioc_config.CONFIG.resolve('test')
    context.test_data = ioc_config.TEST_DATA.resolve('test')
    # start_mock_server()


def before_scenario(context, scenario):
    """Run before each scenario"""
    context.page_factory = PageFactory()

    browser_name = ioc_config.CONFIG.resolve('driver').browser
    scenario.name = '%s_%s' % (scenario.name, browser_name.upper())


def after_scenario(context, scenario):
    """Run after each scenario"""
    context.page_factory = PageFactory()

    executor = ioc_config.EXECUTOR.resolve('test')
    browser_name = ioc_config.CONFIG.resolve('driver').browser
    scenario.name = '%s_%s' % (scenario.name, browser_name.upper())
    executor.clear_cookies()


def after_all(context):
    """Run after the whole shooting match"""
    context.page_factory = PageFactory()

    executor = ioc_config.EXECUTOR.resolve('test')
    executor.close_browser()


def after_step(context, step):
    """Run after each step"""
    if step.status == 'failed':
        scenario_name = _clean(context.scenario.name.title())
        feature_name = _clean(context.feature.name.title())
        step_name = _clean(step.name.title())
        filename = f'{feature_name}_{scenario_name}_{step_name}'
        executor = ioc_config.REPORTER.resolve('test')
        executor.save_screenshot_and_page_source(filename)


def _clean(text_to_clean):
    """Method to clean text which will be used for tests run reporting"""
    text = ''.join(x if x.isalnum() else '' for x in text_to_clean)
    return text
