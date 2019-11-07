"""Separate module to handle framework test data"""
from attrdict import AttrDict


def load_test_data():
    test_data_dict = {
        'USER': AttrDict({"ADMIN_USERNAME": "test@test.pl",
                          "ADMIN_PASSWORD": "abc123"})
    }

    return AttrDict(test_data_dict)


TEST_DATA = load_test_data()


class TestData:

    def __init__(self, config__test):
        self._base_page = config__test.base_page

        """ User section """
        self.admin_username = TEST_DATA.USER.ADMIN_USERNAME
        self.admin_password = TEST_DATA.USER.ADMIN_PASSWORD
