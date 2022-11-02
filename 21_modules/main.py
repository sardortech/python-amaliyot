# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 00:51:33 2022

@author: Sardorbek
"""

#import avto_info_mod

# avto1 = avto_info_mod.avto_info("GM", "Malibu", "Qora", "Avtomat", 2020, 40000)
# avto_info_mod.info_print(avto1)

# funksiyalar fayl nomini har doim yozmaslik uchun:
# import avto_info_mod as aim
# avto1 = aim.avto_info("GM", "Malibu", "Qora", "Avtomat", 2020, 40000)
# aim.info_print(avto1)

#har gal modulni nomini yozmasdan togridan togri funksiya nomini yozib ketishimiz ham mumkin
# from avto_info_mod import avto_info, info_print

# avto1 = avto_info("GM", "Malibu", "Qora", "Avtomat", 2020, 40000)
# info_print(avto1)

#chaqirayotgan funksiyamizga yangi nom beramiz:
# from avto_info_mod import avto_info as ainfo, info_print as iprint
# avto1 = ainfo("GM", "Malibu", "Qora", "Avtomat", 2020, 40000)
# iprint(avto1)

# * - avto_info_mod faylimizdagi hamma funksiyalarimizni chaqirish uchun
# lekin kopincha bu tavsiya qilinmaydi, chunki bazida katta modulla boladi, va ularni ichida yuzlab funksiylar boladi, qorishib ketishi mumkin
# from avto_info_mod import *
# avto1 = avto_info("GM", "Malibu", "Qora", "Avtomat", 2020, 40000)
# info_print(avto1)

#PYTHON MODULLARI
# Python dasturlash tili tayyor modullar bilan keladi, modullarning to'liq ro'yxatini quyidagi bo'glama orqali kirib ko'rishingiz mumkin: https://docs.python.org/3/py-modindex.html

# import math

# x = 400
# print(math.sqrt(x))
# print(math.pow(5,3)) # pow(x,y) - xning  y-darjasini qaytaradi
# print(math.pi) #pi ni qiymati aniq chiqazib beradi
# print(math.log2(8))
# print(math.log10(100))  # (log2(x) va log10(x) - x` ning 2va 10-lik logorifmini qaytaruvchi funksiya

# random Moduli
# random(a,b)
# import random as r # random modulini r deb chaqirayapmiz

# #randint(a,b)
# son = r.randint(50,100) # 0 va 100 oralig'ida tasodifiy son
# print(son)

# CHOICE funksiyasi bizdagi biror bir qiymatdan tasodifiy tanlab oladi
#choice(x)
# import random as r
# # ismlar = ['olim','anvar','hasan','husan']
# # ism = r.choice(ismlar) # ismlar dan tasodifiy ism tanlaymiz
# # print(ism)
# # print(r.choice(ism)) # ismdan tasodifiy harf tanlaymiz

# x = list(range(0,51,5))
# print(x)
# print(r.choice(x))

#SHUFFLE - shuffle(x) x ichidagi elementlarni tasodifiy tartibda qaytaruvchi funksiya. - aralashtrib tashaydi
# import random as r
# x = list(range(11))
# print(x)
# r.shuffle(x)
# print(x)