import dataclasses
import typing

from . import models

@dataclasses.dataclass(repr = False)
class Record(list):
    hook: typing.Optional[typing.Callable[[typing.Any], typing.Any]] = None

    def __call__(self, item: typing.Any) -> typing.Any:
        self.append(self.hook(item) if self.hook is not None else item)

        return item

@dataclasses.dataclass(repr = False)
class Register(dict):
    hook: typing.Optional[typing.Callable[..., typing.Any]] = models.Context

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> typing.Callable[[typing.Any], typing.Any]:
        def decorator(item: typing.Any) -> typing.Any:
            self.__setitem__(item, self.hook(*args, **kwargs))

            return item

        return decorator
