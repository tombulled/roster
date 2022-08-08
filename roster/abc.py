from abc import ABC, abstractmethod
from typing import (
    Any,
    Callable,
    Generic,
    MutableMapping,
    MutableSequence,
    MutableSet,
    Tuple,
    TypeVar,
)

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


class RecordABC(ABC, Generic[V]):
    @abstractmethod
    def record(self, value: V, /) -> None:
        raise NotImplementedError

    def __call__(self, value: V, /) -> V:
        self.record(value)

        return value

    def item(self, func: Callable[[T], V], /) -> Callable[[T], T]:
        def proxy(item: T, /) -> T:
            self.record(func(item))

            return item

        return proxy


class SequenceRecordABC(RecordABC[V], MutableSequence[V]):
    def record(self, value: V, /) -> None:
        self.append(value)


class SetRecordABC(RecordABC[V], MutableSet[V]):
    def record(self, value: V, /) -> None:
        self.add(value)


class RegisterABC(ABC, Generic[K, V]):
    @abstractmethod
    def register(self, key: K, value: V, /) -> None:
        raise NotImplementedError

    def __call__(self, key: K, /) -> Callable[[V], V]:
        def proxy(value: V, /) -> V:
            self.register(key, value)

            return value

        return proxy

    def key(self, func: Callable[..., K], /) -> Callable[..., Callable[[V], V]]:
        def proxy(*args: Any, **kwargs: Any) -> Callable[[V], V]:
            key: K = func(*args, **kwargs)

            def decorator(value: V, /) -> V:
                self.register(key, value)

                return value

            return decorator

        return proxy

    def value(self, func: Callable[..., V], /) -> Callable[..., Callable[[K], K]]:
        def proxy(*args: Any, **kwargs: Any) -> Callable[[K], K]:
            value: V = func(*args, **kwargs)

            def decorator(key: K, /) -> K:
                self.register(key, value)

                return key

            return decorator

        return proxy

    def entry(self, func: Callable[[T], Tuple[K, V]], /) -> Callable[[T], T]:
        def proxy(item: T, /) -> T:
            self.register(*func(item))

            return item

        return proxy


class MappingRegisterABC(RegisterABC[K, V], MutableMapping[K, V]):
    def register(self, key: K, value: V, /) -> None:
        self[key] = value
