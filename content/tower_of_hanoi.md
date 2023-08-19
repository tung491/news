title: Giải bài toán tháp Hà Nội dùng đệ quy
date: 2023-08-19
modified: 2023-08-19
tags: python, algorithm, recursive
category: news
slug: towerofhanoi
authors: Pymier0
description: Phân tích và giải quyết

Tower of Hanoi là một bài toán kinh điển trong ngành khoa học máy tính, được dạy ở mọi trường đại học dạy CNTT ở Việt Nam trong môn "Toán Rời Rạc".

### Tower of Hanoi không phải của người Việt
Tower of Hanoi được phát minh bởi nhà toán học người Pháp Édouard Lucas năm 1883 và ông này không có gốc Việt.

Bài toán phát biểu như sau:

- Cho 3 cái cột, cần chuyển các đĩa từ cột 1 sang cột 3, thông qua cột 2
- Mỗi lần chỉ được chuyển 1 đĩa, đĩa bên dưới phải to hơn đĩa bên trên.

### Bài giải
Hình ảnh minh họa sinh động bài giải:

![solve Tower of Hanoi](https://upload.wikimedia.org/wikipedia/commons/6/60/Tower_of_Hanoi_4.gif)

Phân tích cách viết function đệ quy:

Đặt 3 cột là source (nguồn), dest (đích), tmp (trung gian), function tên move, ban đầu có thể nghĩ function trông như sau:

```py
move(source, dest, tmp)
```

Khi viết recursive function, thường sử dụng các argument để lưu trạng thái (state) function.
Bài toán này có 1 trạng thái là số lượng đĩa còn lại cần chuyển, ban đầu có giá trị là n, khi kết thúc là 0.
Sau mỗi bước chuyển, trạng thái của bài toán được lưu giữ trong số đĩa còn lại và nội dung của mỗi cột.
Vậy function sẽ trở thành

```py
move(n, source, dest, tmp)
```
Có thể cho rằng chỉ cần 3 cột cũng đủ biểu diễn trạng thái của chương trình, không cần tới `n`, và dùng `len(source)` để tính số đĩa còn lại, nhưng khi giải, các cột lần lượt thay đổi vai trò của nhau khiến không thể biết cột nào là cột `source` ban đầu.

```py
A = [3,2,1]
B = []
C = []
def move(n, source, dest, tmp):
    if n > 0:
        move(n-1, source, tmp, dest)
        dest.append(source.pop())
        print(A, B, C, "#####")
        move(n-1, tmp, dest, source)

move(3, A, C, B)
```
(code theo <https://en.wikipedia.org/w/index.php?title=Tower_of_Hanoi&oldid=1139870102#Recursive_implementation>)

Bài toán dừng lại khi n = 0, để move đĩa 3 từ A sang C:

- cần move 2 đĩa trên từ A sang B, dùng C làm trung gian
- rồi chuyển đĩa 3 từ A sang C
- sau đó, chuyển 2 đĩa từ B sang C sử dụng A làm trung gian.

Chú ý `print` A B C chứ không in ra source, dest, tmp, bởi dùng A B C mới giữ được thứ tự các cột.

```
[3, 2] [] [1] #####
[3] [2] [1] #####
[3] [2, 1] [] #####
[] [2, 1] [3] #####
[1] [2] [3] #####
[1] [] [3, 2] #####
[] [] [3, 2, 1] #####
```

### Tham khảo
 <https://en.wikipedia.org/wiki/Tower_of_Hanoi>

### Kết luận
Tháp Hà Nội ở đó, chuyển đi đâu?

Hết.

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
