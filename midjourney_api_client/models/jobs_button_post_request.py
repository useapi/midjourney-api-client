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
from pydantic import BaseModel, Field, StrictStr, conint, validator

class JobsButtonPostRequest(BaseModel):
    """
    JobsButtonPostRequest
    """
    jobid: StrictStr = Field(..., description="jobid of successfully completed (status set to completed) jobs/imagine, jobs/blend, jobs/describe or jobs/button job")
    button: StrictStr = Field(..., description="button from buttons array of job referenced via jobid")
    discord: Optional[StrictStr] = Field(None, description="Optional Discord token, if provided will override discord value of referenced jobid")
    max_jobs: Optional[conint(strict=True, le=15, ge=1)] = Field(None, alias="maxJobs", description="Optional Maximum Concurrent Jobs for current Midjourney subscription")
    reply_url: Optional[StrictStr] = Field(None, alias="replyUrl", description="Optional callback URL, API will call the provided replyUrl once generation completed")
    reply_ref: Optional[StrictStr] = Field(None, alias="replyRef", description="Optional reference id which will be stored and returned along with this job response / result")
    __properties = ["jobid", "button", "discord", "maxJobs", "replyUrl", "replyRef"]

    @validator('button')
    def button_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('U1', 'U2', 'U3', 'U4', 'V1', 'V2', 'V3', 'V4', '⬅️', '➡️', '⬆️', '⬇️', '🔄', 'Vary (Strong)', 'Vary (Subtle)', 'Zoom Out 1.5x', 'Zoom Out 2x', 'Make Square', 'Make Variations', 'Remaster'):
            raise ValueError("must be one of enum values ('U1', 'U2', 'U3', 'U4', 'V1', 'V2', 'V3', 'V4', '⬅️', '➡️', '⬆️', '⬇️', '🔄', 'Vary (Strong)', 'Vary (Subtle)', 'Zoom Out 1.5x', 'Zoom Out 2x', 'Make Square', 'Make Variations', 'Remaster')")
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
    def from_json(cls, json_str: str) -> JobsButtonPostRequest:
        """Create an instance of JobsButtonPostRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> JobsButtonPostRequest:
        """Create an instance of JobsButtonPostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return JobsButtonPostRequest.parse_obj(obj)

        _obj = JobsButtonPostRequest.parse_obj({
            "jobid": obj.get("jobid"),
            "button": obj.get("button"),
            "discord": obj.get("discord"),
            "max_jobs": obj.get("maxJobs"),
            "reply_url": obj.get("replyUrl"),
            "reply_ref": obj.get("replyRef")
        })
        return _obj


