import collections

import attr

from . import models

'''
Notes:
    Should work with unhashable objects? (e.g. don't use a dict)
'''

class FlatRegister(list):
    __call__ = list.append

class Register(collections.OrderedDict):
    def __call__(self, *args, **kwargs):
        def decorator(item):
            self[item] = models.State(args = args, kwargs = kwargs)

            return item

        return decorator

@attr.s(repr = False)
class HookedRegister(Register):
    hook = attr.ib()

    def __setitem__(self, key: str, state: models.State) -> None:
        super().__setitem__(key, self.hook(*state.args, **state.kwargs))
