title: CPython list thực chất là 1 array
date: 2021-05-24
modified: 2021-05-24
tags: list, array, CPython, deque
category: features
slug: listarray
authors: Pymier0
description: gọi là list nhưng không phải linkedlist mà lại là array

![img](https://images.unsplash.com/photo-1586294839852-650d52bb6923?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2MjE4MjAwMTc&ixlib=rb-1.2.1&q=80&w=600)

Trong CPython (bản/implementation Python phổ biến nhất - tải tại python.org),
kiểu dữ liệu list thực chất là 1 array tương tự như array trong các ngôn ngữ
lập trình khác (C/Java...).
Nó không phải kiểu linked-list mà trong ngành khoa học máy tính thường hay
gọi là (linkedlist) list (xem link phần tham khảo).

Thư viện standard `deque` cung cấp kiểu dữ liệu `double-ended queue`, giống
với kiểu `double linked list`. Và thư viện `array` cung cấp kiểu dữ liệu...
array (như list với yêu cầu các phàn tử phải cùng kiểu).

`deque` có thể dùng để lấy 10 dòng cuối của 1 file rất đơn giản, dùng ít
bộ nhớ:

```py
def tail(filename, n=10):
    'Return the last n lines of a file'
    with open(filename) as f:
        return deque(f, n)
```

### Tham khảo
- https://docs.python.org/3/faq/design.html#how-are-lists-implemented-in-cpython
- https://docs.python.org/3/library/collections.html#collections.deque
- https://docs.python.org/3/library/array.html
- [https://www.geeksforgeeks.org/linked-list-vs-array/](https://www.geeksforgeeks.org/linked-list-vs-array/)

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
