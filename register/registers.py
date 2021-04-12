import attr

import functools
import collections

@attr.s
class Register(collections.OrderedDict):
    def __call__(self, *args, **kwargs):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            self[wrapper] = self._parse(*args, **kwargs)

            return wrapper

        return decorator

    def _parse(self, *args, **kwargs):
        return (args, kwargs)

@attr.s
class ObjectRegister(Register):
    type: type = attr.ib()

    def _parse(self, *args, **kwargs):
        return self.type(*args, **kwargs)
