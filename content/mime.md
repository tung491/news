title: MIME trên MacOS không như MIME trên Linux
date: 2023-10-11
modified: 2023-10-11
tags: python, mime, macos, linux, mimetype
category: news
slug: mime
authors: Pymier0
description: code chạy trên MacOS mà không chạy trên Linux

Viết code chạy trên được nhiều hệ điều hành gọi là "cross-platform", là lý do mà
lập trình viên sẽ dùng các thư viện thay vì "hard-code".

### Cross-platform file path với os
Ví dụ đường dẫn thư mục "a" chứa thư mục "b": trên Linux/MacOS: `a/b` thì trên Windows là `a\b`.
Sử dụng thư viện như `os` sẽ giải quyết các sự khác biệt phía dưới.

Trên Linux

```py
>>> import os
>>> os.path.join("a", "b")
'a/b'
```

### MIME - Multipurpose Internet Mail Extensions
> Multipurpose Internet Mail Extensions (MIME) is an Internet standard that
> extends the format of email messages to support text in character sets other
> than ASCII, as well as attachments of audio, video, images, and application
> programs.

<https://en.wikipedia.org/wiki/MIME>

Lúc mới có máy tính, email chỉ để gửi text, sau này được mở rộng ra để gửi ảnh,
nhạc, video, game... MIME là tên tiêu chuẩn để hỗ trợ việc mở rộng này.

Thư viện `mimetypes` trong standard lib của Python giúp đoán "MIME type" và
encoding của 1 URL/filename.

Trên MacOS

```py
>>> import mimetype
>>> mimetypes.guess_type("nginx.log.gz")
('text/plain', 'gzip')
```

Trên Ubuntu server (hay `docker run -it python:3.8.18`)

```py
>>> import mimetypes
>>> mimetypes.guess_type("nginx.log.gz")
(None, 'gzip')
```

Có vẻ như kết quả khác nhau là do hệ điều hành?

Dùng strace xem mimetypes đọc thông tin từ đâu:
```
$ strace -e openat python3 mime.py
...
openat(AT_FDCWD, "/etc/mime.types", O_RDONLY|O_CLOEXEC) = 3
('text/plain', 'gzip')
+++ exited with 0 +++
```

Tìm xem gói nào cài /etc/mime.types:

```sh
$ dpkg -S /etc/mime.types
media-types: /etc/mime.types
$ apt-cache show media-types
Priority: important
...
Task: minimal, server-minimal
```

Gói này rất quan trọng và có sẵn trên server Ubuntu, kể cả trong python:3.8.18 Docker image cũng có:

```
$ dpkg -l media-types
ii  media-types    10.0.0       all          List of standard media types and their usual file extension
```

Nhưng trong file `/etc/mime.types` trên Ubuntu 22.04, docker fedora:38, docker python:3.8.18 chạy debian 12 đều có kết quả như nhau:

```
>>> import mimetypes
>>> mimetypes.guess_type("nginx.log.gz")
(None, 'gzip')
```

Do trong /etc/mime.types không chứa dòng nào cho `log`

```
# grep ' log' /etc/mime.types -c
0
```

Trên docker `python:3.8.18-alpine` thậm chí còn không có file /etc/mime.types
```
$ docker run -it python:3.8.18-alpine sh -c 'ls -l /etc/mime.types'
ls: /etc/mime.types: No such file or directory
```

Trên Manjaro 23 desktop, mở `/etc/mime.types` tìm thấy:

```
$ grep text/plain /etc/mime.types
text/plain		txt asc text pm el c h cc hh cxx hxx f90 conf log
```
chạy code cho kết quả:
```
>>> import mimetypes
>>> mimetypes.guess_type("nginx.log.gz")
('text/plain', 'gzip')
```

Vậy kết quả của function này phụ thuộc vào nội dung của các file "mime.types".

Thư viện mimetypes sẽ tìm trong các files:

```py
knownfiles = [
    "/etc/mime.types",
    "/etc/httpd/mime.types",                    # Mac OS X
    "/etc/httpd/conf/mime.types",               # Apache
    "/etc/apache/mime.types",                   # Apache 1
    "/etc/apache2/mime.types",                  # Apache 2
    "/usr/local/etc/httpd/conf/mime.types",
    "/usr/local/lib/netscape/mime.types",
    "/usr/local/etc/httpd/conf/mime.types",     # Apache 1.2
    "/usr/local/etc/mime.types",                # Apache 1.3
]
```
<https://github.com/python/cpython/blob/3.12/Lib/mimetypes.py#L48-L58>

### Kết luận
Một ví dụ nữa cho việc "code chạy trên máy tôi" nhưng không chạy khi deploy thật trên server.
Dev trên MacOS deploy trên Ubuntu/Container vẫn có đầy đau thương, và dùng "container" (docker) khi dev trên local là 1 giải pháp.

Hết.

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
