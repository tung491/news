title: dict.get hay or?
date: 2023-07-12
modified: 2023-07-12
tags: python, dict, default, get, or
category: news
slug: dict.get
authors: Pymier0
description: dict.get(k, default) có như dict.get(k) or default

`dict.get(k, default)` có bằng `dict.get(k) or default`?

`or` thường được dùng để trả về giá trị mặc định:

```
host = os.environ.get("host") or "localhost"
```

Nhưng:

`or` có cách hoạt động khá lắt léo:

các giá trị được biến thành boolean trước khi xử lý, với giá trị trong dict là
0, "", [],... nó lại bị `or` coi là không có gì, và lấy vế phải ra dùng.

Nên nếu dict là :

```py
d = {"red": 0, "yellow": 1, "green": 2}
```
thì kết quả khác nhau:

```py
d.get("red", 3) == 0
```
còn

```py
d.get("red") or 3 == 3
```

### Kết luận

```py
get(key, default=None, /) method of builtins.dict instance
    Return the value for key if key is in the dictionary, else default.
```

Đôi khi nhìn qua thì giống, nhưng phải sờ tận tay mới biết khác chỗ nào.

Hết.

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
