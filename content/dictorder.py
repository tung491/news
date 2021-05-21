title: Từ Python3.7 trở đi, các key trong dict có thứ tự
date: 2021-05-21
modified: 2021-05-21
tags: dictorder
category: features, tip, dict
slug: dictorder
authors: Pymier0
description: dict key không phải không có thứ tự (unordered) như trước

![img](https://images.unsplash.com/photo-1577303600246-c694ab6ad8a1?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2MjE1NjIwMjc&ixlib=rb-1.2.1&q=80&w=600)

Các key sẽ theo thứ tự chúng được thêm vào dict.

```py
In [1]: for i in {1:None, 3: None, 20: None, 2: None}:
   ...:     print(i)
   ...:
1
3
20
2
```

khác với trước kia, các key không có thứ tự (khác với ngẫu nhiên - ngẫu nhiên
là mỗi lần chạy qua key dict ra 1 kết quả khác nhau, còn ở đây là luôn
giống nhau trong 1 lần chạy code).

```py
$ python2
Python 2.7.18 (default, Mar  8 2021, 13:02:45)
[GCC 9.3.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> for i in {1:None, 3:None, 20:None, 2:None}:
...     print(i)
...
1
2
3
20
>>> for i in {1:None, 3:None, 20:None, 2:None}:
...     print(i)
...
1
2
3
20
```

### Tham khảo
- https://docs.python.org/3/whatsnew/3.7.html
- https://mail.python.org/pipermail/python-dev/2017-December/151283.html

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
