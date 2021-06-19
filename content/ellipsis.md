title: Tôi muốn ... em
date: 2021-06-19
modified: 2021-06-19
tags: features
category: news
slug: ellipsis
authors: Pymier0
description: Python cũng có thể rất mập mờ với dấu 3 chấm: ...

`...` là một keyword hợp lệ trong Python, đã có từ rất lâu, và rất ít được biết
tới.

![img](https://images.unsplash.com/photo-1560336767-9bb468f204c0?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2MjQwNzMxNzQ&ixlib=rb-1.2.1&q=80&w=600)

`...` trong tiếng Anh là Ellipsis, trong Python có thể viết 1 trong 2 giá trị này, chúng có kiểu `ellipsis` chữ e viết thường.

```
>>> x = ...
>>> type(x)
<class 'ellipsis'>
>>> Ellipsis is ...
True
```

Ellipsis dùng để giữ chỗ khi cần, ví dụ khi viết function:

```py
def pikachu():
    ...
```

có tác dụng như

```py
def pikachu()
    pass
```

Mới đây, `...` được trọng dụng trong 1 framework siêu hot mới nổi có tên [FastAPI](https://fastapi.tiangolo.com/tutorial/body-multiple-params/):


```py
def update_item(
    item_id: int, item: Item, user: User, importance: int = Body(...)
)
```


### Ellipsis

> The same as the ellipsis literal “...”. Special value used mostly in conjunction with extended slicing syntax for user-defined container data types.

### Tham khảo
- [https://docs.python.org/3/library/constants.html#Ellipsis](https://docs.python.org/3/library/constants.html#Ellipsis)

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
