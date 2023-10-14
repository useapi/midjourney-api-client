# coding: utf-8

"""
    Midjourney API by useapi.net

    Simple, reliable and affordable way to use Midjourney via standard REST API

"""  # noqa: E501


import unittest
import datetime

from midjourney_api_client.models.button_response_error_upscaled import ButtonResponseErrorUpscaled  # noqa: E501

class TestButtonResponseErrorUpscaled(unittest.TestCase):
    """ButtonResponseErrorUpscaled unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ButtonResponseErrorUpscaled:
        """Test ButtonResponseErrorUpscaled
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ButtonResponseErrorUpscaled`
        """
        model = ButtonResponseErrorUpscaled()  # noqa: E501
        if include_optional:
            return ButtonResponseErrorUpscaled(
                error = '',
                button = 'U1',
                jobid = '',
                code = 409
            )
        else:
            return ButtonResponseErrorUpscaled(
                error = '',
                button = 'U1',
                jobid = '',
                code = 409,
        )
        """

    def testButtonResponseErrorUpscaled(self):
        """Test ButtonResponseErrorUpscaled"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
