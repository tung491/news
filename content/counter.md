title: collections.Counter có phải là dict? 
date: 2023-07-14
modified: 2023-07-14
tags: python, dict, collections, counter, 
category: news
slug: counter
authors: Pymier0
description: người có phải là vượn? 

Lập trình viên Python xịn không bao giờ phải tự đếm số lần xuất hiện của mỗi phần tử, bởi có sẵn Counter:
## Python Counter là gì

```py
>>> from collections import Counter
>>> c = Counter("py py thon thon py".split())
>>> c
Counter({'py': 3, 'thon': 2})
>>> for k, v in c.items():
...     print(k, v)
... 
py 3
thon 2
```

Thay vì tự viết:

```py
>>> c = {}
>>> for w in "py py thon thon py".split():
...     if w not in c:
...         c[w] = 1
...     else:
...         c[w] += 1
... 
>>> c
{'py': 3, 'thon': 2}
```

## Counter có là dict?
Trước tiên, cần làm rõ, "là dict" có nghĩa là là gì? 

- Là kế thừa từ dict? (theo nghĩa của OOP)
- Là mọi method giống dict? và có thêm vài method khác

Dễ thấy, Counter kế thừa từ dict, nên 1 Counter, theo nghĩa của OOP, là 1 dict:

```py
class Counter(dict):
...

>>> c = collections.Counter()
>>> isinstance(c, dict)
True
```

Nếu một người tin vào **THUYẾT** tiến hóa, thì 1 người có phải 1 con vượn? hay 1 con bò sát? hay 1 con sinh vật đơn bào? Theo OOP thì là vậy.



### Kết luận

Hết.

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
