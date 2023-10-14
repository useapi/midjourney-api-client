# coding: utf-8

"""
    Midjourney API by useapi.net

    Simple, reliable and affordable way to use Midjourney via standard REST API

"""  # noqa: E501


import unittest
import datetime

from midjourney_api_client.models.button_response import ButtonResponse  # noqa: E501

class TestButtonResponse(unittest.TestCase):
    """ButtonResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ButtonResponse:
        """Test ButtonResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ButtonResponse`
        """
        model = ButtonResponse()  # noqa: E501
        if include_optional:
            return ButtonResponse(
                jobid = '',
                verb = 'button',
                status = 'started',
                created = '',
                updated = '',
                button = 'U1',
                parent_job_id = '',
                channel = '',
                server = '',
                max_jobs = 56,
                code = 200
            )
        else:
            return ButtonResponse(
                jobid = '',
                verb = 'button',
                status = 'started',
                created = '',
                updated = '',
                button = 'U1',
                parent_job_id = '',
                channel = '',
                server = '',
                max_jobs = 56,
                code = 200,
        )
        """

    def testButtonResponse(self):
        """Test ButtonResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
