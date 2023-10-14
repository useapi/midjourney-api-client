# coding: utf-8

"""
    Midjourney API by useapi.net

    Simple, reliable and affordable way to use Midjourney via standard REST API

"""  # noqa: E501


import unittest
import datetime

from midjourney_api_client.models.job_response_embeds_inner_image import JobResponseEmbedsInnerImage  # noqa: E501

class TestJobResponseEmbedsInnerImage(unittest.TestCase):
    """JobResponseEmbedsInnerImage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JobResponseEmbedsInnerImage:
        """Test JobResponseEmbedsInnerImage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JobResponseEmbedsInnerImage`
        """
        model = JobResponseEmbedsInnerImage()  # noqa: E501
        if include_optional:
            return JobResponseEmbedsInnerImage(
                url = '',
                proxy_url = '',
                width = 1.337,
                height = 1.337
            )
        else:
            return JobResponseEmbedsInnerImage(
        )
        """

    def testJobResponseEmbedsInnerImage(self):
        """Test JobResponseEmbedsInnerImage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
