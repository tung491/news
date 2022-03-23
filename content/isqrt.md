title: Tính căn số lớn
date: 2022-03-23
modified: 2022-03-23
tags: float, sqrt, math, big number, isqrt
category: news
slug: big_float
authors: Pymier0
description: số kiểu int lớn tùy ý, tính toán thỏa thích, float thì sao? 

![img](https://images.unsplash.com/photo-1594013755115-76c4fe78b165?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2NDgwMzg1Nzg&ixlib=rb-1.2.1&q=80&w=600)

Trong Python, kiểu int có độ lớn tùy ý, như 2 mũ 2048:

```py
>>> b = 2**2048
>>> b
32317006071311007300714876688669951960444102669715484032130345427524655138867890893197201411522913463688717960921898019494119559150490921095088152386448283120630877367300996091750197750389652106796057638384067568276792218642619756161838094338476170470581645852036305042887575891541065808607552399123930385521914333389668342420684974786564569494856176035326322058077805659331026192708460314150258592864177116725943603718461857357598351152301645904403697613233287231227125684710820209725157101726931323469678542580656697935045997268352998638215525166389437335543602135433229604645318478604952148193555853611059596230656
```

cộng trừ vẫn thoải mái, nhưng... tính căn 2 (hoặc chia) thì sao? 

```py
>>> from math import sqrt
>>> sqrt(b)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
OverflowError: int too large to convert to float
```

Nội dung error cho thấy số này quá lớn để biến thành kiểu float (kết quả của phép chia, căn đều là float). Giải pháp là dùng math.isqrt

```py
>>> from math import isqrt
>>> isqrt(b)
179769313486231590772930519078902473361797697894230657273430081157732675805500963132708477322407536021120113879871393357658789768814416622492847430639474124377767893424865485276302219601246094119453082952085005768838150682342462881473913110540827237163350510684586298239947245938479716304835356329624224137216
>>> isqrt(b) == 2**1024
True
```


Docstring: 

```py
isqrt(n, /)
    Return the integer part of the square root of the input.
```

kết quả không chắc CHÍNH XÁC là căn 2 (bởi không phải căn 2 số nào cũng là số nguyên), nên cần test lại nếu bình phương kết quả có bằng số ban đầu không.

```py
>>> isqrt(10)
3
>>> 3 ** 2 == 10
False

>>> 2**1000/2
5.357543035931337e+300
>>> isqrt(2**1000) ** 2 == 2**1000
True
```

Hết.

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
