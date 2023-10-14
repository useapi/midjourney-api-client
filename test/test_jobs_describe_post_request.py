# coding: utf-8

"""
    Midjourney API by useapi.net

    Simple, reliable and affordable way to use Midjourney via standard REST API

"""  # noqa: E501


import unittest
import datetime

from midjourney_api_client.models.jobs_describe_post_request import JobsDescribePostRequest  # noqa: E501

class TestJobsDescribePostRequest(unittest.TestCase):
    """JobsDescribePostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JobsDescribePostRequest:
        """Test JobsDescribePostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JobsDescribePostRequest`
        """
        model = JobsDescribePostRequest()  # noqa: E501
        if include_optional:
            return JobsDescribePostRequest(
                describe_url = '',
                discord = '',
                server = '',
                channel = '',
                max_jobs = 1,
                reply_url = '',
                reply_ref = ''
            )
        else:
            return JobsDescribePostRequest(
                describe_url = '',
                discord = '',
                server = '',
                channel = '',
        )
        """

    def testJobsDescribePostRequest(self):
        """Test JobsDescribePostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
