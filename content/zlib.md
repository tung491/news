title: Build Python từ source với zlib và ssl trên Ubuntu 20.04
date: 2021-10-05
modified: 2021-10-05
tags: zlib, ssl, compile, source
category: news
slug: zlib
authors: Pymier0
description: tiếp tục mất 5 phút, nhưng đã giải nén được

Tiếp bài trước, sau khi compile CPython thành công, ta import thử vài thư viện

```py
>>> import gzip
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/root/Python-3.9.7/Lib/gzip.py", line 9, in <module>
    import zlib
ModuleNotFoundError: No module named 'zlib'
>>> import ssl
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/root/Python-3.9.7/Lib/ssl.py", line 98, in <module>
    import _ssl             # if we can't import it, let the error propagate
ModuleNotFoundError: No module named '_ssl'
```

![img](https://images.unsplash.com/photo-1626862647712-a38156ab0488?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2MzMzOTg1ODA&ixlib=rb-1.2.1&q=80&w=600)

Bản Python này bị thiếu các thư viện C cần thiết nên khi compile, kết quả không
có các thư viện tương ứng, cài:

```sh
sudo apt-get install -y zlib1g-dev libssl-dev
```

Sau khi cài xong, chạy lại `./configure && make`

Cuối output của make có hiện ra đoạn: 

```
Python build finished successfully!
The necessary bits to build these optional modules were not found:
_bz2                  _curses               _curses_panel      
_dbm                  _gdbm                 _lzma              
_sqlite3              _tkinter              _uuid              
readline    
```

cho thấy bản build này còn thiếu những thư viện nào, như: sqlite3, tkinter, bz2.

Nhưng giờ thì đã có zlib và ssl

```py
./python 
Python 3.9.7 (default, Oct  5 2021, 01:53:51) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import gzip
>>> import ssl
>>> ssl
<module 'ssl' from '/root/Python-3.9.7/Lib/ssl.py'>
>>> gzip
<module 'gzip' from '/root/Python-3.9.7/Lib/gzip.py'>
>>> import zlib
>>> zlib
<module 'zlib' from '/root/Python-3.9.7/build/lib.linux-x86_64-3.9/zlib.cpython-39-x86_64-linux-gnu.so'>
```

Hết.

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
