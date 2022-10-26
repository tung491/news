title: Python 3.10 integer lớn tùy ý, nhưng không còn in được ra màn hình
date: 2022-10-26
modified: 2022-10-26
tags: python, changes, CVE, DOS, int, str
category: news
slug: int2str
authors: Pymier0
description: sự thật hôm qua không thật đến hôm nay 

Chỉ có sự thay đổi là cố định. Đặc biệt trong ngành IT, sau mỗi [2 năm CPU "nhanh" gấp đôi](https://en.wikipedia.org/wiki/Moore%27s_law), công nghệ 2 3 năm lại thay đổi, thì những thứ đúng hôm qua, hôm nay càng chưa chắc còn đúng.

![img](https://images.unsplash.com/photo-1537949721120-e8f21f6698e6?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2NjY3OTU0MTA&ixlib=rb-4.0.3&q=80&w=600)

Vào bài học đầu tiên của lớp [PYMI2210]({filename}/pymi2210.md), học viên được xõa thoải mái với integer (số nguyên), cộng trừ nhân chia thì tự dưng phép lũy thừa lại bị không thoải mái:

```py
Python 3.10.8 (main, Oct 25 2022, 05:28:56) [GCC 10.2.1 20210110] on linux
>>> 10**4301
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: Exceeds the limit (4300) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
```

Phản ứng duy nhất của bạn chỉ có thể là "WTF", sau hơn 40 khóa dạy học Python, thì đây là lần đầu tiên nhìn thấy điều này. Vậy nên nhớ rằng kiến thức cũng chỉ là nhất thời, sự thật hôm qua không thật đến ngày mai.

Đây là một thay đổi liên quan đến [security trong Python 3.10.7](https://docs.python.org/3/whatsnew/3.10.html#notable-security-feature-in-3-10-7), tức thậm chí Python 3.10.6 cũng chưa có, nó nằm tít dưới cùng trong doc release của 3.10: 

> Converting between int and str in bases other than 2 (binary), 4, 8 (octal), 16 (hexadecimal), or 32 such as base 10 (decimal) now raises a ValueError if the number of digits in string form is above a limit to avoid potential denial of service attacks due to the algorithmic complexity. This is a mitigation for CVE-2020-10735. This limit can be configured or disabled by environment variable, command line flag, or sys APIs. See the integer string conversion length limitation documentation. The default limit is 4300 digits in string form.

Vì biến đổi từ int, sang string để in ra màn hình, khi số đủ lớn, có thể khiến hệ thống bị quá tải, dẫn tới có thể bị tấn công "DOS". Nên từ bản 3.10.7 trở đi, số có hơn **4300** chữ số sẽ không được in ra màn hình nữa, muốn in phải chỉnh qua "import sys".

```py
>>> x = 10**4301
>>> x // 100
100....
```

Tính thì vẫn tính thoải mái, nhưng mặc định không in được số lớn vậy ra màn hình.

Hết.

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
