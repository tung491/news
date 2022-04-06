title: Xin chào opencv-python
date: 2022-04-06
modified: 2022-04-06
tags: cv2, opencv, image
category: news
slug: cv2
authors: Pymier0
description: cài đặt opencv cho Python, đọc và ghi file ảnh

![img](https://images.unsplash.com/photo-1459255418679-d6424da9ee33?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2NDkyNTUwMjY&ixlib=rb-1.2.1&q=80&w=600)

OpenCV (https://opencv.org/)

> OpenCV (Open Source Computer Vision Library: http://opencv.org) is an open-source library that includes several hundreds of computer vision algorithms.

là một thư viện xử lý hình ảnh (ảnh, video, ...) viết bằng C++ nhưng có thể dùng từ nhiều ngôn ngữ khác nhau, trong Python, cài

```
pip install opencv-python
```

sau đó để dùng `import cv2 as cv`.

### Mở file ảnh

```py
img = cv.imread("/home/hvn/Pictures/python-logo.png")
print(type(img))
# Output: <class 'numpy.ndarray'>
```
Vậy một file ảnh trong OpenCV chính là 1 ndarray của numpy.

### Ghi file

```py
cv.imwrite("filename.png", img)
```

## Tham khảo
- https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html

Hết.

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
