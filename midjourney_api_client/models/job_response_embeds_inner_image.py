# coding: utf-8

"""
    Midjourney API by useapi.net

    Simple, reliable and affordable way to use Midjourney via standard REST API

"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr

class JobResponseEmbedsInnerImage(BaseModel):
    """
    JobResponseEmbedsInnerImage
    """
    url: Optional[StrictStr] = None
    proxy_url: Optional[StrictStr] = None
    width: Optional[Union[StrictFloat, StrictInt]] = None
    height: Optional[Union[StrictFloat, StrictInt]] = None
    __properties = ["url", "proxy_url", "width", "height"]

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
    def from_json(cls, json_str: str) -> JobResponseEmbedsInnerImage:
        """Create an instance of JobResponseEmbedsInnerImage from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> JobResponseEmbedsInnerImage:
        """Create an instance of JobResponseEmbedsInnerImage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return JobResponseEmbedsInnerImage.parse_obj(obj)

        _obj = JobResponseEmbedsInnerImage.parse_obj({
            "url": obj.get("url"),
            "proxy_url": obj.get("proxy_url"),
            "width": obj.get("width"),
            "height": obj.get("height")
        })
        return _obj


