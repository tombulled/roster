from roster import Register
from typing import Tuple

identifiers: Register[str, str] = Register()

@identifiers.entry
def identifier(code: str, /) -> Tuple[str, str]:
    return (code[0], code.upper())

identifier('foo')
identifier('bar')