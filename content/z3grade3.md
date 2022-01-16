title: Giải "Bài toán lớp 3 có số lượng đáp án khổng lồ" bằng Z3
date: 2022-01-16
modified: 2022-01-16
tags: z3, SMT, SAT, theorem prover 
category: news
slug: z3grade3
authors: Pymier0
description: bài toán lớp 3 truyền thuyết tốn nhiều giấy mực báo chí, giải trong 1 nốt nhạc với Z3

[Bài toán lớp 3](https://www.familug.org/2015/05/codegolf-giai-bai-toan-lop-3-co-so.html): 

![img](https://images.unsplash.com/photo-1539213492139-7b268eb93c82?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2NDIzMjY0Nzg&ixlib=rb-1.2.1&q=80&w=600)

```
a + 13 * b / c + d + 12 * e – f – 11 + g * h / i – 10 = 66
```

![lop3](https://3.bp.blogspot.com/-JbRWh5-nuHw/VVzPv0QAE0I/AAAAAAAATXs/35mGvnHLS3g/s320/baitoan1-2539-1431999391.jpg)

Tìm các số nguyên dương < 10, a đến i thoả mãn bài toán (tìm một nghiệm của bài toán)

Giải bằng Z3:

```py
from z3 import solve, Ints
a,b,c,d,e,f,g,h,i = Ints('a b c d e f g h i')
solve( a + 13 * b / c + d + 12 * e - f - 11 + g * h / i - 10 == 66)
```

Thấy kết quả sai, do chưa có điều kiện giới hạn khoảng giá trị cho a,b,c,d,e,f,g,h,i.

```
[a = 87,
 b = 0,
 c = 0,
 d = 0,
 e = 0,
 f = 0,
 g = 0,
 i = 0,
 h = 1]
```

Thêm các điều kiện vào:
```py
from z3 import solve, Ints
a,b,c,d,e,f,g,h,i = Ints('a b c d e f g h i')
solve(
0< a, a < 10,
0< b, b < 10,
0< c, c < 10,
0< d, d < 10,
0< e, e < 10,
0< f, f < 10,
0< g, g < 10,
0< h, h < 10,
0< i, i < 10,
a + 13 * b / c + d + 12 * e - f - 11 + g * h / i - 10 == 66)
```

Kết quả

```
[f = 5,
 i = 1,
 g = 7,
 c = 1,
 d = 5,
 e = 2,
 a = 1,
 h = 7,
 b = 1,
 div0 = [(49, 1) -> 49, else -> 13],
 mod0 = [else -> 0]]
```

Dù ở đây đã tìm được ra 1 nghiệm, nhưng cách gọi solve() khá giới hạn do phải liệt kê hết các điều kiện cùng 1 lúc. Thay vì gọi trực tiếp solve, tạo 1 object "solver" rồi add các điều kiện vào, kiểm tra và nhận về "model":

```py
from z3 import Solver, Ints
vars = [a,b,c,d,e,f,g,h,i] = Ints('a b c d e f g h i')
solver = Solver()
solver.add(a + 13 * b / c + d + 12 * e - f - 11 + g * h / i - 10 == 66)
for v in vars:
    solver.add(0 < v)
    solver.add(v < 10)

print(solver.check())
m = solver.model()
print(type(m), m)
print(m.eval((a + 13 * b / c + d + 12 * e - f - 11 + g * h / i - 10) == 66))
```

Kết quả:

```
sat
<class 'z3.z3.ModelRef'> [f = 9,
 i = 7,
 g = 2,
 c = 1,
 d = 8,
 e = 4,
 a = 1,
 h = 1,
 b = 3,
 div0 = [(2, 7) -> 0, else -> 39],
 mod0 = [(2, 7) -> 2, else -> 0]]
True
```

Khi gọi `solver.check()`, nó sẽ tìm một "kết quả" và trả về "sat" (satisfy - thỏa mãn), gọi `solver.model()` trả về 1 model (nghiệm) của bài toán. `m.eval()` thay các giá trị trong nghiệm vào biểu thức và tính ra vế trái bằng vế phải bằng 66.

Phần sau sẽ dùng Z3 để tìm tất cả các nghiệm bài toán này.

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
