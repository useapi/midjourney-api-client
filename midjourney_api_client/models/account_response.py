# coding: utf-8

"""
    Midjourney API by useapi.net

    Simple, reliable and affordable way to use Midjourney via standard REST API

"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictStr

class AccountResponse(BaseModel):
    """
    AccountResponse
    """
    email: StrictStr = Field(...)
    created: StrictStr = Field(...)
    name: StrictStr = Field(...)
    verified: StrictStr = Field(...)
    sub: StrictStr = Field(...)
    __properties = ["email", "created", "name", "verified", "sub"]

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
    def from_json(cls, json_str: str) -> AccountResponse:
        """Create an instance of AccountResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AccountResponse:
        """Create an instance of AccountResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AccountResponse.parse_obj(obj)

        _obj = AccountResponse.parse_obj({
            "email": obj.get("email"),
            "created": obj.get("created"),
            "name": obj.get("name"),
            "verified": obj.get("verified"),
            "sub": obj.get("sub")
        })
        return _obj


