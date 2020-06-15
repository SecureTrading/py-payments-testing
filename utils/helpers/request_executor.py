import json

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


def get_number_of_requests_with_data(request_type, pan, expiry_date, cvv):
    count = requests.post("https://webservices.securetrading.net:8443/__admin/requests/count",
                          json={"url": "/jwt/", "bodyPatterns": [
                              {"matchesJsonPath": "$.request[:1][?(@.requesttypedescriptions==['" + request_type + "'])]"},
                              {"matchesJsonPath": "$.request[:1][?(@.pan=='" + pan + "')]"},
                              {"matchesJsonPath": "$.request[:1][?(@.expirydate=='" + expiry_date + "')]"},
                              {"matchesJsonPath": "$.request[:1][?(@.securitycode=='" + cvv + "')]"}
                          ]}, verify=False)
    data = json.loads(count.content)
    return data['count']


def get_number_of_requests_with_data_and_fraudcontroltransactionid_flag(request_type, pan, expiry_date, cvv):
    count = requests.post("https://webservices.securetrading.net:8443/__admin/requests/count",
                          json={"url": "/jwt/", "bodyPatterns": [
                              {"matchesJsonPath": "$.request[:1][?(@.requesttypedescriptions==['" + request_type + "'])]"},
                              {"matchesJsonPath": "$.request[:1][?(@.pan=='" + pan + "')]"},
                              {"matchesJsonPath": "$.request[:1][?(@.expirydate=='" + expiry_date + "')]"},
                              {"matchesJsonPath": "$.request[:1][?(@.securitycode=='" + cvv + "')]"},
                              {"matchesJsonPath": "$.request[:1][?(@.fraudcontroltransactionid=='63d1d099-d635-41b6-bb82-96017f7da6bb')]"}
                          ]}, verify=False)
    data = json.loads(count.content)
    return data['count']


def get_number_of_requests_with_fraudcontroltransactionid_flag(request_type):
    count = requests.post("https://webservices.securetrading.net:8443/__admin/requests/count",
                          json={"url": "/jwt/", "bodyPatterns": [
                              {"matchesJsonPath": "$.request[:1][?(@.requesttypedescriptions==['" + request_type + "'])]"},
                              {"matchesJsonPath": "$.request[:1][?(@.fraudcontroltransactionid=='63d1d099-d635-41b6-bb82-96017f7da6bb')]"}
                          ]}, verify=False)
    data = json.loads(count.content)
    return data['count']


def get_number_of_requests_with_updated_jwt(request_type):
    count = requests.post("https://webservices.securetrading.net:8443/__admin/requests/count",
                          json={"url": "/jwt/", "bodyPatterns": [
                              {"matchesJsonPath": "$.request[:1][?(@.requesttypedescriptions==['" + request_type + "'])]"},
                              {"matchesJsonPath": "$.[?(@.jwt=='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhbTAzMTAuYXV0b2FwaSIsImlhdCI6MTU4ODY5NTEzOS41NTgwOTc0LCJwYXlsb2FkIjp7ImJhc2VhbW91bnQiOiIxMDAwIiwiYWNjb3VudHR5cGVkZXNjcmlwdGlvbiI6IkVDT00iLCJjdXJyZW5jeWlzbzNhIjoiR0JQIiwic2l0ZXJlZmVyZW5jZSI6InRlc3RfamFtZXMzODY0MSIsImxvY2FsZSI6ImVuX0dCIiwicGFuIjoiNTIwMDAwMDAwMDAwMTAwNSIsImV4cGlyeWRhdGUiOiIwMS8yMiJ9fQ.wAmn0JqsAfj7ZtsqbDadknWpPhUhJb7CPiQT8VqZ4hk')]"}
                          ]}, verify=False)
    data = json.loads(count.content)
    return data['count']


def get_number_of_requests_without_data(request_type):
    count = requests.post("https://webservices.securetrading.net:8443/__admin/requests/count",
                          json={"url": "/jwt/", "bodyPatterns": [
                              { "matchesJsonPath": "$.request[:1][?(@.requesttypedescriptions==['" + request_type + "'])]"}
                          ]}, verify=False)
    data = json.loads(count.content)
    return data['count']


def get_number_of_thirdparty_requests(url):
    count = requests.post("https://webservices.securetrading.net:8443/__admin/requests/count",
                          json={"url": url}, verify=False)
    data = json.loads(count.content)
    return data['count']


def get_number_of_AUTH_thirdparty_requests(url, walletsource):
    count = requests.post("https://webservices.securetrading.net:8443/__admin/requests/count",
                          json={"url": "/jwt/", "bodyPatterns": [
                              {"matchesJsonPath": "$.request[:1][?(@.requesttypedescriptions==['AUTH'])]"},
                              {"matchesJsonPath": "$.request[:1][?(@.walletsource=='" + walletsource + "')]"}]},
                          verify=False)
    data = json.loads(count.content)
    return data['count']


def get_number_of_requests_with_auth_riskdec(pan, expiry_date, cvv):
    count = requests.post("https://webservices.securetrading.net:8443/__admin/requests/count",
                          json={"url": "/jwt/", "bodyPatterns": [
                              {"matchesJsonPath": "$.request[:1][?(@.requesttypedescriptions==['AUTH', 'RISKDEC'])]"},
                              {"matchesJsonPath": "$.request[:1][?(@.pan=='" + pan + "')]"},
                              {"matchesJsonPath": "$.request[:1][?(@.expirydate=='" + expiry_date + "')]"},
                              {"matchesJsonPath": "$.request[:1][?(@.securitycode=='" + cvv + "')]"}
                          ]}, verify=False)
    data = json.loads(count.content)
    return data['count']


def get_number_of_requests_with_accountcheck_3dq(pan, expiry_date, cvv):
    count = requests.post("https://webservices.securetrading.net:8443/__admin/requests/count",
                          json={"url": "/jwt/", "bodyPatterns": [
                              {"matchesJsonPath": "$.request[:1][?(@.requesttypedescriptions==['ACCOUNTCHECK', 'THREEDQUERY'])]"},
                              {"matchesJsonPath": "$.request[:1][?(@.pan=='" + pan + "')]"},
                              {"matchesJsonPath": "$.request[:1][?(@.expirydate=='" + expiry_date + "')]"},
                              {"matchesJsonPath": "$.request[:1][?(@.securitycode=='" + cvv + "')]"}
                          ]}, verify=False)
    data = json.loads(count.content)
    return data['count']


def get_number_of_requests_with_riskdec_accountcheck_3dq(pan, expiry_date, cvv):
    count = requests.post("https://webservices.securetrading.net:8443/__admin/requests/count",
                          json={"url": "/jwt/", "bodyPatterns": [
                              {"matchesJsonPath": "$.request[:1][?(@.requesttypedescriptions==['RISKDEC', 'ACCOUNTCHECK', 'THREEDQUERY'])]"},
                              {"matchesJsonPath": "$.request[:1][?(@.pan=='" + pan + "')]"},
                              {"matchesJsonPath": "$.request[:1][?(@.expirydate=='" + expiry_date + "')]"},
                              {"matchesJsonPath": "$.request[:1][?(@.securitycode=='" + cvv + "')]"}
                          ]}, verify=False)
    data = json.loads(count.content)
    return data['count']

def remove_item_from_request_journal():
    requests.delete("https://webservices.securetrading.net:8443/__admin/requests", verify=False)
