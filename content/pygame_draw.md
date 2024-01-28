title: pygame - vẽ logo Windows
date: 2024-01-28
modified: 2024-01-28
tags: python, pygame, draw
category: news
slug: pygame-draw
authors: Pymier0
description:

Pygame là thư viện làm game với Python, nhưng dùng để vẽ thì cũng không ai phản đối cả.
Lập trình viên JavaScript dễ dàng vẽ hình tròn, vuông với vài dòng code thì với lập trình viên Python, thế giới chỉ có màn hình đen chữ trắng, cần thêm chút "sắc màu".

### Cài đặt pygame
```
pip install pygame
```

### Khái niệm main loop, surface, blit, framerate

- Surface: Mỗi "hiển thị" trên cửa sổ pygame gọi là Surface. Vẽ surface theo tọa độ (x,y)  với góc trên bên phải là (0, 0).
- Framerate: Clock tick 60 gọi là framerate, ở đây sẽ hiển thị 60 hình mỗi giây.
- blit: draw one image onto another

Bộ màu lấy từ <https://colorhunt.co> thay vì dùng logo của Windows để tránh vấn đề bản quyền.

### Code

[A flag](({static}/images/pygame_flag.png)

```py
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# color pallete from https://colorhunt.co/palette/f38181fce38aeaffd095e1d3
c1 = pygame.Surface((400,300))
c1.fill((243, 129, 129))
c2 = pygame.Surface((400,300))
c2.fill((252, 227, 138))

c3 = pygame.Surface((400,300))
c3.fill((234, 255, 208))

c4 = pygame.Surface((400,300))
c4.fill((149, 225, 211))

#logo = pygame.image.load("graphics/Mi_200_200.jpeg").convert_alpha()

pygame.display.set_caption("GAMI")

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(c1, (0, 0))
    screen.blit(c2, (400, 0))
    screen.blit(c3, (400, 300))
    screen.blit(c4, (0, 300))

    #screen.blit(logo, (300, 200))

    pygame.display.update()
    clock.tick(60)
```

### Kết luận
Pygame giúp vẽ dễ dàng không kém gì JavaScript trên trình duyệt.

Hết.

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
