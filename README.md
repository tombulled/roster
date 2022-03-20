# roster
Python object registers. Keep track of your classes, functions and data.

## Installation
`roster` can be installed from [PyPI](https://pypi.org/project/roster/)
```console
pip install roster
```

## Usage:

### `Record`

#### Default Record
```python
from roster import Record

numbers: Record[int] = Record()

numbers(1)
numbers(2)
numbers(3)
```

```python
>>> numbers
[1, 2, 3]
```

#### Generate each `item`
```python
from roster import Record

characters: Record[str] = Record()

@characters.item
def character(char: str, /) -> str:
    return char.upper()

character('a')
character('b')
character('c')
```

```python
>>> characters
['A', 'B', 'C']
```

### `Register`

#### Default Register
```python
from roster import Register

services: Register[str, type] = Register()

@services('youtube')
class YouTube: pass

@services('spotify')
class Spotify: pass
```

```python
>>> services
{'youtube': <class '__main__.YouTube'>, 'spotify': <class '__main__.Spotify'>}
```

#### Generate each `key`
```python
from roster import Register
from typing import Callable

functions: Register[str, Callable] = Register()

@functions.key
def function(name: str, /) -> str:
    return name.upper()

@function('foo')
def foo(): pass

@function('bar')
def bar(): pass
```

```python
>>> functions
{'FOO': <function foo at 0x7f9c4f065790>, 'BAR': <function bar at 0x7f9c4f065820>}
```

#### Generate each `value`
```python
from roster import Register
from typing import Callable

functions: Register[str, Callable] = Register()

@functions.value
def function(name: str, /) -> str:
    return name.upper()

@function('foo')
def foo(): pass

@function('bar')
def bar(): pass
```

```python
>>> functions
{<function foo at 0x7f26443aa790>: 'FOO', <function bar at 0x7f26443aa820>: 'BAR'}
```

#### Generate each `entry`
```python
from roster import Register
from typing import Tuple

identifiers: Register[str, str] = Register()

@identifiers.entry
def identifier(code: str, /) -> Tuple[str, str]:
    return (code[0], code.upper())

identifier('foo')
identifier('bar')
```

```python
>>> identifiers
{'f': 'FOO', 'b': 'BAR'}
```