# coding: utf-8

"""
    Midjourney API by useapi.net

    Simple, reliable and affordable way to use Midjourney via standard REST API

"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, conint

class JobsDescribePostRequest(BaseModel):
    """
    JobsDescribePostRequest
    """
    describe_url: StrictStr = Field(..., alias="describeUrl", description="Must contain valid URL image link")
    discord: StrictStr = Field(..., description="Discord token")
    server: StrictStr = Field(..., description="Discord server id")
    channel: StrictStr = Field(..., description="Discord channel id")
    max_jobs: Optional[conint(strict=True, le=15, ge=1)] = Field(None, alias="maxJobs", description="Optional Maximum Concurrent Jobs for current Midjourney subscription")
    reply_url: Optional[StrictStr] = Field(None, alias="replyUrl", description="Optional callback URL, API will call the provided replyUrl once generation completed")
    reply_ref: Optional[StrictStr] = Field(None, alias="replyRef", description="Optional reference id which will be stored and returned along with this job response / result")
    __properties = ["describeUrl", "discord", "server", "channel", "maxJobs", "replyUrl", "replyRef"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> JobsDescribePostRequest:
        """Create an instance of JobsDescribePostRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> JobsDescribePostRequest:
        """Create an instance of JobsDescribePostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return JobsDescribePostRequest.parse_obj(obj)

        _obj = JobsDescribePostRequest.parse_obj({
            "describe_url": obj.get("describeUrl"),
            "discord": obj.get("discord"),
            "server": obj.get("server"),
            "channel": obj.get("channel"),
            "max_jobs": obj.get("maxJobs"),
            "reply_url": obj.get("replyUrl"),
            "reply_ref": obj.get("replyRef")
        })
        return _obj


