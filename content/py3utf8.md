title: Python3 str là unicode và rắc rối với UTF-8
date: 2022-07-25
modified: 2022-07-25
tags: Unicode, UTF-8, python2, python3, str, bytes, hack, hex
category: news
slug: py3utf8
authors: Pymier0
description: Một trường hợp print cho kết quả khác nhau giữa python2 và python3

Python3 chỉ có 1 kiểu string là `str`.
Python2 có 2 kiểu string: `str` và `unicode`

Sự hợp nhất này chính là [ưu điểm rất lớn của Python3](https://docs.python.org/3/howto/unicode.html), lập trình viên không phải đau đầu khi chuyển đổi giữa 2 kiểu string. 

Python3 mặc định sử dụng UTF-8, với các giá trị ASCII < 128 (bảng chữ cái tiếng Anh, các số, các dấu) được giữ nguyên kích thước là 1 byte.

- If the code point is < 128, it’s represented by the corresponding byte value.
- If the code point is >= 128, it’s turned into a sequence of two, three, or four bytes, where each byte of the sequence is between 128 and 255.

Cho nên khi viết Python2: print "PyMiEr2022" và Python3 print("PyMiEr2022") cho kết quả như nhau.

Vì một số giá trị char < 128 không phải "ký tự" bình thường, có thể dùng dạng hex để viết nó, ví dụ print "\x13\x37" hay python3 print("\x13\x37") cho kêt quả như nhau.

Nhưng khi viết: python2 `print "\xaa"` so với Python3 `print("\xaa")` kết quả lại **khác nhau**:

```py
$ python2 -c 'print "\xaa"'
�
$ python3 -c 'print("\xaa")'
ª
```

Sử dụng lệnh `hexdump` để nhìn output ở dạng hex:

```py
$ python2 -c 'print "\xaa"' | hexdump 
0000000 0aaa                                   
0000002
 $ python3 -c 'print("\xaa")' | hexdump 
0000000 aac2 000a                              
0000003
```
Python2 tạo ra 2 bytes: 0a (newline xuống dòng) và aa, 
còn Python3 tạo ra tới 4 bytes, trong đó `aa` trở thành `aac2`. Tại sao?

![img](https://images.unsplash.com/photo-1568884149074-a93f17583719?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2NTg3NTQxNzY&ixlib=rb-1.2.1&q=80&w=600)


Lý do bởi 0xaa có giá trị 170 > 128, trên Python3 sẽ được biểu diễn bằng 2 bytes, với aa là giá trị, còn c2 là ký tự "control" để thêm vào cho đủ 2 bytes.

## Tham khảo
- [https://discuss.python.org/t/unusal-behavior-of-python3-print-hex-values/15418/9](https://discuss.python.org/t/unusal-behavior-of-python3-print-hex-values/15418/9)
- [https://docs.python.org/3/howto/unicode.html](https://docs.python.org/3/howto/unicode.html)


Hết. 

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
