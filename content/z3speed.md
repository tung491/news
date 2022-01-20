title: Z3 nhanh chậm ra sao?
date: 2022-01-20
modified: 2022-01-20
tags: Z3, SMT, SAT, theorem prover
category: news
slug: z3speed
authors: Pymier0
description: tìm 1000 nghiệm mất bao lâu?

![img](https://images.unsplash.com/photo-1630071634094-64b2d5b40c57?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2NDI2ODk5MjM&ixlib=rb-1.2.1&q=80&w=600)

Z3 giải toán vi diệu là vậy, nhưng mỗi lần tìm ra 1 nghiệm thôi, vậy tìm 1000 nghiệm của bất phương trình 0 < x < 1001 thì mất bao lâu?

Cách làm tương tự [phần trước]({filename}/z3ineq.md), ta tìm ra 1 nghiệm rồi thêm nghiệm đó vào điều kiện loại trừ.

```py
from z3 import *
solver = Solver()
x = Int('x')
solver.add(x < 1001, x > 0)

while solver.check() == sat:
    model = solver.model()
    var = model[0]
    solver.add(var() != model[var()])
```

```
$ time python3 z3speed.py

real    0m1.508s
```

mất 1.5 giây. Trong khi với 1.5 giây, chương trình Python đơn giản có thể thêm 14 triệu phần tử vào list:

```
i = 0
xs = []
while i < 14_000_000:
    xs.append(i)
    i = i + 1
```

Kết luận: tốc độ tìm ra 1 nghiệm của Z3 không nhanh, so với append list chậm hơn 14 nghìn lần.

Thử tăng số lên 2001,

```
$ time python3 z3speed.py

real    0m5.499s
user    0m5.460s
```

Chậm gấp > 3 lần, chứ không phải 2 lần. Và nếu tăng lên 10001,
```
$ time python3 z3speed.py

real    3m33.323s
user    3m32.711s
sys     0m0.216s
```

~ 210 giây.

![speed]({static}/images/z3speed.png)

Vậy việc mang Z3 đi đếm số nghiệm (450k) của [bài toán lớp
3]({filename}/z3grade3.md) có vẻ như không khả thi.

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
