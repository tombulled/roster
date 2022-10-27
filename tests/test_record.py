from typing import List

import pytest

import roster


@pytest.fixture
def record() -> roster.Record[int]:
    return roster.Record()


@pytest.fixture
def set_record() -> roster.SetRecord[int]:
    return roster.SetRecord()


def test_list_not_processed(record: roster.Record[int]) -> None:
    inputs: List[int] = [1, 2, 3, 1]
    outputs: List[int] = [record(input) for input in inputs]

    assert outputs == inputs
    assert record == inputs


def test_list_processed(record: roster.Record[int]) -> None:
    @record.item
    def preprocess(n: int, /) -> int:
        return n * 10

    inputs: List[int] = [1, 2, 3, 1]
    outputs: List[int] = [preprocess(input) for input in inputs]

    assert outputs == inputs
    assert record == [10, 20, 30, 10]


def test_set_not_processed(set_record: roster.SetRecord[int]) -> None:
    inputs: List[int] = [1, 2, 3, 1]
    outputs: List[int] = [set_record(input) for input in inputs]

    assert outputs == inputs
    assert set_record == set(inputs)


def test_set_processed(set_record: roster.SetRecord[int]) -> None:
    @set_record.item
    def preprocess(n: int, /) -> int:
        return n * 10

    inputs: List[int] = [1, 2, 3, 1]
    outputs: List[int] = [preprocess(input) for input in inputs]

    assert outputs == inputs
    assert set_record == {n * 10 for n in inputs}
