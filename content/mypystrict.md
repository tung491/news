title: mypy là chưa đủ, cần phải nghiêm khắc hơn
date: 2022-09-17
modified: 2022-09-17
tags: bug, fixbug, mypy, type
category: news
slug: mypystrict
authors: Pymier0
description: chỉ mypy thì không cứu được, dù là type

![img](https://images.unsplash.com/photo-1663312314645-555d6bb36435?ixlib=rb-1.2.1&dl=single-earth-AxkQNRFzIow-unsplash.jpg&w=640&q=80&fm=jpg&crop=entropy&cs=tinysrgb)

[mypy](https://pp.pymi.vn/article/mypy/) là công cụ không thể thiếu khi code Python ở thập niên thứ 2 thế kỷ 21.
[mypy](https://pp.pymi.vn/article/mypy/) giúp phát hiện hàng loạt lỗi liên quan đến type, mang tới sức mạnh của static typing language tới Python. Nhưng đôi khi, là chưa đủ.

Thử sức xem bạn có phát hiện ra lỗi trong đoạn code này? Tác giả muốn bật DEBUG (django) khi dev trên MacOS:

```py
import platform

if platform.system == "Darwin":
    DEBUG = True

if platform.system + "Darwin":
    DEBUG = True
```

mypy phát hiện ra lỗi khi thực hiện phép `+` ở câu `if` thứ hai

```sh
$ mypy testtype.py
testtype.py:6: error: Unsupported left operand type for + ("Callable[[], str]")
Found 1 error in 1 file (checked 1 source file)
```

nhưng không phát hiện ra vấn đề ở câu `if` thứ nhất, vì đó là việc làm hoàn toàn hợp lệ trong Python: so sánh hai giá trị khác kiểu.
Tác giả viết thiếu dấu `()`, code sau khi cào đầu bứt tóc:

```py
import platform

if platform.system() == "Darwin":
    DEBUG = True
```

Thực chất, mypy cũng có thể phát hiện ra vấn đề này, nhưng phải thêm option strict:

```sh
$ mypy --strict testtype.py
testtype.py:3: error: Non-overlapping equality check (left operand type: "Callable[[], str]", right operand type: "Literal['Darwin']")
testtype.py:6: error: Unsupported left operand type for + ("Callable[[], str]")
Found 2 errors in 1 file (checked 1 source file)
```

### Kết luận
Bật --strict lên.


Bài viết thực hiện với

```sh
$ python3 --version
Python 3.8.10

$ mypy --version
mypy 0.942
```

Hết.

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
