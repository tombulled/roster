from typing import Dict, List, TypeVar

from .abc import RecordABC, RegisterABC

K = TypeVar("K")
V = TypeVar("V")


class Record(List[V], RecordABC[V]):
    pass


class Register(Dict[K, V], RegisterABC[K, V]):
    pass
