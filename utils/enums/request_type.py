from enum import Enum


class RequestType(Enum):
    THREEDQUERY = 1
    AUTH = 2
    WALLETVERIFY = 3
    JSINIT = 4
