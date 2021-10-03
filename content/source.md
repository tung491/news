title: Build Python từ source trên Ubuntu 20.04
date: 2021-10-03
modified: 2021-10-03
tags: build, source, C,
category: news
slug: build
authors: Pymier0
description: mất 5 phút, dành cho mục đích học tập và nghiên cứu...

Build phần mềm từ source dù là chuyện phổ biến trong giới mã nguồn mở từ xưa nhưng dần dần trở thành bí kíp thất
truyền với việc các package manager (như apt, yum, ...) đều cài sẵn binary (sản phẩm của việc build).

Build từ source không tiện lợi cho mục đích cài phần mềm hàng ngày, nhưng là một kiến thức tốt trong học tập và nghiên cứu.

Build CPython bản mới nhất trên Ubuntu cũng không có khó khăn gì, mất khoảng 3-5 phút tùy tốc độ máy tính.

![img](https://images.unsplash.com/photo-1570760295437-3627311f8fbe?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2MzMyNzgzOTE&ixlib=rb-1.2.1&q=80&w=600)

### Chuẩn bị
Để thực hiện bài này, cần có 4 phần mềm:

- curl để tải file source của Python
- tar để giải nén
- gcc có C compiler - để build
- make để chạy lệnh build

Chạy trên Ubuntu 20.04.3 LTS

Cài:

```
sudo apt update && sudo apt-get install -y curl make gcc tar
```

### Bắt đầu

Tải từ trang chủ https://www.python.org/downloads/release/python-397/

```
curl -LO https://www.python.org/ftp/python/3.9.7/Python-3.9.7.tgz
```

Giải nén

```
tar xf Python-3.9.7.tgz;  cd Python-3.9.7
```

Build - theo hướng dẫn trong file README.rst


```
    ./configure
    make
    # make test
    # sudo make install
```

`configure` là 1 shell script, chạy các câu lệnh kiểm tra các điều kiện cần thiết (như có C compiler chưa, ...) và sinh ra file Makefile.

`make` chạy lệnh trong Makefile, nếu quá trình thành công sẽ tạo ra file `python`.

Đây chính là chương trình `python` thu được.

```
# ./python
Python 3.9.7 (default, Oct  3 2021, 16:21:43)
[GCC 9.3.0] on linux
```

Sau khi xong có thể chạy thêm `make test` để đảm bảo `python` chạy thành công các test, và `sudo make install` để cài vào máy thay Python trên máy.

Trong quá trình compile, người dùng sẽ nhìn thấy các thành phần của Python nằm ở file C code nào - không nhất thiết phải biết code C, nhưng ít ra biết nó ở đâu. Ví dụ:

```
gcc -pthread -c -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O3 -Wall    -std=c99 -Wextra -Wno-unused-result -Wno-unused-parameter -Wno-missing-field-initializers -Werror=implicit-function-declaration -fvisibility=hidden  -I./Include/internal  -I. -I./Include    -DPy_BUILD_CORE -o Objects/listobject.o Objects/listobject.c
```

Hết.

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
