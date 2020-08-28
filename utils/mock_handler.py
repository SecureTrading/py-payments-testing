import json

from wiremock.constants import Config
from wiremock.resources.mappings import Mapping, MappingRequest, HttpMethods, MappingResponse
from wiremock.resources.mappings.resource import Mappings
from wiremock.server import WireMockServer
from enum import Enum


class MockUrl(Enum):
    BASE_URI = "https://merchant.example.com:8443"
    WEBSERVICES_DOMAIN = "https://webservices.securetrading.net:8443"
    THIRDPARTY_URL = "https://thirdparty.example.com:8443"
    VISA_MOCK_URI = "/visaPaymentStatus"
    CC_MOCK_ACS_URI = "/cardinalAuthenticateCard"
    APPLEPAY_MOCK_URI = "/applePaymentStatus"
    GATEWAY_MOCK_URI = "/jwt/"
    CONFIG_MOCK_URI = "/config.json"
    PORT = 8443


def get_mock_response_from_json(mock):
    with open(f'wiremock/__files/{mock}', 'r') as f:
        mock_json = json.load(f)
    return mock_json


class MockServer():
    wiremock_server = WireMockServer()

    @classmethod
    def start_mock_server(cls):
        cls.wiremock_server.port = MockUrl.PORT.value
        cls.wiremock_server.start()
        configure_for_local_host()

    @classmethod
    def stop_mock_server(cls):
        cls.wiremock_server.stop()


def configure_for_local_host():
    Config.base_url = f'{MockUrl.WEBSERVICES_DOMAIN.value}/__admin'
    Config.requests_verify = False

def configure_for_thirdparty_host():
    Config.base_url = f'{MockUrl.THIRDPARTY_URL.value}/__admin'
    Config.requests_verify = False


def stub_config(config_json):
    mapping = Mapping(
        priority=100,
        request=MappingRequest(
            method=HttpMethods.GET,
            url=MockUrl.CONFIG_MOCK_URI.value
        ),
        response=MappingResponse(
            status=200,
            headers={'Access-Control-Allow-Headers': 'Content-Type',
                     'Access-Control-Allow-Methods': "GET, POST"},
            json_body=get_mock_response_from_json(config_json)
        ),
        persistent=False)
    Mappings.create_mapping(mapping)


def stub_st_request_type(mock_json, request_type):
    stub_url_options_for_cors(MockUrl.GATEWAY_MOCK_URI.value)
    configure_for_local_host()
    mapping = Mapping(
        priority=100,
        request=MappingRequest(
            method=HttpMethods.POST,
            url=MockUrl.GATEWAY_MOCK_URI.value,
            body_patterns=[{"matchesJsonPath": "$.request[:1][?(@.requesttypedescriptions==["+request_type+"])]"}]
        ),
        response=MappingResponse(
            status=200,
            headers={'Access-Control-Allow-Headers': 'Content-Type',
                     'Access-Control-Allow-Methods': "GET, POST"},
            json_body=get_mock_response_from_json(mock_json)
        ),
        persistent=False)
    Mappings.create_mapping(mapping)


def stub_st_request_type_acheck_tdq(mock_json, request_type):
    stub_url_options_for_cors(MockUrl.GATEWAY_MOCK_URI.value)
    configure_for_local_host()
    mapping = Mapping(
        priority=100,
        request=MappingRequest(
            method=HttpMethods.POST,
            url=MockUrl.GATEWAY_MOCK_URI.value
        ),
        response=MappingResponse(
            status=200,
            headers={'Access-Control-Allow-Headers': 'Content-Type',
                     'Access-Control-Allow-Methods': "GET, POST"},
            json_body=get_mock_response_from_json(mock_json)
        ),
        persistent=False)
    Mappings.create_mapping(mapping)


def stub_st_request_type_server_error(mock_json, request_type):
    stub_url_options_for_cors(MockUrl.GATEWAY_MOCK_URI.value)
    configure_for_local_host()
    mapping = Mapping(
        priority=100,
        request=MappingRequest(
            method=HttpMethods.POST,
            url=MockUrl.GATEWAY_MOCK_URI.value,
            body_patterns = [{"contains": request_type}]
    ),
        response=MappingResponse(
            status=500,
            headers={'Access-Control-Allow-Headers': 'Content-Type',
                     'Access-Control-Allow-Methods': "GET, POST"},
            json_body=get_mock_response_from_json(mock_json)
        ),
        persistent=False)
    Mappings.create_mapping(mapping)


def stub_payment_status(mock_url, mock_json):
    configure_for_thirdparty_host()
    mapping = Mapping(
        priority=100,
        request=MappingRequest(
            method=HttpMethods.GET,
            url=mock_url
        ),
        response=MappingResponse(
            status=200,
            headers={'Access-Control-Allow-Headers': 'Content-Type',
                     'Access-Control-Allow-Methods': "GET, POST"},
            json_body=get_mock_response_from_json(mock_json)
        ),
        persistent=False)
    Mappings.create_mapping(mapping)


def stub_url_options_for_cors(mock_url):
    mapping = Mapping(
        priority=100,
        request=MappingRequest(
            method=HttpMethods.OPTIONS,
            url=mock_url
        ),
        response=MappingResponse(
            status=200,
            headers={'Access-Control-Allow-Headers': 'Content-Type',
                     'Access-Control-Allow-Methods': "GET, POST"},
            body=''
        ),
        persistent=False)
    Mappings.create_mapping(mapping)
