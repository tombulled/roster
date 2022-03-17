import roster


def test_basic() -> None:
    record: roster.Record = roster.Record()

    a: int = record(1)
    b: int = record(2)
    c: int = record(3)

    assert record == [1, 2, 3]


def test_hooked() -> None:
    record: roster.Record = roster.Record(hook=lambda n: n * 2)

    record(1)
    record(2)
    record(3)

    assert record == [2, 4, 6]
