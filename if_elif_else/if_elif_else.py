# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 23:22:11 2022

@author: Sardorbek
"""

#IF_ELSE
# son = -50
# if son<0:
#   print("Manfiy son")
# else:
#   print("Musbat son")

#IF_ELIF_ELSE
# yosh = int(input("Yoshingiz nechida?\n>>>"))
# if yosh <=4:
#   print("Sizga kirish bepul")
# elif yosh<=12:
#   print("Sizga kirish 5000 so'm")
# elif yosh<=18:
#   print('Sizga kirish 8000 so\'m')
# else:
#   print('Sizga kirish 10000 so\'m')
#qisqartirilgan variant
# yosh= int(input("Yoshingiz nechida?"))
# if yosh<=4:
#   narx = 0
# elif yosh<=12:
#   narx = 5000
# elif yosh<=18:
#   narx = 8000
# else:
#   narx = 10000

# print(f"Sizga kirish {narx} so'm")

# kun = input ("Bugun qaysi kun?>>>")
# if kun.lower() =='shanba' or kun.lower()=='yakshanba':
#   print("Bugun dam olish kuni.")
# else:
#   print("Bugun ish kuni.")

# kun = input ("Bugun qaysi kun?>>>")
# harorat = float(input('Havo harorati qanday?'))
# if kun.lower() =='shanba' and harorat>=30:
#   print("Cho'milgani ketdik.")
# elif kun.lower()=="yakshanba" and harorat <30:
#   print("Uyda dam olamiz.")

# kun = input ("Bugun qaysi kun?>>>")
# harorat = float(input('Havo harorati qanday?'))
# if (kun.lower() =='shanba' or kun.lower() == 'yakshanba') and harorat>=30:
#   print("Cho'milgani ketdik.")
# elif (kun.lower() =='shanba' or kun.lower()=="yakshanba") and harorat <30:
#   print("Uyda dam olamiz.")

# narx = 15000 #mijoz 15000ga taom oldi
# choy = True #mijoz choy ham oldi
# salat = False #mijoz salat olmadi
# if choy and salat: #agar mijoz choy ham salat ham olgan bulsa
#   narx = narx + 10000 #narxga 10000 som qushamiz
# elif choy or salat: #agar choy yoki salat olgan bulsa
#   narx = narx + 5000 #narxga 5000 qoshamiz
# print(f"Jami {narx} so'm")

# narx = 15000 #mijoz 15minga ovqat sotib oldi
# choy = 1
# salat = 0
# non = 1
# kampot = 1
# assorti = 0
# #Quyidagi har bir shart alohida tekshiriladi vva bir biriga bogliq emas
# if choy: #agar choy olsa
#   print("Mijoz choy oldi.")
#   narx = narx + 3000
# if salat: #agar salat olsa
#   print("Mijoz salat oldi.")
#   narx = narx + 5000
# if non: #agar non olsa
#   print("Mijoz non oldi.")
#   narx = narx + 2000
# if kampot:
#   print("Mijoz kampot oldi")
#   narx = narx + 15000
# if assorti:
#   print("Mijoz assorti oldi")
#   narx = narx + 20000

# print(f"Jami {narx} so'm.\nTashrifingiz uchun rahmat!")

#in operatori
# menu = ['osh', 'kabob', 'shahlik', 'norin']
# 'manti' in menu # menuda manti bormi?
# print(menu)

# menu = ['osh', 'kabob', 'shahlik', 'norin']
# ovqat = input("Nima ovqat yeysiz?\n")
# if ovqat.lower() in menu:
#   print("Buyurtma qabul qilindi.")
# else:
#   print("Afsuski bizfa bunday ovqat yo'q")

#not in -  operatori - yoqmi deb tarjima qilinadi
#ikki royxatni solishtirish
# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ["osh","somsa","manti", "shashlik"]

# for taom in buyurtmalar:
#     if taom in menu:
#         print(f"Menuda {taom} bor")
#     else:
#         print(f"Kechirasiz, menuda {taom} yo'q")

#Royxat bosh emasligini tekshirish
# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ["osh","somsa","manti", "shashlik"]

# if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"Menuda {taom} bor")
#         else:
#             print(f"Kechirasiz, menuda {taom} yo'q")
# else: # agar ro'yxat bo'sh bo'lsa
#     print("Savatchangiz bo'sh!")

#AMALIYOT
# son = float(input("Juft son kiriting: "))
# if son%2:
#     print('Bu son juft emas.')
# else:
#     print("Rahmat!")

# yosh = int(input("Yoshingiz nechida?"))

# if yosh<=4 or yosh>=60:
#     narh = 0;
# elif yosh < 18:
#     narh = 10000
# else:
#     narh = 20000
# print(f"Chipta {narh} so'm")

# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# if x == y:
#   print(f"{x} = {y}")
# elif x<y:
#   print(f"{x}<{y}")
# else:
#   print(f"{x}>{y}")

# mahsulotlar = ['sabzi', 'kartoshka', 'pomidor', 'gosht', 'tovuq', 'ichimliklar', 'sir', 'kolbasa', 'yog', 'karam', 'bodring']

# savat = []
# for n in range(5):
#   savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# for mahsulot in savat:
#   if mahsulot in mahsulotlar:
#     print(f"Do'konimizda {mahsulot} bor.")
#   else:
#     print(f"Kechirasiz, do'konimizda {mahsulot} yo'q.")

# mahsulotlar = ['un', "yog'", "sovun",'tuxum', 'piyoz', 'kartoshka', 'olma', 'banan','uzum', 'qovun']

# savat = []
# for n in range(5):
#   savat.append(input(f"Savatga {n+1}-mahsulotigizni kiriting: "))
  
# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#   if mahsulot in mahsulotlar:
#     bor_mahsulotlar.append(mahsulot)
#   else:
#     mavjud_emas.append(mahsulot)

# if mavjud_emas:
#   print(f"Do'konimizda quyida mahsulotlar yo'q:")
#   for mahsulot in mavjud_emas:
#     print(mahsulot)
# else:
#   print('Siz so\'raga barcha mahsulotlar bor')

# foydalanuvchilar = ['sardors', 'sabirovs', 'sobirs', 'shoxruxs', 'suxrobs', 'navruzs']
# yangi_login=input('Yangi login kiriting:\n>>>')

# if yangi_login.lower() in foydalanuvchilar:
#   print('Login band, yangi login tanlang: ')
# else:
#   print(f"Xush kelibsiz, {yangi_login.title()}!")

# son = int(input("Butun son kiriting: "))
# for n in range(2,11):
#   if not (son%n):
#     print(f"{son} soni {n} ga qoldiqsiz bo'linadi")

  







