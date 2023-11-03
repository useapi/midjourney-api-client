# coding: utf-8

"""
    Midjourney API by useapi.net

    Simple, reliable and affordable way to use Midjourney via standard REST API

"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictStr, validator

class JobResponseChildrenInner(BaseModel):
    """
    JobResponseChildrenInner
    """
    button: StrictStr = Field(...)
    jobid: StrictStr = Field(...)
    message_id: StrictStr = Field(..., alias="messageId")
    __properties = ["button", "jobid", "messageId"]

    @validator('button')
    def button_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('U1', 'U2', 'U3', 'U4', 'V1', 'V2', 'V3', 'V4', '⬅️', '➡️', '⬆️', '⬇️', '🔄', 'Vary (Strong)', 'Vary (Subtle)', 'Zoom Out 1.5x', 'Zoom Out 2x', 'Upscale (2x)', 'Upscale (4x)', 'Redo Upscale (2x)', 'Redo Upscale (4x)', 'Make Square', 'Make Variations', 'Remaster'):
            raise ValueError("must be one of enum values ('U1', 'U2', 'U3', 'U4', 'V1', 'V2', 'V3', 'V4', '⬅️', '➡️', '⬆️', '⬇️', '🔄', 'Vary (Strong)', 'Vary (Subtle)', 'Zoom Out 1.5x', 'Zoom Out 2x', 'Upscale (2x)', 'Upscale (4x)', 'Redo Upscale (2x)', 'Redo Upscale (4x)', 'Make Square', 'Make Variations', 'Remaster')")
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
    def from_json(cls, json_str: str) -> JobResponseChildrenInner:
        """Create an instance of JobResponseChildrenInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> JobResponseChildrenInner:
        """Create an instance of JobResponseChildrenInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return JobResponseChildrenInner.parse_obj(obj)

        _obj = JobResponseChildrenInner.parse_obj({
            "button": obj.get("button"),
            "jobid": obj.get("jobid"),
            "message_id": obj.get("messageId")
        })
        return _obj


