# coding: utf-8

"""
    Midjourney API by useapi.net

    Simple, reliable and affordable way to use Midjourney via standard REST API

"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist, validator

class ResponseMaxJobs(BaseModel):
    """
    ResponseMaxJobs
    """
    error: StrictStr = Field(...)
    executing_jobs: conlist(StrictStr) = Field(..., alias="executingJobs")
    code: StrictInt = Field(...)
    __properties = ["error", "executingJobs", "code"]

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
    def from_json(cls, json_str: str) -> ResponseMaxJobs:
        """Create an instance of ResponseMaxJobs from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ResponseMaxJobs:
        """Create an instance of ResponseMaxJobs from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ResponseMaxJobs.parse_obj(obj)

        _obj = ResponseMaxJobs.parse_obj({
            "error": obj.get("error"),
            "executing_jobs": obj.get("executingJobs"),
            "code": obj.get("code")
        })
        return _obj


