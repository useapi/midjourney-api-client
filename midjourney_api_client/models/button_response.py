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

class ButtonResponse(BaseModel):
    """
    ButtonResponse
    """
    jobid: StrictStr = Field(..., description="Use returned jobid value to retrieve job status and results")
    verb: StrictStr = Field(...)
    status: StrictStr = Field(...)
    created: StrictStr = Field(...)
    updated: StrictStr = Field(...)
    button: StrictStr = Field(...)
    parent_job_id: StrictStr = Field(..., alias="parentJobId")
    channel: StrictStr = Field(...)
    server: StrictStr = Field(...)
    max_jobs: StrictInt = Field(..., alias="maxJobs")
    code: StrictInt = Field(...)
    __properties = ["jobid", "verb", "status", "created", "updated", "button", "parentJobId", "channel", "server", "maxJobs", "code"]

    @validator('verb')
    def verb_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('button'):
            raise ValueError("must be one of enum values ('button')")
        return value

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('started', 'completed'):
            raise ValueError("must be one of enum values ('started', 'completed')")
        return value

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
    def from_json(cls, json_str: str) -> ButtonResponse:
        """Create an instance of ButtonResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ButtonResponse:
        """Create an instance of ButtonResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ButtonResponse.parse_obj(obj)

        _obj = ButtonResponse.parse_obj({
            "jobid": obj.get("jobid"),
            "verb": obj.get("verb"),
            "status": obj.get("status"),
            "created": obj.get("created"),
            "updated": obj.get("updated"),
            "button": obj.get("button"),
            "parent_job_id": obj.get("parentJobId"),
            "channel": obj.get("channel"),
            "server": obj.get("server"),
            "max_jobs": obj.get("maxJobs"),
            "code": obj.get("code")
        })
        return _obj


