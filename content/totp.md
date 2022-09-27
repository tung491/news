title: totp là gì? quét mã qr để thêm totp là làm gì?
date: 2022-09-27
modified: 2022-09-27
tags: totp, cryptography
category: news
slug: totp
authors: Pymier0
description: quét mã để điện thoại sinh ra dãy 6 số thay đổi mỗi 30 giây là gì? làm sao backup?

![img](https://freeotp.github.io/img/android.png)

Ngày nay, khi có đủ chiêu trò để lừa người dùng lấy password, mọi tài khỏan "nghiêm túc" đều cần có xác thực 2FA (2 factors authen) tức cung cấp thêm 1 bí mật khác kèm password.
2FA "lạc hậu" gửi OTP qua tin nhắn, mặc dù việc hack sóng nhà mạng không quá phổ biến, nhưng hòan toàn khả thi khi tấn công có tổ chức.
2FA hiện đại, thay vì tin nhắn, sử dụng 1 phần mềm sinh mã 6-8 số mỗi 30s, được các tập đoàn công nghệ hàng đầu như Google, Facebook, GitHub, CloudFlare, GitLab... tin dùng.
Hay có chỗ dùng phần cứng chuyên dụng sinh mã OTP.

### Các phần mềm sinh TOTP

Nhiều phần mềm free, open source có cung cấp khả năng tương đương như:

- [mobile] FreeOTP của [RedHat](https://freeotp.github.io/)
- [KeepassXC](https://keepassxc.org/docs/KeePassXC_UserGuide.html#_adding_totp_to_an_entry)
- [Python lib onetimepass](https://github.com/tadeck/onetimepass)
- ...

hoặc closed source:

- Google Authenticator
- 1Password
- Authy
- LastPass Authenticator
- Microsoft Authenticator.

### Đăng ký TOTP (Timed One-Time Passwords) là gì?
mã TOTP  được sinh ra theo thuật toán mô tả ờ [RFC6238](https://www.ietf.org/rfc/rfc6238.txt) từ một mã bí mật (secret) và thời gian.

Khi quét mã QR để thêm một OTP vào app, thông tin mã QR chứa secret là một đoạn text đã encode [base32 (A-V0-9)]({filename}/base64.md). Ví du: `otpauth://totp/alice@google.com?secret=JBSWY3DPEHPK3PXP`

### Backup TOTP
Copy mã secret. Với phần mềm như FreeOTP, cần truy cập vào file trên điện thoại để lấy secret.

Hết.

Bonus:

- TOTP app trong 20 dòng Python [mintotp](https://github.com/susam/mintotp)

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
