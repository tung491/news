title: slice[::-1] là slice[len(slice):0:-1] hay slice[0:len(slice):-1]?
date: 2024-08-19
modified: 2024-08-19
tags: slice
category: pymi.vn
slug: slice_reverse
authors: Pymier0
description: làm thế nào để đảo ngược 1 list?

### Slice là gì
Slice là cú pháp tiện dụng của Python để lấy 1 list con của list đã có.

```py
>>> names = ['c', 'java', 'js', 'php', 'python', 'go', 'rust', 'elixir']
```

Với cú pháp `slice[START:STOP:STEP]`, START và STOP là index bắt đầu và kết thúc,
STEP là bước dịch chuyển của index, để chọn index tiếp theo.

```Py
>>> names[0:len(names):2]
['c', 'js', 'python', 'rust']
>>> names[::2]
['c', 'js', 'python', 'rust']
```

Ở ví dụ trên lấy các phần tử có index 0, 0+2 = 2, 2+2 = 4, 4+2 = 6.

- START khi không ghi cụ thể giá trị trước dấu : có giá trị mặc định là 0
- STOP mặc định là `len(slice)`, tức 8, kết quả 2 biểu thức sau tương đương
- STEP nếu không ghi, mặc định là `1`.

Một tính năng thú vị của slice khiến nhiều người phỏng vấn tỏ ra khó chịu khi hỏi: hãy đảo ngược 1 list/str và câu trả lời là `names[::-1]`.

```
>>> names[::-1]
['elixir', 'rust', 'go', 'python', 'php', 'js', 'java', 'c']
```

Khi sử dụng STEP = -1, cách tính sẽ thế nào?  names[::-1] là phương án a hay b?

- a) names[len(names):0:-1]
- b) names[0:len(names):-1]

### Tìm lời giải slice với step -1 bằng builtin function
Theo reference,

<https://docs.python.org/3/reference/datamodel.html#objects-values-and-types>

Thử sử dụng built-in function `slice` để test 2 trường hợp trên:

```py
>>> S = slice(None, None, -1)
>>> print(S.indices.__doc__)
S.indices(len) -> (start, stop, stride)

Assuming a sequence of length len, calculate the start and stop
indices, and the stride length of the extended slice described by
S. Out of bounds indices are clipped in a manner consistent with the
handling of normal slices.
>>> names = ['c', 'java', 'js', 'php', 'python', 'go', 'rust', 'elixir']
>>> start, stop, step = S.indices(len(names))
>>> print(start, stop, step)
7 -1 -1
```

Câu trả lời là khi step = -1 thì start index là `len(names)-1`, stop index là `-1`. Cả 2 phương án nêu từ đầu đều sai.

### Tìm lời giải slice với step -1 bằng cách đọc code CPython

Tải code Python v3.12.0

```
$ git clone https://github.com/python/cpython --depth 1 --branch v3.12.0 python3120
Cloning into 'python3120'...
...
Resolving deltas: 100% (513/513), done.
Note: switching to '0fb18b02c8ad56299d6a2910be0bab8ad601ef24'.

You are in 'detached HEAD' state. You can look around, make experimental
...
$ du -csh python3120
136M	python3120
136M	total
$ cd python3120
```
Tìm file code C chứa từ khóa `slice`:

```
$ grep -Rin 'slice' -l | grep -F .c
Python/ast_opt.c
Python/import.c
Python/Python-ast.c
Python/compile.c
...
Objects/sliceobject.c
Objects/bytes_methods.c
Objects/listobject.c
...
```

trong file `sliceobject.c`:
```c
/* Implementation of slice.indices. */

static PyObject*
slice_indices(PySliceObject* self, PyObject* len)
{
    PyObject *start, *stop, *step;
    ...
    error = _PySlice_GetLongIndices(self, length, &start, &stop, &step);
    ...
}
...

int
_PySlice_GetLongIndices(PySliceObject *self, PyObject *length,
                        PyObject **start_ptr, PyObject **stop_ptr,
                        PyObject **step_ptr)
{
    /* Convert step to an integer; raise for zero step. */
    if (self->step == Py_None) {
        step = _PyLong_GetOne();
        step_is_negative = 0;
    }
    else {
        int step_sign;
        ...
        step_is_negative = step_sign < 0;
    }

    /* Find lower and upper bounds for start and stop. */
    if (step_is_negative) {
        lower = PyLong_FromLong(-1L);
        ...
        upper = PyNumber_Add(length, lower);
    }
    else {
        lower = _PyLong_GetZero();
        upper = Py_NewRef(length);
    }

    /* Compute start. */
    if (self->start == Py_None) {
        start = Py_NewRef(step_is_negative ? upper : lower);
    }
    else {
        ...
    }

    /* Compute stop. */
    if (self->stop == Py_None) {
        stop = Py_NewRef(step_is_negative ? lower : upper);
    }
    else {
        stop = evaluate_slice_index(self->stop);
        ...
    }
    ...
}
```

