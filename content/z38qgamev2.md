title: Duyệt qua mọi đáp án bài toán 8 hậu trên Pygame với Z3
date: 2022-01-24
modified: 2022-01-24
tags: Z3, pygame, algorithm, 8 queens
category: news
slug: z3pygame8q
authors: Pymier0
description: nhấn SPACE để xem đáp án tiếp theo

![img](https://images.unsplash.com/photo-1602426005943-50054a7be960?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2NDI5MjIwMzc&ixlib=rb-1.2.1&q=80&w=600)

Bài [trước]({filename}/z38qgame.md) đã hiển thị 1 đáp án bài toán 8 hậu giải bằng Z3 lên Pygame. Bài này sẽ hiển thị [mọi đáp án]({filename}/z3ineq.md), mỗi lần người dùng nhấn phím SPACE sẽ chuyển sang đáp án tiếp theo.

Trong Pygame để nhận việc người dùng nhấn phím, dùng pygame.event.get:

```py
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                TÍNH ĐÁP ÁN TIẾP THEO, VẼ LẠI
```

Để chuyển qua đáp án tiếp theo, có 2 cách làm:

- tìm mọi đáp án, chứa sẵn trong 1 list, khi người dùng ấn SPACE thì chuyển tới đáp án tiếp theo. Ưu điểm: đơn giản, không cần biết khái niệm gì "lạ", nhược điểm: tốn RAM để chứa 1 list các kết quả.
- dùng generator, mỗi lần người dùng nhấn SPACE sẽ lấy ra đáp án tiếp theo. Ưu điểm: chỉ tốn RAM chứa 1 đáp án duy nhất, nhược điểm: generator nghe có vẻ đáng sợ mặc dù thay đổi code chỉ 1 2 dòng.

Trong function tìm nghiệm của bài toán, thay vì tạo list, append các đáp án (model), viết `yield model`.
Để lấy ra lần lượt từng đáp án, gõ next:

```py
    solver = Solver()
    solver.add(columns + distinct + diags)
    while solver.check() == sat:
        m = solver.model()
        yield m  # <=======

        block = []
        for var in m:
            v = var()
            block.append(v != m[var])

        solver.add(Or(block))
```

```py
it = find_queens()
# ...

while running:
    # ...
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                draw_board(board)
                try:
                    m = next(it)  # <=====
                    counter += 1
                except Exception:
                    pygame.exit()

                d = {i.name(): m[i].as_long() for i in m}
```

Thêm 1 biến đếm hiển thị lên màn hình đáp án thứ bao nhiêu.

```py
    myfont = pygame.font.SysFont("monospace", 80)
    scoretext = myfont.render("#{0}".format(counter), 10, (0xFF, 0, 0))
    display.blit(scoretext, (5, 10))
```

Kết quả:

![8q game]({static}/images/z3pygame8qv2.png)

Full [code]({static}/z38qgamev2.py)

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
