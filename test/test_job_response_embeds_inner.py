# coding: utf-8

"""
    Midjourney API by useapi.net

    Simple, reliable and affordable way to use Midjourney via standard REST API

"""  # noqa: E501


import unittest
import datetime

from midjourney_api_client.models.job_response_embeds_inner import JobResponseEmbedsInner  # noqa: E501

class TestJobResponseEmbedsInner(unittest.TestCase):
    """JobResponseEmbedsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JobResponseEmbedsInner:
        """Test JobResponseEmbedsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JobResponseEmbedsInner`
        """
        model = JobResponseEmbedsInner()  # noqa: E501
        if include_optional:
            return JobResponseEmbedsInner(
                type = '',
                description = '',
                image = midjourney_api_client.models.job_response_embeds_inner_image.jobResponse_embeds_inner_image(
                    url = '', 
                    proxy_url = '', 
                    width = 1.337, 
                    height = 1.337, )
            )
        else:
            return JobResponseEmbedsInner(
        )
        """

    def testJobResponseEmbedsInner(self):
        """Test JobResponseEmbedsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
