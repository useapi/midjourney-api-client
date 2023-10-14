# coding: utf-8

"""
    Midjourney API by useapi.net

    Simple, reliable and affordable way to use Midjourney via standard REST API

"""  # noqa: E501


import unittest
import datetime

from midjourney_api_client.models.jobs_imagine_post_request import JobsImaginePostRequest  # noqa: E501

class TestJobsImaginePostRequest(unittest.TestCase):
    """JobsImaginePostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JobsImaginePostRequest:
        """Test JobsImaginePostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JobsImaginePostRequest`
        """
        model = JobsImaginePostRequest()  # noqa: E501
        if include_optional:
            return JobsImaginePostRequest(
                prompt = '',
                discord = '',
                server = '',
                channel = '',
                max_jobs = 1,
                reply_url = '',
                reply_ref = ''
            )
        else:
            return JobsImaginePostRequest(
                prompt = '',
                discord = '',
                server = '',
                channel = '',
        )
        """

    def testJobsImaginePostRequest(self):
        """Test JobsImaginePostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
