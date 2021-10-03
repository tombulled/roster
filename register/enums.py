import enum

# NOTE: No longer needed?
class Position(str, enum.Enum):
    _generate_next_value_ = lambda name, *_: name.lower()

    KEY:   str = enum.auto()
    VALUE: str = enum.auto()
