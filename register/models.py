import typing

import pydantic

class BaseModel(pydantic.BaseModel): pass

class State(BaseModel):
    args:   typing.Tuple[typing.Any, ...]
    kwargs: typing.Dict[str, typing.Any]
