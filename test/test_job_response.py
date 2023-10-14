# coding: utf-8

"""
    Midjourney API by useapi.net

    Simple, reliable and affordable way to use Midjourney via standard REST API

"""  # noqa: E501


import unittest
import datetime

from midjourney_api_client.models.job_response import JobResponse  # noqa: E501

class TestJobResponse(unittest.TestCase):
    """JobResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JobResponse:
        """Test JobResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JobResponse`
        """
        model = JobResponse()  # noqa: E501
        if include_optional:
            return JobResponse(
                jobid = '',
                parent_job_id = '',
                verb = 'imagine',
                status = 'created',
                created = '',
                updated = '',
                prompt = '',
                blend_urls = [
                    ''
                    ],
                blend_dimensions = 'Portrait',
                describe_url = '',
                button = 'U1',
                children = [
                    midjourney_api_client.models.job_response_children_inner.jobResponse_children_inner(
                        button = 'U1', 
                        jobid = '', 
                        message_id = '', )
                    ],
                buttons = [
                    'U1'
                    ],
                channel = '',
                server = '',
                max_jobs = 56,
                message_id = '',
                content = '',
                timestamp = '',
                attachments = [
                    midjourney_api_client.models.job_response_attachments_inner.jobResponse_attachments_inner(
                        proxy_url = '', 
                        size = 56, 
                        url = '', 
                        width = 56, 
                        content_type = '', 
                        filename = '', 
                        height = 56, 
                        id = '', )
                    ],
                embeds = [
                    midjourney_api_client.models.job_response_embeds_inner.jobResponse_embeds_inner(
                        type = '', 
                        description = '', 
                        image = midjourney_api_client.models.job_response_embeds_inner_image.jobResponse_embeds_inner_image(
                            url = '', 
                            proxy_url = '', 
                            width = 1.337, 
                            height = 1.337, ), )
                    ],
                code = 200
            )
        else:
            return JobResponse(
                jobid = '',
                verb = 'imagine',
                status = 'created',
                created = '',
                channel = '',
                server = '',
                max_jobs = 56,
                code = 200,
        )
        """

    def testJobResponse(self):
        """Test JobResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
