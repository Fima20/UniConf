A simple shell allows you to quickly save and then load settings or any other project data, based on the "configparser" module. Allows you to save variable types and also supports "datetime".

## Examples

Import:

```python
>>> import uniconf
```

Create an instance:

```python
>>> config = uniconf.Config()
```

Review:

```python
>>> config.struct()
[info]
name:{str}
number:{int}
```

Сreate and edit:

```python
>>> a = 123
>>> config.set("info_2", "number", a)
>>> config.struct()
[info]
name:{str}
number:{int}
[info_2]
number:{int}
```

Get:

```python
>>> config.get("info_2", "number")
123
>>> config("info_2", "number")
123
>>> type(config("info_2", "number"))
<class 'int'>
```

Delete:

```python
>>> config.delete("info", "name")
>>> config.struct()
[info]
number:{int}
[info_2]
number:{int}
```

