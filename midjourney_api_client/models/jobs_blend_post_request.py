# coding: utf-8

"""
    Midjourney API by useapi.net

    Simple, reliable and affordable way to use Midjourney via standard REST API

"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conint, conlist, validator

class JobsBlendPostRequest(BaseModel):
    """
    JobsBlendPostRequest
    """
    blend_urls: conlist(StrictStr, max_items=5, min_items=2) = Field(..., alias="blendUrls", description="Must contain at least 2 valid URL image links, up to 5 URL image links supported")
    blend_dimensions: Optional[StrictStr] = Field(None, alias="blendDimensions")
    discord: StrictStr = Field(..., description="Discord token")
    server: StrictStr = Field(..., description="Discord server id")
    channel: StrictStr = Field(..., description="Discord channel id")
    max_jobs: Optional[conint(strict=True, le=15, ge=1)] = Field(None, alias="maxJobs", description="Optional Maximum Concurrent Jobs for current Midjourney subscription")
    reply_url: Optional[StrictStr] = Field(None, alias="replyUrl", description="Optional callback URL, API will call the provided replyUrl once generation completed")
    reply_ref: Optional[StrictStr] = Field(None, alias="replyRef", description="Optional reference id which will be stored and returned along with this job response / result")
    __properties = ["blendUrls", "blendDimensions", "discord", "server", "channel", "maxJobs", "replyUrl", "replyRef"]

    @validator('blend_dimensions')
    def blend_dimensions_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Portrait', 'Square', 'Landscape'):
            raise ValueError("must be one of enum values ('Portrait', 'Square', 'Landscape')")
        return value

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
    def from_json(cls, json_str: str) -> JobsBlendPostRequest:
        """Create an instance of JobsBlendPostRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> JobsBlendPostRequest:
        """Create an instance of JobsBlendPostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return JobsBlendPostRequest.parse_obj(obj)

        _obj = JobsBlendPostRequest.parse_obj({
            "blend_urls": obj.get("blendUrls"),
            "blend_dimensions": obj.get("blendDimensions"),
            "discord": obj.get("discord"),
            "server": obj.get("server"),
            "channel": obj.get("channel"),
            "max_jobs": obj.get("maxJobs"),
            "reply_url": obj.get("replyUrl"),
            "reply_ref": obj.get("replyRef")
        })
        return _obj


