from enum import Enum


class TDQresponse(Enum):
    ENROLLED_Y = "ccTDQEnrolledY.json"
    NOT_ENROLLED_N = "ccTDQEnrolledN.json"
    NOT_ENROLLED_U = "ccTDQEnrolledU.json"
    INVALID_ACQUIRER = "ccTDQInvalidAcquirer.json"
