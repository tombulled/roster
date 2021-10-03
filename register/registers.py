import typing

from . import models
from . import hooks

# NOTE: Use `attr` ?
# NOTE: Use `collections.OrderedDict` ?

class FlatRegister(list):
    def __call__(self, item):
        self.append(item)

        return item

class Register(dict):
    hook = None

    def __init__(self, hook = hooks.state) -> None:
        super().__init__()

        self.hook = hook

    def __call__(self, *args, **kwargs):
        def decorator(item):
            self.__setitem__(item, self.hook(*args, **kwargs))

            return item

        return decorator

class InverseRegister(dict):
    hook = None

    def __init__(self, hook = hooks.identity) -> None:
        super().__init__()

        self.hook = hook

    def __call__(self, *args, **kwargs):
        def decorator(item):
            self.__setitem__(self.hook(*args, **kwargs), item)

            return item

        return decorator
