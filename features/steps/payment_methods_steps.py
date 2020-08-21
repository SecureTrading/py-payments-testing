import time

from assertpy import soft_assertions
from behave import *

from configuration import CONFIGURATION
from utils.configurations.inline_config_generator import create_inline_config
from utils.configurations.jwt_generator import encode_jwt_for_json
from utils.dict.url_after_redirection import url_after_redirection
from utils.enums.config import config
from utils.enums.e2e_config import e2eConfig
from utils.enums.example_page import ExamplePage

from utils.enums.field_type import FieldType
from utils.enums.jwt_config import JwtConfig
from utils.enums.payment_type import PaymentType
from utils.enums.request_type import RequestType, request_type_response, request_type_applepay, request_type_visa
from utils.enums.responses.acs_response import ACSresponse
from utils.enums.responses.apple_pay_response import ApplePayResponse
from utils.enums.responses.auth_response import AUTHresponse
from utils.enums.responses.invalid_field_response import InvalidFieldResponse
from utils.enums.responses.tdq_response import TDQresponse
from utils.enums.responses.visa_response import VisaResponse
from utils.helpers.request_executor import remove_item_from_request_journal
from utils.mock_handler import stub_config, stub_st_request_type, MockUrl, stub_payment_status, \
    stub_st_request_type_server_error

use_step_matcher("re")


@given("JavaScript configuration is set for scenario based on scenario's @config tag")
def step_impl(context):
    remove_item_from_request_journal()
    if 'config_skip_jsinit' not in context.scenario.tags:
        if 'config_tokenization_visa' in context.scenario.tags[0] or 'config_tokenization_bypass_cards_visa' in context.scenario.tags[0]:
            stub_st_request_type("jsinitTokenizationVisa.json", RequestType.JSINIT.name)
        elif 'config_tokenization_amex' in context.scenario.tags[0]:
            stub_st_request_type("jsinitTokenizationAmex.json", RequestType.JSINIT.name)
        elif 'subscription' in context.scenario.tags[0]:
            stub_st_request_type("jsinitSubscription.json", RequestType.JSINIT.name)
        else:
            stub_st_request_type("jsinit.json", RequestType.JSINIT.name)
    config_tag = context.scenario.tags[0]
    stub_config(config[config_tag])


@step("User opens page with payment form")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    if 'config_immediate_payment' not in context.scenario.tags[0] and 'parent_iframe' not in context.scenario.tags and \
        'config_cybertonica_immediate_payment' not in context.scenario.tags:
        if ('safari' in context.browser) or ('iP' in CONFIGURATION.REMOTE_DEVICE):
            payment_page.open_page(MockUrl.WEBSERVICES_DOMAIN.value)
            if 'safari' in context.browser or 'visa_test' in context.scenario.tags or 'apple_test' in context.scenario.tags:
                payment_page.open_page(MockUrl.THIRDPARTY_URL.value)
        payment_page.open_page(CONFIGURATION.URL.BASE_URL)
        payment_page.is_connection_not_private_dispayed(CONFIGURATION.URL.BASE_URL)
        payment_page.wait_for_iframe()


@when(
    'User fills payment form with credit card number "(?P<card_number>.+)", expiration date "(?P<exp_date>.+)" and cvv "(?P<cvv>.+)"')
def step_impl(context, card_number, exp_date, cvv):
    context.pan = card_number
    context.exp_date = exp_date
    context.cvv = cvv
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.fill_payment_form(card_number, exp_date, cvv)


@step('THREEDQUERY mock response is set to "(?P<tdq_response>.+)"')
def step_impl(context, tdq_response):
    stub_st_request_type(TDQresponse[tdq_response].value, RequestType.THREEDQUERY.name)
    if 'ie' in context.browser and 'config_submit_cvv_only' in context.scenario.tags:
        context.executor.wait_for_javascript()


