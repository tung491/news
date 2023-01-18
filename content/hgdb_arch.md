title: Thêm câu lệnh python vào gdb để in ra binary architecture
date: 2023-01-18
modified: 2023-01-18
tags: gdb, debugger, extension
category: news
slug: hgdb-arch
authors: Pymier0
description: amd64? x86? arm64? !!!

### Architecture
Mỗi file binary được compile cho một kiến trúc(architecture) CPU cụ thể.

Các architecture phổ biến như:

- x86-32 (32 bits)
- x86-64 (64 bits)
- arm-64 (phổ biến trên các máy điện thoại/máy tính bảng/hay Apple M1 M2...)

Một file binary đã compile sẵn cho x86-64 thì không thể chạy trực tiếp trên arm-64.
Ví dụ khi download [phần mềm prometheus thấy có sẵn file binary](https://github.com/prometheus/prometheus/releases/tag/v2.41.0) cho từng architecture trên từng hệ điều hành.

Cách đơn giản nhất là gõ lệnh `file tenbinary`:

```
$ file /usr/bin/top                                                                           [0]
/usr/bin/top: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=867346cd2ce3350129fc1e6fb923e92380eaf6e9, for GNU/Linux 3.2.0, stripped
```

thấy `x86-64`, ELF là format binary trên Linux, ở đây thấy ELF 64-bit.

Trong gdb, gõ

```
(gdb) maintenance info sections ?
Exec file:
    `/usr/bin/top', file type elf64-x86-64.
```

Câu lệnh này rất dài và khó nhớ, viết một câu lệnh mới tên là `arch` in ra `elf64-x86-64` sẽ ngắn gọn hơn nhiều.

### Thêm command arch vào gdb
Đoạn code tham khảo từ [PEDA](https://github.com/longld/peda), các bước thực hiện là chạy các câu lệnh của gdb
rồi lấy kết quả ra và in ra phần mong muốn. Thêm vào file code `/home/hvn/me/hgdb/hgdb.py` như [bài trước]({filename}/hgdb.md).


```
import tempfile
class Arch(gdb.Command):
    def __init__(self):
        super (Arch, self).__init__("arch", gdb.COMMAND_USER)


    def invoke(self, arg, from_tty):
        tmpfile = tempfile.mktemp()
        with open(tmpfile, 'w+') as f:
            gdb.execute("set logging off")
            gdb.execute("set height 0")
            gdb.execute(f"set logging file {tmpfile}")
            gdb.execute("set logging overwrite on")
            gdb.execute("set logging redirect on")
            gdb.execute("set logging on")
            gdb.execute("maintenance info sections ?")
            gdb.flush()
            gdb.execute("set logging off")
            output = f.read()
            for line in output.splitlines():
                if 'file type' in line:
                    print(line.split()[-1].strip('.'))
                    break
Arch()
```

Chạy:

```
$ gdb -q /bin/top
Reading symbols from /bin/top...
(No debugging symbols found in /bin/top)
(gdb) arch
elf64-x86-64
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
- [bài trước]({filename}/hgdb.md)

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
