"""
PageFactory module is responsible for creation of a Page objects
"""
from pyioc.containers import NamespacedContainer, InstanceLifetime
from ioc_config import EXECUTOR, EXTENSIONS, REPORTER, CONFIG, WAITS


# Register modules here
from pages.payment_methods_page import PaymentMethodsPage
from pages.animated_card_page import AnimatedCardPage
from pages.reactjs_page import ReactjsPage

MODULES = NamespacedContainer('modules')

PAGES = NamespacedContainer('pages')
PAGES.add_sub_container(EXECUTOR)
PAGES.add_sub_container(EXTENSIONS)
PAGES.add_sub_container(WAITS)
PAGES.add_sub_container(REPORTER)
PAGES.add_sub_container(CONFIG)
PAGES.add_sub_container(MODULES)

# Register pages here
PAGES.register_callable_with_deps('payment_methods_page', PaymentMethodsPage,
                                  lifetime=InstanceLifetime.NewInstancePerCall)
PAGES.register_callable_with_deps('animated_card_page', AnimatedCardPage,
                                  lifetime=InstanceLifetime.NewInstancePerCall)
PAGES.register_callable_with_deps('reactjs_page', ReactjsPage,
                                  lifetime=InstanceLifetime.NewInstancePerCall)


class PageFactory:
    """PageFactory class to create proper page name"""

    @staticmethod
    def get_page(page_name):
        """Get page name method"""
        page_name = '%s_page' % page_name
        page_name = page_name.lower()
        page_name = page_name.replace(' ', '_')
        page = PAGES.resolve(page_name)
        return page