@step("(?P<request_type>.+) mock response is set to OK")
def step_impl(context, request_type):
    stub_st_request_type(request_type_response[request_type], request_type)


@step("(?P<request_type>.+) ApplePay mock response is set to SUCCESS")
def step_impl(context, request_type):
    stub_st_request_type(ApplePayResponse.SUCCESS.value, RequestType.WALLETVERIFY.name)
    stub_payment_status(MockUrl.APPLEPAY_MOCK_URI.value, ApplePayResponse.SUCCESS.value)
    stub_st_request_type(request_type_applepay[request_type], request_type)

@step("(?P<request_type>.+) Visa Checkout mock response is set to SUCCESS")
def step_impl(context, request_type):
    stub_payment_status(MockUrl.VISA_MOCK_URI.value, VisaResponse.SUCCESS.value)
    stub_st_request_type(request_type_visa[request_type], request_type)



@step('ACS mock response is set to "(?P<acs_response>.+)"')
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


@step('User clicks Pay button - (?P<request_type>.+) response is set to "(?P<action_code>.+)"')
def step_impl(context, request_type, action_code):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    if request_type == "AUTH":
        stub_st_request_type(AUTHresponse[action_code].value, RequestType.AUTH.name)
    else:
        stub_st_request_type(request_type_response[request_type], request_type)

    if 'ie' in context.browser and 'config_submit_cvv_only' in context.scenario.tags:
        context.executor.wait_for_javascript()
    payment_page.choose_payment_methods(PaymentType.CARDINAL_COMMERCE.name)
    if 'config_submit_on_success_and_error_true' not in context.scenario.tags:
        payment_page.scroll_to_top()


@then('User will see payment status information: "(?P<payment_status_message>.+)"')
def step_impl(context, payment_status_message):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.switch_to_parent_iframe()
    payment_page.validate_payment_status_message(payment_status_message)


@step('User will see that notification frame has "(?P<color>.+)" color')
def step_impl(context, color):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_notification_frame_color(color)


@step("User clicks Pay button")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.choose_payment_methods(PaymentType.CARDINAL_COMMERCE.name)


@step("User clicks Additional button")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.click_additional_btn()


@step("User accept success alert")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.accept_alert()


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
    context.pan = card_number
    context.exp_date = exp_date
    context.cvv = cvv
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


@when('User chooses Visa Checkout as payment method - response is set to "(?P<action_code>.+)"')
def step_impl(context, action_code):
    context.action_code = action_code
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    if action_code == "ERROR":
        stub_payment_status(MockUrl.VISA_MOCK_URI.value, VisaResponse.SUCCESS.value)
        stub_st_request_type(VisaResponse.ERROR.value, RequestType.AUTH.name)
    else:
        stub_st_request_type(VisaResponse.VISA_AUTH_SUCCESS.value, RequestType.AUTH.name)
        stub_payment_status(MockUrl.VISA_MOCK_URI.value, VisaResponse[action_code].value)
    payment_page.choose_payment_methods(PaymentType.VISA_CHECKOUT.name)


@when('User chooses ApplePay as payment method - response is set to "(?P<action_code>.+)"')
def step_impl(context, action_code):
    context.action_code = action_code
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
    payment_page.choose_payment_methods(PaymentType.APPLE_PAY.name)


@when('User chooses (?P<payment_method>.+) as payment method')
def step_impl(context, payment_method):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.choose_payment_methods(PaymentType[payment_method].name)


@then('User will see that Submit button is "(?P<form_status>.+)" after payment')
def step_impl(context, form_status):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    time.sleep(1)
    payment_page.validate_form_status(FieldType.SUBMIT_BUTTON.name, form_status)


@step('User will see that (?P<field>.+) input fields are "(?P<form_status>.+)"')
def step_impl(context, field: FieldType, form_status):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    field = FieldType.__members__[field]
    if field.name == "ALL":
        payment_page.validate_form_status(FieldType.SECURITY_CODE.name, form_status)
        payment_page.validate_form_status(FieldType.CARD_NUMBER.name, form_status)
        payment_page.validate_form_status(FieldType.EXPIRATION_DATE.name, form_status)
    else:
        payment_page.validate_form_status(field.name, form_status)


