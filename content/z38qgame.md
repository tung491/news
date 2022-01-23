title: Giải bài toán 8 hậu trên Pygame với Z3
date: 2022-01-23
modified: 2022-01-23
tags: Z3, pygame, visualization
category: news
slug: z3pygame
authors: Pymier0
description: đã đúng, còn đẹp!

![img](https://images.unsplash.com/photo-1596434934651-0cc599e2c7c1?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2NDI5MTEwNzg&ixlib=rb-1.2.1&q=80&w=600)

Pygame vốn để làm game, nhưng cũng là một công cụ tiện lợi để hiển thị các vấn đề.
Tải pygame `pip install pygame` rồi viết code:

Hiện 1 cửa sổ vuông tương ứng với bàn cờ, kích thước 800x800 pixel:

```py
import time
import pygame
pygame.init()

display = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Z3 8 queens - pymi.vn")
running = True
while running:
    time.sleep(1)
```

Tạo bề mặt để vẽ, là 1 object Surface, đổ nền trắng, và tính toán để tô đen các ô đan xen.

Hệ màu được sử dụng là RGB (Red, Green, Blue), mỗi màu được thể hiện bằng 3 con số trong khoảng 0-255, viết bằng hệ 16 (hexadecimal) sẽ có dạng 0x00 -> 0xff.

```py
white = (0xff, 0xff, 0xff)
black = (0x00, 0x00, 0x00)

cell_size = 100
board = pygame.Surface((cell_size * 8, cell_size * 8))
board.fill(white)

cntr = 0
for x in range(8):
    for y in range(8):
        if cntr % 2 == 0:
            pygame.draw.rect(board, black,
(x*cell_size, y*cell_size, cell_size, cell_size))
        cntr += 1
    cntr += 1

while running:
    display.blit(board, board.get_rect())
    pygame.display.flip()
    time.sleep(1)
```

Đã được bàn cờ với các ô đen và trắng.

Mang code bài [giải 8 hậu trước]({filename}/z38q.md) ghép vào, dùng 1 bức ảnh bên ngoài để đại diện cho quân hậu:

```py
def find_queens():
    from z3 import Int, And, Distinct, Solver
    queens = [Int(f'Q{i+1}') for i in range(8)]
    columns = [And(1 <= q, q <=8) for q in queens]
    distinct = [Distinct(queens)]
    diags = [And(queens[i] - queens[j] != i - j,
                 queens[i] - queens[j] != j - i)
             for i in range(8) for j in range(i)]

    solver = Solver()
    solver.add(columns+ distinct + diags)
    solver.check()
    m = solver.model()
    return m

#...
m = find_queens()
d = {i.name(): m[i].as_long() for i in m}
image = pygame.image.load("beerqueen.PNG")

while running:
    display.blit(board, board.get_rect())

    for row in range(8):
        for col in range(8):
            if row+1 == d[f'Q{col+1}']:
                board.blit(image, (row*cell_size, col * cell_size))

    pygame.display.flip()
```


Kết quả:

![8queenpygame]({static}/images/z38queenpygame.png)

full code tại [đây]({filename}/z38qgame.py)

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
