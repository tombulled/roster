import typing

from . import models
from . import hooks
from . import enums
from . import utils

# NOTE: Use `attr` ?
# NOTE: Use `collections.OrderedDict` ?
# NOTE: Just rememberd why functions were wrapped (so that each one was unique!)
#   ... probably don't need this behaviour??

# Rename -> 'Roster', 'Record', 'List', 'Index', 'Series'
class Record(list):
    hook = None

    def __init__(self, hook = hooks.identity) -> None:
        super().__init__()

        self.hook = hook

    def __call__(self, item):
        hooked_item = self.hook(item)

        self.append(hooked_item)

        return hooked_item

class Roster(dict):
    generator = None

    def __init__(self, generator):
        self.generator = generator

    def __call__(self, item):
        self.__setitem__(item, self.generator(item))

        return item

    def invert(self):
        return utils.invert(self)

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

    def invert(self):
        return utils.invert(self)
