# coding: utf-8

"""
    Midjourney API by useapi.net

    Simple, reliable and affordable way to use Midjourney via standard REST API

"""  # noqa: E501


import unittest
import datetime

from midjourney_api_client.models.imagine_response import ImagineResponse  # noqa: E501

class TestImagineResponse(unittest.TestCase):
    """ImagineResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImagineResponse:
        """Test ImagineResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImagineResponse`
        """
        model = ImagineResponse()  # noqa: E501
        if include_optional:
            return ImagineResponse(
                jobid = '',
                verb = 'imagine',
                status = 'started',
                created = '',
                updated = '',
                prompt = '',
                channel = '',
                server = '',
                max_jobs = 56,
                message_id = '',
                content = '',
                timestamp = '',
                code = 200
            )
        else:
            return ImagineResponse(
                jobid = '',
                verb = 'imagine',
                status = 'started',
                created = '',
                updated = '',
                prompt = '',
                channel = '',
                server = '',
                max_jobs = 56,
                message_id = '',
                content = '',
                timestamp = '',
                code = 200,
        )
        """

    def testImagineResponse(self):
        """Test ImagineResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
