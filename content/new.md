title: __new__ và __init__
date: 2023-05-28
modified: 2023-05-28
tags: python, class,
category: news
slug: new
authors: Pymier0
description: lại một câu hỏi phỏng vấn chán ngắc

<center>
![new](https://images.unsplash.com/photo-1620924049153-4d32fcbe88fe?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&dl=nick-fewings-1SsUquHPNT8-unsplash.jpg&w=640)
Photo by <a href="https://unsplash.com/@jannerboy62?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Nick Fewings</a> on <a href="https://unsplash.com/photos/1SsUquHPNT8?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
</center>

### `__new__` và `__init__` khác gì?
Như đa phần các câu hỏi phỏng vấn nặng tính lý thuyết, ít ứng dụng thực tế hay trăm năm dùng 1 lần, đây không là ngoại lệ.

Các câu khác tương tự:

- decorator là gì (**CHƯA** bao giờ thấy ai hỏi generator dù generator dùng nhiều gấp decorator trăm lần).
- GIL là gì, thread với process khác gì nhau, nhược điểm của thread trong Python. (Không thực sự vô dụng, nhưng hiếm dùng với web-developer) Xem câu trả lời ở <https://docs.python.org/3/library/threading.html>

### Python `__init__`
`__init__` thì ai viết class cũng dùng, method `__init__` dùng để khởi tạo một object (class instance), ví dụ:

```py
class Cat():
    def __init__(self, name, age):
        print("Calling __init__")
        self.name = name
        self.age = age
```

### Python `__new__` có hay dùng không?
`__new__` rất ít khi thấy, vì rất ít được dùng. Thử tìm trong 3 web framework phổ biến nhất của Python: Django, Flask, FastAPI, thấy:

```py
$ grep -Rin 'def __new__' django
django/tests/model_forms/tests.py:3615:    def __new__(cls, name, bases, attrs):
django/django/utils/datastructures.py:233:    def __new__(cls, *args, warning="ImmutableList object is immutable.", **kwargs):
django/django/utils/deconstruct.py:15:        def __new__(cls, *args, **kwargs):
django/django/utils/deprecation.py:55:    def __new__(cls, name, bases, attrs):
django/django/test/selenium.py:23:    def __new__(cls, name, bases, attrs):
django/django/forms/widgets.py:216:    def __new__(mcs, name, bases, attrs):
django/django/forms/models.py:269:    def __new__(mcs, name, bases, attrs):
django/django/forms/forms.py:24:    def __new__(mcs, name, bases, attrs):
django/django/db/migrations/operations/base.py:36:    def __new__(cls, *args, **kwargs):
django/django/db/migrations/migration.py:231:    def __new__(cls, value, setting):
django/django/db/models/manager.py:21:    def __new__(cls, *args, **kwargs):
django/django/db/models/enums.py:12:    def __new__(metacls, classname, bases, classdict, **kwds):
django/django/db/models/base.py:95:    def __new__(cls, name, bases, attrs, **kwargs):
django/django/conf/__init__.py:41:    def __new__(self, value, setting_name):
$ grep -Rin 'def __new__' flask
$ grep -Rin 'def __new__' fastapi
$ grep -Rin 'def __new__' werkzeug
werkzeug/src/werkzeug/urls.py:71:    def __new__(cls, *args: t.Any, **kwargs: t.Any) -> BaseURL:
werkzeug/examples/cupoftee/application.py:49:        def __new__(metacls, name, this_bases, d):
```

Chỉ mình `django` có viết `__new__`, 2 framework còn lại không hề thấy, tìm thêm `werkzeug` (của Flask), thấy 1 ví dụ không quá hữu dụng (để hiện warning deprecate method) werkzeug/src/werkzeug/urls.py:

```py
def __new__(cls, *args: t.Any, **kwargs: t.Any) -> BaseURL:
    warnings.warn(
        f"'werkzeug.urls.{cls.__name__}' is deprecated and will be removed in"
        " Werkzeug 3.0. Use the 'urllib.parse' library instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return super().__new__(cls, *args, **kwargs)
```

> `__new__()` is intended mainly to allow subclasses of immutable types (like int, str, or tuple) to customize instance creation. It is also commonly overridden in custom metaclasses in order to customize class creation.

Django subclass str:

```py
# django/conf/__init__.py
class SettingsReference(str):
    """
    String subclass which references a current settings value. It's treated as
    the value in memory but serializes to a settings.NAME attribute reference.
    """

    def __new__(self, value, setting_name):
        return str.__new__(self, value)

    def __init__(self, value, setting_name):
        self.setting_name = setting_name
```

### Python `__new__` là gì
`__new__` là một staticmethod (là một trường hợp đặc biệt, nên không cần @staticmethod), dùng để tạo 1 instance của class (tạo object). Sau khi tạo ra object rồi, object gọi `__init__` để "initialize" (khởi tạo các giá trị).

```py
class Cat():
    def __new__(cls, *args, **kwarsg):
        print("Calling __new__")
        return super().__new__(cls)

    def __init__(self, name, age):
        print("Calling __init__")
        self.name = name
        self.age = age

c = Cat("Meo", 2)
```

```
Calling __new__
Calling __init__
```

> Because `__new__()` and `__init__()` work together in constructing objects (`__new__()` to create it, and `__init__()` to customize it), no non-None value may be returned by `__init__()`

`__new__` thực hiện việc tạo object, nên có thể đặt các logic đặc biệt về tạo object ở đây, ví dụ chỉ cho phép tạo N object, hay chỉ cho phép tạo 1 object duy nhất (còn gọi là singleton pattern). Ví dụ:

- <https://docs.python.org/3/faq/programming.html?highlight=__new__#how-can-a-subclass-control-what-data-is-stored-in-an-immutable-instance>
- <https://stackoverflow.com/a/8106977>
- <https://stackoverflow.com/a/8665179>

### Kết luận
- `__new__` là static method (thuộc về class), `__init__` là method (thuộc về instance/object)
- `__new__` gọi trước, `__init__` gọi sau
- `__new__` trả về instance của class, `__init__` trả về None
- `__init__` ở mọi nơi, `__new__` ít được dùng.

Code Flask hay FastAPI 5 năm, cũng không 1 lần viết `__new__`!

### Tham khảo
- <https://docs.python.org/3/reference/datamodel.html?highlight=__new__#object.__new__>

Hết.

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
