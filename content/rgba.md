title: rgba == rgb + alpha
date: 2022-04-13 20:00:00
modified: 2022-04-13 20:00:00
tags: opencv, image, opencv-python, RGB, RGBA
category: news
slug: rgba
authors: Pymier0
description: 3 cây chưa đủ thì thêm cây four-th

![img](https://images.unsplash.com/photo-1639898831036-a9d330e25eee?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2NDk4NTkzNDQ&ixlib=rb-1.2.1&q=80&w=600)

[Bài trước]({filename}/3c.md) giới thiệu 3 kênh màu RGB thường dùng để biểu diễn
ảnh màu trên máy tính, với OpenCV dùng hơi ngược 1 chút: BGR.

Ngoài 3 kênh này, ảnh còn có thể có thêm 1 kênh thứ 4 nữa gọi là alpha. Và RGB
giờ sẽ gọi là RGBA.
Kênh alpha cũng chứa giá trị từ 0->255, thể hiện độ "rõ" của ảnh. Gía trị 0 sẽ
trong suốt, giá trị 255 sẽ "không trong tí nào".

Để đọc kênh thứ 4 từ file có kênh này (thường ở định dạng PNG), ta dùng:

```py
import cv2 as cv
img = cv.imread("/home/hvn/Pictures/python-logo.png", cv.IMREAD_UNCHANGED)
print(img.shape)
# (82, 290, 4)
cp = img.copy()
cv.imwrite("alpha.png", cp[:,:, 3])
```
Tương tự bài trước, ta tách kênh alpha này ra riêng 1 file, sẽ thấy kết quả:

![alpha]({static}/images/alpha.png)

Hết.
## Tham khảo
https://en.wikipedia.org/wiki/RGBA_color_model

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
