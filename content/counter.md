title: collections.Counter có phải là dict?
date: 2023-07-14
modified: 2023-07-14
tags: python, dict, collections, counter,
category: news
slug: counter
authors: Pymier0
description: người có phải là vượn?

Lập trình viên Python không bao giờ phải tự đếm số lần xuất hiện của mỗi phần tử, bởi có sẵn Counter:

### Python Counter là gì

```py
from collections import Counter
c = Counter("py py thon thon py".split())
print(c)
# Counter({'py': 3, 'thon': 2})
for k, v in c.items():
    print(k, v)
# py 3
# thon 2
```

Thay vì tự viết:

```py
d = {}
for w in "py py thon thon py".split():
    if w not in d:
        d[w] = 1
    else:
        d[w] += 1

print(d)
# {'py': 3, 'thon': 2}
```

### Counter có phải là dict?
Trước tiên, cần làm rõ, "là dict" có nghĩa là gì?

- Là kế thừa từ dict?
- Là mọi method giống dict? và có thêm vài method khác

Dễ thấy, Counter kế thừa từ dict, nên 1 Counter, theo nghĩa của lập trình hướng đối tượng - OOP, là 1 dict:

```py
class Counter(dict):
...

>>> c = collections.Counter()
>>> isinstance(c, dict)
True
```

Nếu một người tin vào **THUYẾT** tiến hóa, thì 1 người có phải 1 con vượn? hay 1 con bò sát? hay 1 con sinh vật đơn bào? Theo OOP thì là vậy.

Đó là lỗ hổng trong cách tư duy OOP, những ngôn ngữ lập trình mới ngày nay không theo lối suy nghĩ này, mà dựa trên khả năng của 1 object để xét nó là gì như Go interface hay Rust trait: một object là `Writer` nếu nó có thể `write`, là `Reader` nếu nó có thể `read`.

Quay trờ lại câu trả lời: Counter là 1 dict, câu trả lời này có tác dụng gì? có thể dùng Counter như dict mà không có khác biệt gì?
Đôi khi không phải:

dict

```py
print(d['py'])
# 3
print(d.get('secret'))
# None
print(d['secret'])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'secret'
```

Counter thì khác

```py
print(c['py'])
# 3
print(c.get('recret'))
# None
print(c['secret'])
# 0
```

Truy cập 1 key không tồn tại trong Counter trả về 0, [method `__missing__`](https://docs.python.org/3.10/reference/datamodel.html?highlight=__missing__#object.__missing__) quyết định điều này:

```py
object.__missing__(self, key)

    Called by dict.__getitem__() to implement self[key] for dict subclasses
    when key is not in the dictionary.
```

Code Counter <https://github.com/python/cpython/blob/v3.11.0/Lib/collections/__init__.py#L599C1-L602C17>:
```py
def __missing__(self, key):
    'The count of elements not in the Counter is zero.'
    # Needed so that self[missing_item] does not raise KeyError
    return 0
```

Giờ thì cách hoạt động của Counter đã khác hoàn toàn dict, vậy counter có phải dict?

### Kết luận
Nói đúng cũng phải, nói không đúng cũng phải, chủ yếu là người nghe muốn nghe cái gì.

Hết.

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
