title: Lambda function có default argument
date: 2022-10-19
modified: 2022-10-19
tags: lambda, function
category: news
slug: lambda_default
authors: Pymier0
description: không thấy bao giờ không phải là không có

Từ khóa lambda dùng để tạo function 1 biểu thức trong Python, thường thấy dùng kèm
với sort, ví dụ sắp xếp giảm dần 1 list int:

```py
>>> sorted([2,3,1], key=lambda x: -x)
[3, 2, 1]
```

![img](https://images.unsplash.com/photo-1591537580018-04f735250c5f?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2NjYxOTA4NjY&ixlib=rb-4.0.3&q=80&w=600)

Có thể gán function được tạo ra từ lambda vào một biến, ví dụ f:

```py
>>> f = lambda x: x+1
>>> f(2)
3
>>> (lambda x: x+1)(2)
3
```

Lambda function cũng hỗ trợ default argument, tức nếu không đưa argument vào,
nó sẽ dùng giá trị mặc định:

```py
>>> (lambda x=1: x+1)()
2
```

Hết.


Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
