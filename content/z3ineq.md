title: Tìm tất cả nghiệm của bất phương trình bằng Z3
date: 2022-01-18
modified: 2022-01-18
tags: Z3, SMT, SAT, theorem prover
category: news
slug: z3ineq
authors: Pymier0
description: Thay vì chỉ tìm 1 nghiệm, tìm tất cả các nghiệm

![img](https://images.unsplash.com/photo-1542805700-2fadb851b97a?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2NDI1MTA1ODA&ixlib=rb-1.2.1&q=80&w=600)

Các bài trước dùng Z3 để trả về 1 nghiệm của bài toán (do Z3 quyết định), lần này 
ta sẽ viết thêm code để khiến Z3 tìm thêm các nghiệm cho tới khi đủ nghiệm.

Cho bất phương trình: x + y < 4, với x, y nguyên dương.
Dễ mò được có 3 nghiệm: 1 1, 1 2, 2 1.

```py
from z3 import *

solver = Solver()

x, y= Ints('x y')

solver.add(x > 0)
solver.add(y > 0)
solver.add(x + y < 4)
solver.check() == sat
print(solver.model())
```

[x = 1, y = 1]

Để tìm ra tất cả các nghiệm, cần viết thêm code để sau khi giải ra 1 nghiệm,
đưa thêm vào solver một dữ kiện là nghiệm cần tìm tiếp theo phải khác nghiệm
vừa tìm được.

Tức thêm vào: `x != 1 or y != 1`
Để viết or như vậy, trong Z3 viết: `Or(list)` hay ở đây là `Or([x != 1, y != 1])`

thay vì phải tự gõ x, y, và các giá trị của nghiệm vừa tìm được, dùng:

`for var in model` sẽ trả về x và y khi gọi `var()`, sẽ có giá trị nghiệm tương
ứng khi viết `model[x]` và `model[y]`


```py
solver = Solver()

x, y= Ints('x y')

solver.add(x > 0)
solver.add(y > 0)
solver.add(x + y < 4)
while solver.check() == sat:
    model = solver.model()
    print(model)
    block = []
    for var in model:
        symbol = var()
        value = model[symbol]
        block.append(symbol != value)
        
    print("Blocking: ", Or(block))
    solver.add(Or(block))
```

Kết quả được 3 nghiệm:

```
[x = 1, y = 1]
Blocking:  Or(1 != x, 1 != y)
[x = 1, y = 2]
Blocking:  Or(1 != x, 2 != y)
[x = 2, y = 1]
Blocking:  Or(2 != x, 1 != y)
```
 
Hết.

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
