from typing import Any, Callable, Generic, TypeVar

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


class Record(Generic[T, V], list[V]):
    def __init__(self, hook: Callable[[T], V], /) -> None:
        self._hook: Callable[[T], V] = hook

    def __call__(self, item: T, /) -> T:
        self.append(self._hook(item))

        return item


class Roster(Generic[K, V], dict[K, V]):
    def __init__(self, hook: Callable[[V], K], /) -> None:
        self._hook: Callable[[V], K] = hook

    def __call__(self, value: V, /) -> V:
        self[self._hook(value)] = value

        return value


class Register(Generic[K, V], dict[K, V]):
    def __init__(self, hook: Callable[..., K], /) -> None:
        self._hook: Callable[..., K] = hook

    def __call__(self, *args: Any, **kwargs: Any) -> Callable[[V], V]:
        key: K = self._hook(*args, **kwargs)

        def decorator(value: V, /) -> V:
            self[key] = value

            return value

        return decorator


def record(hook: Callable[[T], V], /) -> Record[T, V]:
    return Record(hook)


def roster(hook: Callable[[V], K], /) -> Roster[K, V]:
    return Roster(hook)


def register(hook: Callable[..., K], /) -> Register[K, V]:
    return Register(hook)
