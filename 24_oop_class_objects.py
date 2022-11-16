# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 20:16:19 2022

OOP: Klasslar

@author: Sardorbek
"""

# def salom():
#     print("Assalamu Aleykum")
    
# print(type(salom))


#Klass yaratamiz obyek yaratish uchun

# class Talaba:
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
        
#     def get_name(self):
#         return self.ism
    
#     def last_name(self):
#         return self.familiya
    
#     def get_age(self,yil):
#         return yil-self.tyil
    
#     def tanishtir(self):
#         return f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tu'gilganman"    
    
    
        
# talaba1= Talaba("Olim","Olimov",2001)

# ## KLASSDAN BIR NECHTA OBYEKTLAR YARATISH
# # Yuqoridagi klassdan biz istalgancha obyektlar yaratishimiz mumkin:
# talaba2 = Talaba("Olim","Olimov",1995)
# talaba3 = Talaba("Husan","Akbarov",2004)
# talaba4 = Talaba("Hasan","Akbarov",2004)



# PASS - OPERATORI (hech qanday vazifa bajarmaydigan operator)
#bunday operatordan bosh Metodlar yaratish mumkin

# AMALIYOT

# class User:
#     def __int__(self,name,username,email):
#         self.name = name
#         self.uname = username
#         self.mail = email
    
#     def describe():
#         pass
    
#     def get_email():
#         pass


# class User:
#     def __init__(self,name,username,email):
#         self.name = name
#         self.username = username
#         self.email = email
        
#     def get_info(self):
#         print("Foydalanuvchi haqidagi ma'lumot:")
#         return f"Ismi: {self.name}, Foydalanuvchi ismi: {self.username}, Elektron pochta: {self.email}"

# user1 = User("Sardor", "sabirovs","123@mail.ru")