from enum import Enum


class AUTHresponse(Enum):
    OK = "ccAUTHoK.json"
    INVALID_FIELD = "ccAUTHInvalidField.json"
    SOCKET_ERROR = "ccAUTHSocketError.json"
    UNAUTHENTICATED = "ccAUTHUnauthenticated.json"
    DECLINE = "ccAUTHDeclineError.json"
    UNKNOWN_ERROR = "ccAUTHUnknownError.json"
    MERCHANT_DECLINE = "ccAUTHMerchantDeclineError.json"
