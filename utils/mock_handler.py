from wiremock.constants import Config
from wiremock.resources.mappings import Mapping, MappingRequest, HttpMethods, MappingResponse
from wiremock.resources.mappings.resource import Mappings
from wiremock.server import WireMockServer
from enum import Enum

class MockUrl(Enum):
    BASE_URI = "https://merchant.example.com:8443"
    WEBSERVICES_DOMAIN = "https://webservices.securetrading.net:8443"
    VISA_MOCK_URI = "/visaPaymentStatus"
    CC_MOCK_ACS_URI = "/cardinalAuthenticateCard"
    APPLEPAY_MOCK_URI = "/applePaymentStatus"
    GATEWAY_MOCK_URI = "/jwt/"
    CONFIG_MOCK_URI = "/config.json"
    PORT = "8443"

def start_mock_server():
    wm = WireMockServer()
    wm.port = 8084
    wm.start()
    Config.base_url = f'http://localhost:{wm.port}/__admin'


def stub_sample_json():
    mapping = Mapping(
        priority=100,
        request=MappingRequest(
            method=HttpMethods.GET,
            url='/test'
        ),
        response=MappingResponse(
            status=200,
            json_body={
                "test": "wiremock"
            }
        ),
        persistent=False)

    Mappings.create_mapping(mapping)

def stub_config(config_json):
    #TO DO
    print("ToDo")

def stub_st_request_type(mock_json, request_type):
    # TO DO
    print("ToDo")

def stub_st_request_type_request_error(request_type):
    # TO DO
    print("ToDo")

def stub_payment_status(mock_url, mock_json):
    # TO DO
    print("ToDo")