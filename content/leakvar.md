title: Python leak var
date: 2022-08-10
modified: 2022-08-10
tags: bug, variable, feature, exp
category: news
slug: leakvar
authors: Pymier0
description: rồi sẽ có ngày bạn gặp bug

![img](https://images.unsplash.com/photo-1645220305088-85956fc0d482?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2NjAxNDAwODM&ixlib=rb-1.2.1&q=80&w=600)

Python có một "tính năng" rất bất ngờ nếu bạn đã lập trình các ngôn ngữ khác:

```py
i = "Bánh Trung Thu"
for i in range(5):
    print(i)

print(i)  # cái này hiện ra gì?
```
tất cả các i trong đoạn code trên đều là 1 i, đầu tiên nó là string, sau đó được gán cho các số 0 tới 4, sau vòng for nó... giữ giá trị cuối cùng: 4

Tính năng này không có ở hầu hết các ngôn ngữ lập trình khác, và thậm chí với Python, nó cũng là 1 bug, nhưng vì đã tồn tại quá lâu và không thể sửa mà không ảnh hưởng tới các đoạn code đã tồn tại, nên người ta giữ nó, coi như 1 tính năng.

Tính năng này sẽ có ngày khiến bạn vò đầu bứt tai, càng dễ gặp khi làm đúng các best practice đặt tên có nghĩa. Ví dụ:

```py
name = "ABC"
send_to_slack = True
send_to_telegram = True
if send_to_slack:
    ...
    for name in names:
        send_message_to(name)

...
#10 dòng sau
...
...

if send_to_telegram:
    ...
    do_something_with_name(name)

```

Việc dùng `name` trong vòng lặp for vô tình đã thay mất giá trị của `name` đã
có trước, và chỉ ảnh hưởng tới câu if số 2 nếu câu if số 1 được chạy.

Một lỗi không luôn xảy ra, cũng không dễ dàng nhìn ra.

Kết luận: best practice không phải lúc nào cũng best, dùng biến `i` hay `n` cho vòng lặp là OK.

TRÁNH dùng lại tên biến.

Ví dụ:

```py
students = ["Pikachu", "Doremon"]
students = ",".join(students)
```

Hết.

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
