title: Dịch ngược mã máy Python: if/else
date: 2021-09-01
modified: 2021-09-01
tags: internal, bytecode, control flow, ifelse, dis, disassembly
slug: disif
authors: Pymier0
description: tiếp tục tìm hiểu bytecode với if/else

![img](https://images.unsplash.com/photo-1608634769432-f9b6524aa2bf?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2MzA0NjE2MDE&ixlib=rb-1.2.1&q=80&w=600)

Tiếp loạt bài về [CPython compiler]({filename}/compile.md)

```py
# ifelse.py
x = 20
if x > 18:
    print("18+")
else:
    print("vaccine is coming")
```

```
 $ python3 -m dis i
  1           0 LOAD_CONST               0 (20)
              2 STORE_NAME               0 (x)

  2           4 LOAD_NAME                0 (x)
              6 LOAD_CONST               1 (18)
              8 COMPARE_OP               4 (>)
             10 POP_JUMP_IF_FALSE       22

  3          12 LOAD_NAME                1 (print)
             14 LOAD_CONST               2 ('18+')
             16 CALL_FUNCTION            1
             18 POP_TOP
             20 JUMP_FORWARD             8 (to 30)

  5     >>   22 LOAD_NAME                1 (print)
             24 LOAD_CONST               3 ('vaccine is coming')
             26 CALL_FUNCTION            1
             28 POP_TOP
        >>   30 LOAD_CONST               4 (None)
             32 RETURN_VALUE
```

Code `LOAD_CONST` số 20, gán `x = 20`,
sau đó `LOAD_NAME` x và `LOAD_CONST` 18 để thực hiện so sánh.
So sánh sử dụng bytecode `COMPARE_OP`, biểu thức so sánh này nằm trong phần điều kiện của lệnh `if`. Xuất hiện BYTECODE mới:

`POP_JUMP_IF_FALSE` chú ý số 22 theo sau nó.
Để ý trước mỗi BYTECODE là một con số.
Số này là [**offset**](https://docs.python.org/3/library/dis.html#dis.Instruction.offset) hiểu đơn giản là vị trí hay địa chỉ trong đoạn code.
```
    start index of operation within bytecode sequence
```
`POP_JUMP_IF_FALSE       22` nói rằng sẽ JUMP (nhảy) tới
offset 22 nếu sai. Offset 22 ở đây chính là code trong khối `else`.

Sau khi hết code trong khối `if`, xuất hiện BYTECODE:
`20 JUMP_FORWARD             8 (to 30)`
tức JUMP tới offset 30. Rõ ràng khi code trong `if` chạy hết thì Python sẽ bỏ qua phần code else và nhảy tới vị trí ngoài if/else.

Trong output của `dis`, các vị trí JUMP (jump target) được ký hiệu bởi dấu `>>`. Xem trong code của [dis](https://github.com/python/cpython/blob/3.9/Lib/dis.py#L245)


Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
