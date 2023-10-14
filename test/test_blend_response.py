# coding: utf-8

"""
    Midjourney API by useapi.net

    Simple, reliable and affordable way to use Midjourney via standard REST API

"""  # noqa: E501


import unittest
import datetime

from midjourney_api_client.models.blend_response import BlendResponse  # noqa: E501

class TestBlendResponse(unittest.TestCase):
    """BlendResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BlendResponse:
        """Test BlendResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BlendResponse`
        """
        model = BlendResponse()  # noqa: E501
        if include_optional:
            return BlendResponse(
                jobid = '',
                verb = 'blend',
                status = 'started',
                created = '',
                updated = '',
                blend_urls = [
                    ''
                    ],
                blend_dimensions = 'Portrait',
                channel = '',
                server = '',
                max_jobs = 56,
                message_id = '',
                content = '',
                timestamp = '',
                code = 200
            )
        else:
            return BlendResponse(
                jobid = '',
                verb = 'blend',
                status = 'started',
                created = '',
                updated = '',
                blend_urls = [
                    ''
                    ],
                channel = '',
                server = '',
                max_jobs = 56,
                message_id = '',
                content = '',
                timestamp = '',
                code = 200,
        )
        """

    def testBlendResponse(self):
        """Test BlendResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
