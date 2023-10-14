# midjourney_api_client.DefaultApi

All URIs are relative to *https://api.useapi.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_get**](DefaultApi.md#account_get) | **GET** /account | 
[**jobs_blend_post**](DefaultApi.md#jobs_blend_post) | **POST** /jobs/blend | 
[**jobs_button_post**](DefaultApi.md#jobs_button_post) | **POST** /jobs/button | 
[**jobs_cancel_get**](DefaultApi.md#jobs_cancel_get) | **GET** /jobs/cancel/ | 
[**jobs_describe_post**](DefaultApi.md#jobs_describe_post) | **POST** /jobs/describe | 
[**jobs_get**](DefaultApi.md#jobs_get) | **GET** /jobs/ | 
[**jobs_get_list**](DefaultApi.md#jobs_get_list) | **GET** /jobs | 
[**jobs_imagine_post**](DefaultApi.md#jobs_imagine_post) | **POST** /jobs/imagine | 


# **account_get**
> AccountResponse account_get()



Retrieve account information

### Example

* Bearer Authentication (apiToken):
```python
import time
import os
import midjourney_api_client
from midjourney_api_client.models.account_response import AccountResponse
from midjourney_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.useapi.net/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = midjourney_api_client.Configuration(
    host = "https://api.useapi.net/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: apiToken
configuration = midjourney_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with midjourney_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = midjourney_api_client.DefaultApi(api_client)

    try:
        api_response = api_instance.account_get()
        print("The response of DefaultApi->account_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->account_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**AccountResponse**](AccountResponse.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_blend_post**
> BlendResponse jobs_blend_post(jobs_blend_post_request)



Submit the Midjourney /blend command

### Example

* Bearer Authentication (apiToken):
```python
import time
import os
import midjourney_api_client
from midjourney_api_client.models.blend_response import BlendResponse
from midjourney_api_client.models.jobs_blend_post_request import JobsBlendPostRequest
from midjourney_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.useapi.net/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = midjourney_api_client.Configuration(
    host = "https://api.useapi.net/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: apiToken
configuration = midjourney_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with midjourney_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = midjourney_api_client.DefaultApi(api_client)
    jobs_blend_post_request = midjourney_api_client.JobsBlendPostRequest() # JobsBlendPostRequest | 

    try:
        api_response = api_instance.jobs_blend_post(jobs_blend_post_request)
        print("The response of DefaultApi->jobs_blend_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->jobs_blend_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobs_blend_post_request** | [**JobsBlendPostRequest**](JobsBlendPostRequest.md)|  | 

### Return type

[**BlendResponse**](BlendResponse.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**412** | blendUrls, discord, server or channel value is missing, one of blendUrls values not a valid URL or URL which can not be retrieved |  -  |
**413** | replyRef or replyUrl is too long |  -  |
**422** | Unable to find posted message, likely moderated or invalid url |  -  |
**429** | API query is full and can not accept new jobs/blend requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_button_post**
> ButtonResponse jobs_button_post(jobs_button_post_request)



Midjourney upscale or create variations and enhance or modify buttons

### Example

* Bearer Authentication (apiToken):
```python
import time
import os
import midjourney_api_client
from midjourney_api_client.models.button_response import ButtonResponse
from midjourney_api_client.models.jobs_button_post_request import JobsButtonPostRequest
from midjourney_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.useapi.net/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = midjourney_api_client.Configuration(
    host = "https://api.useapi.net/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: apiToken
configuration = midjourney_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with midjourney_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = midjourney_api_client.DefaultApi(api_client)
    jobs_button_post_request = midjourney_api_client.JobsButtonPostRequest() # JobsButtonPostRequest | 

    try:
        api_response = api_instance.jobs_button_post(jobs_button_post_request)
        print("The response of DefaultApi->jobs_button_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->jobs_button_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobs_button_post_request** | [**JobsButtonPostRequest**](JobsButtonPostRequest.md)|  | 

### Return type

[**ButtonResponse**](ButtonResponse.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Button not supported or not found in jobid buttons array |  -  |
**401** | Unauthorized |  -  |
**404** | Unable to locate jobid |  -  |
**409** | Upscale button already executed by jobid |  -  |
**412** | jobid or button value is missing |  -  |
**413** | replyRef or replyUrl is too long |  -  |
**429** | API query is full and can not accept new jobs/button requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_cancel_get**
> JobCancelResponse jobs_cancel_get(jobid)



Cancel execution of job created by jobs/imagine, jobs/button, jobs/blend or jobs/describe

### Example

* Bearer Authentication (apiToken):
```python
import time
import os
import midjourney_api_client
from midjourney_api_client.models.job_cancel_response import JobCancelResponse
from midjourney_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.useapi.net/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = midjourney_api_client.Configuration(
    host = "https://api.useapi.net/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: apiToken
configuration = midjourney_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with midjourney_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = midjourney_api_client.DefaultApi(api_client)
    jobid = 'jobid_example' # str | jobid value returned by jobs/imagine, jobs/button, jobs/blend or jobs/describe

    try:
        api_response = api_instance.jobs_cancel_get(jobid)
        print("The response of DefaultApi->jobs_cancel_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->jobs_cancel_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| jobid value returned by jobs/imagine, jobs/button, jobs/blend or jobs/describe | 

### Return type

[**JobCancelResponse**](JobCancelResponse.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Query param jobid not provided |  -  |
**401** | Unauthorized |  -  |
**404** | Unable to locate jobid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_describe_post**
> DescribeResponse jobs_describe_post(jobs_describe_post_request)



Submit the Midjourney /describe command

### Example

* Bearer Authentication (apiToken):
```python
import time
import os
import midjourney_api_client
from midjourney_api_client.models.describe_response import DescribeResponse
from midjourney_api_client.models.jobs_describe_post_request import JobsDescribePostRequest
from midjourney_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.useapi.net/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = midjourney_api_client.Configuration(
    host = "https://api.useapi.net/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: apiToken
configuration = midjourney_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with midjourney_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = midjourney_api_client.DefaultApi(api_client)
    jobs_describe_post_request = midjourney_api_client.JobsDescribePostRequest() # JobsDescribePostRequest | 

    try:
        api_response = api_instance.jobs_describe_post(jobs_describe_post_request)
        print("The response of DefaultApi->jobs_describe_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->jobs_describe_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobs_describe_post_request** | [**JobsDescribePostRequest**](JobsDescribePostRequest.md)|  | 

### Return type

[**DescribeResponse**](DescribeResponse.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**412** | describeUrl, discord, server or channel value is missing, describeUrl value not a valid URL or URL which can not be retrieved |  -  |
**413** | replyRef or replyUrl is too long |  -  |
**422** | Unable to find posted message, likely moderated or invalid url |  -  |
**429** | API query is full and can not accept new jobs/blend requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_get**
> JobResponse jobs_get(jobid)



Retrieve status and results of jobs/imagine, jobs/button, jobs/blend or jobs/describe

### Example

* Bearer Authentication (apiToken):
```python
import time
import os
import midjourney_api_client
from midjourney_api_client.models.job_response import JobResponse
from midjourney_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.useapi.net/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = midjourney_api_client.Configuration(
    host = "https://api.useapi.net/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: apiToken
configuration = midjourney_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with midjourney_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = midjourney_api_client.DefaultApi(api_client)
    jobid = 'jobid_example' # str | jobid value returned by jobs/imagine, jobs/button, jobs/blend or jobs/describe

    try:
        api_response = api_instance.jobs_get(jobid)
        print("The response of DefaultApi->jobs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->jobs_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| jobid value returned by jobs/imagine, jobs/button, jobs/blend or jobs/describe | 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Query param jobid not provided |  -  |
**401** | Unauthorized |  -  |
**404** | Unable to locate jobid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_get_list**
> List[str] jobs_get_list()



Get list of currently executing jobs

### Example

* Bearer Authentication (apiToken):
```python
import time
import os
import midjourney_api_client
from midjourney_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.useapi.net/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = midjourney_api_client.Configuration(
    host = "https://api.useapi.net/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: apiToken
configuration = midjourney_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with midjourney_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = midjourney_api_client.DefaultApi(api_client)

    try:
        api_response = api_instance.jobs_get_list()
        print("The response of DefaultApi->jobs_get_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->jobs_get_list: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**List[str]**

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_imagine_post**
> ImagineResponse jobs_imagine_post(jobs_imagine_post_request)



Submit the Midjourney /imagine command

### Example

* Bearer Authentication (apiToken):
```python
import time
import os
import midjourney_api_client
from midjourney_api_client.models.imagine_response import ImagineResponse
from midjourney_api_client.models.jobs_imagine_post_request import JobsImaginePostRequest
from midjourney_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.useapi.net/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = midjourney_api_client.Configuration(
    host = "https://api.useapi.net/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: apiToken
configuration = midjourney_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with midjourney_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = midjourney_api_client.DefaultApi(api_client)
    jobs_imagine_post_request = midjourney_api_client.JobsImaginePostRequest() # JobsImaginePostRequest | 

    try:
        api_response = api_instance.jobs_imagine_post(jobs_imagine_post_request)
        print("The response of DefaultApi->jobs_imagine_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->jobs_imagine_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobs_imagine_post_request** | [**JobsImaginePostRequest**](JobsImaginePostRequest.md)|  | 

### Return type

[**ImagineResponse**](ImagineResponse.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**412** | prompt, discord, server or channel value is missing |  -  |
**413** | prompt, replyRef or replyUrl is too long |  -  |
**422** | Unable to find posted message, likely moderated or invalid prompt |  -  |
**429** | API query is full and can not accept new jobs/imagine requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

