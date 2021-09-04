title: Dịch ngược mã máy Python: function/lambda
date: 2021-09-04
modified: 2021-09-04
tags: dis, disassembly, compile, internal, bytecode, function
category: features
slug: disfun
authors: Pymier0
description: tiếp tục tìm hiểu bytecode với function

Tiếp loạt bài về [CPython compiler]({filename}/compile.md)
![img](https://images.unsplash.com/photo-1601100521677-598dc05293c5?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2MzA3MjU5MTM&ixlib=rb-1.2.1&q=80&w=600)

Code định nghĩa 2 function dùng def và lambda:

```py
# $ cat -n fun.py
     1  def sum_two(x, y):
     2      z = x + y
     3      return z
     4
     5  a = 5
     6  b = 7
     7  sum_two(a, b)
     8
     9  double = lambda x: x * 2
    10  double(5)
```

Chạy dis. Việc tạo function dùng def hay lambda đều sử dụng
BYTECODE `MAKE_FUNCTION` sau đó `STORE_NAME`

```py
  1           0 LOAD_CONST               0 (<code object sum_two at 0x7fc64dcca190, file "fun.py", line 1>)
              2 LOAD_CONST               1 ('sum_two')
              4 MAKE_FUNCTION            0
              6 STORE_NAME               0 (sum_two)

  5           8 LOAD_CONST               2 (5)
             10 STORE_NAME               1 (a)

  6          12 LOAD_CONST               3 (7)
             14 STORE_NAME               2 (b)

  7          16 LOAD_NAME                0 (sum_two)
             18 LOAD_NAME                1 (a)
             20 LOAD_NAME                2 (b)
             22 CALL_FUNCTION            2
             24 POP_TOP

  9          26 LOAD_CONST               4 (<code object <lambda> at 0x7fc64dcca2f0, file "fun.py", line 9>)
             28 LOAD_CONST               5 ('<lambda>')
             30 MAKE_FUNCTION            0
             32 STORE_NAME               3 (double)

 10          34 LOAD_NAME                3 (double)
             36 LOAD_CONST               2 (5)
             38 CALL_FUNCTION            1
             40 POP_TOP
             42 LOAD_CONST               6 (None)
             44 RETURN_VALUE

Disassembly of <code object sum_two at 0x7fc64dcca190, file "fun.py", line 1>:
  2           0 LOAD_FAST                0 (x)
              2 LOAD_FAST                1 (y)
              4 BINARY_ADD
              6 STORE_FAST               2 (z)

  3           8 LOAD_FAST                2 (z)
             10 RETURN_VALUE

Disassembly of <code object <lambda> at 0x7fc64dcca2f0, file "fun.py", line 9>:
  9           0 LOAD_FAST                0 (x)
              2 LOAD_CONST               1 (2)
              4 BINARY_MULTIPLY
              6 RETURN_VALUE
```

khác với các khái niệm trước, khi viết function sẽ thấy python dis riêng ra từng mục cho từng function.

Với function sum_two tại dòng 1, có riêng mục

`Disassembly of <code object sum_two at 0x7fc64dcca190, file "fun.py", line 1>:`

chú ý thêm sự khác biệt khi dùng biến trong function sử dụng `LOAD_FAST` thay vì `LOAD_NAME`, tạo biến sử dụng `STORE_FAST` thay `STORE_NAME`. function kết thúc bằng việc `RETURN_VALUE`.

Thế nhưng.. return cái gì? câu `RETURN_VALUE` không thấy ghi thêm gì sau, làm 
sao biết nó return gì?
`RETURN_VALUE` sẽ return giá trị cuối cùng tính toán được. Như trong `sum_two`
sẽ return giá trị của z sau khi `LOAD_FAST`. Với `lambda` function, return 
kết quả của phép nhân `BINARY_MULTIPLY`. Cụ thể hơn, trong Python VM gọi đây là
TOP OF STACK (TOS), kết quả của giá trị tính toán xong sẽ luôn nằm ở đây.
Vậy nếu tôi muốn return cái không tính cuối cùng thì nó return gì?


Thử nghiệm với 2 functio không trả về giá trị vừa tính xong:

```py
     1  def r_none(x, y):
     2      z = x + y
     3      return
     4
     5
     6  def r_i(x, y):
     7      i = 8
     8      z = x + y
     9      return i
```

Kết quả dis

```py
Disassembly of <code object r_none at 0x7fdd4b47bdf0, file "fun.py", line 1>:
  2           0 LOAD_FAST                0 (x)
              2 LOAD_FAST                1 (y)
              4 BINARY_ADD
              6 STORE_FAST               2 (z)

  3           8 LOAD_CONST               0 (None)
             10 RETURN_VALUE

Disassembly of <code object r_i at 0x7fdd4b47f030, file "fun.py", line 6>:
  7           0 LOAD_CONST               1 (8)
              2 STORE_FAST               2 (i)

  8           4 LOAD_FAST                0 (x)
              6 LOAD_FAST                1 (y)
              8 BINARY_ADD
             10 STORE_FAST               3 (z)

  9          12 LOAD_FAST                2 (i)
             14 RETURN_VALUE
```

function `r_none` load giá trị None để return vì code chỉ ghi return không gì cả.
function `r_i` sẽ `LOAD_FAST` giá trị `i` rồi return i.




Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.