@step('(?P<request_type>.+) response is set to "(?P<action_code>.+)"')
def step_impl(context, request_type, action_code):
    if request_type == "AUTH":
        stub_st_request_type(AUTHresponse[action_code].value, RequestType.AUTH.name)


@when('User fills "(?P<field>.+)" field "(?P<value>.+)"')
def step_impl(context, field, value):
    context.cvv = value
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.fill_credit_card_field(FieldType[field].name, value)


@then('User will see that "(?P<field>.+)" field has correct style')
def step_impl(context, field):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    if field == FieldType.CARD_NUMBER.name:
        payment_page.validate_css_style(FieldType.CARD_NUMBER.name, "background-color", '100, 149, 237')
    elif field == FieldType.EXPIRATION_DATE.name:
        payment_page.validate_css_style(FieldType.EXPIRATION_DATE.name, "background-color", '143, 188, 143')
    elif field == FieldType.SECURITY_CODE.name:
        payment_page.validate_css_style(FieldType.SECURITY_CODE.name, "background-color", '255, 243, 51')
    if field == FieldType.NOTIFICATION_FRAME.name:
        payment_page.validate_css_style(FieldType.NOTIFICATION_FRAME.name, "background-color", '100, 149, 237')


@when('User changes page language to "(?P<language>.+)"')
def step_impl(context, language):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    jwt = payment_page.get_translation_from_json(language, "jwt")
    payment_page.open_page(f"{CONFIGURATION.URL.BASE_URL}?jwt={jwt}")
    context.executor.wait_for_javascript()


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
    if 'safari' in context.browser or ('iP' in CONFIGURATION.REMOTE_DEVICE):
        payment_page.open_page(MockUrl.WEBSERVICES_DOMAIN.value)
        payment_page.open_page(MockUrl.THIRDPARTY_URL.value)
        context.executor.wait_for_javascript()
        payment_page.wait_for_iframe()
    if 'parent_iframe' in context.scenario.tags:
        payment_page.open_page(CONFIGURATION.URL.BASE_URL+'/iframe.html')
        payment_page.switch_to_parent_iframe()
        payment_page.wait_for_iframe()
    else:
        payment_page.open_page(CONFIGURATION.URL.BASE_URL)

@then("User is redirected to action page")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    time.sleep(1)
    for key, value in url_after_redirection.items():
        if key in context.scenario.name:
            if "Cardinal Commerce - successful" in key and 'IE' in CONFIGURATION.REMOTE_BROWSER:
                payment_page.validate_if_url_contains_info_about_payment(url_after_redirection['IE - success'])
            elif "Cardinal Commerce - error" in key and 'IE' in CONFIGURATION.REMOTE_BROWSER:
                payment_page.validate_if_url_contains_info_about_payment(url_after_redirection['IE - error'])
            else:
                payment_page.validate_if_url_contains_info_about_payment(value)
                break

@step('User will be sent to page with url "(?P<url>.+)" having params')
def step_impl(context, url: str):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    with soft_assertions():
        payment_page.validate_base_url(url)
        for param in context.table:
            payment_page.validate_if_url_contains_param(param['key'], param['value'])


@when('User fills payment form with credit card number "(?P<card_number>.+)", expiration date "(?P<exp_date>.+)"')
def step_impl(context, card_number, exp_date):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.fill_payment_form_without_cvv(card_number, exp_date)


@step("User calls updateJWT function by filling amount field")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.fill_amount_field('1')


@then('User will see that "(?P<field_type>.+)" field is disabled')
def step_impl(context, field_type):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_if_field_is_disabled(field_type)


