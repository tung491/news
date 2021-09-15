title: Speed test cpu dùng Python
date: 2021-09-15
modified: 2021-09-15
tags: cpu, fast, sum, timeit, stdlib
category: features
slug: speedtest
authors: Pymier0
description: Test speed CPU với 43 ký tự Python CLI

https://cpu.pymi.vn/ cho ta một cách để so sánh các CPU với nhau, đồng thời nắm được tốc độ của Python. Nhưng khi cần test nhanh tốc độ CPU trên máy mà ko muốn tải/code nhiều thì làm sao?

Việc làm này rất hữu dụng khi test CPU của các máy ảo (cloud VM) - mặc dù ghi có 1 2 3 CPU, nhưng ko phải CPU nào cũng mạnh như nhau.

![img](https://images.unsplash.com/photo-1593697703081-129cf07ed377?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2MzE3MjA3MDI&ixlib=rb-1.2.1&q=80&w=600)

Python có sẵn thư viện timeit dùng để đo tốc độ code chạy,
kết hợp với tính sum(range(N)) để đo tốc độ của 1 CPU trên máy.

```sh
$ python3 -m timeit 'sum(range(100_000_000))'
1 loop, best of 5: 962 msec per loop
```

962ms (0.952s) trên CPU AMD Ryzen 3 4300U, để tính tổng của range này, chú ý cả 2 function này đề viết bằng C nên rất nhanh so với loop bằng Python.

PS: phiên bản Python cũng sẽ ảnh hưởng đến kết quả, vd 3.7 vs 3.10, và để chắc ăn nhớ chạy vài lần.

Còn bạn?

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
