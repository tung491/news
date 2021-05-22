title: dataclass trong Python3.7
date: 2021-05-22
modified: 2021-05-22
tags: features, dataclass
category: features
slug: dataclass
authors: Pymier0
description: viết class ngắn gọn hơn, đủ tiện để thay dict/tuple chứa dữ liệu.

![img](https://images.unsplash.com/flagged/photo-1587096472434-8b65b343980d?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2MjE2NTM1NTg&ixlib=rb-1.2.1&q=80&w=600)

Python3.7 trở đi có thêm 1 thư viện mới: `dataclasses`, thư viện này cho phép
tạo 1 data class (class với mục đích chính để biểu diễn/chứa dữ liệu,
thường không định nghĩa method)
với cú pháp ngắn gọn, kết hợp với cú pháp type annotation:

```py
import dataclasses as dc
from typing import List


@dc.dataclass
class User:
    name: str
    languages: List[str]
    age: int = 20


p1 = User("Pymier1", ["Python", "SQL"])
print(p1)
```

output

```sh
User(name='Pymier1', languages=['Python', 'SQL'], age=20)
```

Chú ý: từ Python3.9 trở đi, có thể viết `list[str]` mà không cần import typing.

code này tương đương với code sau ở Python các bản trước 3.7:

```py
class User:
    def __init__(self, name, languages, age=20):
        self.name = name
        self.languages = languages
        self.age = age

    def __str__(self):
        return f"User(name='{self.name}', languages={self.languages}, age={self.age})"

    # ... và nhiều nữa https://stackoverflow.com/a/47955313/807703
p1 = User("Pymier1", ["Python", "Vietnames"])
print(p1)
```

Để biến 1 dataclass thành dict, chỉ cần dùng function `asdict`:

```py
... print(dc.asdict(p1))
{'name': 'Pymier1', 'languages': ['Python', 'Vietnames'], 'age': 20}
```

Để class trở nên "immutable", gọi dataclass với argument `frozen=True`
https://docs.python.org/3.8/library/dataclasses.html#frozen-instances

dataclass thích hợp để thay cho namedtuple, tuple hay các class chỉ để chứa
dữ liệu, hay dictionary hoạt động như 1 container chứa dữ liệu.

### Tham khảo:
- https://www.python.org/dev/peps/pep-0557/#why-not-just-use-namedtuple

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
