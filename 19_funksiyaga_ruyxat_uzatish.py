# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 00:49:53 2022

@author: Sardorbek
"""

# def bahola(ismlar):
#   baholar = {}
#   while ismlar:
#     ism = ismlar.pop()
#     baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#     baholar[ism] = int(baho)
#   return baholar

# talabalar = ['ali','vali','hasan','husan']
# baholar = bahola(talabalar[:])
# print(baholar)
# #RO'YXATGA O'ZGARTIRISH KIRITISH
# print(talabalar)


#AMALIYOT

# def katta_harf(matnlar):
#   """Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgatiruvchi funksiya"""
#   for i in range(len(matnlar)):
#     matnlar[i]=matnlar[i].title()

# ismlar = ['ali','vali','hasan','husan']
# katta_harf(ismlar)
# print(ismlar)

# def katta_harf(matnlar):
#   """Yuqoridagi funksiyani asl ro'yxatni o'zgartirmaydigan va yangi ro'yxat qaytaradigan qiluvchi funksiya"""
#   matnlar = matnlar[:]
#   for i in range(len(matnlar)):
#     matnlar[i]=matnlar[i].title()
    

# ismlar = ['ali','vali','hasan','husan']
# yangi_ismlar = katta_harf(ismlar)
# print(ismlar)
# print(yangi_ismlar)



# talabalar = ['ali','vali','hasan','husan']

# def bahola(ismlar):
#   baholar = {}
#   for ism in ismlar:
#     baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#     baholar[ism] = int(baho)
#   return baholar

# baholar = bahola(talabalar)
# print(baholar)
# #RO'YXATGA O'ZGARTIRISH KIRITISH
# #print(talabalar)  