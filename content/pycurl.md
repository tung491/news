title: http dùng requests?  pycurl nhanh gấp 2!
date: 2023-04-04
modified: 2023-04-04
tags: python, requests, curl, pycurl, http
category: news
slug: pycurl
authors: Pymier0
description: thư viện cực phổ biến nhưng ít dùng trong thế giới Python

![curl](https://curl.se/logo/curl-logo.svg)

### curl - câu lệnh HTTP client phổ biến nhất
Đó là điều không phải bàn cãi. Đa phần các lập trình viên hay các devops/sysadmin đều ít nhiều biết dùng curl.

Cài đặt: `sudo apt install curl`

```py
$ curl -XGET https://httpbin.org/get
{
  "args": {},
  "headers": {
    "Accept": "*/*",
    "Host": "httpbin.org",
    "User-Agent": "curl/7.68.0",
    "X-Amzn-Trace-Id": "Root=1-642c2f63-1e6528c964ff9d9b39d7dc7f"
  },
  "origin": "14.1.11.1",
  "url": "https://httpbin.org/get"
}
```

Chương trình này sử dụng thư viện lo tất cả bên dưới: libcurl

```sh
$ ldd `which curl` | grep curl
	libcurl.so.4 => /lib/x86_64-linux-gnu/libcurl.so.4 (0x00007f0a91282000)
```

`libcurl` có "binding" cho hầu hết tất cả các ngôn ngữ lập trình.

Đếm đơn giản có hơn 50 ngôn ngữ: PHP, Java, C, Rust, ... và cả Python

```sh
$ curl https://curl.se/libcurl/bindings.html | grep '<a href="http' -c
57
```

### pycurl - code dài x2 nhưng nhanh cũng x2 lần requests

requests phổ biến nhờ API dễ dùng requests.get requests.post ... viết hoàn tòan bằng Python. Ưu điểm này cũng chỉ ra yếu điểm của Python: chậm khi so với C.

Nếu viết 1 script gọi 10 requests nhỏ nhỏ chạy cỡ 10s, viết lại bằng pycurl có thể mất 5s, việc này không có gì đáng kể, nên vẫn sẽ dùng requests.

Nhưng với chương trình phải GET/POST hàng trăm ngàn requests mỗi giờ, hay gửi vài GB/TB, thay pycurl sẽ mang lại cải thiện đáng kể.
Benchmark tại trang chủ pycurl: <https://github.com/svanoort/python-client-benchmarks>

Giải thích khi nào dùng pycurl vs request <http://pycurl.io/docs/latest/index.html#pycurl-vs-requests>

Ví dụ đơn giản với 3 dòng requests và 10 dòng pycurl:

Trên Ubuntu 20.04 cài đặt:

```
sudo apt install -y libcurl4-openssl-dev
```

```
python3 -m venv cenv
. cenv/bin/activate
python3 -m pip install pycurl requests
```

#### requests ngắn và chậm

```py
import requests
r = requests.get("https://pymi.vn")
print(r.text[:200])
```

Tốc độ:

```
$ /usr/bin/time -v python3 req.py
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Học lập trình Python — PyMI.vn</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta name="descri
	Command being timed: "python3 req.py"
	User time (seconds): 0.10
	System time (seconds): 0.01
	Percent of CPU this job got: 20%
	Elapsed (wall clock) time (h:mm:ss or m:ss): 0:00.58
	Average shared text size (kbytes): 0
	Average unshared data size (kbytes): 0
	Average stack size (kbytes): 0
	Average total size (kbytes): 0
	Maximum resident set size (kbytes): 23152
```


#### pycurl dài và nhanh

```py
import pycurl
from io import BytesIO
buff = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, 'https://pymi.vn')
c.setopt(c.WRITEDATA, buff)
c.setopt(c.HTTPHEADER, ['User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0/8mqLkJuL-86'])
c.perform()
c.close()
body = buff.getvalue()
print(body.decode()[:200])
```

Tốc độ

```html
$ /usr/bin/time -v python3  curl.py
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Học lập trình Python — PyMI.vn</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta name="descri
	Command being timed: "python3 curl.py"
	User time (seconds): 0.05
	System time (seconds): 0.00
	Percent of CPU this job got: 9%
	Elapsed (wall clock) time (h:mm:ss or m:ss): 0:00.60
	Average shared text size (kbytes): 0
	Average unshared data size (kbytes): 0
	Average stack size (kbytes): 0
	Average total size (kbytes): 0
	Maximum resident set size (kbytes): 20576
```

PS: tuy "khó dùng" hơn requests, một khi biết dùng, có thể dùng ở ~50 ngôn ngữ khác nhau là một lợi thế không hề nhỏ của libcurl.

### Kết luận
Ngắn chậm hay dài nhanh? sự lựa chọn là của bạn.

Hết.

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
