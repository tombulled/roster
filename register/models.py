import typing

import pydantic

class BaseModel(pydantic.BaseModel): pass

class State(BaseModel):
    args:   typing.Tuple[typing.Any, ...] = pydantic.Field(default_factory = tuple)
    kwargs: typing.Dict[str, typing.Any]  = pydantic.Field(default_factory = dict)
