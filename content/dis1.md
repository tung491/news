title: Hello dis
date: 2021-08-31
modified: 2021-08-31
tags: dis, bytecode, disassembly, internal
category: features
slug: dis1
authors: Pymier0
description: 10 phút làm quen với thư viện dis

Tiếp loạt bài về Python compiler.

![img](https://images.unsplash.com/photo-1563775506308-5812e69b313e?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2MzAzNzU1Njg&ixlib=rb-1.2.1&q=80&w=600Wrote%20newpost.md)

Trong [CPython compiler]({filename}/compile.md), ta đã biết CPython có thực
hiện việc compile code, sinh ra các bytecode, rồi bytecode sẽ được CPython VM
chạy. Khi import module, CPython sinh ra các file `.pyc` sau khi compile. Nội dung
các file này ở dạng binary, người dùng sẽ không thể đọc được.

Python có sẵn thư viện `dis`, giúp thực hiện "disassembly", biến code thành
dạng mã bytecode đọc được.
Bài này giới thiệu các phép toán đơn giản để làm quen:
Tạo các file code .py đơn giản rồi chạy chúng với lệnh: `python3 -m dis tenfile.py`

```py
# ==> d1.py <==
x = 5

# ==> d2.py <==
x = 5
y = 7

# ==> d3.py <==
x = 5
y = 7
z = x + y

# ==> d4.py <==
x = 5
y = 7
z = x + y
s = x - y
print(z)
print(s)
print(len("Python"))

# ==> d5.py <==
x = 5
y = -x
```

File đầu tiên gán x = 5, số 1 trong cột đầu tiên thể hiện
dòng code.
```sh
$ python3 -m dis d1.py
  1           0 LOAD_CONST               0 (5)
              2 STORE_NAME               0 (x)
              4 LOAD_CONST               1 (None)
              6 RETURN_VALUE
```

5 là một giá trị có sẵn, Python thực hiện việc lấy nó `LOAD_CONST`, sau đó gán x = 5 với `STORE_NAME`. 2 dòng sau tạm không bàn tới và xem tiếp các ví dụ còn lại:

chạy d2.py sẽ không khác với d1.py, chỉ thêm phần LOAD_CONST cho 7 và thưc hiện `STORE_NAME` y = 7.

d3.py thêm một phép tính cộng, có BYTECODE là `BINARY_ADD`.
```sh
d3.py
  1           0 LOAD_CONST               0 (5)
              2 STORE_NAME               0 (x)

  2           4 LOAD_CONST               1 (7)
              6 STORE_NAME               1 (y)

  3           8 LOAD_NAME                0 (x)
             10 LOAD_NAME                1 (y)
             12 BINARY_ADD
             14 STORE_NAME               2 (z)
             16 LOAD_CONST               2 (None)
             18 RETURN_VALUE
```

d4.py có phép trừ, có BYTECODE là `BINARY_SUBTRACT`.
Chú ý chữ `BINARY` nói đây là phép toán có 2 toán tử như x + y hay x - y, một
loại phép toán khác chỉ có 1 toán tử như phép lấy số âm (-x), thì - là
`UNARY_NEGATIVE`.

```
$ python3 -m dis d5.py
  1           0 LOAD_CONST               0 (5)
              2 STORE_NAME               0 (x)

  2           4 LOAD_NAME                0 (x)
              6 UNARY_NEGATIVE
              8 STORE_NAME               1 (y)
             10 LOAD_CONST               1 (None)
             12 RETURN_VALUE
# d5.py
x = 5
y = -x
```

d4.py có gọi các function có sẵn, việc đầu tiên là lấy ra function với
`LOAD_NAME`, rồi gọi với `CALL_FUNCTION`. Chú ý sau mỗi lần gọi function có
`POP_TOP`, sẽ tìm hiểu ở bài sau.

```py
d4.py
  1           0 LOAD_CONST               0 (5)
              2 STORE_NAME               0 (x)

  2           4 LOAD_CONST               1 (7)
              6 STORE_NAME               1 (y)

  3           8 LOAD_NAME                0 (x)
             10 LOAD_NAME                1 (y)
             12 BINARY_ADD
             14 STORE_NAME               2 (z)

  4          16 LOAD_NAME                0 (x)
             18 LOAD_NAME                1 (y)
             20 BINARY_SUBTRACT
             22 STORE_NAME               3 (s)

  5          24 LOAD_NAME                4 (print)
             26 LOAD_NAME                2 (z)
             28 CALL_FUNCTION            1
             30 POP_TOP

  6          32 LOAD_NAME                4 (print)
             34 LOAD_NAME                3 (s)
             36 CALL_FUNCTION            1
             38 POP_TOP

  7          40 LOAD_NAME                4 (print)
             42 LOAD_NAME                5 (len)
             44 LOAD_CONST               2 ('Python')
             46 CALL_FUNCTION            1
             48 CALL_FUNCTION            1
             50 POP_TOP
             52 LOAD_CONST               3 (None)
             54 RETURN_VALUE
```

BYTECODE trông lạ nhưng không hề khó.

https://docs.python.org/3/library/dis.html
Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
