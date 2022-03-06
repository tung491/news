title: Các method của boolean True False
date: 2022-03-06
modified: 2022-03-06
tags: boolean, bool, methods
category: news
slug: bool-methods
authors: Pymier0
description: hông ngờ tới phải không?

![img](https://images.unsplash.com/photo-1512441933491-7b8cc442ed32?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2NDY1ODExODQ&ixlib=rb-1.2.1&q=80&w=600)

True và False là hai giá trị kiểu bool trong Python, có thể nói thuộc một trong những thứ đơn giản nhất, vì chỉ có hai giá trị.

Sau khi học hành tử tế sẽ biết các operator and or not và chúng có tính [short-circuit](https://pymi.vn/tutorial/boolean/), và... hết.

Hỏi: giá trị boolean có các methods nào?

Trả lời: what?!!! đó có lẽ là thứ mà bạn chưa từng thử.

bool trong Python thực chất inherit từ class base là `int`, nó có mọi methods của `int`. WHAT? int cũng có method? chính xác, mọi thứ trong Python đều là object.

```py
>>> dir(True) == dir(83)
True
>>> print(dir(83))
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '_class__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mpow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_ing', 'numerator', 'real', 'to_bytes']
>>> True.__class__.__base__
<class 'int'>
```

Các "public" methods:

```py
>>> x.as_integer_ratio()
(1, 1)
>>> x.bit_length()
1
>>> x.to_bytes(1, 'big')
b'\x01'
```

Hết.

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
