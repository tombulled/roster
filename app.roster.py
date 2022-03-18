from roster import Roster, roster
from roster.api import InverseRoster
from types import FunctionType

# @roster
# def d(func: FunctionType, /) -> str:
#     return func.__name__

a: Roster[str, FunctionType] = Roster(lambda func: func.__name__)
b: InverseRoster[FunctionType, str] = InverseRoster(lambda func: func.__name__)

@a
def f1(): pass

@a
def f2(): pass

@b
def f3(): pass

@b
def f4(): pass