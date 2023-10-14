import os
import time
from typing import Union
from pprint import pprint
import midjourney_api_client
from midjourney_api_client.api.default_api import DefaultApi
from midjourney_api_client.models.describe_response import DescribeResponse
from midjourney_api_client.models.imagine_response import ImagineResponse
from midjourney_api_client.models.job_response import JobResponse
from midjourney_api_client.models.jobs_blend_post_request import JobsBlendPostRequest
from midjourney_api_client.models.jobs_button_post_request import JobsButtonPostRequest
from midjourney_api_client.models.jobs_describe_post_request import JobsDescribePostRequest
from midjourney_api_client.models.jobs_imagine_post_request import JobsImaginePostRequest
from midjourney_api_client.rest import ApiException

configuration = midjourney_api_client.Configuration(
    host = "https://api.useapi.net/v1"
)

# Extract setting from environment
# Suggested shell execution command:
# USEAPI_TOKEN="..." USEAPI_DISCORD="..." USEAPI_SERVER="..." USEAPI_CHANNEL="..." python3 ./test.py
api_token = os.environ["USEAPI_TOKEN"]
discord = os.environ["USEAPI_DISCORD"]
server = os.environ["USEAPI_SERVER"]
channel = os.environ["USEAPI_CHANNEL"]
# Optional callback url
# We recommend using sites like webhook.site to test callback URL functionality.
reply_url = os.environ.get("USEAPI_CALLBACK", "")

# Configure Bearer authorization: apiToken
configuration = midjourney_api_client.Configuration(
    access_token = api_token
)

# This function is not not needed if job parameter reply_url (callback) specified
def wait_for_job_to_complete(api_instance: DefaultApi, job: Union[DescribeResponse, ImagineResponse, JobResponse]):
    verb = job.verb.upper()
    print(f"{verb} : {job.status}", job.jobid)

    while job.code == 200 and job.status in ['started', 'progress']:
        # Sleep for 20 seconds
        time.sleep(20)  
        job = api_instance.jobs_get(job.jobid)
        print(f"{verb} : {job.status}", {"jobid": job.jobid, "content": job.content})

    if isinstance(job, JobResponse) and job.attachments:
        print(f"{verb} url", job.attachments[0].url)
    if isinstance(job, JobResponse) and job.buttons:
        print(f"{verb} buttons", ", ".join(job.buttons))

    return job

def main():
    # Enter a context with an instance of the API client
    with midjourney_api_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = midjourney_api_client.DefaultApi(api_client)

        # Midjourney /describe
        try:
            jobs_describe_post_request = JobsDescribePostRequest(
                describeUrl="https://mymodernmet.com/wp/wp-content/uploads/2017/12/free-images-national-gallery-of-art-9.jpg",
                discord=discord,
                server=server,
                channel=channel,
                reply_url=reply_url
            )
            describe_response = api_instance.jobs_describe_post(jobs_describe_post_request)
            pprint(describe_response)

            # Not needed if job parameter reply_url (callback) specified
            describe_response = wait_for_job_to_complete(api_instance, describe_response)

        except ApiException as e:
            print("Exception when calling jobs_describe_post_request: %s\n" % e)

        # Midjourney /blend
        try:
            jobs_blend_post_request = JobsBlendPostRequest(
                blendUrls = [
                    "https://mymodernmet.com/wp/wp-content/uploads/2017/12/free-images-national-gallery-of-art-6.jpg",
                    "https://mymodernmet.com/wp/wp-content/uploads/2017/12/free-images-national-gallery-of-art-2.jpg"
                ],
                discord=discord,
                server=server,
                channel=channel,
                reply_url=reply_url
            )
            blend_response = api_instance.jobs_blend_post(jobs_blend_post_request)
            pprint(blend_response)

            # Not needed if job parameter reply_url (callback) specified
            blend_response = wait_for_job_to_complete(api_instance, blend_response)

        except ApiException as e:
            print("Exception when calling jobs_blend_post: %s\n" % e)

        # Midjourney /imagine
        try:
            jobs_imagine_post_request = JobsImaginePostRequest(
                prompt="Steampunk cat cycling in San Francisco, vintage photo",
                discord=discord,
                server=server,
                channel=channel,
                reply_url=reply_url
            )
            imagine_response = api_instance.jobs_imagine_post(jobs_imagine_post_request)
            pprint(imagine_response)

            imagine_response = wait_for_job_to_complete(api_instance, imagine_response)

        except ApiException as e:
            print("Exception when calling jobs_imagine_post: %s\n" % e)

        # Midjourney button commands
        try:
            jobs_button_post_request = JobsButtonPostRequest(
                button="V1",
                jobid=imagine_response.jobid,
                reply_url=reply_url
            )
            button_response = api_instance.jobs_button_post(jobs_button_post_request)
            pprint(button_response)

            # Not needed if job parameter reply_url (callback) specified
            button_response = wait_for_job_to_complete(api_instance, button_response)

        except ApiException as e:
            print("Exception when calling jobs_button_post: %s\n" % e)

main()