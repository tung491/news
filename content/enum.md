title: Enum trong Python
date: 2021-06-10
modified: 2021-06-10
tags: features, stdlib
category: news
slug: enum
authors: Pymier0
description: biểu diễn 1 nhóm các giá trị rời rạc - như size xs s m l xl xxl

Khái niệm Enum có trong hầu hết các ngôn ngữ static typing nhưng mãi đến 3.4
mới xuất hiện trong Python standard lib [enum](https://docs.python.org/3/library/enum.html).
Tức Python developers đã nghĩ ra cách để không phải dùng
enum cũng chẳng sao... nhưng có thì tốt.

![img](https://images.unsplash.com/photo-1575846008827-b0167ab20bb9?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2MjMyNDkyNTI&ixlib=rb-1.2.1&q=80&w=600)

## Enum để làm gì?
Enum là viết tắt của enumeration (tránh nhầm với function enumerate).
Enum là một bộ hữu hạn các tên ứng với các giá trị cố định.
Ví dụ
- kích thước áo chỉ có trong 1 tập giới hạn các giá trị XXS XS S M L XL XXL
- điểm số tây chỉ nằm trong tập A B C D E F
- các ngày trong tuần chỉ có từ thứ 2 đến chủ nhật
- các lá bài chỉ có 4 chất dô cơ tép bích :))))) (Diamond Heart Club Spade)

Làm thế nào để biểu diễn 4 chất này lên Python?

Cách 1: dùng string 'D', 'H', 'C', 'S'

Nhược điểm: không so sánh được nếu ta có luật Spade < Club < Diamond < Heart,
lập trình viên cũng có thể gõ nhầm chữ P và để lại lỗi chỉ phát hiện ra lúc
chạy.

Cách 2: đặt tên theo kiểu CONSTANT gán giá trị số - cách này phổ biến ở các
ngôn ngữ không có Enum.

```py
SPADE = 1
CLUB = 2
DIAMOND = 3
HEART = 4
ALL_SUITS = (SPADE, CLUB, DIAMOND, HEART)
```

Nhược điểm: người dùng có thể đưa nhầm số khác vào và vẫn chạy, do bản chất
đây là các số. Không lấy được tập giá trị, hoặc phải tự tạo 1 list.

Và Enum đến giải cứu, để tạo 1 enum, kế thừa nó từ class Enum, ví dụ game 1 cây:

```py
import random
from typing import List, Tuple
from enum import IntEnum, auto


class Suit(IntEnum):
    SPADE = auto()
    CLUB = auto()
    DIAMOND = auto()
    HEART = auto()


for s in Suit:
    print(s, s.name, s.value)

assert Suit.SPADE < Suit.HEART


def create_cards() -> List[Tuple[int, Suit]]:
    return [(i, s) for i in range(1, 13) for s in Suit]


def play_1_cay(n: int, s: Suit):
    r = random.choice(create_cards())
    print("LeMe: {} vs No: {}: {}".format((n, s), r, (n, s) >= r))


play_1_cay(8, Suit.CLUB)
play_1_cay(8, 5)
```

[Link glot.io](https://glot.io/snippets/fze7cclp5r)

Output:

```py
Suit.SPADE SPADE 1
Suit.CLUB CLUB 2
Suit.DIAMOND DIAMOND 3
Suit.HEART HEART 4
LeMe: (8, <Suit.CLUB: 2>) vs No: (5, <Suit.DIAMOND: 3>): True
LeMe: (8, 5) vs No: (12, <Suit.HEART: 4>): False
```

[mypy](https://pp.pymi.vn/article/mypy/) sẽ báo: ở dòng gọi `play_1_cay(8, 5)`
```
enumtest.py:24: error: Argument 2 to "play_1_cay" has incompatible type "int"; expected "Suit"
```

`auto()` tự sinh số tăng dần.

Happy enum.

## Tham khảo
- https://docs.python.org/3/library/enum.html

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
