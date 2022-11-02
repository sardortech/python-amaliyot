# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 12:53:36 2022

@author: Sardorbek
"""

#15 Lug'at elementlari bilan ishlash


# .items() METODI

#talaba_0 = {
#    'ism':'alijon',
#    'familiya':'shamshiyev',
#    'yosh':22,
#    'fakultet':'matematika',
#    'kurs':4
#    }

#print(talaba_0.items())

#for kalit, qiymat in talaba_0.items():
#    print(f"Kalit: {kalit}")
#    print(f"Qiymat: {qiymat} \n")
 
#telefonlar = {'ali':'iphone x',
#              'vali':'galaxy s9',
#              'olim':'mi 11 pro',
#              'orif':'nokia 3310'
#              }

#for k, q in telefonlar.items():
#    print(f"{k.title()}ning telefoni {q}")

# .keys() METODI
#mahsulotlar = { # Do'kondagi mahsulotlar
#    'olma':10000,
#    'anor':20000,
#    'uzum':40000,
#    'anjir':25000,
#    'shaftoli':30000
#    }

#print(mahsulotlar.keys())
#print('Do\'kondagi mahsulotlar:')
#for mahsulot in mahsulotlar.keys():
#    print(mahsulot.title())

#print('Do\'kondagi mahsulotlar:')
#for mahsulot in mahsulotlar:
#    print(mahsulot.title())

#bozorlik = ['anor', 'uzum', 'non', 'baliq']
##for mahsulot in mahsulotlar:
#    if mahsulot in bozorlik:
#        print(f"{mahsulot.title()} \
#{mahsulotlar[mahsulot]} so'm")

#for buyum in bozorlik:
#    if buyum not in mahsulotlar:
#        print(f"Iltimos, do'koningizga {buyum} \
#ham olib keling.")

## LUG'AT ELEMENTLARINI TARTIB BILAN CHIQARISH

#print("Do'konimizdagi mahsulotlar:")    
#for mahsulot in sorted(mahsulotlar):
#    print(mahsulot.title())
    
# `.values()` METODI
#print(telefonlar.values())

#print('Foydalanuvchilar quyidagi \
#telefonlarni ishlatishadi:')
#for tel in telefonlar.values():
#    print(tel)

#telefonlar = {
#    'ali':'iphone x',
#    'vali':'galaxy s9',
#    'olim':'mi 10 pro',
#    'orif':'nokia 3310',
#    'hamida':'galaxy s9',
#    'maryam':'huawei p30',
#    'tohir':'iphone x',
#    'umar':'iphone x'    
#    }

#print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
#for tel in set(telefonlar.values()):
#    print(tel)
    
#toys = {"ball", "car","lamp","ball"}

#AMALIYOT
#python_lugat = {'int':"butun son",
 #               'float':"o'nlik son",
#                'boolean':"Mantiqiy qiymat",
#                'for':"biror amalni qayta-qayta takrorlash tsikli",
#                'if':"shartlarni tekshirish operatori"
#                }

#for key, value in sorted(python_lugat.items()):
#    print(f"{key.title()}-{value.capitalize()}")


#davlatlar = {'uzbekistan':"tashkent",
#             'usa':"new York",
#             'russia':"moscow",
#             'canada':"toronto",
#             'norway':"oslo"
#             }

#print("Davlatlar:")
#for davlat in sorted(davlatlar.keys()):
#    print(davlat.upper())

#print('\nDavlatlarning poytaxtlari:')
#for poytaxt in sorted(davlatlar.values()):
#    print(poytaxt.title())

#menu = {
#        'osh':20000,
#        "lag'mon":22000,
#        'non':4000,
#        'choy':5000,
#        'shashlik':12000,
#        'somsa':6000,
#        'tabaka':15000
#        }

#print('3 ta taom buyurtma bering.')
#buyurtmalar = []
#for n in range(3):
#    buyurtmalar.append(input(f"{n+1}-taom:").lower())

#for buyurtma in buyurtmalar:
#    if buyurtma in menu:
#        print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
#    else:
#        print(f"Kechirasiz, bizda {buyurtma} yo'q.")