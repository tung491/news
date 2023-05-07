title: Bất ngờ với __builtins__
date: 2023-05-07 11:00:01
modified: 2023-05-07 11:00:01
tags: python, __builtins__
category: news
slug: builtins
authors: Pymier0
description: print, len, min, max, từ đâu mà ra?

Python có vài chục function có sẵn, liệt kê tại <https://docs.python.org/3/library/functions.html>, bật lệnh `python3` lên gõ là có:

```py
$ python3
Python 3.10.10 (main, Mar  5 2023, 22:26:53) [GCC 12.2.1 20230201] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print(len([1,3,2]))
3
```

Định nghĩa 1 function rồi gọi `globals` để liệt kê tất cả các "tên" có thể truy cập được:

```py
>>> def double(x):
...     return x*2
...
>>> n = 42
>>> globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'double': <function double at 0x7f729f6065f0>, 'n': 42}
>>> help(globals)
globals()
    Return the dictionary containing the current scope's global variables.

    NOTE: Updates to this dictionary *will* affect name lookups in the current
    global scope and vice-versa.
```

Python interpreter interative mode có hỗ trợ "autocomplete", gõ `__` rồi bấm phím Tab, thấy:

```py
>>> __
__annotations__   __doc__           __name__
__build_class__(  __import__(       __package__
__debug__         __loader__()      __spec__
```

Thấy có chút khác biệt: autocomplete không hiện `__builtins__`, còn `globals()` lại không có `__debug__` và `__import__`, `__build_class__`.

### `__import__`

```py
__import__(...)
    __import__(name, globals=None, locals=None, fromlist=(), level=0) -> module

    Import a module. Because this function is meant for use by the Python
    interpreter and not for general use, it is better to use
    importlib.import_module() to programmatically import a module.
    ...
```

Function `__import__` thực hiện import khi gõ `import lib`.

### `__builtins__`
`__builtins__`  là module `builtins`

```py
>>> import builtins
>>> builtins.print(builtins.len([3,2,1]))
3
>>> help(__builtins__)
Help on built-in module builtins:

NAME
    builtins - Built-in functions, exceptions, and other objects.
    ...
```

nơi chứa các builtin functions như print, len, ...

```py
>>> [i for i in dir(__builtins__) if not i.startswith("__") and i.islower()]
['abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
```

Trong [tài liệu](https://docs.python.org/3/reference/executionmodel.html?highlight=__builtins__#builtins-and-restricted-execution) viết

> CPython implementation detail: Users should not touch __builtins__; it is strictly an implementation detail. Users wanting to override values in the builtins namespace should import the builtins module and modify its attributes appropriately.


**should not** không có nghĩa là **cannot**, thử gán cho `__builtins__` một module khác:

```py
>>> import os
>>> __builtins__ = os
>>> getcwd()
'/home/hvn'
>>> globals()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'globals' is not defined
>>> print
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'print' is not defined
```

các builtin function như print hay globals không còn nữa, thay vào đó là các funtion trong module `os`.

Bất ngờ chưa?!

### Kết luận
Python vẫn luôn có những bí mật rất không muốn bật mí.

Hết.

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
