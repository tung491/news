title: Tìm kiếm trong dict nhanh gấp list hàng ngàn lần
date: 2021-11-06
modified: 2021-11-06
tags: dict, list, timeit, speed, bigO
category: news
slug: dictvslist
authors: Pymier0
description: Dictionary tối ưu cho việc tìm kiếm

Python rất dễ dùng, để tìm kiếm chỉ cần gõ: `i in X`
dù X là list, dict, set, str, tuple đều chạy.

Code giống nhau, nhưng cách chạy thì khác nhau. Viết `i in List` so với
`i in Dict` hoặc `i in Set` có tốc độ khác nhau rất nhiều.

![img](https://images.unsplash.com/photo-1624724585603-967eb2073e03?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2MzYxNzA5Nzk&ixlib=rb-1.2.1&q=80&w=600)

`i in List`: list là 1 array/list, để tìm 1 giá trị, Python sẽ kiểm tra lần
lượt từng giá trị từ đầu tới cuối cho đến khi tìm thấy. Tức trường hợp xấu nhất,
khi không thấy, Python phải kiểm tra hết `len(List)` phần tử. Số lần kiểm tra
tỷ lệ thuận với số phần tử, gọi là có độ phức tạp thuật toán về thời gian `O(n)`.

Dùng timeit để đo:

```py
$ python3 -m timeit -s 'n=10_000; L=list(range(n))' 'n in L'
5000 loops, best of 5: 55.2 usec per loop
$ python3 -m timeit -s 'n=100_000; L=list(range(n))' 'n in L'
500 loops, best of 5: 569 usec per loop
```

Thấy khi list có 100_000 phần tử, trường hợp xấu nhất sẽ chậm hơn 10 lần so với
list có 10_000 phần tử.

Kiểu dict được tối ưu cho việc tìm kiếm (nên đặt tên là dictionary), việc tìm
kiếm diễn ra "tức thì", không quan tâm dict lớn đến đâu. Việc tìm kiếm với tốc
độ cố định này gọi là thuật toán có độ phức tạp hằng số (constant), hay `O(1)`:

```py
$ python3 -m timeit -s 'n = 10_000; D = {i: i**2 for i in range(n)}' 'n in D'
20000000 loops, best of 5: 17.7 nsec per loop
$ python3 -m timeit -s 'n = 100_000; D = {i: i**2 for i in range(n)}' 'n in D'
20000000 loops, best of 5: 18.3 nsec per loop
```

Trường hợp đầu tiên với 10_000, tìm trong dict nhanh hơn trong list 3000 lần,
trường hợp thứ 2 là 30_000 lần.

Khi cần tìm kiếm, nhớ dùng dict (và set).


Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
