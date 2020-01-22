from enum import Enum


class ApplePayResponse(Enum):
    SUCCESS = "appleSuccess.json"
    APPLE_AUTH_SUCCESS = "appleAuthSuccess.json"
    ERROR = "appleAuthError.json"
    CANCEL = "appleCancel.json"
    DECLINE = "appleAuthError.json"
