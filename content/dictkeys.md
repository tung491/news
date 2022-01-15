title: k in dict.keys() chậm hơn k in dict bao nhiêu?
date: 2022-01-15
modified: 2022-01-15
tags: dict, set, speed, big O
category: news
slug: dictkey
authors: Pymier0
description: dict.keys() không trả về 1 list

![img](https://images.unsplash.com/photo-1517331237869-8c4ed7fadcb4?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2NDIyMjQ5ODg&ixlib=rb-1.2.1&q=80&w=600)

Python2, khi gọi dict.keys() sẽ trả về 1 list các key của dict. Một cải tiến
lớn của Python3 là không trả về list mà trả về những thứ tương tự
[generator](https://pp.pymi.vn/article/tuple_comps/) để tiết kiệm bộ nhớ.

```py
In [32]: type({}.keys())
Out[32]: dict_keys

In [33]: type({}.items())
Out[33]: dict_items

In [34]: type({}.values())
Out[34]: dict_values
```

Khi nhìn `k in dict`, đó là phép toán có độ phức tạp O(1), nhanh tức thì, thì
có thể đoán `k in dict.keys()` sẽ tìm k trong 1 generator iterator (hay nôm na
là 1 list), sẽ rất chậm. Dùng timeit để thử:

```py
# import timeit

In [38]: timeit.timeit('-1 in d', setup='d = {i:i for i in range(30_000_000)}', number=1)
Out[38]: 2.053999196505174e-06

In [39]: timeit.timeit('-1 in d.keys()', setup='d = {i:i for i in range(30_000_000)}', number=1)
Out[39]: 5.510002665687352e-06
```

Thấy `k in d.keys()` chậm bằng nửa `k in d`, đúng là chậm hơn, nhưng chỉ 1 nửa.
Trong khi nếu là list, thì tìm kiếm phải [chậm hơn dict hàng nghìn
lần](https://n.pymi.vn/dictvslist.html).

Sự chênh lệch này hóa ra do gọi `d.keys()`

```py
In [40]: timeit.timeit('d.keys()', setup='d = {i:i for i in range(30_000_000)}', number=1)
Out[40]: 2.93600169243291e-06
```

Nếu trừ phần này, thì 2 đoạn code nhanh như nhau. Tại sao?

Lý do bởi Python3, [dict.keys() trả về key view](https://docs.python.org/3/library/stdtypes.html#dictionary-view-objects):
> The objects returned by dict.keys(), dict.values() and dict.items() are view objects. They provide a dynamic view on the dictionary’s entries, which means that when the dictionary changes, the view reflects these changes.

Với chú ý keys view hoạt động như kiểu set chứ không phải list. Mà dict key hoạt động như set nên tốc độ là như nhau:

> Keys views are set-like since their entries are unique and hashable. If all values are hashable, so that (key, value) pairs are unique and hashable, then the items view is also set-like. (Values views are not treated as set-like since the entries are generally not unique.)

Keys view dùng như set:

```py
In [26]: d = {i:i for i in range(5)}

In [27]: d2 = {i:i for i in range(4,10)}

In [28]: d.keys() & d2.keys()
Out[28]: {4}
```

Dù vậy, viết `k in dict` vẫn là nhanh, ngắn nhất.

Xem: https://docs.python.org/3/library/stdtypes.html#dictionary-view-objects

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
