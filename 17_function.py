# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 21:56:40 2022

@author: Sardorbek
"""

#Funksiya yaratishda "def" kalit sozi yordamida yaratamiz

# def salom_ber():
#   """Salom beruvchi funksiya"""
#   print("Assalamu Aleykum")

# salom_ber()

#FUNKSIYAga qiymat uzatish
# def salom_ber(ism):
#   """Foydalanuvchi ismini qabul qilib, unga salom beruvchi funksiya"""
#   print(f"Assalamu Aleykum, hurmatli {ism.title()}")

# salom_ber('sardor')
# salom_ber('sobir')

#DOCSTRING - funksiya qanday ishlashi to'grisidagi ma'lumot
# def toliq_ism(ism, familiya):
#   """Foydalanuvchi ism va familiyasini jamlash chiqaruvchi funksiya"""
#   print(f"Foydalanuvchi ismi: {ism.title()}\n"
#   f"Foydalanuvchi familiyasi: {familiya.title()}")

#toliq_ism('olim', 'hokimov')
#toliq_ism('hokimov', 'olim') #argumentlarni kiritishda ketma-ketlikka etibor berish kerak

# def yosh_hisobla(ism, tugilgan_yil):
#     """Foydalanuvchi yoshini hisoblaydigan dastur"""
#     print(f"{ism.title()} {2020-tugilgan_yil} yoshda")

# #yosh_hisobla('olim', 1997)
# #yosh_hisobla(1997, 'olim') #Error

# #xato chiqmasligini uchu
# ### KALIT SO'Z BILAN UZATISH
# yosh_hisobla(tugilgan_yil=1997, ism='olim')

### STANDART QIYMAT

# def yosh_hisobla(tugilgan_yil, joriy_yil=2020): # joriy yil uchun st.qiymat 2020
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")

#yosh_hisobla(1995,2020)
#yosh_hisobla(1993)

## FUNKSIYAGA MUROJAT QILISHDA XATOLIKLAR
# def yosh_hisobla(tugilgan_yil, joriy_yil=2020):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")

# tyil = input("Tug'ilgan yilingizni kiriting: ")
# yosh_hisobla(tyil)

#AMALIYOT
# def tugilgan_yil_hisobla(ism, yosh):
#   """Foydalanuvchi ismi va yoshini sorab, uning tug'gilgan yilini hisoblaydigan funksiya"""
#   print(f"{ism.title()}, siz {2022-yosh}-yildasiz")

# tugilgan_yil_hisobla('sardor', 21)

#yoki
# Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.
# def tyiltop(ism, yosh):
#     print(f"{ism.title()} {2020-yosh} yoshda")

# tyiltop('olim',2002)

#Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
# def kv_kub_top(son):
#   """Kiritilgan sonning kvadrati va kubini konsolga chiqaruvchi funksiya"""
#   print(f"{son} ning kvadrati {son**2} ga, kubi {son**3} ga teng")

# kv_kub_top(12)

# def juft_toq_top(son):
#   """Sonni qabul qilib, juft yoki toq sonligini konsolga chiqaruvchi funksiya"""
#   if (son % 2) == 0:
#     print(f"{son} juft son")
#   else:
#     print(f"{son} toq son")

# juft_toq_top(6)
# juft_toq_top(11)

# def solishtir(x,y):
#   """Ikki sonni solishtiruvchi funksiya"""
#   if x>y:
#     print(f"{x}>{y}")
#   elif x<y:
#     print(f"{y}>{x}")
#   else:
#     print(f"{x}={y}")

# solishtir(10,20)
# solishtir(-9,12)
# solishtir(1223*5,5**4)

# Foydalanuvchidan x va y sonlarini olib, x^y ni konsolga chiqaruvchi funksiya yozing.
# Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.
# def daraja(x,y=2):
#     print(f"{x} ning {y}-darajasi {x**y} ga teng")

# daraja(5,2)
# daraja(3,3)
# daraja(94,4)
# daraja(6)

# Foydalanuvchidan son qabul qilib, sonni 2, 3, 4 va 5 ga qoldiqsiz bo'linishini tekshiruvchi
# funksiya yozing.
# Natijalarni konsolga chiqaring ("15 soni 3 ga qoldiqsiz bo'linadi" ko'rinishida)
# def bolinish_alomatlari(son):
#     for n in range(2,11):
#         if not son%n:
#             print(f"{son} {n} ga qoldiqsiz bo'linadi")

# bolinish_alomatlari(20)