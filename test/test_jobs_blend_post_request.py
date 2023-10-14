# coding: utf-8

"""
    Midjourney API by useapi.net

    Simple, reliable and affordable way to use Midjourney via standard REST API

"""  # noqa: E501


import unittest
import datetime

from midjourney_api_client.models.jobs_blend_post_request import JobsBlendPostRequest  # noqa: E501

class TestJobsBlendPostRequest(unittest.TestCase):
    """JobsBlendPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JobsBlendPostRequest:
        """Test JobsBlendPostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JobsBlendPostRequest`
        """
        model = JobsBlendPostRequest()  # noqa: E501
        if include_optional:
            return JobsBlendPostRequest(
                blend_urls = [
                    ''
                    ],
                blend_dimensions = 'Portrait',
                discord = '',
                server = '',
                channel = '',
                max_jobs = 1,
                reply_url = '',
                reply_ref = ''
            )
        else:
            return JobsBlendPostRequest(
                blend_urls = [
                    ''
                    ],
                discord = '',
                server = '',
                channel = '',
        )
        """

    def testJobsBlendPostRequest(self):
        """Test JobsBlendPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
