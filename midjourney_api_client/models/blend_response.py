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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist, validator

class BlendResponse(BaseModel):
    """
    BlendResponse
    """
    jobid: StrictStr = Field(..., description="Use returned jobid value to retrieve job status and results")
    verb: StrictStr = Field(...)
    status: StrictStr = Field(...)
    created: StrictStr = Field(...)
    updated: StrictStr = Field(...)
    blend_urls: conlist(StrictStr) = Field(..., alias="blendUrls")
    blend_dimensions: Optional[StrictStr] = Field(None, alias="blendDimensions")
    channel: StrictStr = Field(...)
    server: StrictStr = Field(...)
    max_jobs: StrictInt = Field(..., alias="maxJobs")
    message_id: StrictStr = Field(..., alias="messageId")
    content: StrictStr = Field(..., description="Contains message generated by Midjourney reflecting current generation parameters and progress")
    timestamp: StrictStr = Field(...)
    code: StrictInt = Field(...)
    __properties = ["jobid", "verb", "status", "created", "updated", "blendUrls", "blendDimensions", "channel", "server", "maxJobs", "messageId", "content", "timestamp", "code"]

    @validator('verb')
    def verb_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('blend'):
            raise ValueError("must be one of enum values ('blend')")
        return value

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('started'):
            raise ValueError("must be one of enum values ('started')")
        return value

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
    def from_json(cls, json_str: str) -> BlendResponse:
        """Create an instance of BlendResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BlendResponse:
        """Create an instance of BlendResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BlendResponse.parse_obj(obj)

        _obj = BlendResponse.parse_obj({
            "jobid": obj.get("jobid"),
            "verb": obj.get("verb"),
            "status": obj.get("status"),
            "created": obj.get("created"),
            "updated": obj.get("updated"),
            "blend_urls": obj.get("blendUrls"),
            "blend_dimensions": obj.get("blendDimensions"),
            "channel": obj.get("channel"),
            "server": obj.get("server"),
            "max_jobs": obj.get("maxJobs"),
            "message_id": obj.get("messageId"),
            "content": obj.get("content"),
            "timestamp": obj.get("timestamp"),
            "code": obj.get("code")
        })
        return _obj


