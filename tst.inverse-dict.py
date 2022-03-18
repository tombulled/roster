from typing import Dict, TypeVar

K = TypeVar('K')
V = TypeVar('V')

class InverseDict(Dict[K, V]):
    def __setitem__(self, value: V, key: K) -> None:
        super().__setitem__(key, value)

d: InverseDict[str, int] = InverseDict[str, int]()

d[1] = 'a'