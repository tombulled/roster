import typing

Hook: type = typing.Callable[[typing.Any], typing.Any]
CompositionHook: type = typing.Callable[..., typing.Any]


class List(list):
    _hook: typing.Optional[Hook]

    def __init__(self, hook: typing.Optional[Hook] = None):
        self._hook = hook

    def __call__(self, item: typing.T) -> typing.T:
        if self._hook is not None:
            item = self._hook(item)

        self.append(item)

        return item


# TODO: Support ability for (key, value) *and* (value, key)
# Like Kafka's usage of .mapKey, .mapValue, .map
class Register(dict):
    _map_key: typing.Optional[CompositionHook]
    _map_value: typing.Optional[CompositionHook]

    def __init__(
        self,
        map_key: typing.Optional[CompositionHook] = None,
        map_value: typing.Optional[CompositionHook] = None,
    ) -> None:
        self._map_key = map_key
        self._map_value = map_value

    def __call__(
        self, *args: typing.Any, **kwargs: typing.Any
    ) -> typing.Callable[[typing.T], typing.T]:
        value: typing.Any = None

        if self._map_value is not None:
            value = self._map_value(*args, **kwargs)
        elif args:
            value = args[0]

        def decorator(*args: typing.Any, **kwargs: typing.Any) -> typing.T:
            key: typing.Any = None

            if self._map_key is not None:
                key = self._map_key(*args, **kwargs)
            elif args:
                key = args[0]

            self[key] = value

            return key

        return decorator