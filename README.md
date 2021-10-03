# register
Python function registers

## Usage:

### `FlatRegister`
```python
>>> import register
>>>
>>> classes = register.FlatRegister()
>>>
>>> @classes
>>> class Foo: pass
>>>
>>> classes
[<class '__main__.Foo'>]
>>>
```

### `Register`

#### Example: Basic State

##### Implementation
```python
import register

routes = register.Register()

@routes('/user', method = 'POST')
def create_user(name: str): -> str
    return f'Created user: {name!r}'
```

##### Usage
```python
>>> routes
Register([(<function create_user at 0x7f579ea07ca0>, State(args=('/user',), kwargs={'method': 'POST'}))])
>>>
>>> routes[create_user]['kwargs']
{'method': 'POST'}
>>>
```

#### Example: Data Class

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

#### Implementation
```python
import register

browsers = register.InverseRegister()

@browsers('google-chrome')
class GoogleChrome:
    pass
```

#### Usage
```python
>>> browsers
{'google-chrome': <class '__main__.GoogleChrome'>}
>>>
```
