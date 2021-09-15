title: Dùng Python để giải nén file zip, gz, tarball
date: 2021-07-08
modified: 2021-07-08
tags: zip, unzip, gz, gzip, tar, 1liner, CLI
category: news
slug: ziptargz
authors: Pymier0
description: có Python không cần lo zip/unzip/gzip/gunzip/tar

Python3 mang lại nhiều câu lệnh mới từ các module khiến Python có thể dùng
thay cho các công cụ chuyên biệt khác, và làm rất tốt.

![img](https://images.unsplash.com/photo-1548382340-e7280a94e3ae?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2MjU3MDc5ODE&ixlib=rb-1.2.1&q=80&w=600)

Khi máy đã cài Python, người dùng không phải lo cài `unzip`, `gzip`, `tar`...
vì Python đã có sẵn các thư viện làm những công việc này.
Nhưng phải viết code? KHÔNG! Python có thể "chạy" các thư viện như các chương
trình CLI.
Cú pháp:

```py
python3 -m MODULENAME INPUT
```

Ví dụ để nén/giải nén 1 file zip:

```sh
$ python3 -m zipfile --create post.zip content/*.md
$ file post.zip
post.zip: Zip archive data, at least v2.0 to extract
$ python3 -m zipfile --extract post.zip /tmp
$ ls /tmp/*.md
/tmp/36eol.md	   /tmp/dictorder.md  /tmp/equal.md    /tmp/hn2107.md
```

Sợ chậm? no no no! các thư viện này đều gọi đến thư viện viết bằng C bên dưới,
tốc độ nhiều khi **test nhanh** còn cho kết quả nhanh hơn
các chương trình CLI chuyên dụng.

Giải nén tar.gz
```sh
$ python3 -m gzip -d ~/Downloads/go1.15.7.linux-amd64.tar.gz
$ python3 -m tarfile -e ~/Downloads/go1.15.7.linux-amd64.tar
$ du -csh go
377M	go
377M	total
```

## Hết
```
$ python3 -V
Python 3.8.10
```

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
