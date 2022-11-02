# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 00:15:03 2022

@author: Sardorbek
"""

# lambda - nomsiz funksiya
#1-qulayligi: funksiyani ichida ishlatish
# import math

# def nom(argument):
#   return ifoda

# uzunlik = lambda pi, r : 2*pi*r
# print(uzunlik(math.pi,10))

# kvadrat = lambda x, y : x ** y #x ning y-nchi darajasini topadigan funksiya
# print(kvadrat(3,2))

# def daraja(n):
#   return lambda x : x**n

# kvadrat = daraja(2)
# kub = daraja(3)
# print(f"3-ning kvadrati {kvadrat(3)} ga, kubi {kub(3)} ga teng")

# map() FUNKSIYASI

# from math import sqrt #sqrt - kvadrat ildiz hisoblaydigan funksiya

# sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati
# ildizlar = list(map(sqrt,sonlar))
# print(ildizlar)

#sonlar = list(range(11)) # 0 dan 10gacha sonlar royxati

# def daraja2(x):
#   """Berilgan sonning kvadratini qaytaruvchi funksiya"""
#   return x*x

#print(list(map(daraja2,sonlar))) # sonlarning kvadratini hisoblaymiz


# kvadratlar = list(map(lambda x:x**2,sonlar))
# print(kvadratlar)

#tsikl yordamida yozganimiz quyidagicha:
# kvadratlar = []
# for son in sonlar:
#   kvadratlar.append(sonlar) 
# print(kvadratlar)

# a = [4,5,6]
# b=[7,8,9]
# a_plus_b = list(map(lambda x,y:x+y,a,b)) # x ning orniga a, yning orniga b
# print(a_plus_b)

# ismlar = ['hasan','husan','olim','umid']
# print(list(map(lambda matn:matn.upper(),ismlar))) 

# filter() FUNKSIYASI
#import random as r
#sonlar = r.sample(range(100),10) #0 - 99 oralig'ida
#print(sonlar)
# def juftmi(x):
#   """x juft bo'lsa True, akso holda False qaytaradi"""
#   return x%2==0

# juft_sonlar = list(filter(juftmi,sonlar))
#print(juft_sonlar)

# juft_sonlar = list(filter(lambda x: x%2==0,sonlar))
# print(juft_sonlar)

# .stratswith(harf) - Bu metod, berilgan matn shu harfdan boshlanadimi yoki yo'q tekshiradi va True yoki False qiymat qaytaradi.

# mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]

#mevalar_b = list(filter(lambda meva:meva.startswith('a'),mevalar))
#print(mevalar_b)

# mevalar2 = list(filter(lambda meva:len(meva)<=5, mevalar))
# print(mevalar2)

# mevalar_a, mevalar_r = list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')), mevalar))

# print(f"{mevalar_a}"
#      f"\n{mevalar_r}")