from behave import *

from configuration import CONFIGURATION
from utils.enums.field_type import FieldType
from utils.mock_handler import MockUrl

use_step_matcher("re")


@step("User opens page with animated card")
def step_impl(context):
    animated_card_page = context.page_factory.get_page(page_name='animated_card')
    if 'safari' in context.browser:
        animated_card_page.open_page(MockUrl.WEBSERVICES_DOMAIN.value)
    animated_card_page.open_page(CONFIGURATION.URL.BASE_URL)
    context.executor.wait_for_javascript()


@when('User fills payment form with data: "(?P<card_number>.+)", "(?P<expiration_date>.+)" and "(?P<cvv>.+)"')
def step_impl(context, card_number, expiration_date, cvv):
    animated_card_page = context.page_factory.get_page(page_name='animated_card')
    animated_card_page.fill_payment_form_without_iframe(card_number, expiration_date, cvv)


@then("User will see card icon connected to card type (?P<card_type>.+)")
def step_impl(context, card_type):
    animated_card_page = context.page_factory.get_page(page_name='animated_card')
    animated_card_page.scroll_to_bottom()
    animated_card_page.validate_credit_card_icon(card_type, context.is_field_in_iframe)
    context.card_type = card_type


@step(
    'User will see the same provided data on animated credit card "(?P<formatted_card_number>.+)",'
    ' "(?P<expiration_date>.+)" and "(?P<cvv>.+)"')
def step_impl(context, formatted_card_number, expiration_date, cvv):
    animated_card_page = context.page_factory.get_page(page_name='animated_card')
    animated_card_page.validate_all_data_on_animated_card(formatted_card_number, expiration_date, cvv,
                                                          context.card_type, context.is_field_in_iframe)


@step('User will see that animated card is flipped, except for "AMEX"')
def step_impl(context):
    animated_card_page = context.page_factory.get_page(page_name='animated_card')
    animated_card_page.validate_if_animated_card_is_flipped(context.card_type, context.is_field_in_iframe)


@when('User fills payment form with data: "(?P<card_number>.+)", "(?P<expiration_date>.+)"')
def step_impl(context, card_number, expiration_date):
    animated_card_page = context.page_factory.get_page(page_name='animated_card')
    animated_card_page.fill_payment_form_without_iframe(card_number, expiration_date, None)


@step('User will see the same provided data on animated credit card "(?P<card_number>.+)", "(?P<expiration_date>.+)"')
def step_impl(context, card_number, expiration_date):
    animated_card_page = context.page_factory.get_page(page_name='animated_card')
    animated_card_page.validate_all_data_on_animated_card(card_number, expiration_date, None, "PIBA",
                                                          context.is_field_in_iframe)


@step("User changes the field focus")
def step_impl(context):
    animated_card_page = context.page_factory.get_page(page_name='animated_card')
    animated_card_page.change_field_focus()


@step('User will see that "(?P<field>.+)" no-iframe-field is highlighted')
def step_impl(context, field):
    animated_card_page = context.page_factory.get_page(page_name='animated_card')
    animated_card_page.validate_if_no_iframe_field_is_highlighted(FieldType[field].name)


@then('User will see "(?P<expected_message>.+)" message under no-iframe-field: "(?P<field>.+)"')
def step_impl(context, expected_message, field):
    animated_card_page = context.page_factory.get_page(page_name='animated_card')
    animated_card_page.validate_no_iframe_field_validation_message(FieldType[field].name, expected_message)


@then('User will see that labels displayed on animated card are translated into "(?P<language>.+)"')
def step_impl(context, language):
    animated_card_page = context.page_factory.get_page(page_name='animated_card')
    animated_card_page.scroll_to_bottom()
    animated_card_page.validate_animated_card_translation(language, context.is_field_in_iframe)


@then('User will see "(?P<field>.+)" field is disabled')
def step_impl(context, field):
    animated_card_page = context.page_factory.get_page(page_name='animated_card')
    animated_card_page.is_field_displayed(FieldType[field].name)
