title: Dịch ngược mã máy Python: import
date: 2021-09-06
modified: 2021-09-06
tags: dis, disassembly, compile, internal, bytecode
category: features
slug: disimport
authors: Pymier0
description: tiếp tục tìm hiểu bytecode với import

Tiếp loạt bài về [CPython compiler]({filename}/compile.md)

![img](https://images.unsplash.com/photo-1519750783826-e2420f4d687f?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2MzA5NDEwMzg&ixlib=rb-1.2.1&q=80&w=600)

```py
 rand.py 
     1  import random
     2  do = random.choice(['an', 'ngu'])
     3  print(do)
     4
     5  from datetime import timedelta
     6  print("Mot ngay co: {}s".format(timedelta(days=1).total_seconds()))
     7
     8  from math import *
     9  print(factorial(5))
```

3 kiểu import trong Python.
Chạy dis:

```py
#  python3 -m dis rand.py
  1           0 LOAD_CONST               0 (0)
              2 LOAD_CONST               1 (None)
              4 IMPORT_NAME              0 (random)
              6 STORE_NAME               0 (random)

  2           8 LOAD_NAME                0 (random)
             10 LOAD_METHOD              1 (choice)
             12 LOAD_CONST               2 ('an')
             14 LOAD_CONST               3 ('ngu')
             16 BUILD_LIST               2
             18 CALL_METHOD              1
             20 STORE_NAME               2 (do)

  3          22 LOAD_NAME                3 (print)
             24 LOAD_NAME                2 (do)
             26 CALL_FUNCTION            1
             28 POP_TOP

  5          30 LOAD_CONST               0 (0)
             32 LOAD_CONST               4 (('timedelta',))
             34 IMPORT_NAME              4 (datetime)
             36 IMPORT_FROM              5 (timedelta)
             38 STORE_NAME               5 (timedelta)
             40 POP_TOP

  6          42 LOAD_NAME                3 (print)
             44 LOAD_CONST               5 ('Mot ngay co: {}s')
             46 LOAD_METHOD              6 (format)
             48 LOAD_NAME                5 (timedelta)
             50 LOAD_CONST               6 (1)
             52 LOAD_CONST               7 (('days',))
             54 CALL_FUNCTION_KW         1
             56 LOAD_METHOD              7 (total_seconds)
             58 CALL_METHOD              0
             60 CALL_METHOD              1
             62 CALL_FUNCTION            1
             64 POP_TOP

  8          66 LOAD_CONST               0 (0)
             68 LOAD_CONST               8 (('*',))
             70 IMPORT_NAME              8 (math)
             72 IMPORT_STAR

  9          74 LOAD_NAME                3 (print)
             76 LOAD_NAME                9 (factorial)
             78 LOAD_CONST               9 (5)
             80 CALL_FUNCTION            1
             82 CALL_FUNCTION            1
             84 POP_TOP
             86 LOAD_CONST               1 (None)
             88 RETURN_VALUE

```

`import random` sẽ dùng BYTECODE `IMPORT_NAME`, random sẽ trở thành 1 name
trong module này, được chứa `STORE_NAME` tương tự khi đặt `x = 5`.
Để gọi random.choice, đầu tiên phải 
`LOAD_NAME` random rồi `LOAD_METHOD` choice.

Code `from datetime import timedelta`, chạy `IMPORT_NAME` datetime, nhưng không
`STORE_NAME` này mà `IMPORT_FROM` timedelta rồi `STORE_NAME` timedelta.

Code `from math import *` sử dụng BYTECODE `IMPORT_STAR`.

Chú ý khi gọi `random.choice` thì BYTECODE là `CALL_METHOD` do choice gắn liền
vào random - xem như 1 method của 1 module object, nhưng khi gọi 
`factorial` đã `from math import *` thì BYTECODE là `CALL_FUNCTION`.

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
