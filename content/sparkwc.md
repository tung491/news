title: PySpark đi phỏng vấn đếm từ count words
date: 2021-09-19
modified: 2021-09-19
tags: Spark, PySpark, word count, interview question
category: news
slug: sparkwc
authors: Pymier0
description: Dùng Python có sẵn Counter, giải bài này PySpark

Word-count là 1 bài phỏng vấn kinh điển trong ngành IT, nó không quá khó/thuật toán/thách đố, mà lại rất thực tế, yêu cầu đủ các kiến thức cần có để viết code:

- dùng dictionary 
- viết vòng lặp for
- có thể cần viết if
- xử lý string
- sort (sắp xếp) kết quả bằng dict value
- đọc file (IO)

![img](https://images.unsplash.com/photo-1598210854169-af04499e4899?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2MzIwMjY5Mzk&ixlib=rb-1.2.1&q=80&w=600)

Nó không quá dễ/beginner như [FizzBuzz](https://en.wikipedia.org/wiki/Fizz_buzz), hoàn toàn có thể làm bài test "số 2" sau khi ứng viên giải bài FizzBuzz sau 5 phút, cũng không quá khó/thuật toán kiểu "leetcode.com", nên có thể dành test cho cả non-developer (như Sysadmin/devops/QA...) lẫn developer (PS: tác giả bài viết trong link cuối bài là người phỏng vấn các kỹ sư tại Canonical - công ty đứng sau Ubuntu). Python giải bài này dùng dict rất đơn giản, thậm chí cực đơn giản khi có sẵn kiểu Counter:

```py
In [42]: from collections import Counter

In [56]: t = "ga meo Bo meo bo meo"

In [57]: Counter(t.lower().split()).most_common(10)
Out[57]: [('meo', 3), ('bo', 2), ('ga', 1)]
```

dùng sẵn chuẩn Pythonic vậy nên khi đi phỏng vấn, nhiều khi bị coi là "hack"/"cheat", bắt phải tự viết bằng dict:

```py
In [47]: t = "ga meo Bo meo bo meo"

In [48]: d = {}

In [49]: for word in t.lower().split():
    ...:     d[word] = d.get(word, 0) + 1
    ...: 

In [55]: sorted(d.items(), key=lambda e: e[1], reverse=True)[:10]
Out[55]: [('meo', 3), ('bo', 2), ('ga', 1)]
```

Giải bằng PySpark thì sao?

import và tạo kết nối đến Spark rồi đọc file text vào:

```py
In [1]: from pyspark.sql import SparkSession

In [2]: spark = SparkSession.builder.getOrCreate()
...
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use set

In [3]: text = spark.read.text("kjvbible.txt")
```

File kjvbible.text nặng 4.2MB tải từ 
https://github.com/benhoyt/countwords/raw/master/kjvbible.txt

Mỗi dòng sẽ được cho vào thành 1 row trong cột "value":

```py
In [60]: text.printSchema()
root
 |-- value: string (nullable = true)

In [64]: text.show(10)
+--------------------+
|               value|
+--------------------+
|The Old Testament...|
|                    |
|                    |
|                    |
|                    |
|The First Book of...|
|                    |
|                    |
|1:1 In the beginn...|
|                    |
+--------------------+
```

Biến thành chữ thường (lower) rồi cắt thành các từ sử dụng split, split ở đây khác với string method split của Python, đây thực chất là split của Java string, nó nhận vào 1 regex pattern, ở đây dùng "\s+" tức 1 hay nhiều ký tự whitespace (space, tab, newline):

```py
In [65]: from pyspark.sql.functions import *

In [69]: text.select(split(lower(text.value), "\s+")).show(10)
+----------------------------+
|split(lower(value), \s+, -1)|
+----------------------------+
|        [the, old, testam...|
|                          []|
|                          []|
|                          []|
|                          []|
|        [the, first, book...|
|                          []|
|                          []|
|        [1:1, in, the, be...|
|                          []|
+----------------------------+
```

Thay vì mỗi string ban đầu ở mỗi dòng, giờ ta có list (spark/Java gọi là array) các string ở mỗi dòng. Cần nối các list này lại với nhau rồi biến cái list đó thành các dòng. 

```py
[1,2,3] 
[4,5,6]

=> [1,2,3] + [4,5,6] == [1,2,3,4,5,6] => các dòng 1,2,3,4,5,6.
```

Function `explode` thực hiện việc này:

```py
In [70]: text.select(explode(split(lower(text.value), "\s+"))).show()
+---------+
|      col|
+---------+
|      the|
|      old|
|testament|
|       of|
```

Giờ đặt lại tên cột cho hay với alias, bỏ đi các dòng empty, rồi nhóm (groupBy) các từ giống nhau lại, rồi đếm (count), sắp xếp theo từ nào có count nhiều nhất, giảm dần, lấy 10 từ top:

```py
In [97]: text.select(explode(split(lower(text.value), "\s+")).alias("word")).filter("word != ''").groupBy("word").count().sort("count", ascending=False).show(10)
+-----+-----+                                                                   
| word|count|
+-----+-----+
|  the|64015|
|  and|51313|
|   of|34634|
|   to|13567|
| that|12784|
|   in|12503|
|   he|10261|
|shall| 9838|
| unto| 8987|
|  for| 8810|
+-----+-----+
only showing top 10 rows

```

Kết quả trùng khớp với https://github.com/benhoyt/countwords/blob/master/output.txt (x10 - do trong repo họ tạo file text 10 lần).

Tham khảo:

https://benhoyt.com/writings/count-words/

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
