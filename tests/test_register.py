from typing import Dict, List, Tuple
import pytest
import roster


@pytest.fixture
def register() -> roster.Register[str, int]:
    return roster.Register[str, int]()


def test_default(register: roster.Register[str, int]) -> None:
    inputs: Dict[str, int] = {"foo": 1, "bar": 2}
    outputs: List[int] = [register(key)(value) for key, value in inputs.items()]

    assert outputs == list(inputs.values())
    assert register == inputs


def test_gen_key(register: roster.Register[str, int]) -> None:
    @register.key
    def reg(key: str, /) -> str:
        return key.upper()

    inputs: Dict[str, int] = {"foo": 1, "bar": 2}
    outputs: List[int] = [reg(key)(value) for key, value in inputs.items()]

    assert outputs == list(inputs.values())
    assert register == {key.upper(): value for key, value in inputs.items()}


def test_gen_value(register: roster.Register[str, int]) -> None:
    @register.value
    def reg(value: int, /) -> int:
        return value * 10

    inputs: Dict[str, int] = {"foo": 1, "bar": 2}
    outputs: List[str] = [reg(value)(key) for key, value in inputs.items()]

    assert outputs == list(inputs.keys())
    assert register == {key: value * 10 for key, value in inputs.items()}


def test_gen_entry(register: roster.Register[str, int]) -> None:
    @register.entry
    def reg(item: str, /) -> Tuple[str, int]:
        return (item.upper(), len(item))

    inputs: List[str] = ["foo", "bar"]
    outputs: List[str] = [reg(item) for item in inputs]

    assert outputs == inputs
    assert register == {item.upper(): len(item) for item in inputs}
