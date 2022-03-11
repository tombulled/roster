import dataclasses
import typing

from . import models


@dataclasses.dataclass(repr=False)
class Record(list):
    hook: typing.Callable[[typing.T], typing.T] = lambda x: x

    def __call__(self, item: typing.T) -> typing.T:
        self.append(self.hook(item))

        return item


@dataclasses.dataclass(repr=False)
class Register(dict):
    hook: typing.Callable[..., typing.Any] = models.Context

    def __call__(
        self, *args: typing.Any, **kwargs: typing.Any
    ) -> typing.Callable[[typing.T], typing.T]:
        def decorator(item: typing.T) -> typing.T:
            self[item] = self.hook(*args, **kwargs)

            return item

        return decorator
