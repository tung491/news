title: Django template gọi method không cần ()
date: 2023-07-16
modified: 2023-07-16
tags: python, Django, template, Jinja2
category: news
slug: django-template
authors: Pymier0
description: Flask Jinja2 template gọi method cần (), Django thì không

Python có 2 template engine phổ biến nhất: Jinja2 (hay dùng với Flask, SaltStack, Ansible...) và Django template.

Cả 2 khá giống nhau về cú pháp: viết for/if như Python, dùng function qua các filter có sẵn, đoạn code sau chạy
cho cả 2:

```py
{% for fw in frameworks %}
  {% if fw|length > 5 %}
    <b>{{ fw }}</b>
  {% else %}
    {{ fw }}
  {% endif %}
{% endfor %}
```

nhưng sự khác biệt bắt đầu xuất hiện khi sử dụng method.

### Gọi method trong Django template

Jinja2 sử dụng cú pháp gọi method như Python, kết quả không có gì ngạc nhiên khi gọi `c.items()`:

```py
import jinja2
from collections import Counter

c = Counter("meo meo go".split())
print(jinja2.Template('{{ c.items }}').render(c=c))
# <built-in method items of Counter object at 0x7fbe37ce64b0>
print(jinja2.Template('{% for k, v in c.items() %} {{ k }} {{ v }} {%endfor%}').render(c=c))
#  meo 2  go 1
```


Django template không dùng cú pháp gọi method

```py
{{ counter.items() }}
```

Gặp error:
```py
Could not parse the remainder: '()' from 'counter.items()'
```

Trong tài liệu Django template [topic](https://docs.djangoproject.com/en/4.2/topics/templates/#variables) viết:

> Dictionary lookup, attribute lookup and list-index lookups are implemented with a dot notation:
  ```
  {{ my_dict.key }}
  {{ my_object.attribute }}
  {{ my_list.0 }}
  ```
  If a variable resolves to a callable, the template system will call it with no arguments and use its result instead of the callable.

Khi sử dụng `object.key`, Django sẽ thử tìm `object["key"]`, `object.key` hay nếu key là method, sẽ gọi `object.key`,
vì vậy sẽ phải viết `{{ counter.items }}`.

Chỉ đơn giản là không phải viết `()`, gì mà phức tạp?

### Tìm bug

Cho 1 đoạn Django template, nhận context là 1 [Counter]({filename}/counter.md):

Code `views.py`

```py
from django.shortcuts import render
from collections import Counter
def index(request):
    counter = Counter("red green green red red green green".split())
    for k, v in counter.items():
        print("from counter", k, v)
    return render(request, "index.html", {"d": d, "counter": counter})
```

File `templates/index.html`
```py
{% for k, v in counter.items %}
  {{ k }} {{ v }}<br>
{% endfor %}
```

Xảy ra exception tại dòng for:

```py
TypeError at /

'int' object is not iterable
```

có nghĩa `counter.items` ở đây là một `int` chứ không phải 1 tuple như `dict.items` vẫn trả về.
Khó hiểu hơn nữa, khi phần code tương tự trong function `index` vẫn chạy bình thường, tại sao `counter.items` trong Django template trả về 0?

May mắn thay, tìm `items()` trong tài liệu [reference](https://docs.djangoproject.com/en/4.2/ref/templates/language/) của Django Template viết:

<https://docs.djangoproject.com/en/4.2/ref/templates/language/#variables>

> Technically, when the template system encounters a dot, it tries the following lookups, in this order:
>     Dictionary lookup
>     Attribute or method lookup
>     Numeric index lookup
> If the resulting value is callable, it is called with no arguments. The result of the call becomes the template value.

Cũng giống phần đã viết trong [topic](https://docs.djangoproject.com/en/4.2/topics/templates/#variables), nhưng nhấn mạnh hơn về thứ tự thử:

- tìm kiếm trong dict trước: `object[key]`
- truy cập attribute, method cũng là 1 loại attribute: `object.key`

Trở lại ví dụ, `counter.items` đầu tiên sẽ gọi `counter[items]`,
mà [Counter trả về 0 với item không tồn tại thay vì raise KeyError]({filename}/counter.md), nên kết quả là `0`,
không có lần gọi nào tới method `counter.items()`.

> This lookup order can cause some unexpected behavior with objects that override dictionary lookup. For example, consider the following code snippet that attempts to loop over a collections.defaultdict:
>
> {% for k, v in defaultdict.items %}
>     Do something with k and v here...
> {% endfor %}
>
> Because dictionary lookup happens first, that behavior kicks in and provides a default value instead of using the intended .items() method. In this case, consider converting to a dictionary firs

Xem code tại <https://github.com/django/django/blob/4.2/django/template/base.py#L867-L942>

### Kết luận
Magic không tự xảy ra, muốn dùng magic nhớ đọc doc, hãy thử, đừng đoán.

Hết.

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
