title: Dùng C shared object .so trong CPython
date: 2022-10-12
modified: 2022-10-12
tags: C, shared object, so, import
category: news
slug: so
authors: Pymier0
description: chuyện ít ai thèm nói

![img](https://images.unsplash.com/photo-1579546928686-286c9fbde1ec?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2NjU1MDQ5MTU&ixlib=rb-1.2.1&q=80&w=600)

CPython có thể import file C "shared library" (trên Linux là các file "shared object" có đuôi `.so` bằng việc gõ "import filename".

Nếu có cả file `.so` và `.py` cùng tồn tại, CPython ưu tiên gọi file `.so` trước.

Trong stdlib của CPython, có nhiều thư viện dùng C như sqlite3 hay json, các thư viện này thường có 1 file .py, thực hiện nhiệm vụ import file `.so`:

```
$ find /usr/lib/python3.8/ -name '*sqlite*'
/usr/lib/python3.8/lib-dynload/_sqlite3.cpython-38-x86_64-linux-gnu.so
/usr/lib/python3.8/sqlite3

$ grep import -R /usr/lib/python3.8/sqlite3
...
/usr/lib/python3.8/sqlite3/dbapi2.py:from _sqlite3 import *
...

$ find /usr/lib/python3.8/ -name '*json*'
/usr/lib/python3.8/lib-dynload/_json.cpython-38-x86_64-linux-gnu.so
...
$ grep '_json' -R /usr/lib/python3.8/json
/usr/lib/python3.8/json/decoder.py:    from _json import scanstring as c_scanstring
/usr/lib/python3.8/json/decoder.py:    # Note that this exception is used from _json
/usr/lib/python3.8/json/scanner.py:    from _json import make_scanner as c_make_scanner
/usr/lib/python3.8/json/encoder.py:    from _json import encode_basestring_ascii as c_encode_basestring_ascii
/usr/lib/python3.8/json/encoder.py:    from _json import encode_basestring as c_encode_basestring
/usr/lib/python3.8/json/encoder.py:    from _json import make_encoder as c_make_encoder
...
```
Xem qua 1 file .so:
```
$ file /usr/lib/python3.8/lib-dynload/_sqlite3.cpython-38-x86_64-linux-gnu.so
/usr/lib/python3.8/lib-dynload/_sqlite3.cpython-38-x86_64-linux-gnu.so: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, BuildID[sha1]=b65897eefdf7fd0290ce9885a91dda3781d59b59, stripped

$ readelf -a /usr/lib/python3.8/lib-dynload/_sqlite3.cpython-38-x86_64-linux-gnu.so
ELF Header:
  Magic:   7f 45 4c 46 02 01 01 00 00 00 00 00 00 00 00 00 
  Class:                             ELF64
  Data:                              2's complement, little endian
  Version:                           1 (current)
  OS/ABI:                            UNIX - System V
  ABI Version:                       0
  Type:                              DYN (Shared object file)
  Machine:                           Advanced Micro Devices X86-64
  Version:                           0x1
  Entry point address:               0x8480
  Start of program headers:          64 (bytes into file)
  Start of section headers:          98160 (bytes into file)
  Flags:                             0x0
  Size of this header:               64 (bytes)
  Size of program headers:           56 (bytes)
  Number of program headers:         11
... còn rất dài
```

Hết.

Bài viết thực hiện trên Ubuntu 20.04, Python 3.8

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
