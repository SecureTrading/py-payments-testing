from enum import Enum


class VisaResponse(Enum):
    VISA_AUTH_SUCCESS = "visaAuthSuccess.json"
    SUCCESS = "visaSuccess.json"
    ERROR = "visaError.json"
    CANCEL = "visaCancel.json"
