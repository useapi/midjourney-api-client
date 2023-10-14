# coding: utf-8

"""
    Midjourney API by useapi.net

    Simple, reliable and affordable way to use Midjourney via standard REST API

"""  # noqa: E501


import unittest
import datetime

from midjourney_api_client.models.imagine_response_moderated import ImagineResponseModerated  # noqa: E501

class TestImagineResponseModerated(unittest.TestCase):
    """ImagineResponseModerated unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImagineResponseModerated:
        """Test ImagineResponseModerated
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImagineResponseModerated`
        """
        model = ImagineResponseModerated()  # noqa: E501
        if include_optional:
            return ImagineResponseModerated(
                error = '',
                jobid = '',
                status = 'moderated',
                code = 422
            )
        else:
            return ImagineResponseModerated(
                error = '',
                jobid = '',
                status = 'moderated',
                code = 422,
        )
        """

    def testImagineResponseModerated(self):
        """Test ImagineResponseModerated"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
