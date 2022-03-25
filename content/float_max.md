title: Số float lớn nhất
date: 2022-03-25
modified: 2022-03-25
tags: float, IEEE754
category: news
slug: float_max
authors: Pymier0
description: float không "lớn tùy ý"

![img](https://images.unsplash.com/photo-1595160561341-267c085e1257?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2NDgyMDg4MTU&ixlib=rb-1.2.1&q=80&w=600)

Bài trước sau khi thử lấy 2**2048/2, xảy ra exception 

> OverflowError: int too large to convert to float

float không lớn tùy ý như int.

Số float lớn nhất? là `inf`

```py
>>> float('inf')
inf
```

Số float lớn nhất sau `inf`? 

```py
>>> import sys
>>> sys.float_info.max
1.7976931348623157e+308
>>> sys.float_info.max*2
inf
```

`1.79 * 10**308`, một số có 309 chữ số, độ lớn gần bằng 2**1024. 
```py
>>> len(str(2**1024))
309
>>> 2**1024
179769313486231590772930519078902473361797697894230657273430081157732675805500963132708477322407536021120113879871393357658789768814416622492847430639474124377767893424865485276302219601246094119453082952085005768838150682342462881473913110540827237163350510684586298239947245938479716304835356329624224137216
>>> 2**1024*1.0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
OverflowError: int too large to convert to float
>>> 2**1024 > sys.float_info.max
True

```

Hết.

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
