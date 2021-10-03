# register
Python object registers. Keep track of your classes, functions and data.

## Usage:

### `FlatRegister`

#### Example: Basic Data Registration

##### Implementation
```python
import register

datas = register.FlatRegister()

datas(1)
datas('foo')
datas(print)
```

##### Usage
```python
>>> datas
[1, 'foo', <built-in function print>]
>>>
```

#### Example: Simple Class Register

##### Implementation
```python
import register

classes = register.FlatRegister()

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
import register

square_numbers = register.FlatRegister(lambda n: n ** 2)

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

#### Example: Basic Stateful Registration

##### Implementation
```python
import register

functions = register.Register()

@functions(author = 'Sam')
def foo(): ...

@functions(author = 'Robbie')
def bar(): ...
```

##### Usage
```python
>>> functions
{<function foo at 0x7fa9110a50d0>: State(args=(), kwargs={'author': 'Sam'}), <function bar at 0x7fa9110a5160>: State(args=(), kwargs={'author': 'Robbie'})}
>>>
```

#### Example: Hooked Registration

##### Implementation
```python
import register
import dataclasses

@dataclasses.dataclass
class Route:
    path: str
    method: str = 'GET'

routes = register.Register(Route)

@routes('/user', method = 'POST')
def create_user(name: str) -> str:
    return f'Created user: {name!r}'
```

##### Usage
```python
>>> routes
{<function create_user at 0x7f2f9d775ee0>: Route(path='/user', method='POST')}
>>>
>>> routes[create_user].path
'/user'
```

### `InverseRegister`

#### Example: Basic Inverse Registration

##### Implementation
```python
import register

numbers = register.InverseRegister()

numbers('one')(1)
numbers('two')(2)
```

##### Usage
```python
>>> numbers
{'one': 1, 'two': 2}
>>>
```

#### Example: Basic Inverse Class Registration

##### Implementation
```python
import register

browsers = register.InverseRegister()

@browsers('google-chrome')
class GoogleChrome:
    pass
```

##### Usage
```python
>>> browsers
{'google-chrome': <class '__main__.GoogleChrome'>}
>>>
```
