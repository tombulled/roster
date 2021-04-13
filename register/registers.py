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
class HookedRegister(Register):
    hook = attr.ib()

    def __setitem__(self, key, val: tuple):
        args, kwargs = val

        super().__setitem__(key, self.hook(*args, **kwargs))
