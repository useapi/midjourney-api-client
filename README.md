# midjourney-api-client

This package contains Python client library for Midjourney API by [useapi.net](https://useapi.net).  

[Useapi.net](https://useapi.net)  provides a simple, reliable and affordable way to use [Midjourney](https://midjourney.com/) via standard REST API.

Quick [demo](https://useapi.net/demo).
## Requirements.

Python 3.7+

## Installation & Usage
### pip install

```sh
pip install midjourney-api-client
```
You may need to run `pip` with root permission: `sudo pip install midjourney-api-client`.

Then import the package:
```python
import midjourney_api_client
```
## API Overview

Midjourney [/imagine](https://docs.midjourney.com/docs/quick-start#5-use-the-imagine-command) command available via [jobs/imagine](https://useapi.net/docs/api-v1/jobs-imagine) API endpoint.

Midjourney [upscale or create variations](https://docs.midjourney.com/docs/quick-start#8-upscale-or-create-variations) and [enhance or modify](https://docs.midjourney.com/docs/quick-start#9-enhance-or-modify-your-image) button commands available via [jobs/button](https://useapi.net/docs/api-v1/jobs-button) API endpoint. 

Midjourney [/describe](https://docs.midjourney.com/docs/describe) command available via [jobs/describe](https://useapi.net/docs/api-v1/jobs-describe) API endpoint. 

Midjourney [/blend](https://docs.midjourney.com/docs/blend) command available via [jobs/blend](https://useapi.net/docs/api-v1/jobs-blend) API endpoint. 

Use [jobs/?jobid=<code class="language-plaintext highlighter-rouge">jobid</code>](https://useapi.net/docs/api-v1/jobs-jobid) API endpoint to retrieve job results. 

Postman [collection](https://www.postman.com/useapinet/workspace/useapi-net).

Swagger OpenAPI [documentation](https://app.swaggerhub.com/apis/useapi/Midjourney_API_v1/1.0) for generating server stubs and client SDKs.

## Usage

You will need to [set up and configure](https://useapi.net/docs/start-here) the Midjourey Discord account as well as subscribe to useapi.net service before you can start using API. 

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
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

```

## Documentation for API Endpoints

All URIs are relative to *https://api.useapi.net/v1*

Method | HTTP request | Description
 ------------- | ------------- | -------------
[**jobs_imagine_post**](https://github.com/useapi/midjourney-api-client/blob/main/docs/DefaultApi.md#jobs_imagine_post) | **POST** /jobs/imagine | Midjourney /imagine command
[**jobs_blend_post**](https://github.com/useapi/midjourney-api-client/blob/main/docs/DefaultApi.md#jobs_blend_post) | **POST** /jobs/blend | Midjourney /blend command
[**jobs_describe_post**](https://github.com/useapi/midjourney-api-client/blob/main/docs/DefaultApi.md#jobs_describe_post) | **POST** /jobs/describe | Midjourney /describe command
[**jobs_button_post**](https://github.com/useapi/midjourney-api-client/blob/main/docs/DefaultApi.md#jobs_button_post) | **POST** /jobs/button | Midjourney upscale or create variations and enhance or modify buttons
[**jobs_get**](https://github.com/useapi/midjourney-api-client/blob/main/docs/DefaultApi.md#jobs_get) | **GET** /jobs/ | Retrieve job status and results
[**jobs_get_list**](https://github.com/useapi/midjourney-api-client/blob/main/docs/DefaultApi.md#jobs_get_list) | **GET** /jobs | Get list of currently executing jobs
[**jobs_cancel_get**](https://github.com/useapi/midjourney-api-client/blob/main/docs/DefaultApi.md#jobs_cancel_get) | **GET** /jobs/cancel/ | Cancel job
[**account_get**](https://github.com/useapi/midjourney-api-client/blob/main/docs/DefaultApi.md#account_get) | **GET** /account | Retrieve useapi.net account information

## Documentation For Models

 - [AccountResponse](https://github.com/useapi/midjourney-api-client/blob/main/docs/AccountResponse.md)
 - [BlendResponse](https://github.com/useapi/midjourney-api-client/blob/main/docs/BlendResponse.md)
 - [ButtonResponse](https://github.com/useapi/midjourney-api-client/blob/main/docs/ButtonResponse.md)
 - [ButtonResponseErrorUpscaled](https://github.com/useapi/midjourney-api-client/blob/main/docs/ButtonResponseErrorUpscaled.md)
 - [DescribeResponse](https://github.com/useapi/midjourney-api-client/blob/main/docs/DescribeResponse.md)
 - [ImagineResponse](https://github.com/useapi/midjourney-api-client/blob/main/docs/ImagineResponse.md)
 - [ImagineResponseModerated](https://github.com/useapi/midjourney-api-client/blob/main/docs/ImagineResponseModerated.md)
 - [JobCancelResponse](https://github.com/useapi/midjourney-api-client/blob/main/docs/JobCancelResponse.md)
 - [JobResponse](https://github.com/useapi/midjourney-api-client/blob/main/docs/JobResponse.md)
 - [JobResponseAttachmentsInner](https://github.com/useapi/midjourney-api-client/blob/main/docs/JobResponseAttachmentsInner.md)
 - [JobResponseChildrenInner](https://github.com/useapi/midjourney-api-client/blob/main/docs/JobResponseChildrenInner.md)
 - [JobResponseEmbedsInner](https://github.com/useapi/midjourney-api-client/blob/main/docs/JobResponseEmbedsInner.md)
 - [JobResponseEmbedsInnerImage](https://github.com/useapi/midjourney-api-client/blob/main/docs/JobResponseEmbedsInnerImage.md)
 - [JobsBlendPostRequest](https://github.com/useapi/midjourney-api-client/blob/main/docs/JobsBlendPostRequest.md)
 - [JobsButtonPostRequest](https://github.com/useapi/midjourney-api-client/blob/main/docs/JobsButtonPostRequest.md)
 - [JobsDescribePostRequest](https://github.com/useapi/midjourney-api-client/blob/main/docs/JobsDescribePostRequest.md)
 - [JobsImaginePostRequest](https://github.com/useapi/midjourney-api-client/blob/main/docs/JobsImaginePostRequest.md)
 - [ResponseError](https://github.com/useapi/midjourney-api-client/blob/main/docs/ResponseError.md)
 - [ResponseMaxJobs](https://github.com/useapi/midjourney-api-client/blob/main/docs/ResponseMaxJobs.md)

<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Authentication schemes defined for the API:
<a id="apiToken"></a>
### apiToken

- **Type**: Bearer authentication

## Changelog 

Version 1.0.1 | November 3, 2023  

Added support for following  [jobs/button](https://useapi.net/docs/api-v1/jobs-button) options:  
- Upscale (2x)
- Upscale (4x)
- Redo Upscale (2x)
- Redo Upscale (4x)

## Support 

Visit our   
-  [Discord Server](https://discord.gg/w28uK3cnmF) for any additional support and questions.
- [YouTube Channel](https://www.youtube.com/@midjourneyapi) for tutorials and demos.