import typing

from . import models

def state(*args, **kwargs) -> models.State:
    return models.State(args = args, kwargs = kwargs)

def identity(argument: typing.Any) -> typing.Any:
    return argument
