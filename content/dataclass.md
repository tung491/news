title: Lộ mật khẩu cùng dataclass
date: 2023-08-30
modified: 2023-08-30
tags: python, dataclass, security, str, repr
category: news
slug: dataclass-leak
authors: Pymier0
description: mới, xịn, tiện, lợi, hại

`dataclasses` module là 1 standard library rất mới, xuất hiện ở Python 3.7, với tác dụng:

> This module provides a decorator and functions for automatically adding generated special methods such as `__init__()` and `__repr__()` to user-defined classes.

<https://peps.python.org/pep-0557/>

đây là một tính năng được yêu thích ở các bản Python mới (3.7+).

### dataclass giúp viết class ngắn hơn, không phải tự gõ `__init__`
`dataclass` là một decorator, dùng trên đầu class:

```py
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    email: str

u = User("Pymier", 8, "hvn@pymi.vn")
print(u)
# User(name='Pymier', age=8, email='hvn@pymi.vn')
```

Tiện vậy có gì mà không tốt?
### dataclass luôn in ra mọi attribute
Mặc định, khi print một object tạo bởi class dùng dataclass, nó sẽ in ra mọi attribute.
Giả sử một ngày, cần chứa mật khẩu trong class User, đoạn code trở thành:

```py
@dataclass
class User:
    name: str
    age: int
    email: str
    password: str

u = User("Pymier", 8, "hvn@pymi.vn", "hunter42")
print(u)
# User(name='Pymier', age=8, email='hvn@pymi.vn', password='hunter42')
```

Vậy là nhờ dùng dataclass, ta VÔ TÌNH để lộ mật khẩu, in ra màn hình, render ra website hay theo log file lộ ra ngoài...

#### Sửa lại thế nào?
muốn print object ra gì, rõ là phải sửa `__str__`!, thêm method `__str__` vào

```py
    ...
    def __str__(self) -> str:
        return f"{self.name=} {self.age=} {self.email=}"

u = User("Pymier", 8, "hvn@pymi.vn", "hunter42")
print(u)
# self.name='Pymier' self.age=8 self.email='hvn@pymi.vn'
```
Kết quả giờ không còn hiện ra password nữa, ta lặng lẽ ỉm đi cái security bug này và không ai biết tới, thật tuyệt vời!

Xong chưa? nên dừng lại 1 chút suy nghĩ rồi hãy đọc tiếp.

Đoạn code ban đầu hoàn hảo, được thiết kế chủ ý dùng dataclass vì có thể in ra mọi thông tin, thì sau 1 thay đổi "nhỏ" và thường là do 1 người khác thay đổi, trở thành code có lỗ hổng bảo mật (security vulnerability).
Người ta thường so sánh ngành lập trình với ngành xây dựng, software thì toàn bug còn nhà thì mấy khi "hỏng"? software bị thay đổi hàng ngày, còn nhà thì vài năm hay thập kỷ mới thay.

### Tạo 1 class mới chứa dataclass này
Tạo 1 team class dùng dataclass, và in ra:

```py
@dataclass
class Team:
    members: list[User]

t = Team(members=[u])
print(t)
# Team(members=[User(name='Pymier', age=8, email='hvn@pymi.vn', password='hunter42')])
```
dù ta đã viết `__str__` cho `User`, nhưng khi in ra `Team` object, nó sử dụng `__repr__` chứ không dùng `__str__`, như dòng đầu tiên trong tài liệu của `dataclasses` đã viết:

>  automatically adding generated special methods such as `__init__()` **and** `__repr__()` to user-defined classes

Cách fix: thêm `__repr__`:

> If a class defines `__repr__()` but not `__str__()`, then `__repr__()` is also used when an “informal” string representation of instances of that class is required.

```py
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    email: str
    password: str
    def __repr__(self) -> str:
        return f"{self.name=} {self.age=} {self.email=}"

u = User("Pymier", 8, "hvn@pymi.vn", "hunter42")
print(u)
# self.name='Pymier' self.age=8 self.email='hvn@pymi.vn'
@dataclass
class Team:
    members: list[User]

t = Team(members=[u])
print(t)
# Team(members=[self.name='Pymier' self.age=8 self.email='hvn@pymi.vn'])
```

Bạn đọc tham khảo sự khác biệt giữa `__str__` và `__repr__`: <https://stackoverflow.com/questions/1436703/what-is-the-difference-between-str-and-repr>

Bất ngờ thay, mấy ông già không "cool" không "trend" không dùng `dataclass` không gặp phải vấn đề này:

```py
from dataclasses import dataclass

class User:
    def __init__(self, name: str, age: int, email: str, password: str):
        self.name = name
        self.age = age
        self.email = email
        self.password = password

u = User("Pymier", 8, "hvn@pymi.vn", "hunter42")
print(u, repr(u))
# <__main__.User object at 0x7f9efd510410> <__main__.User object at 0x7f9efd510410>
```

Update: dataclasses cũng đã tính đến chuyện này, để KHÔNG hiện một attribute khi `__repr__`, dùng `field(repr=False)`

```py
from dataclasses import dataclass, field

@dataclass
class User:
    name: str
    age: int
    email: str
    password: str = field(repr=False)
u = User("Pymier", 8, "hvn@pymi.vn", "hunter42")
print(u)
# User(name='Pymier', age=8, email='hvn@pymi.vn')
```

### Tham khảo
<https://docs.python.org/3.11/library/dataclasses.html>

Xem list các method được dataclass autogenerate tại <https://peps.python.org/pep-0557/#abstract>

### Kết luận
`dataclasses` tiện lợi, giúp viết ít code hơn, nhưng cần biết những gì nó "tự động" để tránh bất ngờ.
Default không có nghĩa là không biết. Explicit is better than implicit.

Hết.

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
