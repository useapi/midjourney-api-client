# coding: utf-8

"""
    Midjourney API by useapi.net

    Simple, reliable and affordable way to use Midjourney via standard REST API

"""  # noqa: E501


import unittest
import datetime

from midjourney_api_client.models.account_response import AccountResponse  # noqa: E501

class TestAccountResponse(unittest.TestCase):
    """AccountResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccountResponse:
        """Test AccountResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccountResponse`
        """
        model = AccountResponse()  # noqa: E501
        if include_optional:
            return AccountResponse(
                email = '',
                created = '',
                name = '',
                verified = '',
                sub = ''
            )
        else:
            return AccountResponse(
                email = '',
                created = '',
                name = '',
                verified = '',
                sub = '',
        )
        """

    def testAccountResponse(self):
        """Test AccountResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