@step('User will see "(?P<callback_popup>.+)" popup')
def step_impl(context, callback_popup):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_if_callback_popup_is_displayed(callback_popup)


@when("User sets incorrect request type in config file")
def step_impl(context):
    # Placeholder for step definition - step is implemented in
    # @given("JavaScript configuration is set for scenario based on scenario's @config tag")
    pass


@then("User will see that application is not fully loaded")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_if_field_is_not_displayed(FieldType.CARD_NUMBER.name)
    payment_page.validate_if_field_is_not_displayed(FieldType.EXPIRATION_DATE.name)


@then("User will see (?P<placeholders>.+) placeholders in input fields: (?P<card>.+), (?P<date>.+), (?P<cvv>.+)")
def step_impl(context, placeholders, card, date, cvv):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    if placeholders == "specific":
        payment_page.validate_placeholders(card, date, cvv)
    if placeholders == "default":
        payment_page.validate_placeholders(card, date, cvv)

@then("User will see '\*\*\*\*' placeholder in security code field")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_placeholder(FieldType.SECURITY_CODE.name, "****")


@then('User will see "(?P<card_type>.+)" icon in card number input field')
def step_impl(context, card_type):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_credit_card_icon_in_input_field(card_type)


@then("User will not see notification frame")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_if_field_is_not_displayed(FieldType.NOTIFICATION_FRAME.name)

    
@step("AUTH and THREEDQUERY requests were sent only once with correct data")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_number_of_requests_with_data(RequestType.THREEDQUERY.name, context.pan, context.exp_date, context.cvv, 1)
    payment_page.validate_number_of_requests_with_data(RequestType.AUTH.name, context.pan, context.exp_date, context.cvv, 1)


@step("AUTH and THREEDQUERY requests were sent only once")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    if 'config_immediate_payment' in context.scenario.tags[0] or ('config_defer_init_and_start_on_load_true' in context.scenario.tags):
        payment_page.validate_number_of_requests_without_data(RequestType.THREEDQUERY.name, 1)
        payment_page.validate_number_of_requests_without_data(RequestType.AUTH.name, 1)
    else:
        #ToDo
        if 'config_submit_cvv_only' in context.scenario.tags and ('IE' in CONFIGURATION.REMOTE_BROWSER):
            pass
        else:
            payment_page.validate_number_of_requests_with_data(RequestType.THREEDQUERY.name, '', '', context.cvv, 1)
            payment_page.validate_number_of_requests_with_data(RequestType.AUTH.name, '', '', context.cvv, 1)


@step("THREEDQUERY request was sent only once with correct data")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    if 'config_immediate_payment' in context.scenario.tags[0]:
        payment_page.validate_number_of_requests_without_data(RequestType.THREEDQUERY.name, 1)
        payment_page.validate_number_of_requests_without_data(RequestType.AUTH.name, 0)
    else:
        payment_page.validate_number_of_requests_with_data(RequestType.THREEDQUERY.name, context.pan, context.exp_date, context.cvv, 1)
        payment_page.validate_number_of_requests_with_data(RequestType.AUTH.name, context.pan, context.exp_date, context.cvv, 0)


@step("AUTH request was sent only once with correct data")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    if 'config_immediate_payment' in context.scenario.tags[0]:
        payment_page.validate_number_of_requests_without_data(RequestType.AUTH.name, 1)
    else:
        payment_page.validate_number_of_requests_with_data(RequestType.THREEDQUERY.name, context.pan, context.exp_date, context.cvv, 0)
        payment_page.validate_number_of_requests_with_data(RequestType.AUTH.name, context.pan, context.exp_date, context.cvv, 1)


@step("AUTH request was sent only once")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_number_of_requests_without_data(RequestType.AUTH.name, 1)


@step("AUTH and THREEDQUERY requests were not sent")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_number_of_requests_without_data(RequestType.THREEDQUERY.name, 0)
    payment_page.validate_number_of_requests_without_data(RequestType.AUTH.name, 0)


