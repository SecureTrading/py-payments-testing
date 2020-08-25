from behave import use_step_matcher, given, step, when, then

from configuration import CONFIGURATION
from utils.enums.config import config
from utils.enums.payment_type import PaymentType
from utils.enums.request_type import RequestType, request_type_response, request_type_applepay, request_type_visa, \
    request_type_tokenisation_response
from utils.enums.responses.acs_response import ACSresponse
from utils.enums.responses.apple_pay_response import ApplePayResponse
from utils.enums.responses.auth_response import AUTHresponse
from utils.enums.responses.tdq_response import TDQresponse
from utils.enums.responses.visa_response import VisaResponse
from utils.helpers.request_executor import remove_item_from_request_journal
from utils.mock_handler import stub_config, stub_st_request_type, MockUrl, stub_payment_status, \
    stub_st_request_type_server_error, stub_st_request_type_acheck_tdq

use_step_matcher("re")


@given("JavaScript configuration is set for scenario based on scenario's @config tag")
def step_impl(context):
    remove_item_from_request_journal()
    if 'config_skip_jsinit' not in context.scenario.tags:
        if 'config_tokenisation_visa' in context.scenario.tags[0] or 'config_tokenisation_bypass_cards_visa' in \
                context.scenario.tags[0] or 'config_tokenisation_visa_request_types' in context.scenario.tags[0]:
            stub_st_request_type("jsinitTokenisationVisa.json", RequestType.JSINIT.name)
        elif 'config_tokenisation_amex' in context.scenario.tags[0]:
            stub_st_request_type("jsinitTokenisationAmex.json", RequestType.JSINIT.name)
        elif 'subscription' in context.scenario.tags[0]:
            stub_st_request_type("jsinitSubscription.json", RequestType.JSINIT.name)
        elif 'start_on_load_sub' in context.scenario.tags[0]:
            stub_st_request_type("jsinitStartOnLoadSubscription.json", RequestType.JSINIT.name)
        elif 'start_on_load' in context.scenario.tags[0]:
            stub_st_request_type("jsinitStartOnLoad.json", RequestType.JSINIT.name)
        else:
            stub_st_request_type("jsinit.json", RequestType.JSINIT.name)
    config_tag = context.scenario.tags[0]
    stub_config(config[config_tag])


@when("User sets incorrect request type in config file")
def step_impl(context):
    # Placeholder for step definition - step is implemented in
    # @given("JavaScript configuration is set for scenario based on scenario's @config tag")
    pass


@step('THREEDQUERY mock response is set to "(?P<tdq_response>.+)"')
def step_impl(context, tdq_response):
    stub_st_request_type(TDQresponse[tdq_response].value, RequestType.THREEDQUERY.name)
    if 'ie' in context.browser and 'config_submit_cvv_only' in context.scenario.tags:
        context.executor.wait_for_javascript()


@step("(?P<request_type>.+) mock response is set to OK")
def step_impl(context, request_type):
    if "ACCOUNTCHECK, THREEDQUERY" in request_type and 'config_immediate_payment_acheck_tdq_auth_riskdec' in \
            context.scenario.tags[0]:
        stub_st_request_type_acheck_tdq(request_type_response[request_type], request_type)
    else:
        stub_st_request_type(request_type_response[request_type], request_type)
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


@step('(?P<request_type>.+) response is set to "(?P<action_code>.+)"')
def step_impl(context, request_type, action_code):
    if request_type == "AUTH":
        stub_st_request_type(AUTHresponse[action_code].value, RequestType.AUTH.name)


@step("(?P<request_type>.+) mock response for tokenisation is set to OK")
def step_impl(context, request_type):
    stub_st_request_type(request_type_tokenisation_response[request_type], request_type)


@step("AUTH and THREEDQUERY requests were sent only once with correct data")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_number_of_requests_with_data(RequestType.THREEDQUERY.name, context.pan, context.exp_date,
                                                       context.cvv, 1)
    payment_page.validate_number_of_requests_with_data(RequestType.AUTH.name, context.pan, context.exp_date,
                                                       context.cvv, 1)


