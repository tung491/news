title: Vì sao không chương trình nào phát hiện ra lỗi này?
date: 2021-06-06
modified: 2021-06-06
tags: features, quiz
category: news
slug: latebinding
authors: Pymier0
description: một lỗi rất hiển nhiên khi nhìn bằng mắt nhưng flake8, mypy, hay PyCharm đều không phát hiện ra

```py
def n_pymi_vn():
    s = x + 1
    return s


r = n_pymi_vn()
x = 10
print(r)
```

Đoạn code này có bug gì? tại sao các tool không phát hiện ra?
và nên sửa thế nào để các tool có thể phát hiện ra?

Xóa 3 dòng cuối đi, flake8 hay mypy sẽ phát hiện ra bug:

```py
def n_pymi_vn() -> int:
    s = x + 1
    return s

$ flake8 main.py
main.py:2:9: F821 undefined name 'x'
$ mypy main.py
main.py:2: error: Name 'x' is not defined
Found 1 error in 1 file (checked 1 source file)
```

Chú ý câu hỏi về việc phát hiện ra bug này **trước** khi chạy code.

Việc định nghĩa x = 10 sau `def n_pymi_vn` hoàn toàn không phải bug, đoạn code
sau chạy OK, không có bug:

```python
def n_pymi_vn():
    s = x + 1
    return s


x = 10
r = n_pymi_vn()
print(r)
```

https://glot.io/snippets/fzafpx0nqu

![img](https://images.unsplash.com/photo-1571030905044-7458c2a7ac24?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2MjI5NTM3NTI&ixlib=rb-1.2.1&q=80&w=600)

Câu trả lời sẽ được tiết lộ vào bài viết sau.

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.