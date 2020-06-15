from enum import Enum


class RequestType(Enum):
    THREEDQUERY = 1
    AUTH = 2
    WALLETVERIFY = 3
    JSINIT = 4
    RISKDEC_ACHECK_TDQ = 5
    ACHECK_TDQ = 6
    AUTH_RISKDEC = 7