@step("(?P<thirdparty>.+) or AUTH requests were sent only once with correct data")
def step_impl(context, thirdparty):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    context.thirdparty = thirdparty
    if "VISA_CHECKOUT" in thirdparty:
        payment_page.validate_number_of_wallet_verify_requests(MockUrl.VISA_MOCK_URI.value, 1)
    elif "APPLE_PAY" in thirdparty:
        payment_page.validate_number_of_wallet_verify_requests(MockUrl.APPLEPAY_MOCK_URI.value, 1)

    if 'SUCCESS' in context.action_code or 'DECLINE' in context.action_code or 'ERROR' in context.action_code:
        payment_page.validate_number_of_thirdparty_requests(RequestType.AUTH.name, PaymentType[thirdparty].value, 1)
    else:
        payment_page.validate_number_of_thirdparty_requests(RequestType.AUTH.name, PaymentType[thirdparty].value, 0)


@step("(?P<request_type>.+) ware sent only once in one request")
def step_impl(context, request_type):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    if 'config_immediate_payment' in context.scenario.tags[0]:
        payment_page.validate_number_of_requests(request_type, "", "", "", 1)
    else:
        payment_page.validate_number_of_requests(request_type, context.pan, context.exp_date, context.cvv, 1)


@then("JSINIT request was sent only (?P<number>.+)")
def step_impl(context, number):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_number_of_requests_without_data(RequestType.JSINIT.name, int(number))


@step("(?P<request_type>.+) request was sent only once (?P<scenario>.+) 'fraudcontroltransactionid' flag")
def step_impl(context, request_type, scenario):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    if 'with' == scenario:
        if 'config_cybertonica_immediate_payment' in context.scenario.tags or "Visa Checkout - Cybertonica" in context.scenario.name\
            or "ApplePay - Cybertonica" in context.scenario.name:
            payment_page.validate_number_of_requests_with_fraudcontroltransactionid_flag(request_type, 1)
        else:
            payment_page.validate_number_of_requests_with_data_and_fraudcontroltransactionid_flag(request_type, context.pan,
                                                                                 context.exp_date, context.cvv, 1)
    else:
        if "Visa Checkout - Cybertonica" in context.scenario.name or "ApplePay - Cybertonica" in context.scenario.name:
            payment_page.validate_number_of_requests_with_fraudcontroltransactionid_flag(request_type, 0)
        else:
            payment_page.validate_number_of_requests_with_data_and_fraudcontroltransactionid_flag(request_type, context.pan,
                                                                                     context.exp_date, context.cvv, 0)


@step("(?P<request_type>.+) request was not sent")
def step_impl(context, request_type):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_number_of_requests_without_data(request_type, 0)


@when('User fills merchant data with name "(?P<name>.+)", email "(?P<email>.+)", phone "(?P<phone>.+)"')
def step_impl(context, name, email, phone):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.fill_merchant_form(name, email, phone)


@step("(?P<request_type>.+) requests contains updated jwt")
def step_impl(context, request_type):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    if "WALLETVERIFY" in request_type and "APPLE_PAY" in context.thirdparty:
        payment_page.validate_updated_jwt_in_request(request_type, MockUrl.APPLEPAY_MOCK_URI.value, context.test_data.update_jwt, 1)
    elif "VISA_CHECKOUT" in request_type:
        payment_page.validate_updated_jwt_in_request_for_visa(PaymentType.VISA_CHECKOUT.value, context.test_data.update_jwt, 1)
    else:
        payment_page.validate_updated_jwt_in_request(request_type, MockUrl.GATEWAY_MOCK_URI.value, context.test_data.update_jwt, 1)


@then("User will not see (?P<field_type>.+)")
def step_impl(context, field_type):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_if_field_is_not_displayed(FieldType[field_type].name)


