# coding: utf-8

"""
    Midjourney API by useapi.net

    Simple, reliable and affordable way to use Midjourney via standard REST API

"""  # noqa: E501


import unittest
import datetime

from midjourney_api_client.models.response_max_jobs import ResponseMaxJobs  # noqa: E501

class TestResponseMaxJobs(unittest.TestCase):
    """ResponseMaxJobs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResponseMaxJobs:
        """Test ResponseMaxJobs
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResponseMaxJobs`
        """
        model = ResponseMaxJobs()  # noqa: E501
        if include_optional:
            return ResponseMaxJobs(
                error = '',
                executing_jobs = [
                    ''
                    ],
                code = 429
            )
        else:
            return ResponseMaxJobs(
                error = '',
                executing_jobs = [
                    ''
                    ],
                code = 429,
        )
        """

    def testResponseMaxJobs(self):
        """Test ResponseMaxJobs"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
