from locators.reactjs_app_locators import ReactJsAppLocators
from pages.base_page import BasePage
from utils.helpers.request_executor import add_to_shared_dict


class ReactjsPage(BasePage):

    def get_page_title(self):
        page_title = self._executor.get_page_title()
        return page_title

    def validate_notofication_message(self, expected_message):
        self.scroll_to_top()
        actual_message = self._action.get_text_with_wait(ReactJsAppLocators.success_notification)
        assertion_message = f'Payment status is not correct, should be: "{expected_message}" but is: "{actual_message}"'
        add_to_shared_dict("assertion_message", assertion_message)
        assert expected_message in actual_message, assertion_message

    def click_personal_data_tab(self):
        self._executor.wait_for_element_to_be_clickable(ReactJsAppLocators.personal_data_tab)
        self._action.click(ReactJsAppLocators.personal_data_tab)
        self._executor.wait_for_element_visibility(ReactJsAppLocators.personal_data_title)

    def click_home_tab(self):
        self._executor.wait_for_element_to_be_clickable(ReactJsAppLocators.home_tab)
        self._action.click(ReactJsAppLocators.home_tab)

    def click_payment_tab(self):
        self._executor.wait_for_element_to_be_clickable(ReactJsAppLocators.payment_tab)
        self._action.click(ReactJsAppLocators.payment_tab)
