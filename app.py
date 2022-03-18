from typing import TypeVar, Generic, Dict, Callable, Tuple, List, Any

T = TypeVar('T')
K = TypeVar('K')
V = TypeVar('V')

class Record(Generic[T, V], List[V]):
    def __init__(self, hook: Callable[[T], V], /) -> None:
        self._hook: Callable[[T], V] = hook

    def __call__(self, item: T, /) -> T:
        self.append(self._hook(item))

        return item

class Roster(Generic[T, K, V], Dict[K, V]):
    def __init__(self, hook: Callable[[T], Tuple[K, V]], /) -> None:
        self._hook: Callable[[T], Tuple[K, V]] = hook

    def __call__(self, item: T, /) -> T:
        self.__setitem__(*self._hook(item))

        return item
    
class Register(Generic[K, V], Dict[K, V]):
    def __init__(self, hook: Callable[..., Tuple[K, V]], /) -> None:
        self._hook: Callable[..., Tuple[K, V]] = hook

    def __call__(self, *args: Any, **kwargs: Any) -> Callable[[V], V]:
        def decorator(item: V, /) -> V:
            self.__setitem__(*self._hook(item, *args, **kwargs))

            return item

        return decorator

def record(hook: Callable[[T], V], /) -> Record[T, V]:
    return Record(hook)

def roster(hook: Callable[[T], Tuple[K, V]], /) -> Roster[T, K, V]:
    return Roster(hook)

def register(hook: Callable[..., Tuple[K, V]], /) -> Register[K, V]:
    return Register(hook)

@record
def a(func: Callable, /) -> str:
    return func.__name__

@roster
def b(func: Callable, /) -> Tuple[Callable, str]:
    return (func, func.__name__)

@register
def c(func: Callable, path: str, method: str = 'GET') -> Tuple[Callable, Dict[str, str]]:
    return (func, dict(path=path, method=method))

@a
def f1(): pass

@a
def f2(): pass

@b
def f3(): pass

@b
def f4(): pass

@c('f5')
def f5(): pass

@c('f6')
def f6(): pass