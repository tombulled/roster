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

            self[wrapper] = (args, kwargs)

            return wrapper

        return decorator

@attr.s
class ObjectRegister(Register):
    type: type = attr.ib()

    def __call__(self, *args, **kwargs):
        obj = self.type(*args, **kwargs)

        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            self[wrapper] = obj

            return wrapper

        return decorator
