# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 22:30:01 2022

@author: Sardorbek
"""

#14-dars: Dictionary (Lug'at)

#car_0 = {'model': 'ferrari', 'rang': 'qizil'}
#print(car_0['model'])
#print(car_0['rang'])


#en_uz = {'apple':'olma', 'apricot':"o'rik", \
#         'banana':'banan'}

#mevalar = {'olma':10000, 'tarvuz':8000, \
#           'qovun':10000}
#print(f"Olma narxi {mevalar['olma']}")

#talaba_0 = {'ism': 'murod_olimov', 'yosh':20, \
#            't_yil':2000}
#print(f"{talaba_0['ism'].title()}, \
#{talaba_0['t_yil']}-yilda tug'ilgan, \
#{talaba_0['yosh']} yoshda")

#Yangi kalit so'z va qiymat qo'shish
#talaba_0['kurs'] = 4
#talaba_0['fakultet'] = 'informatika'
#talaba_0['ism'] = 'abdulloh'

# Bo'sh lug'at
#talaba_1 = {}
#talaba_1['ism']= 'qobil rasulov'
#talaba_1['kurs'] = 3
#talaba_1['yosh'] = 20
#print(talaba_1)
#print(f"Talaba {talaba_1['ism'].title()} \
#{talaba_1['kurs']}-kurs")

# Qiymatni yangilash
#talaba_1['kurs'] = 4
#print(f"Talaba {talaba_1['ism'].title()} \
#{talaba_1['kurs']}-kurs")

# #Kalit so'z-qiymat ni o'chirib tashlash
#talaba_0 = {'ism': 'murod_olimov', 'yosh':20, \
#            't_yil':2000}
#print(talaba_0)
#del talaba_0['yosh']
#print(talaba_0)

## LUG'ATNI QATORLARGA BO'LIB YOZISH
#telefonlar = {
#    'ali':'iphone x',
#   'vali':'galaxy s9',
#   'olim':'mi 10 pro',
#    'orif':'nokia 3310'
#    }

#.get() Metodi
#phone = telefonlar['ali']
#print(f"Alining telefoni {phone}")

#phone = telefonlar['hasan']
#print(f"Hasanning telefoni {phone}")

#phone = telefonlar.get('hasan','Bunday ism mavjud emas')
#print(phone)

#phone = telefonlar.get('hasan')
#print(phone)

#AMALIYOT
#ukam = {'ism':'saiabdulla', 
#        't_yil': 2005,
#        't_shahar':'xiva'}
#print(f"Ukamning ismi {ukam['ism'].title()}, \
#t_yil =ukam['t_yil']
#t_shahar = ukam['t_shahar']
#{Ukamning ismi {ukam['ism']), u {t_yil}-yilda, {t_shahar.title()} shahrida tug'ilgan.")

#taomlar = {'saidabdulla':'osh',
#           'xojiakbar':'manti',
#           'sobirjon':'shashlik',
#           'joshqin':'kabob',
#           'sardor':'norin'}
#xojiakbar = taomlar['xojiakbar']
#joshqin = taomlar['joshqin']
#saidabdulla = taomlar['saidabdulla']

#print(f"Xojiakbarning sevimli ovqati \
#{xojiakbar}.")

#python_izohli_lugati = {
#    'integer':"Butun son",
#    'float':"O'nlik son",
#    'string':"Matn",
#   'list':"Ro'yxat",
#    'tuple':"O'zgarmas ro'yxat"}
# print(python_izohli_lugati['tuple'])

# kalit = input("Kalit so'z kiriting:").lower()
# print(python_izohli_lugati.get(kalit,"Bunday so'z mavjud emas"))

# kalit = input("Kalit so'z kiriting:").lower()
# tarjima = python_izohli_lugati.get(kalit)
# if tarjima==None:
#     print("Bunday so'z mavjud emas")
# else:
#     print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")


























