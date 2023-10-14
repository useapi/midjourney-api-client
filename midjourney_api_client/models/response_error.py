# coding: utf-8

"""
    Midjourney API by useapi.net

    Simple, reliable and affordable way to use Midjourney via standard REST API

"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictInt, StrictStr, validator

class ResponseError(BaseModel):
    """
    ResponseError
    """
    error: StrictStr = Field(...)
    code: StrictInt = Field(...)
    __properties = ["error", "code"]

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
    def from_json(cls, json_str: str) -> ResponseError:
        """Create an instance of ResponseError from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ResponseError:
        """Create an instance of ResponseError from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ResponseError.parse_obj(obj)

        _obj = ResponseError.parse_obj({
            "error": obj.get("error"),
            "code": obj.get("code")
        })
        return _obj


