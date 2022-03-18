from typing import Any, Callable, TypeVar

from .api import Record, Roster, Register

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


def record(hook: Callable[[T], V], /) -> Record[T, V]:
    return Record(hook)


def roster(hook: Callable[[V], K], /) -> Roster[K, V]:
    return Roster(hook)


def register(hook: Callable[..., K], /) -> Register[K, Any]:
    return Register(hook)
