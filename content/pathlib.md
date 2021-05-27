title: Thư viện pathlib trong Python3.4
date: 2021-05-27
modified: 2021-05-27
tags: features
category: news
slug: pathlib
authors: Pymier0
description: ngắn gọn hơn, dễ dùng hơn so với os.path

![img](https://images.unsplash.com/photo-1584802142766-52eda937f127?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2MjIxMzAzMDQ&ixlib=rb-1.2.1&q=80&w=600)

Làm thế nào để viết code mở 1 file ở ngay cùng thư mục file code hiện tại?

```py
open("./data.csv")
```

cách này sẽ mở file cùng thư mục làm việc hiện tại (current work directory -
cwd), mặc định là thư mục người dùng gõ lệnh để chạy Python script.
Nếu gõ:

```py
python script.py
```
thì ok, nhưng nếu đang ở `/` gõ `python /path/to/script.py` sẽ fail.
Để lấy cwd, gõ `os.getcwd()`.

Python có một biến đặc biệt `__file__` là đường dẫn của chính file code hiện
tại, cách làm truyền thống ở Python2.x sẽ là

```py
import os

f = open(
    os.path.join(
        os.path.dirname(
            os.path.abspath(
                __file__)),
        "data.csv"
    )
)
print(f.read())
```

bước `abspath` là cần thiết, vì `__path__` [có thể trả về đường dẫn tương đối
(như `./script.py`).](https://stackoverflow.com/questions/7116889/is-module-file-attribute-absolute-or-relative)


```py
from pathlib import Path
f = open(
        Path(__file__).parent.absolute() / "data.csv"
)
print(f.read())
```

ngắn gọn hơn nhiều, với dấu `/` là dấu phân cách quen thuộc trên các hệ điều
hành không phải Windows.


PS: nếu bạn nghĩ vậy là phức tạp? đây là [code bash](https://stackoverflow.com/questions/59895/how-can-i-get-the-source-directory-of-a-bash-script-from-within-the-script-itsel)

### Tham khảo

- https://docs.python.org/3/library/pathlib.html
- https://stackoverflow.com/questions/7116889/is-module-file-attribute-absolute-or-relative

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
