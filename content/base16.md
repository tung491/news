title: Base16 là gì? base là gì?
date: 2022-02-19
modified: 2022-02-19
tags: Base16, hex, crypto
category: news
slug: base16
authors: Pymier0
description: Ít khi nghe với cái tên Base16, nhưng hex thì rất phổ biến

![img](https://images.unsplash.com/photo-1542722140-13cfa09585c7?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2NDUyNDM2ODk&ixlib=rb-1.2.1&q=80&w=600)

Bài trước giới thiệu [Base64]({filename}/base64.md) vì nó sử dụng 64 ký tự A-Za-z0-9+/ để biểu diễn binary data tùy ý.
Ngoài Base64, trong tài liệu định nghĩa Base64 còn nhắc tới: Base16, Base32, and Base64.

## Base16
Base16 sử dụng 16 ký tự để biểu diễn binary: 0-9a-f (hoặc viết hoa 0-9A-F) hay còn có tên gọi phổ biến là hex. Mỗi 8bits (1byte) sẽ được chia làm 2 phần 4 bits, mỗi 4 bits có khả năng biểu diễn 2**4 == 16 giá trị.

```py
>>> hex(2022)
'0x7e6'
>>> bin(2022)
'0b11111100110'
```

Chia bit ra thành các nhóm 4:

'111-1110-0110'
111 chưa đủ 4, thêm số 0 vào trước không thay đổi ý nghĩa.

- 0111 là 7
- 1110 là e
- 0110 là 6

hex của giá trị số nguyên 2022 là 7e6.

Để đổi từ string biểu diễn hex về int, dùng `int`

```py
>>> int('0x7e6', 16)
2022
```

Chú ý function hex chỉ nhận đầu vào là số int.
Trong khi Base16 có thể biểu diễn mọi giá trị, ta cần dùng thư viện base64:

```py
>>> base64.b16encode(b'PyMi.vn')
b'50794D692E766E'
>>> base64.b16decode(b'50794D692E766E')
b'PyMi.vn'
```

Các function này nhận đầu vào là các bytes, nên không cho số vào trực tiếp được:

```py
>>> base64.b16encode(2022)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.8/base64.py", line 250, in b16encode
    return binascii.hexlify(s).upper()
TypeError: a bytes-like object is required, not 'int'
```

Có thể đổi từ int qua byte bằng method `.to_bytes()`

```py
>>> base64.b16encode((2022).to_bytes(2, 'big'))
b'07E6'
>>> base64.b16encode((2022).to_bytes(2, 'little'))
b'E607'
```

```
 |  to_bytes(self, /, length, byteorder, *, signed=False)
 |      Return an array of bytes representing an integer.
```

'big' hay 'little' là viết tắt của big-endian, và little-endian, thứ tự sắp xếp các byte trên máy tính.

Để kiểm tra máy mình dùng order nào gõ:

```py
>>> import sys
>>> sys.byteorder
'little'
```

```py
>>> base64.b16encode((2022).to_bytes(2, 'big'))
b'07E6'
>>> base64.b16encode((2022).to_bytes(2, 'little'))
b'E607'
```

Thứ tự giống như việc người Việt đọc truyện tranh từ trái qua phải thì người Nhật đọc từ phải qua trái, không có kiểu nào là "sai" cả. Trên máy tính cũng vậy, dùng little hay big đều không "sai". Ngày nay đa số đều dùng little-endian, tức viết phần nhỏ (little) trước mới đến phần to. Ví dụ số nguyên 1002, thì số 1 ở đây có ý nghĩa là 1000, được viết trước, rồi đến 0, 0, 2, đây là kiểu big-endian.

2022 khi viết thành dạng binary: '111-1110-0110'

- 0111 là 7
- 1110 là e
- 0110 là 6

Ta viết phần nhỏ trước, mỗi lần lấy 1 byte (== 8bits == 2 nhóm 4 bits), vậy có E6, rồi 07 => E607.

PS: [bitcoin cũng dùng little-endian](https://learnmeabitcoin.com/technical/little-endian)

## Base

```py
>>> help(int)
int(x, base=10) -> integer
```

Base là hệ cơ số, hệ nhị phân là base 2, hệ bát phân (oct) là base 8, hệ thập phân (decimal) là base 10, hex là hệ base 16.

Hết.

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
