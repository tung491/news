title: Giải toán lớp 4: 50 cặp chân gà, chó bằng Z3 
date: 2022-01-08
modified: 2022-01-08
tags: z3, SMT, SAT, theorem prover
category: news
slug: z3p1
authors: Pymier0
description: Z3 là một thư viện rất khác biệt, và đặc biệt, giúp giải các bài toán đố, như sudoku, 8 quân hậu, ... trong 1 nốt nhạc

![img](https://images.unsplash.com/photo-1582456313540-088dcd72e53a?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2NDE2NTg4NTc&ixlib=rb-1.2.1&q=80&w=600)

[Z3](https://github.com/Z3Prover/z3#python) là một "theorem prover", thuộc dạng Satisfiability Modulo Theories (SMT) solver, một sản phẩm của [Microsoft Research](https://theory.stanford.edu/~nikolaj/programmingz3.html). Nó có thể làm rất nhiều thứ, một cách "magic", không dễ để hiểu, nhưng không khó để dùng.

Loạt bài sẽ dùng Z3 để giải các bài toán đố chỉ bằng cách: mô tả bài toán.

Toán cấp 1 có một bài toán lừng danh ở dạng "tứ ngôn, tứ tuyệt", như sau:

<center>
Vừa gà, vừa chó

bó lại cho tròn

ba mươi sáu con

một trăm chân chẵn
</center>

Hỏi có bao nhiêu con gà và chó. Và từ đó các cô các thầy sẽ dạy học sinh "phương pháp tìm hai số khi biết tổng và hiệu"...

Cài z3: `pip install z3-solver`

Giải bằng Z3

```py
from z3 import Int, solve
ga = Int('ga')
cho = Int('cho')
solve(ga + cho == 36, ga * 2 + cho * 4 == 100)
```
Kết quả hiện ra: 

> [cho = 14, ga = 22]

Ta mô hình bài toán bằng việc tạo 1 biến Int chứa số con gà, 1 biến Int khác chứa số con chó, gọi function giải: **solve** với lần lượt các điều kiện. Z3 giải và in ra màn hình kết quả.

Thay điều kiện cuối thành 101 chân: 

```py
solve(ga + cho == 36, ga * 2 + cho * 4 == 101)
```

Kết quả: `no solution` do Z3 không tìm thấy nghiệm nào thỏa mãn.

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
