from operator import setitem
from types import SimpleNamespace
from typing import Any, Callable, Dict, Set, Tuple, TypeVar, Generic, List
from dataclasses import dataclass

@dataclass(frozen=True, eq=True)
class Route:
    path: str
    method: str

@dataclass(frozen=True, eq=True)
class Response:
    data: str

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
    def key(self, func: Callable[[V], K], /) -> Callable[[V], V]:
        def proxy(value: V, /) -> V:
            setattr(self, func(value), value)

            return value

        return proxy

    def value(self, func: Callable[[K], V], /) -> Callable[[K], K]:
        def proxy(key: K, /) -> K:
            setattr(self, key, func(key))

            return key

        return proxy

    def entry(self, func: Callable[[T], Tuple[str, V]], /) -> Callable[[T], T]:
        def proxy(item: T, /) -> T:
            setattr(self, *func(item))

            return item

        return proxy

routes: DictStore[Route, Callable[..., Response]] = DictStore[Route, Callable[..., Response]]()
            
@routes.key
def route(path: str, method: str='GET') -> Route:
    return Route(path=path, method=method)

@route('/foo')
def foo() -> Response:
    return Response('Foo!')

@routes(Route('/bar', method='POST'))
def bar() -> Response:
    return Response('Bar!')

numbers: ListStore[int] = ListStore[int]()

@numbers.item
def number(n: int, /) -> int:
    return n * 10

number(1)
number(2)
number(3)
numbers(4)

characters: SetStore[str] = SetStore[str]()

characters('a')
characters('b')
characters('a')

attributes: DictStore[str, Callable] = DictStore[str, Callable]()

@attributes.entry
def attribute(func: Callable, /) -> Tuple[str, Callable]:
    return (func.__name__, func)

@attribute
def func(): pass

namespace: NamespaceStore[type] = NamespaceStore[type]()

@namespace.key
def cls(cls: type) -> str:
    return cls.__name__

@cls
class Foo: pass