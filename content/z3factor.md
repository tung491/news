title: Dùng z3 giải hệ phương trình số lớn giải mã rsa
date: 2022-08-29
modified: 2022-08-29
tags: z3, factorize, CTF, RSA
category: news
slug: z3factor
authors: Pymier0
description: việc gì khó đã có Z3

![img](https://images.unsplash.com/photo-1661621768920-5b5cdafc96c4?ixlib=rb-1.2.1&dl=dibakar-roy-JAvgd-akITY-unsplash.jpg&w=640&q=80&fm=jpg&crop=entropy&cs=tinysrgb)

[MapleCTF 2022](https://ctftime.org/event/1676) ra đề Brsaby Crypto với nội dung:

- Cho p * q == N
- Cho `p**4 - q**3 == hint`
- Tìm p và q rồi giải mã lấy flag.

### RSA trong 2 phút
Đây là 1 phần trong bài tóan giải mã RSA. [RSA là hệ mã hóa phổ biến nhất hiện](https://en.wikipedia.org/wiki/RSA_(algorithm))
tại, được dùng ở hầu hết chỗ nào cần mã hóa trên máy tính.
Nền tảng của RSA dựa trên một bài toán khó "gần như" không giải được dễ dàng:
tìm 2 số nhân với nhau ra một số N rất lớn.
Sau đó, mã hóa một bí mật m bằng công thức:

- `c = m**e % N`

với e cho công khai cùng N, thường có giá trị 65535.

Để giải mã, cần tim ra 2 số đã nhân thành N, gọi là p, q.
Từ p,q tính ra d:

- `phi =(p-1)*(q-1)`
- `d=(e**-1 % phi)`

rồi giải mã bằng công thức `c**d mod N`.

### Factorize N tìm p,q bằng z3
Việc tìm các ước p,q của số N gọi là factorize.

Bài giải:

```
# pip install pycryptodome==3.14.1
from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes
#from secret import FLAG
#msg = bytes_to_long(FLAG)
#p = getPrime(512)
#q = getPrime(512)
#N = p*q
# e = 0x10001
# enc = pow(msg, e, N)
# hint = p**4 - q**3
print(f"{N = }")
print(f"{e = }")
print(f"{enc = }")
print(f"{hint = }")

N = 134049493752540418773065530143076126635445393203564220282068096099004424462500237164471467694656029850418188898633676218589793310992660499303428013844428562884017060683631593831476483842609871002334562252352992475614866865974358629573630911411844296034168928705543095499675521713617474013653359243644060206273
e = 65537
enc = 110102068225857249266317472106969433365215711224747391469423595211113736904624336819727052620230568210114877696850912188601083627767033947343144894754967713943008865252845680364312307500261885582194931443807130970738278351511194280306132200450370953028936210150584164591049215506801271155664701637982648648103
hint = 20172108941900018394284473561352944005622395962339433571299361593905788672168045532232800087202397752219344139121724243795336720758440190310585711170413893436453612554118877290447992615675653923905848685604450760355869000618609981902108252359560311702189784994512308860998406787788757988995958832480986292341328962694760728098818022660328680140765730787944534645101122046301434298592063643437213380371824613660631584008711686240103416385845390125711005079231226631612790119628517438076962856020578250598417110996970171029663545716229258911304933901864735285384197017662727621049720992964441567484821110407612560423282

## giải
from z3 import Solver, Ints
p, q = Ints('p q')
s = Solver()

s.add(p**4-q**3==hint)
s.add(p * q == N)
s.check()
m = (s.model())
p = int(str(m[p]))
q = int(str(m[q]))
assert p*q == N
phi = (p-1)*(q-1)
d = pow(e, -1, phi)
flag= pow(enc, d, N)
print(long_to_bytes(flag))
```

Ta thu được flag `b'maple{s0lving_th3m_p3rf3ct_r000ts_1s_fun}`

Hết.

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
