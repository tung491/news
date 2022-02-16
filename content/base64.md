title: Base64 là gì? tại sao lại là 64?
date: 2022-02-15
modified: 2022-02-15
tags: base64, encoding, crypto
category: news
slug: base64
authors: Pymier0
description: biểu diễn dữ liệu binary tùy ý ở dạng text

![img](https://images.unsplash.com/photo-1580068829493-ee627a9eaf3b?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyMzI1MzN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2NDQ5Mzg3MDY&ixlib=rb-1.2.1&q=80&w=600)

Khi lập trình, hay làm sysadmin, một khái niệm đâu đó với tên encode Base64 xuất hiện và không quá khó để dùng:

Lệnh trên Ubuntu Linux:

```sh
echo -n PyMi.vn | base64
UHlNaS52bg==
```

Hay Python3:

```py
>>> import base64
>>> base64.b64encode("PyMi.vn")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.8/base64.py", line 58, in b64encode
    encoded = binascii.b2a_base64(s, newline=False)
TypeError: a bytes-like object is required, not 'str'
>>> base64.b64encode(b"PyMi.vn")
b'UHlNaS52bg=='
```

một cách nhận diện dữ liệu ở dạng Base64 là gồm ký tự từ A-Z a-z 0-9 và thường kết thúc với một vài dấu `=`.

Nôm na thì đơn giản, chi tiết hơn sẽ có nhiều điều thú vị hay ho rất chi này nọ.

Base64 cho phép biến dữ liệu binary thành dạng text (ASCII). Ví dụ như 1 file ảnh, logo Python, khi viết HTML có thể dùng thẻ img và đường link:

```html
<img src="https://www.python.org/static/img/python-logo.png">
```

Nhưng cũng có thể biến file ảnh này dạng text và viết:

```html
<img src="data:image/png;base64,BASE64OFIMAGE">
```

viết kiểu này có ưu điểm không bị phụ thuộc vào việc link ảnh sống hay chết, vì toàn bộ bức ảnh đã nằm ngay trong file HTML. Chuột phải và copy link của bức ảnh sau để thấy:

<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAASIAAABSCAYAAADw69nDAAAACXBIWXMAAAsTAAALEwEAmpwYAAAg
AElEQVR4nO2dd3wUZf7HP8/M9k2nKIJA4BCUNJKgNJWIBUUgEggCiSgeVhA8jzv05Gc5z4KHiqin
eBZIIBDKIXggKIeCRCAhjQAqx4UiCARSt83uzDy/PzazTDZbwy4BnHde+9qZydNn97Pf5/uUIZRS
KCgoKLQnTHsXQEFBQUERIgUFhXZHESIFBYV2RxEiBQWFdkcRIgUFhXZHESIFBYV2RxEiBQWFdkcR
IoX24Hc7d+6MbO9CKFw6KEKkEHYIIarMzMzEdevWzTpy5Mh/KKXFM2bM6Nfe5VK4dFBdzMxI54SI
2Egm/pq0kV2NHbv1pHauKyW0I6E0ilJoKcBSKtpBqQWU1osgZxiGPX5876ajXO3ZXxuOV/33YpZX
ITRs3bp19G233VYgiqLWarVCFEXodDqhvculcOkQdiEipKsh6f6p98Rc22/8mHmfJIsiHw8KLaUU
lIqglAKUgooUzmsUFCKo2HydUsTEJ4EC9cP+XHDQfLp6Wfm/ly6lNT82hbvsCqHBarXGCYKgNZvN
0iWxPcujcOkRViFKmTx32Kg38xeq9RGpgsMOh9UEQCY6cL5DFF3HtFmUgPPHFBSgYgyr1gyOiU8e
PGTaS7/vc/djTxza9OEP4Sy/QmgQRVGQ7i0AKOsbFdwJm48oZfyzA36XMeVLwrCpdksTLBYLrHYe
Fo4HL4oAnBYPXIIEl3UEuShBsowAURTgsJpAGJLSddDoTddl/fGWcJVfIbS47qdMkBQUJMJiERFC
yKi//+dFzlQXLYoCHLyAlB6xSIvvgJpGK77ZdxJmmx0sQ5o/mACloqsr5vqwUtrimkukRBF2U0P0
Vf1v+TSqb/qgxp9KzoajHgoKlyIJCQkRnTp10tXW1lqNRqPWaDQKdXV1lr1794qUUpfvLTs7W1NY
WGhvz7IGSliEqEO35GvUuojBdksTOIeAW6+/Cs+OTYCKcRpg6b064qXVe8ELIgjQSnCo13PIflEp
RIe9d7eUO6cBmB+Oeih4hhDCPPTQQzeXl5cfKi0tPRlIHKVrFjqmTZs2/q677krr169f/4qKiiMN
DQ0Hk5KSLGq1+i5CyH2UUmHjxo0PFhYW3g1gYnuXNxDC0jXjNUIXQRQ6UgAMAbJu7O4SIQAYcl1n
3NA1BpyDdxMceLaCvIiUyHMwXtVrLCFEmYYQZgghzOTJk/t/9dVXc0+ePLnr008//TYqKqp/e5fr
t8gf/vCHz/v37z+TZVnL9OnT38zIyHhz+/btEVFRUSOysrL6AEBKSsoki8VyTXuXNVDCYhExhGpB
KaHU6YRmmdY6wRLSwsKRRMifVdTimihCZYjujLjfRQBoDEddFJxs2bJl8B133PE1x3F6m80GjuPA
cZwj0PiKRRQWHGq1mgCASqXiAHyblZV101133WXevHmzraGh4Zd2Ll/AhM+SoBSgAM+L+Hfp8Rb/
qjpehwO/1EHDEjeBET0LTotztAgjCgKBYGfDVg8FAIDVao2x2Wx6k8kEnueDEhNBEBRndZgRBEHD
8/x3N954Y58PP/xwTHl5+U4Al81crfAIkeO8WGhVDDaWHcPLa8rwdeUJLP3uZ7xQWAwz53BmLhvG
d/1iSudw+oJcIgTZKBpk/1cIO4IgXDYf6t8QOpZlGQCIjY2NKC0t/fnkyZOG+Pj4Cfn5+dv0en1M
excwUMI2j0guHAwBvtl3AlsqjoNSCjVDoGJkYVyiI+uqeRGgVsKl/LpeNC6ke6V0zULPtm3btjc2
NjYAQHFxcZXZbD7C87xt3759p7Zu3XqotLR016BBg9q7mAERHiFSqQjchEKrYkApCXyY3qe/CLJr
yiTdi4UiRJcWGRkZr+3btw8A8Mc//rFQ9q+vnnjiCQB4qz3K1RbCM49IpDzR6CyMKFBJeEApiCeB
aZ45LVJRpHa7HqKgcvqtfYuSdI2IihApKFzuhEWIzlVX7NJf0+sGQhinStgA6JrfW2CVHRN63ZgZ
H0R17TtadHAeR808WUZOURJJOOoRSgYMGBDDsqwegEOj0ZiLioqsfiMFQJ8+fbSHDh3iQpGWL3ie
twItrRmLxRJQHURRvOQsooSEhAiDwRDB8zxjNBqtO3bsqLuYeep0OltRUVFtuPO8XGizEEV17duR
Ueu6MywxgOdbfLJ4IogMGLvLj6yF06esdU9F3/zuABwARKptsfTDZ3cNABWd6ap0fJ8+kZ26dIm5
AQ6Rl1JnKQhPGIdK4I5u23PmVFvrGiw33XRTh5ycnLT4+PghkZGRqTfeeGOXHTt2xBBC9AAcLMta
jh8/XlNRUbF9+fLlq5cvX14ZTPqDBg26atKkSbdkZGTkfPDBBzsR5IROQgj58ssv73Q4HHGUUqrV
aklxcfGvL7zwwrfycPPmzYsfPHjwIKvVak9OTk63WCyu/1ksFrz11luj1qxZ041hGDUAaLVaUlRU
VPTKK68cDaY8EkOHDu3ctWvX66ZOndqb47iuhBADpdSiVqt/ysvLKy0sLKxuS7oS999/f2pOTs6Y
pKSkW0pKSroIghABgGFZ1nr8+PGzFRUVpUeOHNmwcOHC/4RC3CdPnpw0adKkVJ7nh6alpfUrKSnp
KOVJKbVZrdbasrKyg8XFxRtWrVr11ffff/+bXchNgv11Spo495a4nv0fj+nedzDlhWtFUOa8QHhZ
TS+/7vHc+RIcHKjAu3xA3sLJ02FYzeG9ix7qt2PdfZOHjUlcArOHGe0M+WXfvlMbn5n3zUtbthwL
aCZwW8jOzk6ZPXv29AEDBtwtCEI84By6ttlamYJgWRY6nQ4sy1orKio+mzNnzvP+fpWvvvpq47p1
6+YnJSWNEUWxm06nw/r16xeMGzfuj8GUkxDCiKJ4wGw29wUAo9GITZs2bb/nnntulYfbtGnT9JEj
Ry42m82w2WxwHzhrLr/r3Gg0YuPGjbmjRo3Kl4dbu3btg3feeedn0ur7iIgIcejQoenl5eVlhBD1
u+++OzI1NTUnNTV1kCAI3T2VmWGYc5WVlSufeeaZl3bu3HkmmPpOnjy5/4IFC16MiYkZKwiC2lNd
ZPcD9fX1patXr35t5syZq4PJBwCys7PjcnNz709OTs7p1KlTmiAIGgAe2w8434Y6ne5gYWHhy5Mn
T14RbJ5XAgFbRKRPH23GhBfn/+7WrCd53sE6LCbP3SU0r6aXj3hJW3q4Vt6LbufSGrLzjuhWo2SQ
5dViUayzeJxNEGC2A2YPc+wo7ZZ4Q6dHNuSPu/Xu27qO3fSfEz+FqP0AAFlZWV2efvrpFz///PMH
7Ha7rqGhAcD5D5nBYOAB1MNpv8UJgsDabDaYTCYA0CckJDyxdu3am0aMGJG1detWr9ZEr169YtLT
06ecPXs22lktCgC8t/C+aGpqskgWDqUUVqu1VTdL+uJ4m/8TzJwgeVie58WUlBT7/Pnz7zh58uRf
o6Ojb7Lb7aivr4dKpYJOpwPQ6svbISEh4Yl169bd9pe//GXC3/72t6pA8s3Pz39g6dKlC+vq6mLk
90Wr1QLO7UgEAGpBEKT7AZVKlfrwww+vOnPmzD+GDh36dCDWESFEk5eX9/CyZcuesdlsvW02G5qa
mqDXO61+rVZ7mlLKEUIMADpKP1BSs5tMpuuzsrIKli1bdt2UKVNeDqhRryACEiJCiGr029s/Y9Xa
SXZJgORzfGR/ri095EPu0pm0pYd0RZYOdU/HgwBBdu6SIH9QEYAImHho1aTvv5ZnLsnIiB++bVt1
azOlDeTn5w8vKCj43GKx9GhoaJCEByqV6r9lZWVfFxcXbykoKKhmGKaBYRjapUuXuNmzZ2ekpqY+
ZTKZegiCgKamJmi12rTly5evSE9PH1FSUmLxlJfNZqNWq9UMIDoUZfdHWVlZKSHk7xzH2fv37/+7
2NjYbLF5cIBhGJSUlBQ0NjZWA2ABQKvVsrt37943atQon+mazWbxnXfeWcSy7K1Wq5UxmUzQ6XSI
ioo6c/bs2art27dXA9Cmp6cnxsXFJZtMJhBCpHbq99RTTxUOHTp0uD/LKC8v77Hs7OwPampqCOC0
eiIiIsy7du36l8lkWr98+fLD1dXVwsSJE7vedNNN96akpGSbzeYOPM+joaEBWq328e+///7qPn36
TPIlRgsXLhx48uTJv0dERNxy9uxZKR/U1NR8t3v37sIlS5bsOXbs2Gme521ardaYnZ197cCBA8en
pqZOM5lMEYIggBCC2tpajB8//qX8/PwjOTk5S4O7W5c3AQnR8LnLnmHU2kkOq7mlUFA3oXCdy4fX
3awln34f92ue04FLmHxBm31IFIDoPOYodFHqm/76VPLDAN6/0MZ75513rn/yySe/OHv2bBTg/KDb
7fYfCwoKXsvLy/uipKSkYejQoZg9e7Y82lEAZdnZ2csXLFiwQqvV3ioIAjiOQ0RExKCFCxe+BGCO
11qFyOkbSDrz5s3bC2AvAKxaterWkSNHZktWg16vxzPPPLOwoqJitzyONxGS50cI0Vit1gzA2Z2r
q6sr3b1790d5eXlfFRYWHuvRo4crXH5+fk5WVta7dXV1RgBSO10/f/78/wMww1v98vLy7pkwYcJ7
tbW1BAA0Gg1sNlvx4sWLH5s9e3YpAIwZM0YKXgFg45QpU96eP3/+P3Q63Qi73Q6O46DRaO7bsWPH
OwAe95TPokWL7pwxY8bac+fOGU0mE1iWBcdxewoKCv5v1qxZm3v06IHRo0fLo9QAOAJgx6JFiwoy
MzOXa7XaeMnyq62tRXZ29otJSUkbKisrw+5Av1TwO7M6rvfN3WO79fkTbzU7bRCfPhvJiezf2QyZ
0HhOx/d8Ip9QEaBCszXU/C4dm2zonxg3vU8f0sp1Hiy9evXqZrVao6RznU5Hn3rqqWmzZs1aWlJS
0uArbmFh4anZs2fnGI3G41J9mpqakJKS8tT48eOTLrRsYUAvb3dKKQwGg95HeK9QSsEwDOLi4o6t
X79++u233z5k9OjRiwsLC4+5hbNPmTLl01WrVj1iNBoFeTslJyfnZGVl9fCUfnZ29tUTJ078oLa2
lgUgiUPlpEmTRkki5Illy5YdmjZt2liO43ZKvi+O42AwGB7Lz8/P9hSnZ8+efc1ms1ESEp1OR2fP
nv34rFmzNvtrh5kzZ+5au3btJKPRaJG3rc1mi3/ooYdu8hf/SsKvEHUbdvckkYpxkgjJxcO/KLW+
dj4OENjastZ5tYBQ59C9COKygiQLyPUS4BIknkdsR03ivEeHpF5o43EcJ7jVlR45csRjt8oTa9as
+aWkpOTvOp3OVS+O4zQzZ8582lsc+VA4pRRiG+dRtbpHYYoDtF5r1iwMSx966KEbc3Jy/unPB5Ob
m7u8qanpK5ZlXfkKghCdm5ub4Sn8zJkz/2QymXpIZTYajY6VK1fO2L59e42/sm7evNk8Y8aM6QaD
oUnKy2QyYcKECa/cc889Ue7h7Xa7w/0zcPjw4YAbZ9asWbv37t27QvoMSK/4+Pg+gaZxJeBTiAgh
JLbH9aMEuy0ooXAKDLxYQcGkc97C8vbhJ4R1AOAFUYg6bwkJaGEVub8Enonvbrw9FA3oXh+tVhvU
Atz333+/UK1W10jxrVYrUlNTR6empnrcwqGtYuAvrUAE7ULylsdrthpeX758+elA469YseJT9y+r
w+FIcQ83adKka1NSUh60Wq0uy+v06dObn3766R2B5rV27dqDpaWlS+T52Wy2Pg8//HCrvX08LejV
6/VBzWvbs2fPWklkpZfdbr+oD7Zob3wK0bicR65WGaKvEwU+SCsIQfiC4DWdVkLmBiEMOFPjMUop
7djJ2B+8XHgEOC0jN2GCAFgdSEiOGxaeJg2OwsLCUzU1NXsY2VYpgiB0yM3NvWK3waWU0mPHjgXV
rVuyZEm5KIottnqhlHZ0D5eVlZUpCEKsdK7T6VBaWros2DIuWLBgCcMwrhFJi8WC1NTUnHDsfbVi
xYpjlNIWw70Mw1zYr8xlhs9GvXbw6N5UFDpLYgGZ0PgXmECsILQcpqfU6zC9x8JrtKg5engFIYSk
Drn2Zlg5tPAJuXxDbtYRzyO2o/a6m5NiYj0mHAShsFB27dq1W6/Xt0jj2muvvS2Q/ELVNQuk7KGy
iCilUKvVQcVnWbYWwBm3/FslMmDAgFGSNdTcPqYVK1bsDSozAJWVlVWEkB+ldARBQFxcXEpaWlq8
v7q1AYcoinZ5Gr+1zQ58CpG+U48bQGmz70UmFB6G7Z03QCYeXobp3eMFOtzvDiEMBM5Sefqbd5Ys
fn3oSAh8f9/WkJvj2uG4xq4iHifPBUMohEir1R6Q+34sFgtSUlISCSGtTPxQdc3cfU2BEEohakN5
HaIotvDHEEJaJDRgwICYDh06XCftl0QpBcuyvxw6dCjoSazV1dW24uLi/fLumSAIUffff3+rB0OG
4p6E6r5ervgUIpG393U1jt+tOGQN6TZM3+K8DcP97hDCgNVHnjqw45vc/v3BTp6S/AasdqalT8jP
Majm8Ym9LliIQsGKFSt+lZ8LgoBOnTp1HjZs2GWzn0y4EQSBAPDpe9HpdF0EQbhKOmdZFmfPnj1X
UVFh9hXPG2fOnDkknzkOAL179+7blrQUfOPHIUa7e+5SeRcPuF1znYsUIASMSgNpZrVInSvyW8YX
W1xzhxAGdov5mwM71z3J7Vv9s/XkY/l6NRLBSVaQ29wh13wi2TGcYfr0Mnoc/g0U+S8v4GwPhyPg
3VNdHD582Ewp5SmlrvvB83y03W6PAdBiLol7fm3FPR1/aXmqa6DIHbpS3La0k3saHrqlUQAMUhid
TofvvvuuqXfv3kHnBQAsy56RLEcpT7vdfpU8jKcFvaGo228Nn0JEKY2RhMSf4HgWJREAA0alAiXk
mN1cX22q3tdAQUVQSkSp4SECIgVo8yNAm7tr5yGEAJzFTg9ba2s21u7O25Fzz/NRtuOPrNTr1Nng
HB6FpsWxfEi/OW07x3cOeYu2AYZhOEopB9n9oJTqmxfJKgQIz/MtPs+UUjAMcyEz6D09ike5J2HA
3xChWt4F82YZebaCRDBqHRxW8/ajRV8tOLn9q28oPRHwHBtvZN/TpVP51vFP5q+YMgdmew/Y7HAK
i5vQtBIkt2siAEojLrQ84bBQmlHBy/3xYxUEnV+wPqJg4oQirns67ulJEEKo+3VBENq8nzmllHiw
HFut7QtF3QKw9q5o/FhEaOEcbG0FAaBuTk9KQakIVhvBn6rc/vyPa994A5iMxe/cNmrrv8bdxlL1
NRQ0sHkWFAAEEEIpFalmcFrnzoUrJ/aDne+IRhtaCJBXa8hbV6352gUSig8hwzAspZSVxxdFURBF
sdXQSShN+GA/+G3NO1T7EflLg1JqpZQKlFIWcA65p6WlRbYpM2d6Rg95tpoxfzHqdqXjr2tWLwmP
v66Z/JzRaMXjZf959PAXCz79+J2M2x+4f8Bbjzw6OBFCEF98KrQWEKsdaLCipegE4hOSX5PCUxDQ
Njkx3drI43Ew8DyvR+vdmmxouXNcyPJrazoXkncoyi0XS09pqFSqOlEU6wF0AJx+rQ4dOkQTQlgq
ewJqoPA839G93CzLtnpETyjqFqr7erniu2tGxeMuEXJbCd9i1AxwnTMqNeqPH150+IsFn65bMip7
+sxheaizadAY4D5THv06Piwar0LjR6QoAw0rXvDeRKH4JZs4cWIHqRsgQQipczgcrXbwC9Uvp7sT
NhDau2vmL41Tp06dYln2FKW0g3RNEISr09LSOgP4tVUEP3Ts2LGn5GiX8iwoKPhpwoQJQZUrEH7r
FpHvJR4q1U+UthQgeJorJLOMCKM6Ubl1yUu5Y3v1zcxJ/SfOWjUQAmlYivPzf9wnJHoafndfyiGP
62XukCuu8/jnI5b/XkjjyUeSPPksAqVnz579gPPtyDAMzp49e6KsrKzePax7fpQG2M31n47P8J6W
MvB84FshhaKd3NNw705WV1fbSkpK9mu1Wnm4q7p3794z2LwIIUx6enpv+eRIQsipQ4cOHZKHC+Uz
23zV7UrHpxCZT504EFjXzGl5MCo1ao/9tIoerax79o83Pw+TI7D+ufsC1VZrxnzMC/IhNK0nODYf
iyJAxIZ/rKy+ICEKFZGRkUPkM2m1Wi3Ky8t3BRKX53lj2ArmP+/2ytortbW1/2ZaPlmYmTBhwvBg
08nMzOzO87xr4SnLsmhsbNyzb9++gNfHKQSOTyE6sWf9YQpyGmJrEWp9DoAQnPmp6stBfTpE3ZDe
9XbY/H1QaWDC4Ut0gj2GCDAi6s5xB/ZU2o75Lp9/LvTXcOTIkXEDBw4cJv/lZRiGnjhxYqN7WJVK
JYqiSKVwNpsN6enpbVqlHWy53awMUEoRHx8fcIXDYRF5SmfdunVbCCE18jZKSUnJIoQENXqWnZ19
KyEkRkrHYDBg9erV+Z7ChqNuvzV8CtH6FZ/+ypnqfgbj/mhod6uouSFFyp/ev/UoG0O7Q6BX+86a
BiY0bRYpwXNcKgJaoKq8fhNtgwPTHw6Hw9PcE688/fTT2RzHuVbaMwyDhoaGyjlz5vzgHlalUjWw
LOvanoLnecTFxaWPGjWqRzB5UkpFQkhQtn91dXWrtpo0adIlN6emsLDwVHl5eV7zVrCSwzr11Vdf
9b1tpAxCCElOTv69tI1r8z3Zt2jRon+Hp9QKPoWIUkobj/20hag0XqygVucCCCswIut70zF/lsuF
CI1XH1NzOFEAiGD/dN2ZdaFoQHkbCIJA0tLSegYad8yYMd1TUlKes9lscPvlXUidExxbUFRUZC0v
L6+Q719ksVji3n777ReDKXNubm4XnudjgvkVLigoqKdOXOHNZvO1geQXLj+KNxYvXvy2wWD4VQpj
NptJVlbWKxkZGQHNG1u8ePHU2NjYYVK5m+/JCydOtJ4H575mT7GI2obfLQ1+rfzmXwTgPPuG5CLk
GhYnPPG2oTQNTHQCOvYiNF5FSuqWUZgbhe2ff3F6fygaUN4OVquV/PWvf83bvHnzG9nZ2a1WacvJ
zs6Of+ONN1aYzeZrZV0y1NfXf/vcc8957AIAQFlZ2T/VarUrT57nodVqH9y6des7/r5o6enp0R99
9NETCxYs+MFms/UO5oOv1+sPE0KOy7s8AwcOHO83YjMX88u6Zs2aX9asWTPHYDDI2yjx448//iQj
I0PnK4+PPvpoRGZm5kKTybk3u1qtRlNT0ydz587916VQtysVv0LUdGjPfrvVvBKEOAWnxbC9XJTg
uwFbjXgF2wXzNlrmQZh8Ob2NLAq/OLOQhulZ1WazOeb666//08KFC0u2bNmS99prr41LS0u7Pjk5
uXN6enqXrKys1C1btvzl3Xff3anRaAZLDl9KKaKiok7NmTPnceq2N42cZ599dmtjY+OnkhgBzu1M
+/XrN2vRokU/rFy5clZWVlZqcnJyt+Y8e7/66qsZmzdvfmPDhg3Fd9999/v19fVBdeUAoKioqLaq
qqpA/uWOiYm5Y/HixS8nJCRc8Az1UDN9+vRlBw8enB8dHQ1KKTiOg0qlyv7www83vfbaa7emp6e3
2EJk/PjxvTZv3jzv3nvv/aKuri5KEiGHw/FdVlbWrPaqx2+FgHaBq1yz4P/Scl7IsJsarqXSKnzZ
Nh1UPseoFdKwvyQQ8nk9zeet5v94uibFoX7iuuchhQGgZsCZhS+nzTu08aHnL6jdzteu5S+YoNVq
LQAiGxsb4/r165dzww035OTm5poBnKOUsoSQLqIoMo2N5/f4YhgGUVFRNatXr560fv36H/3kR4cM
GTJj6dKlcUajMVN6VpjZbIZer08YOnToO0OHDhUppWcIIXZKaSQhJFYURTQ2NkKlUsFgMIDjuBaP
CxJF0e/P8LPPPvtaQUFBhkajudFut8NsNpORI0fOu/fee7M3bNjwvdVq3V9cXLzuzTffrPbVThdq
NcjK7DP87bffPnfLli00ISHhzxaLRRKj4bm5ud9OnTq14ssvv/ylvr5eSElJ6fjuu+9ez/N8rNSe
RqMRFovl31OnTn3A3+r99qjblUZAu83VHdh59ETZf+5n9ZG/MKwarlE09y093G+Cu08nGCsGHiya
Njmum2+ogQUniFUTHtn/ZLisIUKI+N57700pKyt7PSoqqoZhGNhsNpjNZqPFYulutVq7WiwWRvIJ
MQyDyMhIOByObR9//PFtjz322LeB5FNUVGTNzMycuH///r9FRkaapREtQRBgsVhgsVgYq9V6tcVi
6W6xWGIFQZDEzmGxWHZ/++23T9TW1hbKh7kJIX6d7CUlJQ2PPPLIWIfD8a/IyEhotVpYrVY0NTX1
TUpKevj2229/Kz09/Wb3eFqtVm0wGCB7MSzLBrXTIc/zxODElY5OegCaFyil9I477pibn59/P8/z
P0ZFRUm+LTQ1NSUnJiaOGj58+BidTjekqakp1m63w2AwIDIy8vT+/fufu++++8b5eyy0RqO54Lqp
VCrGYDAY3eoW3M5xlzkB74t7cNXrRbE3jBjWa+i9zxm7xN9DBbHbeR+RCJFSMCqtFlTtvAkerRaZ
heLJumEooCUAGDiNLtHDsWRhETiXrNHmd9L8P9mxpLMMOV253/Tln14/OO+rHeagZ9h6w31rDL1e
z27cuPF/b7755oasrKwPs7KyMhMTEzPj4uKuE0VRvge1yDDMicbGxsqlS5cunTt37lrqYTGlL6qq
quwAns/MzFz52GOP/T4xMXG4KIrdKKVGOFvMSghpYln2TElJyX8tFst3hYWFP6xdu7YiMTERn3/+
ef8RI0bAYrFIdQho6vu2bdtOARj3+uuvj0xOTp6UlJSULAhCZzhXpVNCSKN7nNLS0oOU0mUcx/GE
EKLRaISamhq/G9nL4TjO8fXXXy/nOK4bnJanqqysbKf7LGdPzJkzZ2Xv3r2/evTRRzNHjx49Pioq
6npRFK8GYKSUQqPR2FiWramtrT1cUlKyfsWKFavXrVt3vKrK/zMcS0tLqwBcUAF/CbYAAAccSURB
VN0aGxvrvv7668V2u11HKaVarVZVXl5eEUjdrhSCfuQ0AER0Tria1Yg9RUJb/iIRIpqOHyy+9cbO
Kd9+/UARzJwHQXITJqkbpSMo3n36lcfm7gpqiJRSSiL0VMOyquYZxi2/zwKIgxD+2Hd7LMeDrqgf
Pvvss9tGjBixVXpiqsFgEMeNGzewpKSkxSNrUlNTr1Gr1ddIIiGKokmlUp3YtWtXyCbHJSQkaAwG
QzdRFI3Nq9Ctoig2lpaWevxSLF269JPhw4dPs1gsMBgM2LZt2+dTp059KNh809PT1TzPd2ZZVs+y
rHjixIlTnkaXLiWSkpJi1Wr11SqVykidS2usdrv9TEVFRVCPslYIHW16UoDpTNUpAKe8/f+WwV2Z
810qb2vC3H09BAA9y9vF/wk6GpBpqxMpscBiLy2l59pSj4tFaWnpSQAXvK7NF80W0v8CDS8IQosf
EUKIzy6IN0pKShwATrQlbnvR/ODC38zDCy8HwvfIkhY+mgAczBaKgUnRr1bsuOcFUJG0tJjkAibI
rxMY8b+MAbG3bSura7Uu62IQCkdle9ChQ4dObvN7QtZlVVAIljA+O0nuYPYykuUuUgI1wMwbfI+C
uYsZE8cLbVv4GQouRyEihJCjR4/GSo+PppSCZdlWI10KCheLkD+jyYXfmdHyUTBvo2VSeCsgmJtf
NjeBEy+9lZeXOAkJCZ3lznNKKb9q1aqAu3UKCqEmTBYR7za07q175q3LJvufaAN01wHRdzmv1W8E
LPsBoglP0YPkcrSIxo8fnwygi1RehmGOV1VVKUKk0G5cHB+Rr9Eyr101CogcoO0FdP87wEY7042+
A6h+ErAdumTE6HJj3LhxT1utVgI4V9Xv27dv++HDh1ttgaqgcLEIS9eMCKCe133Ju2oeJjK2mLAo
OIUoasR5EQIANsZpHUkL51UMdRga2uWxmKFczHmx+OCDD142Go0jpbKr1Wpx7969H7Z3uRR+24TH
R0TIryBCo1+hCWhmtIdlV5IIsQR1Zx01u3fDFJZ6BMDlIkSjRo3qUVFR8dnIkSPnmc1mSKvKq6qq
3n7hhRcC2oRNQSFchEWItu85fdTSaPsWjNzyacO+Q4QA9ZsAh2yemeM00LAJICrAwGL//sY14Vqy
cbmTmpp6zcsvvzxiw4YN77/33nvFKpXqQWlVucFggMViyfvzn//8XHuXU0EhLD4iSqn4z1fT5v3+
ietvxTlHNOBtKN6Db6iFn0gFcNXAkZlA9J3OxBu2ALZqQKcHZ+LLX33/5Mcbc8NRi8C4lJzVBQUF
t5nN5gEMw/RPTEzsu2bNmp6CIFwjCAKampoAOH1CarW68cCBA6+NHj16viLiCpcCYXNW//65vZXr
Ph48KXN8zzzU2zqA9zAi5muCowTRAtwR4PQH54scaQBnFfeNe7Ry4sZdja3WNl0sNBoNYzAYYLPZ
IN9zur2IiYmZMWzYsPs4joPNZoO0wp9lWRgMBhBCGquqqtZ88sknC9avX7+/vYVTQUEifPOIAGRO
/2HTAw9/dzPH8+sRyTif3NVqjpAHP5E7RA0wekBvBKL15n0HzYtGPViR8e8djT+Hs/z++Oyzz0q+
+eab2VardWdERASv1+uDXnkdSk6fPr2eZVlQSqHVaqWV5L9aLJZtRUVFs+fMmTNw7Nix09avXx+S
TeEUFEJFmxa9toV/vp44/Mbk6AeTkqOHgxd6OGdSC4BVJkRyWAJope80pWCZA5WVTRvn//PI5/nr
zh24KIUOgrFjxw6YPHnyXc8///yqQ4cOHW6PMgwZMqTr448//iTHcY0ajeaX1atXHzl27Fh1eXn5
ZbUWTOG3x0UTIon0vqTjA+O7Jsf3MAzqYCDpQ9KiuoEX4wDoAcqAggfLNJ07x9X+UGk6BBa7Pll1
prjkkOXA8eO01ZNPFRQULn8uuhB5pOH7WPCsAUTFQGR40KYmdBrebkPyCgoKF5dLQ4gUFBR+07Sb
Y1VBQUFBIozbgJyHECLfpiPYLTtcJhtVzDcFhSuSC+6ayUSmebNoMF6OPb0giwvIRKf52NtL9HKs
iJWCwmVI0ELULDySyHh7sV6uexMnOd5ER/TwErxcl15UESYFhUufgIWIEOJNbNgAX+4CJYkS0Noi
chcfQfYeyKuVSClLGRQULl0C8hHJRMib+Khk756O3cN5spQAz5aPAOejOeRCw8uuuR8zzcdE9g5C
CBQxUlC4NAmFs5q4vbsfS+fELawvf5G3sJ7y9VYGBQWFy4SAhIhSKsoGvjz5cFg4rQ8VzlsmgXbN
mp+SCMiOg+2ayS0m0e1Y6ZopKFzihNpZzXo5DoezWvByrDirFRQuM0I1fC+JiSex8TWE70qm+T2Q
4XtPQ/eStaMIj4LCZUjYl3j4mczozafjXihlUqOCwhWMstZMQUGh3VHWmikoKLQ7/w/+tIxj8lIu
wgAAAABJRU5ErkJggg==">

Với Base64 thu được khi tải file logo và chạy

```
base64 python-logo.png
```

Base64 được dùng phổ biến khi dùng email với từ khóa MIME, để nhúng ảnh, gửi kèm file với email.

## Base64 là gì
Theo tài liệu định nghĩa Base64 [RFC3548](https://datatracker.ietf.org/doc/html/rfc3548.html#page-4):

**The Base 64 encoding is designed to represent arbitrary sequences of
octets in a form that requires case sensitivity but need not be
humanly readable.**

## Tại sao lại là 64?
Vì việc encoding sử dụng 64 ký tự (+1 ký tự = để padding).

64 ký tự gồm:

- 26 ký tự A-Z
- 26 ký tự a-z
- 10 ký tự 0-9
- `+` và `/` (hoặc thay bằng `-` và `_` khi encode URL)

## Cách encode
Biểu diễn nhóm 24-bit đầu vào thành 4 ký tự đầu ra.

24 bit tạo bởi 3 byte (3 * 8 == 24) đặt cạnh nhau từ trái qua phải, sau đó chia làm 4 phần 6 bits, mỗi phần đổi bit ra số rồi tra trong bảng xem ứng với ký tự nào. Do mỗi phần có 6 bit nên có khả năng biểu diễn 2**6 = 64 ký tự.

```
+--first octet--+-second octet--+--third octet--+
|7 6 5 4 3 2 1 0|7 6 5 4 3 2 1 0|7 6 5 4 3 2 1 0|
+-----------+---+-------+-------+---+-----------+
|5 4 3 2 1 0|5 4 3 2 1 0|5 4 3 2 1 0|5 4 3 2 1 0|
+--1.index--+--2.index--+--3.index--+--4.index--+
```

Đầu vào luôn cần là bội của 6 bits, nên nếu thiếu ta cần thêm vào đó các bit 0
cho đủ. Ví dụ có 4 ký tự đầu vào = 8 * 4 == 32 bits - (6 bits * 5) = 2 bits. 2 bits nên
phải thêm 4 bit 0 vào sau cho đủ 6 bit.

Mỗi 24 bits đầu vào sinh ra 4 ký tự Base64, nên đầu ra nếu thiếu ký tự cần thêm các ký tự `=` cho đủ bội của 4 phục vụ việc decode - chuyển ngược lại từ Base64 thành binary.

## Code Python để encode Base64
Python có sẵn thư viện `base64` với function `b64encode` để biến bytes đầu vào thành dạng text Base64.

Code sau code theo mô tả cách thực hiện Base64 ở trên:

```py
import string
b64 = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'

data = 'PyMi.vn'.encode('utf-8')
bits = []
for c in data:
    print(type(c), c, bin(c))
    bits.extend(bin(c)[2:].zfill(8))

output = []
for i24 in range(0, len(bits), 24):
    g1 = bits[i24:i24+24]
    for i in range(0, len(g1), 6):
        six_bits = g1[i:i+6]
        while len(six_bits) < 6:
            six_bits.append('0')
        n = int(''.join(six_bits), 2)
        output.append(b64[n])
        print(six_bits, n, b64[n])

while len(output) % 4 != 0:
    output.append('=')

print(''.join(output))
print(base64.b64encode(b'PyMi.vn'))
```

Output

```
<class 'int'> 80 0b1010000
<class 'int'> 121 0b1111001
<class 'int'> 77 0b1001101
<class 'int'> 105 0b1101001
<class 'int'> 46 0b101110
<class 'int'> 118 0b1110110
<class 'int'> 110 0b1101110
['0', '1', '0', '1', '0', '0'] 20 U
['0', '0', '0', '1', '1', '1'] 7 H
['1', '0', '0', '1', '0', '1'] 37 l
['0', '0', '1', '1', '0', '1'] 13 N
['0', '1', '1', '0', '1', '0'] 26 a
['0', '1', '0', '0', '1', '0'] 18 S
['1', '1', '1', '0', '0', '1'] 57 5
['1', '1', '0', '1', '1', '0'] 54 2
['0', '1', '1', '0', '1', '1'] 27 b
['1', '0', '0', '0', '0', '0'] 32 g
UHlNaS52bg==
b'UHlNaS52bg=='
```

## Tham khảo
https://datatracker.ietf.org/doc/html/rfc3548.html

Đăng ký ngay tại [PyMI.vn](https://pymi.vn) để học Python tại Hà Nội TP HCM (Sài Gòn),
trở thành lập trình viên #python chuyên nghiệp ngay sau khóa học.
