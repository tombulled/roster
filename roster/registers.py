import typing


Hook: type = typing.Callable[[typing.Any], typing.Any]
CompositionHook: type = typing.Callable[..., typing.Any]


class Record(list):
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
    _key_hook: typing.Optional[CompositionHook]
    _value_hook: typing.Optional[CompositionHook]

    def __init__(
        self,
        key_hook: typing.Optional[CompositionHook] = None,
        value_hook: typing.Optional[CompositionHook] = None,
    ) -> None:
        self._key_hook = key_hook
        self._value_hook = value_hook

    def __call__(
        self, *args: typing.Any, **kwargs: typing.Any
    ) -> typing.Callable[[typing.T], typing.T]:
        key: typing.Any = None

        if self._key_hook is not None:
            key = self._key_hook(*args, **kwargs)
        elif args:
            key = args[0]

        def decorator(*args: typing.Any, **kwargs: typing.Any) -> typing.T:
            value: typing.Any = None

            if self._value_hook is not None:
                value = self._value_hook(*args, **kwargs)
            elif args:
                value = args[0]

            self[key] = value

            return key

        return decorator