title: Giới thiệu concurrent.futures trong Python 3
date: 2022-05-22
modified: 2022-05-22
tags: concurrent.futures, concurrent, threading, multiprocesses
category: news
slug: concurrent
authors: Pymier0
description: tăng tốc độ xử lý với concurent.futures

## Concurrency
Concurrency là khái niệm chương trình thực hiện nhiều công việc cùng một
lúc (dễ thấy ở các chương trình có giao diện đồ họa: vừa hiển thị giao diện,
vừa kết nối đến trang web, hay các chương trình server phục vụ nhiều người dùng
cùng lúc).

Python (cũng như nhiều ngôn ngữ lập trình khác) từ xưa đã có hai cách làm phổ
biến để viết concurrent code: dùng [threading](https://docs.python.org/3/library/threading.html) hoặc [multiprocessing](https://docs.python.org/3/library/multiprocessing.html).

Python 3 giới thiệu thư viện "bậc cao" dễ dùng hơn có tên [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html).

![img](https://images.unsplash.com/photo-1511229577011-6b24bfc30871?crop=entropy&cs=tinysrgb&fm=jpg&ixlib=rb-1.2.1&q=80&raw_url=true&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=600)

## CPU bound & IO bound
"bound" ở đây hiểu theo nghĩa: chương trình tốn hầu hết thời gian **thực hiện**
tính toán (CPU) hay **chờ** (hệ điều hành) đọc ghi dữ liệu, bao gồm cả kết nối
mạng (IO).

CPython có một giới hạn về thiết kế khiến cho khi dùng threading, chỉ 1 thread
được chạy (dùng CPU) 1 lúc ([global interpreter lock](https://docs.python.org/3/glossary.html#term-global-interpreter-lock)) , muốn dùng nhiều CPU phải chuyển qua dùng multiprocessing.
Thread nhẹ hơn process, máy tính bình thường có thể có hàng chục hay trăm ngàn
thread nhưng
không đủ (RAM) để tạo 10_000 process. Trong Python, khi chương trình IO bound,
có thể dùng thread, khi chương trình CPU bound thì dùng multiprocessing mới có
thể tăng tốc.

concurrent.futures cho phép chuyển đổi giữa threading hay multiprocessing một cách
đơn giản.

## Ví dụ
Tính tổng các số từ 1 đến 30 triệu, 4 lần.

Việc dùng concurrent.futures chỉ gồm 2 bước:
- tạo Thread/Process Pool Executor
- chạy executor.map với 2 argument: function sẽ được chạy ở thread/Process, và
list chứa argument cho mỗi lần gọi function.

Trên máy có 8 CPU, kết qủa thấy dùng
ProcessPoolExecutor cho việc tính tóan CPU bound này nhanh gấp gần 4 lần
so với dùng ThreadPoolExecutor.

```py
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

import os
import time

def sumto(n):
    r = 1
    for i in range(1, n+1):
        r = r + i
    return r

start = time.time()
print(f"ThreadPoolExecutor: max_workers={os.cpu_count()}")
executor = ThreadPoolExecutor(max_workers=os.cpu_count())

for r in executor.map(sumto, [30_000_000,30_000_000,30_000_000,30_000_000]):
    print(r)
print(time.time()-start)


start = time.time()
executor = ProcessPoolExecutor(max_workers=os.cpu_count())

print(f"ProcessPoolExecutor: max_workers={os.cpu_count()}")
for r in executor.map(sumto, [30_000_000,30_000_000,30_000_000,30_000_000]):
    print(r)
print(time.time()-start)
```
Kết quả
```
$ python concurrent.py
ThreadPoolExecutor: max_workers=8
450000015000001
450000015000001
450000015000001
450000015000001
5.539357423782349
ProcessPoolExecutor: max_workers=8
450000015000001
450000015000001
450000015000001
450000015000001
1.5521023273468018
```

Hết
## Tham khảo

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
