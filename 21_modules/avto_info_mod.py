# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 00:52:12 2022

@author: Sardorbek
"""

# MODUL yaratamiz

#def avto_info(kompaniya, model, rangi, korobka, yili, narxi=None):
#  """Avtomobil haqidagi malumotlarni lugat korinishida qaytaruvchi funksiya"""
#  avto = {'kompaniya':kompaniya,
#         'model':model,
#         'rangi':rangi,
#         'korobka':korobka,
#         'yili':yili,
#         'narxi':narxi}
#  return avto

#def avto_kirit():
#  """Foydalanuvchiga avto_info funksiyasi yordamida bir nechta avtolar haqida ma'lumotlarni bitta ro'yxatga joylash imkonini beruvchi funksiya"""
#  avtolar = [] #salondagi avtolar uchun bosh royxat
#  while True:
#    print("\nQuyidagi malumotlarni kiriting", end='')
#    kompaniya = input("Ishlab chiqaruvchi: ")
#    model = input("Modeli: ")
#    rangi = input("Rangi: ")
#    korobka = input("Korobka: ")
#    yili = input("Yili: ")
#    narxi = input("Narxi: ")
#    #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
#        #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#    avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili,narxi))
#    #Yana avto qoshish qoshmaslikni soraymiz
#    javob = input("Yana avto qoshasizmi? (ha/yo'q): ")
#    if javob == "yo'q":
#      break
#    return avtolar

#def info_print(avto_info):
#    """Avtomobillar haqida ma'lumotlar saqlangan lug'atni konsolga chiqaruvchi funksiya"""
#    print(f"{avto_info['rangi'].title()} {avto_info['kompaniya'].upper()} "
#          f"{avto_info['model'].upper()}, {avto_info['korobka']} korobka, "
#          f"{avto_info['yili']}-yil, {avto_info['narxi']}$")

#MODULni chaqirib olish