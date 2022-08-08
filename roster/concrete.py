from types import SimpleNamespace
from typing import Dict, List, Set, TypeVar

from .abc import MappingRegisterABC, RegisterABC, SequenceRecordABC, SetRecordABC

K = TypeVar("K")
V = TypeVar("V")


class Record(List[V], SequenceRecordABC[V]):
    pass


class SetRecord(Set[V], SetRecordABC[V]):
    pass


class Register(Dict[K, V], MappingRegisterABC[K, V]):
    pass


class NamespaceRegister(RegisterABC[str, V], SimpleNamespace):
    def register(self, key: str, value: V, /) -> None:
        setattr(self, key, value)