đoạn code này thực hiện tính toán khi step < 0, start = upper = length + lower và stop = lower = -1.
Code CPython khá phức tạp, việc in ra start, stop khi thực hiện slice[::-1] để lại như bài tập cho bạn đọc.

Vậy code nào đơn giản hơn? Python có rất nhiều bản khác nhau và đơn giản nhất có thể kể tới MicroPython.

### MicroPython - khỏe như Python mà nhỏ cỡ micro


```
$ git clone https://github.com/micropython/micropython --depth 1 --branch v1.23.0
Cloning into 'micropython'...
remote: Enumerating objects: 5784, done.
remote: Counting objects: 100% (5784/5784), done.

$ du -csh micropython
55M	micropython
55M	total
$ du -csh cpython
466M	cpython
466M	total
```

Mở file `py/objslice.c` tìm function `slice_indices` và thêm dòng printf để in start, stop, step:

```
void mp_obj_slice_indices(mp_obj_t self_in, mp_int_t length, mp_bound_slice_t *result) {
    mp_obj_slice_t *self = MP_OBJ_TO_PTR(self_in);
    mp_int_t start, stop, step;
    ...
    if (step > 0) {
        // Positive step
        ...
    } else {
        // Negative step
        if (self->start == mp_const_none) {
            start = length - 1;
        } else {
            start = mp_obj_get_int(self->start);
            if (start < 0) {
                start += length;
            }
            start = MIN(length - 1, MAX(start, -1));
        }

        if (self->stop == mp_const_none) {
            stop = -1;
        } else {
            stop = mp_obj_get_int(self->stop);
            if (stop < 0) {
                stop += length;
            }
            stop = MIN(length - 1, MAX(stop, -1));
        }
    }

    result->start = start;
    result->stop = stop;
    result->step = step;
    // Thêm dòng này, và thêm #include <stdio.h> vào đầu file.
    printf("DEBUG: start %ld stop %ld step %ld\n", start, stop, step);
}
```

Build binary:

```py
$ cd micropython
$ cd ports/unix
$ make submodules
$ sudo apt install -y libffi-dev
$ make -j
...
make -j  28,59s user 4,52s system 369% cpu 8,970 total
```

Chỉ mất 8 giây để build trên máy dùng `AMD Ryzen 3 4300U`.

```
$ ./build-standard/micropython
MicroPython v1.23.0-dirty on 2024-08-19; linux [GCC 11.4.0] version
Use Ctrl-D to exit, Ctrl-E for paste mode
>>> names = ['c', 'java', 'js', 'php', 'python', 'go', 'rust', 'elixir']
>>> names[::-1]
DEBUG: start 7 stop -1 step -1
['elixir', 'rust', 'go', 'python', 'php', 'js', 'java', 'c']
```

Vậy khi viết `slice[::-1]` start index là len(slice)-1, stop index là -1.

### Reverse thực hiện thế nào?

Trong MicroPython `py/objlist.c` có code

```c
static mp_obj_t list_reverse(mp_obj_t self_in) {
    mp_check_self(mp_obj_is_type(self_in, &mp_type_list));
    mp_obj_list_t *self = MP_OBJ_TO_PTR(self_in);

    mp_int_t len = self->len;
    for (mp_int_t i = 0; i < len / 2; i++) {
        mp_obj_t a = self->items[i];
        self->items[i] = self->items[len - i - 1];
        self->items[len - i - 1] = a;
    }

    return mp_const_none;
}
```
Hay code Python
```py
>>> names = ['c', 'java', 'js', 'php', 'python', 'go', 'rust', 'elixir']
>>> for i in range(length//2):
...     names[i], names[length-i-1] = names[length-i-1], names[i]
...
>>> names
['elixir', 'rust', 'go', 'python', 'php', 'js', 'java', 'c']
```

### Kết luận
slice với step=-1 có diễn biến bất thường. Nếu cần tìm xuống bên dưới thì đọc code CPython, nhỡ mà khó quá, thì qua MicroPython.
