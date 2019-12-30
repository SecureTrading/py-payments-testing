from enum import Enum


class ACSresponse(Enum):
    OK = "ccACSoK.json"
    NOACTION = "ccACSnoaction.json"
    FAILURE = "ccACSfailure.json"
    ERROR = "ccACSerror.json"
