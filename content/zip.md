title: zip ngắn, zip dài
date: 2023-04-28
modified: 2023-04-28
tags: python, zip, itertools
category: news
slug: zip
authors: Pymier0
description: zip ngắn thì dễ zip dài thì sao?

zip (cái khóa kéo) là một function built-in sẵn trong Python, để có được vị trí này - ngang ngửa với len, và print, zip rõ ràng là rất quan trọng.

![zip](https://pixabay.com/get/g5abfdeab5cb385898885ff39db03f6f20df8e2d03a4a4933afe9f19c5c9f47be5a862afdf0e0d00fabfd1c45ce36e3c50828f18dcf0a85119e934044fc0a3309d42d89f1271d4219b3261ed73ed55ef2_640.jpg)

## zip - builtin function

```
Init signature: zip(self, /, *args, **kwargs)
Docstring:
zip(*iterables) --> A zip object yielding tuples until an input is exhausted.

   >>> list(zip('abcdefg', range(3), range(4)))
   [('a', 0, 0), ('b', 1, 1), ('c', 2, 2)]

The zip object yields n-length tuples, where n is the number of iterables
passed as positional arguments to zip().  The i-th element in every tuple
comes from the i-th iterable argument to zip().  This continues until the
shortest argument is exhausted.
```

zip nhận vào 2 hay nhiều iterable (như list, string ...) và trả về lần lượt tuple chứa các phần tử thứ i của tất cả iterable.

Ví dụ:

```py
In [3]: list(zip([1,2,3], "Python"))
Out[3]: [(1, 'P'), (2, 'y'), (3, 't')]
```

`zip` dừng lại khi iterable ngắn nhất kết thúc.

Vậy làm sao tiếp tục với iterable dài, và gán giá trị mặc định cho các iterable ngắn hơn?


### itertools.zip_longest

Thư viện có sẵn `itertools` cung cấp thêm nhiều công cụ để "iterate",
với function zip_longest, thay vì dừng lại ở iterable ngắn nhất, nó chạy tới khi iterable dài nhất kết thúc:

```py
In [4]: import itertools

In [6]: list(itertools.zip_longest([1,2,3], "Python"))
Out[6]: [(1, 'P'), (2, 'y'), (3, 't'), (None, 'h'), (None, 'o'), (None, 'n')]
```

mặc định điền các phần tử thiếu của iterable ngắn là `None`.

Giá trị mặc định này có thể thay đổi bằng fillvalue:

```py
In [9]: list(itertools.zip_longest([1,2,3], "Python", fillvalue=0))
Out[9]: [(1, 'P'), (2, 'y'), (3, 't'), (0, 'h'), (0, 'o'), (0, 'n')]
```


### Kết luận
Python hàng xịn, zip ngắn zip dài có đủ cả hai.

Hết.

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
