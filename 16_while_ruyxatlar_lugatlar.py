# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 21:56:44 2022

@author: Sardorbek
"""

# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# ismlar = []
# n=1 # ismlarni sanash uchun o'zgaruvchi
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     takrorlash = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     if takrorlash =='ha':
#         n+=1
#         continue
#     else:
#         break

# print("Yaqin do'stlaringiz ro'yxati: ")
# for ism in ismlar:
#   print(ism)

# WHILE YORDAMIDA LUG'ATNI TO'LDIRISH
# print("Do'stlaringizni yoshini saqlaymiz.")
# dostlar = {}
# ishora = True
# while ishora:
#   ism = input("Do'stingiz ismini kiriting: ")
#   yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#   dostlar[ism]=int(yosh) #ism kalit, yosh qiymat

#   javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
#   if javob == "yo'q":
#     ishora = False

# for ism, yosh in dostlar.items():
#   print(f"{ism.title()} {yosh} yoshda")

#Ro'yxat elementlarini o'chirish
#remove(qiymat)
# cars = ['lacetti', 'nexia', 'toyota', 'nexia', 'audi', 'malibu', 'nexia']
# car = 'nexia'
# while car in cars: #toki nexia cars ro'yxati ichida ekan...
#   cars.remove(car) #nexia ni ro'yxatdan olib tashla
# print(cars)

#Ro'yxatdan ro'yxatga element ko'chirish:
# .pop() orqali sugurib olamiz
#talaba -kalit, baho-qiymat
# talabalar = ['hasan','husan','olim','botir']
# baholangan_talabalar = {}
# while talabalar:
#   talaba = talabalar.pop()
#   baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#   print(f"{talaba.title()} baholandi")
#   baholangan_talabalar[talaba]=int(baho)

#AMALIYOT
# print("Buyurtma qabul qiluvchi dastur: ")
# buyurtmalar = []
# n = 1
# while True:
#   savol = f"{n}-buyurtmangizni nomini kiriting: "
#   buyurtma = input(savol)
#   buyurtmalar.append(buyurtma)
#   takrorlash = input("Yana buyurtma qo'shasizmi? (ha/yo'q)")
#   if takrorlash == 'ha':
#     n +=1
#     continue
#   else:
#     break

# print("Buyurtmalaringiz: ")
# for buyurtma in buyurtmalar:
#   print(buyurtma)

#Qisqartirilgan varianti:
# savat =[]
# while True:
#     mahsulot = input("Savatga mahsulot qo'shing:")
#     savat.append(mahsulot)
#     javob = input("Yana mahsulot qo\'shasizmi?(ha/yo\'q)")
#     if javob != 'ha':
#         break

# print("Buyurtmalaringiz: ")
# for mahsulot in savat:
#   print(mahsulot)

# print("E-bozor uchun mahsulotlar va ularning narxlari lug'atini shakllantiruvchi dastur: ")
# mahsulotlar = {}
# while True:
#   mahsulot = input("Mahsulot nomini kiriting: ")
#   narx = input(f"{mahsulot.title()}ning narxini kiriting: ")
#   narx = int(narx)
#   mahsulotlar[mahsulot]=narx
#   javob = input("Yana mahsulot qo'shasizmi? (ha/yo'q)")
#   if javob != 'ha':
#     break

# print("Sizning mahsulotlaringiz va ularning narxlari: ")
# for mahsulot, narx in mahsulotlar.items():
#   print(f"\n{mahsulot.title()}: {narx}so'm")

# buyurtmalar = ['olma', 'anjir', 'uzum', 'qovun']
# mahsulotlar = {
#   'olma': 20000,
#   'shaftoli': 25000,
#   'tarvuz': 18000,
#   'uzum': 22000
# }

# while buyurtmalar:
#   buyurtma = buyurtmalar.pop()
#   if buyurtma in mahsulotlar.keys():
#     narx = mahsulotlar[buyurtma]
#     print(f"{buyurtma.title()} - {narx} so'm")
#   else:
#     print(f"Bizda {buyurtma} yo'q")