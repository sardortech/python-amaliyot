# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 01:55:13 2022

@author: Sardorbek
"""

# Dasturlar foydalanuvchining muammolarini hal qilish uchun yoziladi. Buning uchun esa, foydalanuvchi bilan aloqa o'rnatish, undan turli ma'lumotlarni qabul qilib olib talab etiladi. Misol uchun, dasturimiz foydalanuvchiga ismi bilan murojat qilishi uchun, avval uning ismini so'rashi kerak. Yoki, foydalanuvchi istagan ma'lumotni topish uchun avval undan biror kalit so'z kiritishni so'rash kerak va hokazo.

# Foydalanuvchi kiritgan qiymatni biror o'zgaruvchiga yuklash, va undan dastur davomida foydalanish mumkin.

# ism = input("Ismingiz nima? ")
# print(f'Salom, {ism.title()}')

# `input()` finktsiyasi ichidagi matn ingliz tilida prompt, savol deyiladi. Aslida biz savolni ham o'zgaruvchiga yuklab, shaxsiy so'rovnomalar ham yaratishimiz mumkin.

# ism = input("Ismingiz nima? ")
# savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
# yosh = input(savol)

#Sonlar va input()

# ism = input("Ismingiz nima? ")
# savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
# yosh = input(savol)
# yosh = int(yosh) # yosh ni butun songa o'tkazamiz
# height = input("Bo'yingiz necha metr? ")
# height = float(height) # bo'yni o'nlik songa o'tkazamiz

# while Tsikli bilan tanishamiz
#while ham takrorlash operatori bo'lib, for dan farqli ravishda, toki ma'lum bir shart to'g'ri (True) bo'lsa, kodni takrorlayveradi.

# son = 1 # son ga 1 qiymatini beramiz
# while son<=5: # toki son 5 dan kichik yoki teng ekan...
#     print(son, end=' ') # son ni konsolga chiqaramiz,
#     son = son+1 # songa 1 qo'shamiz.

# while va input()
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)

#ishora (flag)
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing: "
# ishora = True
# while ishora:
#   qiymat = input(savol)
#   if qiymat == 'exit':
#     ishora = False
#   else:
#     print(float(qiymat)**2)
# print("Dastur to'xtadi")

# break while
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True: # abadiy tsikl
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break # tsiklni to'xtatish
#     else:
#         print(float(qiymat)**2)

# break for
# Break operatori fortsiklini to'xtatish uchun ham ishlatiladi.
# sonlar = list(range(1,11))
# for son in sonlar: 
#     if son == 5: # son 5 ga teng bo'lsa kod to'xtaydi
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng")

# Continue operatori - breakning aksi
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5: # son 5 ga teng bo'lsa tiskl boshiga qaytadi
#         continue
#     print(f"{son} ning kvadrati {son**2} ga teng")

# Continue while
# son = 0
# while son<10:
#     son += 1
#     if son%2!=0:
#         continue
#     else:
#         print(son)

#Abadiy tsikl tuzogi 
# infinite loop
# son = 0
# while son<10:
#     if son%2!=0:
#         continue
#     else:
#         print(son)

# son = 1
# while son>0: 
#     son += 1
#     if son%2!=0:
#         continue
#     else:
#         print(son)

#AMALIYOT
# savol = 'Sevga kitobingizni kiriting'
# savol += "(dastur to'xtashi uchun 'exit' deb yozing): "

# while True:
#   kitob = input(savol)
#   if kitob == 'exit':
#     break
# print("Dastur to'xtadi")

# savol = "Yoshingizni kiriting: "

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
#     yosh = int(qiymat)

#     if yosh<7:
#         narh = 2000
#     elif 7<=yosh<18:
#         narh = 3000
#     elif 18<=yosh<65:
#         narh = 10000
#     else: narh = 0
    
#     if narh==0:
#         print("Sizga chipta bepul")
#     else:
#         print(f"Chipta {narh} so'm")

# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat=='exit'.title():
#         break
#     elif float(qiymat)<0:
#       continue
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")