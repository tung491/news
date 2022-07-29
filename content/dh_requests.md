title: [Deep Hacking] Chọc sâu vào thư viện dùng phổ biến nhất của Python: lib requests
date: 2022-07-29
modified: 2022-07-29
tags: deep hacking, requests, code
category: news
slug: dh_requests
authors: Pymier0
description: Đọc code Python requests cùng PyMivn

![img](https://images.unsplash.com/photo-1470509037663-253afd7f0f51?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2NTkxMDIxMDM&ixlib=rb-1.2.1&q=80&w=600)

Nếu 10 năm trước, khi nói bạn "học sâu", người ta nghĩ tới việc tìm hiểu thật kỹ, chọc sâu vào qua nhiều tầng lớp để nắm thật chắc kiến thức, thì sau 10 năm marketing, Deep Learning - một nhánh của AI, được dịch sang tiếng Việt với tên "học sâu", đã chiếm mất nghĩa của từ học sâu ban đầu.

Vậy nên chúng tôi gọi là deep hacking, nghe cho nó đỡ lẫn.

Loạt bài viết deep hacking đi sâu vào các dòng code của các thư viện Python, xem chúng được viết thế nào, bí hiểm ra sao. Và lên thớt đầu tiên chính là thư viện được download nhiều số 1 của Python: requests.

## [Cấu trúc thư mục](https://github.com/psf/requests/tree/v2.28.1/requests)

Code thư viện nằm gọn trong 1 thư mục tên "requests", cùng level nó có 1 thư mục tên "tests". Trong requests, chỉ có 18 files py và không có thư mục con nào:

```sh
ls requests/
adapters.py  auth.py   compat.py   exceptions.py  hooks.py     _internal_utils.py  packages.py  status_codes.py  utils.py
api.py       certs.py  cookies.py  help.py        __init__.py  models.py           sessions.py  structures.py    __version__.py
```

### [Dependencies](https://github.com/psf/requests/blob/v2.28.1/setup.py#L61-L65)
requests phụ thuộc trực tiếp vào 4 thư viện, đáng kể nhất là urllib3.

```py
requires = [
    "charset_normalizer>=2,<3",
    "idna>=2.5,<4",
    "urllib3>=1.21.1,<1.27",
    "certifi>=2017.4.17",
]
```

### [`__init__.py`](https://github.com/psf/requests/blob/v2.28.1/requests/__init__.py)

File đầu tiên nên đọc là `__init__.py` nó chứa những gì ta có thể truy cập khi gõ `requests.`, ví dụ như `requests.get`. File này chỉ import các function, class từ các file khác vào.

### [`api.py`](https://github.com/psf/requests/blob/v2.28.1/requests/api.py)
Các function tiện lợi requests.get requests.post ... đều nằm trong api.py. File này chứa các function ứng với các HTTP verb/method, và chỉ có vậy. Code cũng rất đơn giản:

```py
def request(method, url, **kwargs):
    with sessions.Session() as session:
        return session.request(method=method, url=url, **kwargs)


def get(url, params=None, **kwargs):
    """... đã bỏ comment cho ngắn"""
    return request("get", url, params=params, **kwargs)
```

`get` thực chất chỉ gọi `request`, function `request` tạo một Session và dùng nó để kết nối HTTP qua `session.request`.

### [sessions.py](https://github.com/psf/requests/blob/v2.28.1/requests/sessions.py#L355) - chứa class Session, trái tim của requests
Một Session sẽ chứa đủ thông tin cần thiết như url, headers, auth, proxy, ... rồi thực hiện gọi tới HTTP adapter để thực hiện kết nối.

### [adapters.py](https://github.com/psf/requests/blob/v2.28.1/requests/adapters.py#L101) - nơi kết nối thực sự xảy ra
Dù là thực hiện kết nối HTTP thì trên Python cũng có rất nhiều thư viện, từ thư viện có sẵn của Python stdlib cho tới thư viện bên ngoài và dùng mặc định cho requests: urllib3. Function [`send`](https://github.com/psf/requests/blob/v2.28.1/requests/adapters.py#L436) trong adapters thực hiện kết nối với "Request" được chuẩn bị, và trả về Response. Code của send dài 150 dòng, không có gì quá phức tạp.

Còn gì không? còn nhiều và bạn có thể tự khám phá, nhưng từng ấy cũng đủ vừa sâu để hiểu rõ hơn về requests, hơn hàng ngàn lập trình viên ngoài kia rồi.

Happy deeeeeep hacking.

Hết.

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
