from typing import Any, Callable, Generic, TypeVar, Dict, List
from types import SimpleNamespace

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


class Record(Generic[T, V], List[V]):
    def __init__(self, hook: Callable[[T], V], /) -> None:
        self._hook: Callable[[T], V] = hook

    def __call__(self, item: T, /) -> T:
        self.append(self._hook(item))

        return item


class Roster(Generic[K, V], Dict[K, V]):
    def __init__(self, hook: Callable[[V], K], /) -> None:
        self._hook: Callable[[V], K] = hook

    def __call__(self, value: V, /) -> V:
        self[self._hook(value)] = value

        return value


class InverseRoster(Generic[K, V], Dict[K, V]):
    def __init__(self, hook: Callable[[K], V], /) -> None:
        self._hook: Callable[[K], V] = hook

    def __call__(self, key: K, /) -> K:
        self[key] = self._hook(key)

        return key


class Register(Generic[K, V], Dict[K, V]):
    def __init__(self, hook: Callable[..., K], /) -> None:
        self._hook: Callable[..., K] = hook

    def __call__(self, *args: Any, **kwargs: Any) -> Callable[[V], V]:
        key: K = self._hook(*args, **kwargs)

        def decorator(value: V, /) -> V:
            self[key] = value

            return value

        return decorator


class InverseRegister(Generic[K, V], Dict[K, V]):
    def __init__(self, hook: Callable[..., V], /) -> None:
        self._hook: Callable[..., V] = hook

    def __call__(self, *args: Any, **kwargs: Any) -> Callable[[K], K]:
        value: V = self._hook(*args, **kwargs)

        def decorator(key: K, /) -> K:
            self[key] = value

            return key

        return decorator

# class Namespace(SimpleNamespace[V]):
#     def __init__(self, hook: Callable[[V], V], /) -> None:
#         self._hook: Callable[[V], V] = hook

#     def __call__(self, )