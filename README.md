# registrate
Register your data

## Usage:

### `Record`

#### Example: Basic Data Registration

##### Implementation
```python
import registry

data = registry.Record()

data(1)
data('foo')
data(print)
```

##### Usage
```python
>>> data
[1, 'foo', <built-in function print>]
>>>
```

#### Example: Simple Decorator Registration

##### Implementation
```python
import registry

classes = registry.Record()

@classes
class Foo: pass

@classes
class Bar: pass
```

##### Usage
```python
>>> classes
[<class '__main__.Foo'>, <class '__main__.Bar'>]
>>>
```

#### Example: Hooked Registration

##### Implementation
```python
import registry

square_numbers = registry.Record(lambda n: n ** 2)

square_numbers(1)
square_numbers(2)
square_numbers(3)
```

##### Usage
```python
>>> square_numbers
[1, 4, 9]
>>>
```

### `Register`

#### Example: Basic Contextual Registration

##### Implementation
```python
import registry

functions = registry.Register()

@functions(author = 'Sam')
def foo(): ...

@functions(author = 'Robbie')
def bar(): ...
```

##### Usage
```python
>>> functions
{<function foo at 0x7fa9110a50d0>: Context(author='Sam'), <function bar at 0x7fa9110a5160>: Context(author='Robbie')}
>>>
```

#### Example: Hooked Registration

##### Implementation
```python
import registry
import dataclasses

@dataclasses.dataclass
class Route:
    path: str
    method: str = 'GET'

routes = registry.Register(Route)

@routes('/user', method = 'POST')
def create_user(name: str) -> str:
    return f'Created user: {name!r}'
```

##### Usage
```python
>>> routes
{<function create_user at 0x7f2f9d775ee0>: Route(path='/user', method='POST')}
>>>
```
