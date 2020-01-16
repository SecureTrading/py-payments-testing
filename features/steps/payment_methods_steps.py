import time

from behave import *

from configuration import CONFIGURATION
from utils.enums.config import Config
from utils.enums.field_type import FieldType
from utils.enums.payment_type import PaymentType
from utils.enums.request_type import RequestType
from utils.enums.responses.acs_response import ACSresponse
from utils.enums.responses.apple_pay_response import ApplePayResponse
from utils.enums.responses.auth_response import AUTHresponse
from utils.enums.responses.invalid_field_response import InvalidFieldResponse
from utils.enums.responses.tdq_response import TDQresponse
from utils.enums.responses.visa_response import VisaResponse
from utils.mock_handler import stub_config, stub_st_request_type, MockUrl, stub_payment_status, \
    stub_st_request_type_server_error

use_step_matcher("re")


@given("JavaScript configuration is set for scenario based on scenario's @config tag")
def step_impl(context):
    scenario_tags_list = context.scenario.tags
    if 'config_submit_on_success_true' in scenario_tags_list:
        stub_config(Config.SUBMIT_ON_SUCCESS_TRUE.value)
    elif 'config_field_style' in scenario_tags_list:
        stub_config(Config.FIELD_STYLE.value)
    elif 'config_animated_card_true' in scenario_tags_list:
        stub_config(Config.ANIMATED_CARD.value)
    elif 'config_immediate_payment' in scenario_tags_list:
        stub_config(Config.IMMEDIATE_PAYMENT.value)
    elif 'config_update_jwt_true' in scenario_tags_list:
        stub_config(Config.UPDATE_JWT.value)
    elif 'config_skip_jsinit' in scenario_tags_list:
        stub_config(Config.SKIP_JSINIT.value)
    elif 'config_defer_init_and_start_on_load_true' in scenario_tags_list:
        stub_config(Config.DEFER_INIT_START_ON_LOAD.value)
    elif 'config_submit_cvv_only' in scenario_tags_list:
        stub_config(Config.SUBMIT_CVV_ONLY.value)
    else:
        stub_config(Config.BASE_CONFIG.value)


@step("User opens page with payment form")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.open_page(CONFIGURATION.URL.BASE_URL)


@when(
    'User fills payment form with credit card number "(?P<card_number>.+)", expiration date "(?P<exp_date>.+)" and cvv "(?P<cvv>.+)"')
def step_impl(context, card_number, exp_date, cvv):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.fill_payment_form(card_number, exp_date, cvv)


@step('THREEDQUERY mock response set to "(?P<tdq_response>.+)"')
def step_impl(context, tdq_response):
    stub_st_request_type(TDQresponse[tdq_response].value, RequestType.THREEDQUERY.name)


@step('ACS mock response set to "(?P<acs_response>.+)"')
def step_impl(context, acs_response):
    if acs_response == "OK":
        stub_payment_status(MockUrl.CC_MOCK_ACS_URI.value, ACSresponse[acs_response].value)
    elif acs_response == "NOACTION":
        stub_payment_status(MockUrl.CC_MOCK_ACS_URI.value, ACSresponse[acs_response].value)
        stub_st_request_type(AUTHresponse.OK.value, RequestType.AUTH.name)
    elif acs_response == "FAILURE":
        stub_payment_status(MockUrl.CC_MOCK_ACS_URI.value, ACSresponse[acs_response].value)
        stub_st_request_type(AUTHresponse.MERCHANT_DECLINE.value, RequestType.AUTH.name)
    elif acs_response == "ERROR":
        stub_payment_status(MockUrl.CC_MOCK_ACS_URI.value, ACSresponse[acs_response].value)


@step('User clicks Pay button - AUTH response set to "(?P<action_code>.+)"')
def step_impl(context, action_code):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    stub_st_request_type(AUTHresponse[action_code].value, RequestType.AUTH.name)
    payment_page.choose_payment_methods(PaymentType.CARDINAL_COMMERCE.name)


@then('User will see payment status information: "(?P<payment_status_message>.+)"')
def step_impl(context, payment_status_message):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_payment_status_message(payment_status_message)


@step('User will see that notification frame has "(?P<color>.+)" color')
def step_impl(context, color):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_notification_frame_color(color)


@step("User clicks Pay button")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.choose_payment_methods(PaymentType.CARDINAL_COMMERCE.name)


@then('User will see validation message "(?P<expected_message>.+)" under all fields')
def step_impl(context, expected_message):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_field_validation_message(FieldType.CARD_NUMBER.name, expected_message)
    payment_page.validate_field_validation_message(FieldType.EXPIRATION_DATE.name, expected_message)
    payment_page.validate_field_validation_message(FieldType.SECURITY_CODE.name, expected_message)


@step("User will see that all fields are highlighted")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_if_field_is_highlighted(FieldType.CARD_NUMBER.name)
    payment_page.validate_if_field_is_highlighted(FieldType.EXPIRATION_DATE.name)
    payment_page.validate_if_field_is_highlighted(FieldType.SECURITY_CODE.name)


@when(
    'User fills payment form with incorrect or missing data: card number "(?P<card_number>.+)",'
    ' expiration date "(?P<exp_date>.+)" and cvv "(?P<cvv>.+)"')
def step_impl(context, card_number, exp_date, cvv):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.fill_payment_form(card_number, exp_date, cvv)


@step('User will see "(?P<expected_message>.+)" message under field: "(?P<field>.+)"')
def step_impl(context, expected_message, field):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_field_validation_message(FieldType[field].name, expected_message)


