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
```python
>>> import register
>>>
>>> routes = register.Register()
>>>
>>> @routes('/user', method = 'POST')
>>> def create_user(name: str):
        return f'Created user: {name!r}'
>>>
>>> routes
Register([(<function create_user at 0x7f579ea07ca0>, State(args=('/user',), kwargs={'method': 'POST'}))])
>>>
```

### `HookedRegister`
```python
>>> import register
>>> import dataclasses
>>>
>>> @dataclasses.dataclass
>>> class Route:
        path: str
        method: str = 'GET'
>>>
>>> routes = register.HookedRegister(Route)
>>>
>>> @routes('/user', method = 'POST')
>>> def create_user(name: str):
        return f'Created user: {name!r}'
>>>
>>> routes
HookedRegister([(<function create_user at 0x7f3401c34b80>, Route(path='/user', method='POST'))])
>>> 
```
