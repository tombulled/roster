import operator
from typing import Any, Callable, MutableMapping, MutableSequence, Tuple, TypeVar

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


class RecordABC(MutableSequence[V]):
    def __call__(self, value: V, /) -> V:
        self.append(value)

        return value

    def item(self, func: Callable[[T], V], /) -> Callable[[T], T]:
        def proxy(item: T, /) -> T:
            self.append(func(item))

            return item

        return proxy


class RegisterABC(MutableMapping[K, V]):
    def __call__(self, key: K, /) -> Callable[[V], V]:
        def proxy(value: V, /) -> V:
            self[key] = value

            return value

        return proxy

    def key(self, func: Callable[..., K], /) -> Callable[..., Callable[[V], V]]:
        def proxy(*args: Any, **kwargs: Any) -> Callable[[V], V]:
            key: K = func(*args, **kwargs)

            def decorator(value: V, /) -> V:
                self[key] = value

                return value

            return decorator

        return proxy

    def value(self, func: Callable[..., V], /) -> Callable[..., Callable[[K], K]]:
        def proxy(*args: Any, **kwargs: Any) -> Callable[[K], K]:
            value: V = func(*args, **kwargs)

            def decorator(key: K, /) -> K:
                self[key] = value

                return key

            return decorator

        return proxy

    def entry(self, func: Callable[[T], Tuple[K, V]], /) -> Callable[[T], T]:
        def proxy(item: T, /) -> T:
            operator.setitem(self, *func(item))

            return item

        return proxy
