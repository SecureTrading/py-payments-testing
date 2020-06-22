from enum import Enum

request_type_response = {
    "RISKDEC, ACCOUNTCHECK, THREEDQUERY": "ccRiskdecAcheckTdq.json",
    "ACCOUNTCHECK, THREEDQUERY": "ccAcheckTdq.json",
    "RISKDEC, ACCOUNTCHECK": "ccRiskdecAcheck.json",
    "AUTH, RISKDEC": "ccAuthRiskdec.json",
    "ACCOUNTCHECK, AUTH": "ccAccountcheckAuth.json",
    "RISKDEC, ACCOUNTCHECK, AUTH": "ccRiskdecAccountcheckAuth.json"
}

request_type_applepay = {
    "AUTH": "applAuth.json",
    "ACCOUNTCHECK": "appleAccountcheck.json",
    "ACCOUNTCHECK, AUTH": "appleAccountcheckAuth.json",
    "RISKDEC, AUTH": "appleRiskdecAuth.json",
    "RISKDEC, ACCOUNTCHECK, AUTH": "appleRiskdecAccountcheckAuth.json",
}

class RequestType(Enum):
    THREEDQUERY = 1
    AUTH = 2
    WALLETVERIFY = 3
    JSINIT = 4
    RISKDEC_ACHECK_TDQ = 5
    ACHECK_TDQ = 6
    AUTH_RISKDEC = 7
    RISKDEC_ACHECK = 8
    ACHECK_AUTH = 9
    RISKDEC_ACHECK_AUTH = 10
