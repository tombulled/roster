from types import SimpleNamespace
from typing import Any, Callable, Dict, Generic, List, Set, Tuple, TypeVar

T = TypeVar('T')
K = TypeVar('K')
V = TypeVar('V')

class SetStore(Set[V]):
    def __call__(self, value: V, /) -> V:
        self.add(value)

        return value

    def item(self, func: Callable[[T], V], /) -> Callable[[T], T]:
        def proxy(item: T, /) -> T:
            self.add(func(item))

            return item

        return proxy

class ListStore(List[V]):
    def __call__(self, value: V, /) -> V:
        self.append(value)

        return value

    def item(self, func: Callable[[T], V], /) -> Callable[[T], T]:
        def proxy(item: T, /) -> T:
            self.append(func(item))

            return item

        return proxy

class DictStore(Dict[K, V]):
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
            self.__setitem__(*func(item))

            return item

        return proxy

class NamespaceStore(Generic[V], SimpleNamespace):
    def __setattr__(self, key: str, value: V, /) -> None:
        if key == '__orig_class__':
            raise AttributeError

        return super().__setattr__(key, value)

    def __call__(self, key: str, /) -> Callable[[V], V]:
        def proxy(value: V, /) -> V:
            setattr(self, key, value)

            return value

        return proxy

    def key(self, func: Callable[[V], str], /) -> Callable[[V], V]:
        def proxy(value: V, /) -> V:
            setattr(self, func(value), value)

            return value

        return proxy

    def value(self, func: Callable[[str], V], /) -> Callable[[str], str]:
        def proxy(key: str, /) -> str:
            setattr(self, key, func(key))

            return key

        return proxy

    def entry(self, func: Callable[[T], Tuple[str, V]], /) -> Callable[[T], T]:
        def proxy(item: T, /) -> T:
            setattr(self, *func(item))

            return item

        return proxy