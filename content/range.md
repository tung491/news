title: Kỳ diệu range
date: 2021-07-09
modified: 2021-07-09
tags: range, generator,
category: news
slug: range
authors: Pymier0
description: built-in function đầy magic và không phải là generator

Bất kỳ ai học Python cũng đều biết đến range, function giúp tạo 1 list các
số nguyên:

```py
range(1, 100)
```

![img](https://images.unsplash.com/photo-1550031675-d8ce0062caf7?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2MjU3OTU0MzY&ixlib=rb-1.2.1&q=80&w=600)

`range` có trong Python từ rất lâu rồi, thời Python2, `range` có kèm 1 người
anh em song sinh tên gọi `xrange`. `xrange` này chính là `range` ở Python3.
Khác gì nhau?

- range (cũ) sẽ tạo ra 1 list
- xrange hay range python3 sẽ tạo ra... 1 range

```py
>>> range(1, 100)
range(1, 100)
>>> type(range(1, 100))
<class 'range'>
```

Vậy nên trong Python3, khi muốn tạo list, phải gõ `list(range(1, 100)`.
Tại sao?

Nếu dùng `range` Python2, sẽ khó mà tạo được list chứa 1 tỷ phần tử (do máy sẽ
hết RAM), nhưng `range` Python3 thì tạo cái gì cũng được, và nó chỉ trả
về phần tử khi yêu cầu - đây là ý tưởng chính của ["generator"](https://pp.pymi.vn/article/tuple_comps/).

Nhưng range không phải generator, range là kiểu range, vì nó còn đặc biệt hơn.
Một [generator](https://pp.pymi.vn/article/tuple_comps/) không có len, range thì có:

```py3
>>> len(range(2, 1_000_000_000, 3))
333333333
>>> def gen():
...     yield 1
...
>>> len(gen())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'generator' has no len()
```

## Hết

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
