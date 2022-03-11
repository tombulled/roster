import pytest
import roster


@pytest.fixture
def context() -> roster.Context:
    return roster.Context("/foo", "/bar", method="GET", version=1)


def test_init(context: roster.Context) -> None:
    assert context.args == ("/foo", "/bar")


def test_repr(context: roster.Context) -> None:
    assert repr(context) == "Context('/foo', '/bar', method='GET', version=1)"
