title: Đáp án vì sao không tool nào thấy bug
date: 2021-06-08
modified: 2021-06-08
tags: features
category: news
slug: free
authors: Pymier0
description: free variable

Trong [bài trước](https://n.pymi.vn/latebinding.html), một ví dụ trông đơn giản
và dễ phát hiện lỗi bằng mắt việc x chưa được định nghĩa nhưng không tool nào
của Python phát hiện ra.

```py
def n_pymi_vn() -> int:
    s = x + 1
    return s


r = n_pymi_vn()
x = 10
print(r)
```

![img](https://images.unsplash.com/photo-1593627906979-dc2fdc503e32?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2MjMxMTkyNTE&ixlib=rb-1.2.1&q=80&w=600)

Lý do là bởi khái niệm ít được nghe tới ["free variable"](https://pp.pymi.vn/article/free/).

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
