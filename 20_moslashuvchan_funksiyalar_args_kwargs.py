# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 00:50:37 2022

@author: Sardorbek
"""

# *args usuli
# def summa(*sonlar):
#   """Kiritilgan sonlarni yigindisini hisonlaydigan funksiya"""
#   yigindi = 0
#   for son in sonlar:
#     yigindi += son
#   return yigindi
# print(summa(1,2,5,5,6,200))

# def summa(*sonlar):
#   return sum(sonlar)

# print(summa(2))
# print(summa(3,4,8,9))
# print(summa(552,556,666))

# def summa(x,y,*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     return x+y+sum(sonlar)

# print(summa(2))

## `**kwargs` USULI
# def avto_info(kompaniya,model,**malumotlar):
#     """Avto haqidagi ma'lumotlarni lug'at ko'rinishdia qaytaruvchi funksiya"""
#     malumotlar['kompaniya']=kompaniya
#     malumotlar['model']=model
#     return malumotlar

# avto1 = avto_info("GM", "malibu", rang='qora', yil=2018)
# avto2 = avto_info("Kia", "K5", rang='qizil', narh=35000)

#AMALIYOT
# def multiply(*sonlar):
#   """Kiritilgan sonlarni kopaytmasini hisoblaydigan funksiya"""
#   kopaytma = 1
#   for son in sonlar:
#     kopaytma *= son
#   return kopaytma

# print(multiply(12,12,55))

# def talaba_info(familiya,ism, **malumotlar):
#   """Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing. Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin."""
#   malumotlar['familiya']=familiya
#   malumotlar['ism']=ism
#   return malumotlar

# talaba2 =talaba_info('Abdullayev', 'Abdulla', tyil = 2001, tshahar = 'andijon')