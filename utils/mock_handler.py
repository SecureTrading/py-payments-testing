from wiremock.constants import Config
from wiremock.resources.mappings import Mapping, MappingRequest, HttpMethods, MappingResponse
from wiremock.resources.mappings.resource import Mappings
from wiremock.server import WireMockServer


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
