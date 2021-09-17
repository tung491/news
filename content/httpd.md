title: chạy HTTP server bằng 1 câu lệnh Python
date: 2021-09-17
modified: 2021-09-17
tags: HTTP, web server, stdlib, busybox, CLI, 1liner
category: features
slug: httpd
authors: Pymier0
description: rất tiện lợi khi cần "ngay và luôn"

Python có sẵn trong stdlib thư viện http để bật ngay 1 HTTP server/webserver,
khi chạy THẬT, bạn có thể dùng NGINX, nhưng đôi khi cần "test nhanh", cài và
config NGINX là một chuyện không hề nhanh.

![img](https://images.unsplash.com/photo-1578951141665-41b333cb63cc?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2MzE4ODY3MDk&ixlib=rb-1.2.1&q=80&w=600)

Gõ:

```sh
$ python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

Truy cập qua trình duyệt gõ: localhost:8000

thậm chí máy khác cùng mạng cũng có thể truy cập. Server này trả về list các
file trong thư mục hiện tại. Có thể tạo 1 file index.html để trả về nội dung
file này khi người dùng truy cập.

Đó là sức mạnh thư viện có sẵn của Python, rất tiện và có ở đâu có Python3.
Một nhược điểm là nó có thể hơi chậm so với mong muốn, dùng busybox cũng chạy
được 1 câu lệnh:

```sh
$ busybox httpd -fp8000
```

busybox có sẵn trên Ubuntu 20.04, và rất nhiều nơi khác.

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
