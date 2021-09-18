title: PySpark bigdata giải bài toán ProjectEuler 1
date: 2021-09-18
modified: 2021-09-18
tags: Spark, PySpark, bigdata, data analysis, pandas, PE, projecteuler
category: news
slug: sparkpe1
authors: Pymier0
description: Như Pandas, mà big bao nhiêu cũng được

pandas là công cụ tuyệt vời để xử lý, khám phá dữ liệu dạng bảng như Excel, nó là phần không thể thiếu với các ngành "data analysis", "data science".

pandas có 1 nhược điểm/yêu cầu: là dữ liệu phải nhét vừa vào RAM. Tức nếu có bộ dữ liệu lớn hơn RAM thì sẽ khó/không xử lý được/phải dùng thư viện khác (như dash, etc...)

![img](https://images.unsplash.com/photo-1630011725376-bd68a6403318?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2MzE5NzM5OTY&ixlib=rb-1.2.1&q=80&w=600)

PySpark là 1 giải pháp, Spark đã quá nổi tiếng trong lĩnh vực BigData, thì giờ đây có thể cài, chạy PySpark, gần như Pandas để tính toán dữ liệu, với ưu điểm có thể xử lý song song (nhanh hơn), xử lý được dữ liệu lớn hơn RAM, dùng nhiều máy tính. Người dùng pandas nên biết thêm pyspark để dùng khi cần, chứ không phải để thay thế trong mọi trường hợp.

## Cài đặt
Pandas dùng C ở bên dưới, mà C thì không cần cài gì để chạy cả. 
Spark dùng Java, để chạy phải cài Java Runtime Environment (JRE), trên Ubuntu 20.04 gõ:

```
sudo apt-get update && sudo apt-get install -y  default-jre
```

Tạo 1 venv mới, cài 

```
pip install pyspark
```

## Giải ProjectEuler 1

https://projecteuler.net/problem=1

> Tính tổng các số nhỏ hơn 1000 chia hết cho 3 hoặc 5.

Bật Python trong venv lên và import 

```py
In [1]: from pyspark.sql import SparkSession

In [2]: spark = SparkSession.builder.getOrCreate()
...
Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
```

Tạo dataframe, đầu vào là list của các dòng, mỗi dòng là 1 tuple, do bài này chỉ dùng 1 cột nên tạo tuple 1 phần tử `(i,)`, schema là khái niệm trong SQL database, nói về tên cột (có thể kèm kiểu):

```py
 [10]: df = spark.createDataFrame(((i,) for i in range(1000)), schema=['n'])
```
Giải:

```py
In [12]: df.filter('n % 3 == 0 or n % 5 == 0').agg({'n': 'sum'}).show()
+------+                                                                        
|sum(n)|
+------+
|233168|
+------+
```

`PySpark` không tính toán cho tới khi gọi `show()` hay `collect()`

Bonus: giải bằng pandas:

```py
In [24]: import pandas as pd

In [25]: pdf = pd.DataFrame({'n': range(1000)})

In [26]: pdf.query('n % 3 == 0 or n % 5 == 0').agg({'n': 'sum'})
Out[26]: 
n    233168
dtype: int64
```

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
