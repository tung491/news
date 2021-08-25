title: Tự làm phép cộng
date: 2021-08-25
modified: 2021-08-25
tags: operator, overloading, dunder
category: news
slug: features
authors: Pymier0
description: MyClass() + MyClass() bằng gì?

![img](https://images.unsplash.com/photo-1624355940421-0078a0714838?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2Mjk4OTc5NTQ&ixlib=rb-1.2.1&q=80&w=600)

Các phép toán trong Python thực chất là các "syntactic sugar", giúp cho viết
gọn hơn thay vì dùng các method thực sự bên dưới. Phép cộng, nói 1 cách đơn
giản, sẽ gọi method `__add__`. Việc này làm thay đổi ý nghĩa thông thường của
dấu + để cộng các số, có tên gọi là ["operator overloading"](https://docs.python.org/3/reference/datamodel.html#special-method-names).
Trong Python, ["operator overloading"](https://docs.python.org/3/reference/datamodel.html#special-method-names) được dùng phổ biến, khi string cũng + được với nhau, list cũng + được với nhau.

Ví dụ sau tự định nghĩa class MyInt và thực hiện phép cộng
cho kết quả... bất ngờ:

```py
class MyInt():
    def __init__(self, n):
        self.n = n
    def __add__(self, k):
        return (self.n + k.n) * 2
two = MyInt(2)
three = MyInt(3)
print(two + three == 10)
```

[glot.io](https://glot.io/snippets/g1r0ytsfbq)

Tham khảo phép tính += thực sự làm gì tại [https://pymi.vn/blog/augassign/](https://pymi.vn/blog/augassign/).

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
