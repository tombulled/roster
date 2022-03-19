from typing import TypeVar
from .stores import DictStore, ListStore

K = TypeVar('K')
V = TypeVar('V')

class Record(ListStore[V]): pass
class Register(DictStore[K, V]): pass