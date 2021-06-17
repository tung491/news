title: Python len trả về kết quả: ngay và luôn
date: 2021-06-17
modified: 2021-06-17
tags: features
category: news
slug: len
authors: Pymier0
description: vì list trong CPython là array

![img](https://images.unsplash.com/photo-1553880376-2dec478c8e3b?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2MjM4OTI4ODE&ixlib=rb-1.2.1&q=80&w=600)

Vì [CPython list là 1 array]({filename}/array.md), mà 1 array luôn chứa (phía
sau) kích thước/độ dài
của nó, nên việc tính len(x) luôn luôn trả về kết quả ngay lập tức không phụ
thuộc vào độ lớn của list hay còn gọi là "có độ phức tạp O(1)".

[How are lists implemented in CPython?](https://docs.python.org/3/faq/design.html#how-are-lists-implemented-in-cpython)

> CPython’s lists are really variable-length arrays, not Lisp-style linked
lists. The implementation uses a contiguous array of references to other
objects, and keeps a pointer to this array and the array’s length in a list
head structure.

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
