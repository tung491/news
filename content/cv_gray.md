title: OpenCV đọc ảnh đen trắng (grayscale)
date: 2022-04-11
modified: 2022-04-11
tags: opencv, opencv-python, image, grayscale, crop
category: news
slug: grayscale
authors: Pymier0
description: đọc ảnh màu, biến thành đen trắng, cắt.

Ảnh màu trên máy tính thường sử dụng hệ màu red-green-blue (đỏ - xanh lục - xanh lam) viết tắt là RGB. Bộ màu này có khả năng biểu diễn 256 * 256 * 256 = 16777216 (16 triệu màu), mặc định OpenCV đọc ảnh vào ở dạng ảnh màu. Xem shape của ảnh sau khi đọc thường có dạng (dài, rộng, 3).
 
![img](https://images.unsplash.com/photo-1543739839-be746050f5b7?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2NDk2ODgzODA&ixlib=rb-1.2.1&q=80&w=600)

Ảnh đen trắng (gọi là grayscale), chỉ có 256 màu từ 0 đến 255 (từ đen tới bớt đen tới trắng). Khi đọc vào, sẽ chỉ thấy shape của array (dài, rộng).

```py
import cv2 as cv

cim = cv.imread("/home/hvn/Pictures/anhmau.jpeg")  # cv.IMREAD_COLOR
print(cim.shape)
# (1068, 600, 3)

gim = cv.imread("/home/hvn/Pictures/anhmau.jpeg", cv.IMREAD_GRAYSCALE)
print(gim.shape, "To new crop size: ", gim.shape[0]//2, gim.shape[1]//2)
#(1068, 600) To new crop size:  534 300

cut = gim[:gim.shape[0]//2, :gim.shape[1]//2]
cv.imwrite("gray.jpg", cut)
```

Kết quả thu được 1/4 góc trên trái bức ảnh ban đầu, đen trắng:

![grayscale]({static}/images/gray.jpg).

Hết.

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
