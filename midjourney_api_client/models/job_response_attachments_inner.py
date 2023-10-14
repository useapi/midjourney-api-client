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
from pydantic import BaseModel, StrictInt, StrictStr

class JobResponseAttachmentsInner(BaseModel):
    """
    JobResponseAttachmentsInner
    """
    proxy_url: Optional[StrictStr] = None
    size: Optional[StrictInt] = None
    url: Optional[StrictStr] = None
    width: Optional[StrictInt] = None
    content_type: Optional[StrictStr] = None
    filename: Optional[StrictStr] = None
    height: Optional[StrictInt] = None
    id: Optional[StrictStr] = None
    __properties = ["proxy_url", "size", "url", "width", "content_type", "filename", "height", "id"]

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
    def from_json(cls, json_str: str) -> JobResponseAttachmentsInner:
        """Create an instance of JobResponseAttachmentsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> JobResponseAttachmentsInner:
        """Create an instance of JobResponseAttachmentsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return JobResponseAttachmentsInner.parse_obj(obj)

        _obj = JobResponseAttachmentsInner.parse_obj({
            "proxy_url": obj.get("proxy_url"),
            "size": obj.get("size"),
            "url": obj.get("url"),
            "width": obj.get("width"),
            "content_type": obj.get("content_type"),
            "filename": obj.get("filename"),
            "height": obj.get("height"),
            "id": obj.get("id")
        })
        return _obj


