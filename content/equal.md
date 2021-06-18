title: Là và bằng
date: 2021-06-18
modified: 2021-06-18
tags: features
category: news
slug: equal
authors: Pymier0
description: có tạo được dict chứa key True và 1 được không?

Nếu học Python tại Pymi.vn, chắc chắn bạn biết 1 bí mật ít khi dùng tới: 1 == True và 0 == False:

```py
>>> True == 1 and False == 0
True
```

Thậm chí có thể đem tính toán:

```py
>>> True + True - False
2
```

bí mật này dẫn tới một số vấn đề "kỳ lạ sau".

```py
>>> xs = [False, True, 2, 1, 0]
>>> xs.index(0)
0
```

sẽ có ít nhất 68% được hỏi trả lời sai câu này, dù trình độ code Python lâu đến mấy.
Lý do vì trong thực tế, gần như không bao giờ gặp trường hợp như vậy, việc tạo 1 list chứa cả boolean lẫn integer đã là code quá dở rồi.


Ngày hôm qua, trên "room Telegram chat sách" của Pymi (tham gia [Slack](https://invite.pymi.vn) vào #chem-gio để ra nhập), thành viên cốt cán @no7kai có đố:

```py
dic = {True: 'yes', 1: 'no', 1.0: 'maybe'}
dic[True]
dic[1]
```

no7kai>  Nhìn code đọc luôn kq ae.

Ta cheating, mang luôn đi chạy
```py
>>> dic = {True: 'yes', 1: 'no', 1.0: 'maybe'}
>>> dic
{True: 'maybe'}
```

có người sẽ thấy ngạc nhiên, nhưng Python có ghi rõ trong doc (tất nhiên cái phần doc này cũng không mấy ai đọc:

> A dictionary’s keys are almost arbitrary values. Values that are not hashable, that is, values containing lists, dictionaries or other mutable types (that are compared by value rather than by object identity) may not be used as keys. Numeric types used for keys obey the normal rules for numeric comparison: if two numbers compare equal (such as 1 and 1.0) then they can be used interchangeably to index the same dictionary entry. (Note however, that since computers store floating-point numbers as approximations it is usually unwise to use them as dictionary keys.)

[mapping-types-dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)

Khi giá trị bằng nhau, chúng được dùng thay thế nhau

```py
>>> dic
{True: 'maybe'}
>>> dic[1]
'maybe'
```

Ví dụ ban đầu và ví dụ này, Python đều so sánh `==` để thực hiện các phép tính.

### Hỏi khó
vậy còn set? set([True, 1]) thì trả về mấy phần tử?

![img](https://images.unsplash.com/photo-1542134377-e67fbf4ca699?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2MjM5ODE1ODM&ixlib=rb-1.2.1&q=80&w=600)

```py
>>> set([True, 1, 1.0])
{True}
```

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
