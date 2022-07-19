title: [hack] Biến đổi giữa các kiểu số thành byte
date: 2022-07-19
modified: 2022-07-19
tags: hack, binary, byte, hex
category: news
slug: byt351
authors: Pymier0
description: Hacker 101 - bài học vỡ mộng để trở thành h4x0r

![img](https://images.unsplash.com/photo-1577507801612-5e6e0200774f?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2NTgyMzcwMDA&ixlib=rb-1.2.1&q=80&w=600)

Hệ thập phân (hệ số 10) là hệ số dùng phổ biến nhất ở loài người, 1,2,3,4,5,6,7,8,9...0 đều học
từ lớp 1 2 3.

Máy tính biểu diễn mọi thứ ở hệ nhị phân (hệ số 2) với số 0 và 1, gọi là binary.

Trên máy tính còn dùng các hệ khác như octal, hex và chúng đều có thể biểu diễn
chung ở 1 dạng gọi là byte.

### bit
bit là đơn vị nhỏ nhất trên máy tính, bit có thể có 2 giá trị 0 và 1. Số khi
biểu diễn ở dạng bit viết thành binary: 10010101011

Trên Python, có thể viết 0b rồi gõ giá trị, ví dụ: 0b101010 là dạng binary của số 42.

```py
>>> 0b101010 == 42
True
```

Có thể biến 42 thành str (string) biểu diễn dạng binary với function bin:

```py
>>> bin(42)
'0b101010'
```

Và biến ngược lại từ str thành số 10:

```py
>>> int('101010', base=2)
42
```

### byte
Vì bit quá nhỏ, để viết được số 255 cần tới 8 bit: 11111111 rất dài dòng và
tốn giấy mực, nên người ta đổi 8 bits thành 1 byte. 1 byte có thể biểu diễn
bất kỳ giá trị trong khoảng 0-255 (2 mũ 8).

```py
>>> x = 254
>>> x.bit_length()
8
>>> x.to_bytes(length=1, byteorder='little')
b'\xfe'
>>> x.to_bytes(length=1, byteorder='big')
b'\xfe'
```

bytes là kiểu dữ liệu trên python để biểu diễn các... byte. bytes được ký hiệu bằng chữ
b trước nội dung tương tự kiểu string.

```py
>>> b'python'
b'python'
>>> type(b'python')
<class 'bytes'>
>>> [i for i in b'python']
[112, 121, 116, 104, 111, 110]
>>> [ord(c) for c in 'python']
[112, 121, 116, 104, 111, 110]
```
Khi duyệt qua từng byte, chúng là các giá trị số int.

Khi in ra, các giá trị không có dạng ký tự biểu diễu như 0 1 2 hay a b c ?<>.,+ ...
sẽ được biễu diễn bằng ký hiệu b'\x1f` với 1f là dạng hex của byte này.

```py
>>> bytes(range(256))
b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff'
```

### hex
byte là đơn vị máy tính sử dụng, thì hex là giá trị
con người sử dụng, để dễ dàng biểu diễn byte.
Hex là hệ gồm 16 số 0123456789abcdef, với a = 10, b = 11,... f = 15.
Có thể thấy một sự trùng hợp không hề ngẫu nhiên:

- 256 == 2 mũ 8
- 16 == 2 mũ 4
- Các giá trị từ 0 đến 255 có thể biểu diễn ở dạng hex với 2 ký tự.

Trên Python:

```py
>>> 0xfe == 254
True
```

Đổi từ số sang hex string, và ngược lại:

```
>>> hex(254)
'0xfe'
>>> int('fe', base=16)
254
```

### đổi byte sang hex

```
>>> x = b'python'
>>> x.hex()
'707974686f6e'
>>> bytes.fromhex('707974686f6e')
b'python'
```

Giải 1 bài trong giải CTF [imaginaryctf 2022](https://ctftime.org/event/1670):

Đoạn ký tự này mã hóa cái gì?

```py
s = '👎👍👍👎👍👎👎👍👎👍👍👎👎👎👍👍👎👍👍👍👎👍👎👎👎👍👍👎👎👍👍👎👎👍👍👍👍👎👍👍👎👍👍👎👎👍👎👍👎👍👍👎👍👍👍👎👎👍👍👎👎👎👍👍👎👎👍👍👎👎👎👎👎👍👍👎👎👍👎👎👎👍👍👎👍👎👎👍👎👍👍👎👍👍👍👎👎👍👍👎👎👍👍👍👎👍👎👍👍👍👍👍👎👍👍👎👍👎👎👍👎👍👍👍👎👎👍👍👎👍👎👍👍👍👍👍👎👍👍👎👍👍👍👎👎👎👍👍👎👎👎👎👎👍👍👍👎👍👎👎👎👍👎👍👍👍👍👍👎👍👍👎👎👍👎👍👎👍👍👎👍👍👍👎👎👍👍👎👎👎👍👍👎👍👍👍👎👎👍👎👎👍👍👍👍👎👎👍👎👍👍👍👎👎👎👎👎👍👍👍👎👍👎👎👎👍👍👎👍👎👎👍👎👎👍👍👎👎👎👎👎👍👍👎👍👍👍👎👎👍👎👍👍👍👍👍👎👎👍👍👎👎👎👍👎👍👍👎👎👎👍👎👎👎👍👍👎👎👍👎👎👍👍👎👎👍👎👍👎👎👍👍👎👎👎👎👎👍👍👎👎👍👎👎👎👎👍👍👎👍👎👎👎👎👍👍👎👎👍👍👎👍👍👍👍👍👎👍'
```

Đoán 1 chút, dấu 👎 đại diện cho số 0, dấu 👍 đại diện cho số 1,
biến thành string 0, 1 rồi đổi thành số hệ 10, sau đó đổi sang hex, và biến thành bytes:

```py
b = ''.join('1' if i == '👍' else '0' for i in s)
print(b)
# 0110100101100011011101000110011001111011011001010110111001100011001100000110010001101001011011100110011101011111011010010111001101011111011011100011000001110100010111110110010101101110011000110111001001111001011100000111010001101001001100000110111001011111001100010110001000110010011001010011000001100100001101000011001101111101
fromhex.bytes(hex(int(b, 2))[2:])
# b'ictf{enc0ding_is_n0t_encrypti0n_1b2e0d43}'
```

Thấy thú zị??? tham khảo thêm các writeup của Pymi tại [https://github.com/pymivn/ctf](https://github.com/pymivn/ctf)

Tham gia team CTF PYMI qua [Slack pymi](https://pymi-invite.fly.dev/) #ctf nha

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
