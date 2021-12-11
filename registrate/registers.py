import dataclasses
import typing

from . import models
from . import utils

@dataclasses.dataclass(repr = False)
class Record(list):
    hook: typing.Callable[[typing.Any], typing.Any]] = utils.identity

    def __call__(self, item: typing.Any) -> typing.Any:
        self.append(self.hook(item))

        return item

@dataclasses.dataclass(repr = False)
class Register(dict):
    hook: typing.Callable[..., typing.Any] = models.Context

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> typing.Callable[[typing.Any], typing.Any]:
        def decorator(item: typing.Any) -> typing.Any:
            self[item] = self.hook(*args, **kwargs)

            return item

        return decorator