@step("(?P<request_type>.+) request for (?P<thirdparty>.+) is sent only once with correct data")
def step_impl(context, request_type, thirdparty):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_number_of_thirdparty_requests(request_type, PaymentType[thirdparty].value, 1)


@step("User press enter button")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.press_enter_button_on_security_code_field()


@step("User fills (?P<auth_type>.+) authentication modal")
def step_impl(context, auth_type):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.fill_cardinal_authentication_code(auth_type)
    if 'parent_iframe' in context.scenario.tags:
        payment_page.switch_to_parent_iframe()


@step("User will see the same provided data in inputs fields")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_value_of_input_field(FieldType.CARD_NUMBER.name, "5200 0000 0000 1005")
    payment_page.validate_value_of_input_field(FieldType.EXPIRATION_DATE.name, context.exp_date)
    payment_page.validate_value_of_input_field(FieldType.SECURITY_CODE.name, context.cvv)


@step("User will see correct error code displayed in popup")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_callback_with_data_type("Error code: OK")


@then("User remains on checkout page")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_base_url(CONFIGURATION.URL.BASE_URL[8:])


@given('JS library is configured with (?P<e2e_config>.+) and (?P<jwt_config>.+)')
def step_impl(context, e2e_config : e2eConfig, jwt_config : JwtConfig):
    jwt = encode_jwt_for_json(JwtConfig[jwt_config])
    context.inline_config = create_inline_config(e2eConfig[e2e_config], jwt)


@step("User opens prepared payment form page (?P<example_page>.+)")
def step_impl(context, example_page : ExamplePage):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.open_page(f"{CONFIGURATION.URL.BASE_URL}/?{ExamplePage[example_page].value}")
    payment_page.wait_for_iframe()


@step("User opens (?:example page|example page (?P<example_page>.+))")
def step_impl(context, example_page: ExamplePage):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    # setting url specific params accordingly to example page
    if example_page is None:
        url = f"{CONFIGURATION.URL.BASE_URL}/?{context.inline_config}"
    elif "IN_IFRAME" in example_page:
        url = f"{CONFIGURATION.URL.BASE_URL}/{ExamplePage[example_page].value}{context.inline_config}"
    elif "WITH_UPDATE_JWT" in example_page:
        jwt = ''
        for row in context.table:
            jwt = str(encode_jwt_for_json(JwtConfig[f"{row['jwtName']}"]), "utf-8")
        url = f"{CONFIGURATION.URL.BASE_URL}/?{ExamplePage[example_page].value % jwt}{context.inline_config}"
    else:
        url = f"{CONFIGURATION.URL.BASE_URL}/?{ExamplePage[example_page].value}&{context.inline_config}"
    url = url.replace("??", "?").replace("&&", "&")  # just making sure some elements are not duplicated

    payment_page.open_page(url)

    if example_page is not None and "IN_IFRAME" in example_page:
        payment_page.switch_to_parent_iframe()
    payment_page.wait_for_iframe()

    
@then('User will see that (?P<element>.+) is translated into "(?P<expected_value>.+)"')
def step_impl(context, element, expected_value):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    if element in "Pay button":
        payment_page.validate_element_specific_translation(FieldType.SUBMIT_BUTTON.name, expected_value)
    else:
        payment_page.validate_element_specific_translation(FieldType.CARD_NUMBER.name, expected_value)
        payment_page.validate_element_specific_translation(FieldType.EXPIRATION_DATE.name, expected_value)


@step('"(?P<callback_popup>.+)" callback is called only once')
def step_impl(context, callback_popup):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_number_in_callback_counter_popup(callback_popup)


@step("JSINIT response is set")
def step_impl(context):
    stub_st_request_type("jsinit.json", RequestType.JSINIT.name)


@then('User will see that (?P<field_type>.+) field has (?P<rgb_color>.+) color')
def step_impl(context, field_type, rgb_color):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_css_style(FieldType[field_type].name, "background-color", rgb_color)