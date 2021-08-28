title: CPython compiler
date: 2021-08-28
modified: 2021-08-28
tags: compiler, internal, CPython, bytecode, virtual machine
category: features
slug: compile
authors: Pymier0
description: Python có compile code không? Có!

![img](https://images.unsplash.com/photo-1520491286939-1680f46efe91?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2MzAxNTg0NzA&ixlib=rb-1.2.1&q=80&w=600)

Python thường được biết tới như một ngôn ngữ lập trình scripting/interpreted.
Lập trình viên sau khi viết code xong, chỉ cần gõ python tên_file.py để chạy
code dẫn tới một sự hiểu nhầm phổ biến rằng "python không compile code".

Để tránh các tranh cãi không cần thiết, ở đây chỉ nói tới CPython - tức bản
Python phổ biến nhất mà gần như tất cả mọi người đều dùng, tải từ
[python.org](https://www.python.org/).

Để chạy 1 file code Python, CPython có bước compile code, nhưng bước này
CPython tự thực hiện mà không cần lập trình viên phải thực hiện. Việc compile
này cũng thường diễn ra rất nhanh chóng nên khó có thể phát hiện ra.  Khác với
C/C++/Golang, Python compile code không sinh ra 1 file binary chạy được. Giống
với Java, Python sinh ra bytecode, bytecode này được chạy bởi Python virtual
machine (với Java là JVM).

Dễ quan sát hơn khi sử dụng module, CPython mặc định sẽ sinh ra file `.pyc`
chứa compiled bytecode. Tạo 1 file  tên `mylib.py` và 1 file main `main.py`

```py
# main.py
import mylib
print(mylib.double(21))

 # mylib.py
def double(x):
    return x * 2
```
chạy file main.py
```sh
$ ls -la
total 16
drwxrwxr-x 2 hvn hvn 4096 Aug 28 20:39 .
drwxrwxr-x 3 hvn hvn 4096 Aug 28 20:39 ..
-rw-rw-r-- 1 hvn hvn   37 Aug 28 20:39 main.py
-rw-rw-r-- 1 hvn hvn   32 Aug 28 20:39 mylib.py
$ python3 main.py
42
$ ls -la
total 20
drwxrwxr-x 3 hvn hvn 4096 Aug 28 20:39 .
drwxrwxr-x 3 hvn hvn 4096 Aug 28 20:39 ..
-rw-rw-r-- 1 hvn hvn   37 Aug 28 20:39 main.py
-rw-rw-r-- 1 hvn hvn   32 Aug 28 20:39 mylib.py
drwxrwxr-x 2 hvn hvn 4096 Aug 28 20:39 __pycache__
$ ls -la __pycache__
total 12
drwxrwxr-x 2 hvn hvn 4096 Aug 28 20:39 .
drwxrwxr-x 3 hvn hvn 4096 Aug 28 20:39 ..
-rw-rw-r-- 1 hvn hvn  235 Aug 28 20:39 mylib.cpython-38.pyc
```

Python sẽ đọc các file .pyc này mà bỏ qua bước compile ở lần chạy sau (nếu code
        không thay đổi), tiết kiệm được thời gian compile, NHƯNG SAU ĐÓ CODE
CHẠY KHÔNG NHANH HƠN lần trước.

Để xem nội dung bytecode sinh ra từ code, dùng [standard lib `dis`](https://docs.python.org/3/library/dis.html)

### Tham khảo
- [bytecode](https://docs.python.org/3/glossary.html#term-bytecode)
- [virtual-machine](https://docs.python.org/3/glossary.html#term-virtual-machine)
- [pep-3147](https://www.python.org/dev/peps/pep-3147/)
- [compiled-python-files](https://docs.python.org/3/tutorial/modules.html?highlight=compile#compiled-python-files)

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
