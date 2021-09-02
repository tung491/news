title: Dịch ngược mã máy Python: for/while
date: 2021-09-02
modified: 2021-09-02
tags: dis, internal, bytecode, vm, disassembly, control flow
category: features
slug: disfor
authors: Pymier0
description: tiếp tục tìm hiểu bytecode với for/while

Tiếp loạt bài về [CPython compiler]({filename}/compile.md)

![img](https://images.unsplash.com/photo-1612283592698-6edf01b1edc7?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2MzA1NTAzNjk&ixlib=rb-1.2.1&q=80&w=600)

Xem ví dụ tính tổng 1 tới 100 sau:

### for

```py
# for.py
t = 0
for i in range(1, 101):
    t = t + i

print(t)
```
Chạy dis

```sh
$ python3 -m dis for.py
  1           0 LOAD_CONST               0 (0)
              2 STORE_NAME               0 (t)

  2           4 LOAD_NAME                1 (range)
              6 LOAD_CONST               1 (1)
              8 LOAD_CONST               2 (101)
             10 CALL_FUNCTION            2
             12 GET_ITER
        >>   14 FOR_ITER                12 (to 28)
             16 STORE_NAME               2 (i)

  3          18 LOAD_NAME                0 (t)
             20 LOAD_NAME                2 (i)
             22 BINARY_ADD
             24 STORE_NAME               0 (t)
             26 JUMP_ABSOLUTE           14

  5     >>   28 LOAD_NAME                3 (print)
             30 LOAD_NAME                0 (t)
             32 CALL_FUNCTION            1
             34 POP_TOP
             36 LOAD_CONST               3 (None)
             38 RETURN_VALUE
```

sau khi LOAD xong function range và 2 tham số 1, 101, `CALL_FUNCTION` gọi function `range`.

Tại offset 12 có BYTECODE `GET_ITER` để lấy iterator từ object range.

offset 14 có đánh dấu vị trí jump `>>`, bắt đầu thực hiện
`FOR_ITER`, với đầu vào là iterator lấy ở offset 12, khi thực hiện xong việc lặp sẽ nhảy tới offset 28 (ngoài vòng for).

Code trong thân vòng lặp for kết thúc bằng BYTECODE `JUMP_ABSOLUTE` và nhảy tới offset 14, tức chạy xong thân vòng lặp thì chuyển tới vòng lặp tiếp theo.

### while

```py
# while.py
t = 0
i = 1
while i < 101:
    t = t + i

print(t)
```
Chạy dis

```
$ python3 -m dis while.py
  1           0 LOAD_CONST               0 (0)
              2 STORE_NAME               0 (t)

  2           4 LOAD_CONST               1 (1)
              6 STORE_NAME               1 (i)

  3     >>    8 LOAD_NAME                1 (i)
             10 LOAD_CONST               2 (101)
             12 COMPARE_OP               0 (<)
             14 POP_JUMP_IF_FALSE       26

  4          16 LOAD_NAME                0 (t)
             18 LOAD_NAME                1 (i)
             20 BINARY_ADD
             22 STORE_NAME               0 (t)
             24 JUMP_ABSOLUTE            8

  6     >>   26 LOAD_NAME                2 (print)
             28 LOAD_NAME                0 (t)
             30 CALL_FUNCTION            1
             32 POP_TOP
             34 LOAD_CONST               3 (None)
             36 RETURN_VALUE
```

Điều kiện theo sau vòng lặp while sẽ khiến while nhảy tới ngoài vòng lặp khi điều kiện sai (như if nhảy sang else),
dùng cùng BYTECODE `POP_JUMP_IF_FALSE` tới offset 26 - vị trí ngoài vòng lặp.

Hết thân vòng lặp while, `JUMP_ABSOLUTE` lại nhảy tới vòng lặp tiếp theo.

### Kết luận
for và while đều sinh ra BYTECODE tương tự nhau.
Trong khi for có xuất hiện 2 BYTECODE mới là FOR_ITER và GET_ITER thì while chỉ toàn là JUMP.

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
