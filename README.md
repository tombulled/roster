# roster
Python object registers. Keep track of your classes, functions and data.

## Installation
```console
pip install roster
```

## Usage:

### `Record`

#### Example: Standard Record
```python
import roster

numbers = roster.Record()

numbers(1)
numbers(2)
numbers(3)
```

```python
>>> numbers
[1, 2, 3]
```

#### Example: Hooked Record
```python
import roster

square_numbers = roster.Record(hook=lambda n: n ** 2)

square_numbers(1)
square_numbers(2)
square_numbers(3)
```

```python
>>> square_numbers
[1, 4, 9]
```

#### Example: Decorator
```python
import roster

classes = roster.Record()

@classes
class Foo: pass

@classes
class Bar: pass
```

##### Usage
```python
>>> classes
[<class '__main__.Foo'>, <class '__main__.Bar'>]
```

### `Register`

#### Example: Standard Register
```python
import roster

functions = roster.Register()

@functions(author = 'Sam')
def foo(): ...

@functions(author = 'Robbie')
def bar(): ...
```

```python
>>> functions
{
    <function foo at 0x7fa9110a50d0>: Context(author='Sam'),
    <function bar at 0x7fa9110a5160>: Context(author='Robbie')
}
```

#### Example: Hooked Register
```python
import roster
import dataclasses

@dataclasses.dataclass
class Route:
    path: str
    method: str = 'GET'

routes = roster.Register(hook=Route)

@routes('/user', method = 'POST')
def create_user(name: str) -> str:
    return f'Created user: {name!r}'
```

```python
>>> routes
{<function create_user at 0x7f2f9d775ee0>: Route(path='/user', method='POST')}
```