@step('User will see that "(?P<field>.+)" field is highlighted')
def step_impl(context, field):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_if_field_is_highlighted(FieldType[field].name)


@step('InvalidField response set for "(?P<field>.+)"')
def step_impl(context, field):
    stub_st_request_type(InvalidFieldResponse[field].value, RequestType.THREEDQUERY.name)


@then('User will see notification frame with message: "(?P<expected_message>.+)"')
def step_impl(context, expected_message):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_payment_status_message(expected_message)


@when('User chooses Visa Checkout as payment method - response set to "(?P<action_code>.+)"')
def step_impl(context, action_code):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    stub_st_request_type(VisaResponse.VISA_AUTH_SUCCESS.value, RequestType.AUTH.name)
    stub_payment_status(MockUrl.VISA_MOCK_URI.value, VisaResponse[action_code].value)
    payment_page.choose_payment_methods(PaymentType.CARDINAL_COMMERCE.name)


@when('User chooses ApplePay as payment method - response set to "(?P<action_code>.+)"')
def step_impl(context, action_code):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    stub_st_request_type(ApplePayResponse.SUCCESS.value, RequestType.WALLETVERIFY.name)
    if action_code == "SUCCESS":
        stub_payment_status(MockUrl.APPLEPAY_MOCK_URI.value, ApplePayResponse[action_code].value)
        stub_st_request_type(ApplePayResponse.APPLE_AUTH_SUCCESS.value, RequestType.AUTH.name)
    elif action_code == "ERROR":
        stub_payment_status(MockUrl.APPLEPAY_MOCK_URI.value, ApplePayResponse.SUCCESS.value)
        stub_st_request_type_server_error(RequestType.AUTH.name)
    elif action_code == "DECLINE":
        stub_payment_status(MockUrl.APPLEPAY_MOCK_URI.value, ApplePayResponse.SUCCESS.value)
        stub_st_request_type(ApplePayResponse.ERROR.value, RequestType.AUTH.name)
    elif action_code == "CANCEL":
        stub_payment_status(MockUrl.APPLEPAY_MOCK_URI.value, ApplePayResponse[action_code].value)
    payment_page.choose_payment_methods(PaymentType.CARDINAL_COMMERCE.name)


@then("User will see that Submit button is enabled after payment")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    time.sleep(1)
    payment_page.validate_if_field_is_enabled(FieldType.SUBMIT_BUTTON.name)


@step("User will see that all input fields are enabled")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_if_field_is_enabled(FieldType.CARD_NUMBER.name)
    payment_page.validate_if_field_is_enabled(FieldType.EXPIRATION_DATE.name)
    payment_page.validate_if_field_is_enabled(FieldType.SECURITY_CODE.name)


@step('AUTH response set to "(?P<action_code>.+)"')
def step_impl(context, action_code):
    stub_st_request_type(AUTHresponse[action_code].value, RequestType.AUTH.name)


@when('User fills "(?P<field>.+)" field "(?P<value>.+)"')
def step_impl(context, field, value):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.fill_credit_card_field(FieldType[field].name, value)


@step("User will not see card number and expiration date fields")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_if_field_is_not_displayed(FieldType.CARD_NUMBER.name)
    payment_page.validate_if_field_is_not_displayed(FieldType.EXPIRATION_DATE.name)


@then('User will see that "(?P<field>.+)" field has correct style')
def step_impl(context, field):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    if field == FieldType.CARD_NUMBER.name:
        payment_page.validate_css_style(FieldType.CARD_NUMBER.name, "background-color", "rgba(240, 248, 255, 1)")
    elif field == FieldType.SECURITY_CODE.name:
        payment_page.validate_css_style(FieldType.SECURITY_CODE.name, "background-color", "rgba(255, 243, 51, 1)")


@when('User changes page language to "(?P<language>.+)"')
def step_impl(context, language):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    jwt = payment_page.get_translation_from_json(language, "jwt")
    payment_page.open_page(f"{CONFIGURATION.URL.BASE_URL}?jwt={jwt}")


@then('User will see all labels displayed on page translated into "(?P<language>.+)"')
def step_impl(context, language):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_labels_translation(language)


@step('User will see validation message "(?P<key>.+)" under all fields translated into "(?P<language>.+)"')
def step_impl(context, key, language):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_message_translation_under_field(FieldType.CARD_NUMBER.name, language, key)
    payment_page.validate_message_translation_under_field(FieldType.EXPIRATION_DATE.name, language, key)
    payment_page.validate_message_translation_under_field(FieldType.SECURITY_CODE.name, language, key)


@then(
    'User will see validation message "(?P<key>.+)" under "(?P<field>.+)" field translated into (?P<language>.+)')
def step_impl(context, key, field, language):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_message_translation_under_field(FieldType[field].name, language, key)


@then('User will see "(?P<key>.+)" payment status translated into "(?P<language>.+)"')
def step_impl(context, key, language):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_payment_status_translation(language, key)


@step("User opens payment page")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.open_page(CONFIGURATION.URL.BASE_URL)


@then("User will see payment status information included in url")
def step_impl(context):
    scenario_name = context.scenario.name
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    if scenario_name[0:4] in "Visa":
        payment_page.validate_if_url_contains_info_about_payment(context.test_data.step_payment_visa_url)
    elif scenario_name[0:4] in "Card":
        payment_page.validate_if_url_contains_info_about_payment(context.test_data.step_payment_cardinal_url)
