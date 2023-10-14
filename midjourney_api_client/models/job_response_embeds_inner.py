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
from pydantic import BaseModel, StrictStr
from midjourney_api_client.models.job_response_embeds_inner_image import JobResponseEmbedsInnerImage

class JobResponseEmbedsInner(BaseModel):
    """
    JobResponseEmbedsInner
    """
    type: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    image: Optional[JobResponseEmbedsInnerImage] = None
    __properties = ["type", "description", "image"]

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
    def from_json(cls, json_str: str) -> JobResponseEmbedsInner:
        """Create an instance of JobResponseEmbedsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of image
        if self.image:
            _dict['image'] = self.image.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> JobResponseEmbedsInner:
        """Create an instance of JobResponseEmbedsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return JobResponseEmbedsInner.parse_obj(obj)

        _obj = JobResponseEmbedsInner.parse_obj({
            "type": obj.get("type"),
            "description": obj.get("description"),
            "image": JobResponseEmbedsInnerImage.from_dict(obj.get("image")) if obj.get("image") is not None else None
        })
        return _obj


