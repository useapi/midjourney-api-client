# coding: utf-8

"""
    Midjourney API by useapi.net

    Simple, reliable and affordable way to use Midjourney via standard REST API

"""  # noqa: E501


import unittest
import datetime

from midjourney_api_client.models.job_response_attachments_inner import JobResponseAttachmentsInner  # noqa: E501

class TestJobResponseAttachmentsInner(unittest.TestCase):
    """JobResponseAttachmentsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JobResponseAttachmentsInner:
        """Test JobResponseAttachmentsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JobResponseAttachmentsInner`
        """
        model = JobResponseAttachmentsInner()  # noqa: E501
        if include_optional:
            return JobResponseAttachmentsInner(
                proxy_url = '',
                size = 56,
                url = '',
                width = 56,
                content_type = '',
                filename = '',
                height = 56,
                id = ''
            )
        else:
            return JobResponseAttachmentsInner(
        )
        """

    def testJobResponseAttachmentsInner(self):
        """Test JobResponseAttachmentsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
