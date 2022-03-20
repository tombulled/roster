from typing import List, Tuple
import pytest
import roster


@pytest.fixture
def record() -> roster.Record[int]:
    return roster.Record[int]()


def test_default(record: roster.Record[int]) -> None:
    inputs: List[int] = [1, 2, 3]
    outputs: List[int] = [record(input) for input in inputs]

    assert outputs == inputs
    assert record == inputs


def test_preprocessed(record: roster.Record[int]) -> None:
    @record.item
    def preprocess(n: int, /) -> int:
        return n * 10

    inputs: List[int] = [1, 2, 3]
    outputs: List[int] = [preprocess(input) for input in inputs]

    assert outputs == inputs
    assert record == [10, 20, 30]
