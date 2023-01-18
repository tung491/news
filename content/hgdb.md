title: Python hello world từ debugger gdb
date: 2023-01-17
modified: 2023-01-17
tags: gdb, debugger, extension
category: news
slug: hgdb
authors: Pymier0
description: Tự thêm tính năng cho GDB bằng code Python đơn giản!

### GDB là gì
GDB `GDB: The GNU Project Debugger` là debugger phổ biến bậc nhất thế giới, hỗ
trợ nhiều ngôn ngữ như C, Go, Rust ...
Lập trình viên Python không dùng GDB mà dùng pdb với giao diện tương tự gdb, nhưng lập trình viên CPython (core devs) có thể dùng tới gdb vì code CPython - viết bằng C.

Cài đặt

```
sudo apt-get install gdb
```

![bug](https://images.unsplash.com/photo-1512887000011-f36fc9a9eeaf?ixlib=rb-4.0.3&dl=krzysztof-niewolny-RVd0o9ryfAo-unsplash.jpg&w=640&q=80&fm=jpg&crop=entropy&cs=tinysrgb)

Photo by <a href="https://unsplash.com/fr/@epan5?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Krzysztof  Niewolny</a> on <a href="https://unsplash.com/photos/RVd0o9ryfAo?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

GDB đã có từ rất rất lâu, tuy đa năng, nhưng khá khó dùng, không "đẹp sẵn". Khi chơi [CTF](https://pp.pymi.vn/tag/ctf/), hay làm "binary exploitation"/reverse engineer, người dùng thường dùng các bản mở rộng tính năng, đẹp sãn màu mè thay gdb nguyên bản như:

- <https://github.com/pwndbg/pwndbg>
- <https://github.com/longld/peda>
- <https://github.com/hugsy/gef>

Trích tài liệu của [pwndbg](https://github.com/pwndbg/pwndbg)

> Many other projects from the past (e.g., gdbinit, PEDA) and present (e.g. GEF) exist to fill some these gaps. Each provides an excellent experience and great features -- but they're difficult to extend (some are unmaintained, and all are a single 100KB, 200KB, or 300KB file (respectively)).

Điều thú vị ở đây là cả 3 chương trình này đều viết bằng Python.

Từ bản 7 trở đi, GDB hỗ trợ "extending" (mở rộng) bằng các ngôn ngữ khác như Python hay guile, để kiểm tra xem bản mình cài có không gõ:

```
$ gdb --configuration
This GDB was configured as follows:
   configure --host=x86_64-linux-gnu --target=x86_64-linux-gnu
             --with-auto-load-dir=$debugdir:$datadir/auto-load
             --with-auto-load-safe-path=$debugdir:$datadir/auto-load
             --with-expat
             --with-gdb-datadir=/usr/share/gdb (relocatable)
             --with-jit-reader-dir=/usr/lib/gdb (relocatable)
             --without-libunwind-ia64
             --with-lzma
             --with-babeltrace
             --without-intel-pt
             --with-mpfr
             --without-xxhash
             --with-python=/usr (relocatable)
             --without-guile
             --disable-source-highlight
             --with-separate-debug-dir=/usr/lib/debug (relocatable)
             --with-system-gdbinit=/etc/gdb/gdbinit
```

bản mặc định trên Ubuntu 20.04 này có `--with-python` hỗ trợ Python và `--without-guile` không hỗ trợ Guile.

### Bật Python từ gdb
Gõ `gdb -q` để bật gdb lên, sau đó gõ `pi` (viết tắt của python-interactive) để bật Python interpreter lên:

```
$ gdb -q
(gdb) pi
>>> sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0)
233168
```

### Tự  viết Python extension
gdb có 1 file "init" tại $HOME/.gdbinit, viết nội dung sau để gdb load code từ file khi bật lên. Ở đây ví dụ code nằm trong `/home/hvn/me/hgdb/hgdb.py`:

```
source /home/hvn/me/hgdb/hgdb.py
```

Trong file /home/hvn/me/hgdb/hgdb.py, viết code Python như thường, để tạo 1 command mới trong gdb, viết class kế thừa gdb.Command, chú ý sys và gdb lib được import sẵn:

```py
print(sys.executable)
print(sys.version)
print("Hello world, from python")
gdb.write("Hello world by gdb\n")


class HelloWorld(gdb.Command):
    def __init__(self):
        super (HelloWorld, self).__init__("hello", gdb.COMMAND_USER)


    def invoke(self, arg, from_tty):
        if arg.strip():
            name = arg.strip()
        else:
            name = "World"
        print(f"Chào, {name}!")

HelloWorld()
```

Bật gdb lên:

```
$ gdb -q
/usr/bin/python
3.8.10 (default, Nov 14 2022, 12:59:47)
[GCC 9.4.0]
Hello world, from python
Hello world by gdb
(gdb) hello
Chào, World!
(gdb) hello Pymier
Chào, Pymier!
```

Hết.

Thực hiện trên

```
$ gdb --version
GNU gdb (Ubuntu 9.2-0ubuntu1~20.04.1) 9.2
Copyright (C) 2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
```

## Tham khảo
<https://sourceware.org/gdb/current/onlinedocs/gdb.html/Extending-GDB.html#Extending-GDB>

## Liên quan
- <https://familug.github.io/hoc-rust-voi-gdb.html>
- <https://pp.pymi.vn/tag/ctf/>

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