@step("AUTH and THREEDQUERY requests were sent only once")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    if 'config_immediate_payment' in context.scenario.tags[0] or (
            'config_defer_init_and_start_on_load_true' in context.scenario.tags):
        payment_page.validate_number_of_requests_without_data(RequestType.THREEDQUERY.name, 1)
        payment_page.validate_number_of_requests_without_data(RequestType.AUTH.name, 1)
    else:
        # ToDo
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
        payment_page.validate_number_of_requests_with_data(RequestType.THREEDQUERY.name, context.pan, context.exp_date,
                                                           context.cvv, 1)
        payment_page.validate_number_of_requests_with_data(RequestType.AUTH.name, context.pan, context.exp_date,
                                                           context.cvv, 0)


@step("AUTH request was sent only once with correct data")
def step_impl(context):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    if 'config_immediate_payment' in context.scenario.tags[0] or 'config_start_on_load' in context.scenario.tags[0]:
        payment_page.validate_number_of_requests_without_data(RequestType.AUTH.name, 1)
    else:
        payment_page.validate_number_of_requests_with_data(RequestType.THREEDQUERY.name, context.pan, context.exp_date,
                                                           context.cvv, 0)
        payment_page.validate_number_of_requests_with_data(RequestType.AUTH.name, context.pan, context.exp_date,
                                                           context.cvv, 1)


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
    if 'config_immediate_payment' in context.scenario.tags[0] or 'config_start_on_load' in context.scenario.tags[0]:
        payment_page.validate_number_of_requests(request_type, "", "", "", 1)
    elif 'config_tokenisation' in context.scenario.tags[0]:
        payment_page.validate_number_of_tokenisation_requests(request_type, context.cvv, 1)
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
        if 'config_cybertonica_immediate_payment' in context.scenario.tags or "Visa Checkout - Cybertonica" in context.scenario.name \
                or "ApplePay - Cybertonica" in context.scenario.name:
            payment_page.validate_number_of_requests_with_fraudcontroltransactionid_flag(request_type, 1)
        else:
            payment_page.validate_number_of_requests_with_data_and_fraudcontroltransactionid_flag(request_type,
                                                                                                  context.pan,
                                                                                                  context.exp_date,
                                                                                                  context.cvv, 1)
    else:
        if "Visa Checkout - Cybertonica" in context.scenario.name or "ApplePay - Cybertonica" in context.scenario.name:
            payment_page.validate_number_of_requests_with_fraudcontroltransactionid_flag(request_type, 0)
        else:
            payment_page.validate_number_of_requests_with_data_and_fraudcontroltransactionid_flag(request_type,
                                                                                                  context.pan,
                                                                                                  context.exp_date,
                                                                                                  context.cvv, 0)


@step("(?P<request_type>.+) request was not sent")
def step_impl(context, request_type):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_number_of_requests_without_data(request_type, 0)


@step("(?P<request_type>.+) requests contains updated jwt")
def step_impl(context, request_type):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    if "WALLETVERIFY" in request_type and "APPLE_PAY" in context.thirdparty:
        payment_page.validate_updated_jwt_in_request(request_type, MockUrl.APPLEPAY_MOCK_URI.value,
                                                     context.test_data.update_jwt, 1)
    elif "VISA_CHECKOUT" in request_type:
        payment_page.validate_updated_jwt_in_request_for_visa(PaymentType.VISA_CHECKOUT.value,
                                                              context.test_data.update_jwt, 1)
    else:
        payment_page.validate_updated_jwt_in_request(request_type, MockUrl.GATEWAY_MOCK_URI.value,
                                                     context.test_data.update_jwt, 1)


@step("(?P<request_type>.+) request for (?P<thirdparty>.+) is sent only once with correct data")
def step_impl(context, request_type, thirdparty):
    payment_page = context.page_factory.get_page(page_name='payment_methods')
    payment_page.validate_number_of_thirdparty_requests(request_type, PaymentType[thirdparty].value, 1)
