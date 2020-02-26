import requests
from requests.auth import HTTPBasicAuth
from utils.read_configuration import get_from_env

browserstack_username = get_from_env('BS_USERNAME')
browserstack_access_key = get_from_env('BS_ACCESS_KEY')

shared_dict = {}
def add_to_shared_dict(key, value):
    shared_dict[key] = value


def mark_test_as_failed(session_id):
    requests.put("https://api.browserstack.com/automate/sessions/" + session_id + ".json",
                 auth=HTTPBasicAuth(browserstack_username, browserstack_access_key),
                 headers={'Content-Type': 'application/json'}, json={'status': 'failed',
                                                                     'reason': shared_dict["assertion_message"]})


def set_scenario_name(session_id, scenario_name):
    requests.put("https://api.browserstack.com/automate/sessions/" + session_id + ".json",
                 auth=HTTPBasicAuth(browserstack_username, browserstack_access_key),
                 headers={'Content-Type': 'application/json'}, json={'name': scenario_name})
