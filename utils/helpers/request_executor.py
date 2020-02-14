import requests
from requests.auth import HTTPBasicAuth
from configuration import CONFIGURATION


def mark_test_as_failed(session_id):
    browserstack_username = CONFIGURATION.COMMAND_EXECUTOR[8:25]
    browserstack_access_key = CONFIGURATION.COMMAND_EXECUTOR[26:-28]

    requests.put("https://api.browserstack.com/automate/sessions/" + session_id + ".json",
                 auth=HTTPBasicAuth(browserstack_username, browserstack_access_key),
                                    headers={'Content-Type': 'application/json'}, json={'status': 'failed'})