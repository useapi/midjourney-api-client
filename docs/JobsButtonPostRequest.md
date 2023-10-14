# JobsButtonPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobid** | **str** | jobid of successfully completed (status set to completed) jobs/imagine, jobs/blend, jobs/describe or jobs/button job | 
**button** | **str** | button from buttons array of job referenced via jobid | 
**discord** | **str** | Optional Discord token, if provided will override discord value of referenced jobid | [optional] 
**max_jobs** | **int** | Optional Maximum Concurrent Jobs for current Midjourney subscription | [optional] 
**reply_url** | **str** | Optional callback URL, API will call the provided replyUrl once generation completed | [optional] 
**reply_ref** | **str** | Optional reference id which will be stored and returned along with this job response / result | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


