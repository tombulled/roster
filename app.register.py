from roster import Register, register
from roster.api import InverseRegister
from types import FunctionType

a: Register[str, FunctionType] = Register(lambda name: name.upper())
b: InverseRegister[FunctionType, str] = InverseRegister(lambda name: name.upper())

@a('f1')
def f1(): pass

@a('f2')
def f2(): pass

@b('f3')
def f3(): pass

@b('f4')
def f4(): pass