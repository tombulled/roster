import dataclasses
import itertools
import typing


@dataclasses.dataclass
class Context:
    args: typing.Tuple[typing.Any] = dataclasses.field(default_factory=tuple)
    kwargs: typing.Dict[str, typing.Any] = dataclasses.field(default_factory=dict)

    def __init__(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        self.args = args
        self.kwargs = kwargs

    def __repr__(self) -> str:
        return "{class_name}({arguments})".format(
            class_name=type(self).__name__,
            arguments=", ".join(
                itertools.chain(
                    (f"{arg!r}" for arg in self.args),
                    (f"{key}={value!r}" for key, value in self.kwargs.items()),
                ),
            ),
        )
