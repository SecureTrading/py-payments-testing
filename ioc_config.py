""" IoC enables a framework to take control of the flow of a program
and make calls to our custom code.
"""
from pyioc.containers import NamespacedContainer, InstanceLifetime
from configuration import DriverConfig, TestConfig, TestExecutorConfig
from utils.driver_factory import DriverFactory
from utils.browser import Browser
from utils.extensions import WebElementsExtensions
from utils.reporter import Reporter
from utils.waits import Waits
from utils.test_data import TestData

# configuration
CONFIG = NamespacedContainer('config')
CONFIG.register_callable('driver', DriverConfig, lifetime=InstanceLifetime.Singleton)
CONFIG.register_callable('test', TestConfig, lifetime=InstanceLifetime.Singleton)
CONFIG.register_callable('executor', TestExecutorConfig, lifetime=InstanceLifetime.Singleton)

# executors
DRIVER = NamespacedContainer('driver')
DRIVER.add_sub_container(CONFIG)
DRIVER.register_callable_with_deps('browser', DriverFactory, lifetime=InstanceLifetime.Singleton)

EXECUTOR = NamespacedContainer('executor')
EXECUTOR.add_sub_container(CONFIG)
EXECUTOR.add_sub_container(DRIVER)
EXECUTOR.register_callable_with_deps('test', Browser, lifetime=InstanceLifetime.NewInstancePerCall)

EXTENSIONS = NamespacedContainer('extensions')
EXTENSIONS.add_sub_container(CONFIG)
EXTENSIONS.add_sub_container(DRIVER)
EXTENSIONS.register_callable_with_deps('test', WebElementsExtensions,
                                       lifetime=InstanceLifetime.NewInstancePerCall)
WAITS = NamespacedContainer('waits')
WAITS.add_sub_container(CONFIG)
WAITS.add_sub_container(DRIVER)
WAITS.register_callable_with_deps('test', Waits, lifetime=InstanceLifetime.NewInstancePerCall)

REPORTER = NamespacedContainer('reporter')
REPORTER.add_sub_container(CONFIG)
REPORTER.add_sub_container(DRIVER)
REPORTER.register_callable_with_deps('test', Reporter, lifetime=InstanceLifetime.NewInstancePerCall)

TEST_DATA = NamespacedContainer('test_data')
TEST_DATA.add_sub_container(CONFIG)
TEST_DATA.add_sub_container(DRIVER)
TEST_DATA.register_callable_with_deps('test', TestData, lifetime=InstanceLifetime.Singleton)
