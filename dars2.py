# def avto_info(Kompaniya, model, rangi, karobka, yili, narhi=None):
# 	"""Avtomobil Haqida Ma'lumolarni Lug'at Ko'rinishida Qaytaruvchi Funksiya"""
# 	avto = {
# 	"kompaniya": Kompaniya,
# 	"model": model,
# 	"rang": rangi,
# 	"karobka": karobka,
# 	"yil": yili,
# 	"narh": narhi,
# 	}	
# 	return avto

# def avto_kirit():
# 	"""Foydalanuvchiga avto_info funksiyasi bir nechta avtolar haqida ma'lumotlar qaytaruvchi funksiya"""
# 	avtolar = []
# 	while True:
# 		print("\nQuyidagi ma'lumotlarni Kiriting", end="")
# 		Kompaniya = input("Ishlab Chiqaruvchi: ")
# 		model = input("Modeli: ")
# 		rangi = input("Rangi: ")
# 		karobka = input("Karobka: ")
# 		yili = input("Ishlab Chiqarilgan Yili: ")
# 		narhi = input("Narhi: ")
# 		avtolar.append(avto_info(Kompaniya, model, rangi, karobka, yili, narhi))
# 		javob = input("Yana avto qo'shasizmi? (xa/yo'q): ")
# 		if javob == "yo'q":
# 			break
# 	return avtolar


# def info_print(avto_info):
# 	"""Avtomabillar Haqida Ma'lumotlar Saqlangan Lu'gatni Konsolga Chiqaruchi Funksiya"""
# 	print(
# 		f"{avto_info['rang'].title()} {avto_info['kompaniya'].upper()}"
# 		f"{avto_info['model'].upper()} {avto_info['karobka']} karobka, "
# 		f"{avto_info['yil']}-yil, {avto_info['narh']}$ "
# 	)				'


# print("TESTGA XUSH KELIBSIZ !!!")
# while True:
# 	ism = input("Ismingizni Kiriting: ")
# 	fam = input("Familyangizni Kiriting: ")
# 	print("Test Boshlandi !")
# 	savol = input("Dunyodagi Eng Oson Dasturlash Tili Qaysi (A) Python, (B) RUBY , (C) PASCAL: ")
# 	if savol == 'A':
# 		print("To'gri Javob")
# 	elif savol == 'B':
# 		print("Xato Javob")
# 	elif savol == 'C':
# 		print("Xato Javob")		
# 	print("Ikkinchi Savol !")
# 	savol2 = input("Qaysi Dasturlash Tili Keng Tarqalgan Hozirgi Kunda (A) C++, (B) Delphi, (C) Python: ")
# 	if savol2 == 'C':
# 		print("To'gri Javob")
# 	elif savol2 == 'A':
# 		print("Xato Javob")	
# 	elif savol2 == 'B':
# 		print("Xato Javob")
# 	print("Uchinchi Savol !")

# 	savol3 = input("O'yin Yozish Uchun Eng Qulay Dasturlash Tili Qaysi (A) JavaScript, (B) Python, (C) C++,: ")
# 	if savol3 == 'C':
# 		print("To'g'ri Javob")
# 	elif savol3 == 'A':
# 		print("Xato Javob")
# 	elif savol3 == 'B':
# 		print("Xato Javob")
# 	print("To'rtinchi Savol !")
# 	savol4 = input("Siz Hozirgi Kunda Qaysi Dasturlash Tilini O'rganayapsiz (A) Python, (B) Html, (C) Java, (D) Qiziq Emas,: ")
# 	if savol4 == 'A' or 'B' or 'C':
# 		elif savol4 == 'D':
# 			print("Yo'q Adashasiz IT Sohasi Juda Qiziq")	 		
# 				print("Yaxshi")
# 	print("Beshinchi Savol !")
# 	savol5 = input("Sun'iy Intelect Uchun Qaysi Dasturlash Tilidan Foydalaniladi (A) Python, (B) Go, (C) Github: ")
# 	if savol5 == 'A':
# 		print("To'g'ri Javob")
# 	elif savol5 == 'B':
# 		print("Xato Javob")								
# 	elif savol5 == 'C':
# 		print("Xato Javob")
# 	print(f"Tabriklayman Siz Testni Yakunladingiz !")
# 	savol6 = input("Yana Test Yechasizmi (xa yoki yo'q): ")
# 	if savol6 == "yo'q":
# 		break		

# import turtle
# t = turtle.Turtle()
# p = turtle.Turtle()

# t.width(3)
# t.color("red")

# p.width(3)
# p.color("red")

# t.p = "shape"
# t.left(40)
# t.forward(100)
# for side in range(185):
# 	t.forward(1)
# 	t.left(1)
# t.hideturtle()

# if t.p =="shape":
# 	p.left(140)
# 	p.forward(100)
# 	for side in range(185):
# 		p.forward(1)
# 		p.right(1)
# p.hideturtle()

# t.speed(0)
# p.speed(0)

# import math
# uzunlik = lambda pi, r : 2*pi*r
# print(uzunlik(math.pi,10)) 

# kvadrat = lambda x, y : x ** y
# print(kvadrat(3, 2))		

# a = [4, 5, 6]
# b = [7, 8, 9]
# a_plus_b = list(map(lambda x, y: x + y, a, b))
# print(a_plus_b)

# ismlar = ['hasan', 'husan', 'olim', 'umid']
# print(list(map(lambda matn:matn.upper(),ismlar)))

# sonlar = list(range(50,61)) 
# print(list(map(lambda x : x//2, sonlar)))

# import random as r

# sonlar = r.sample(range(330000000, 340000000), 10)
# print(sonlar)

# def juftmi(x):
# 	"""x juft bo'lsa True, aks holda False qaytaruvchi Funksiya"""
# 	return x % 2 == 0

# import random as r
# sonlar = r.sample(range(100), 10)
# print(sonlar)

# juft_sonlar = list(filter(lambda x: x % 2 == 0, sonlar))
# print(juft_sonlar)

# mevalar = ["olma", "anor", "anjir", "shaftoli", "o'rik", "tarvuz", "banan"]
# harf = "o"
# mevalar1 = list(filter(lambda meva: meva.startswith(harf), mevalar))
# print(mevalar1)

# mevalar2 = list(filter(lambda meva: len(meva) <= 5, mevalar))
# print(mevalar2)

# print(list(filter(lambda meva: (meva.startswith("a") and meva.endswith("r")), mevalar)))

# sonlar = r.sample(range(100), 10)
# juft = [son for son in sonlar if son%2==0]; print(juft)

# f1 = lambda x: x * 10
# print(f1(10))

# f2 = lambda x, y: x * y
# print(f2(5, 4))

# from random import sample
# from math import sqrt

# x = list(range(0, 1001))
# y = sample(x, k=10)
# print(y)

# ildizlar = list(map(lambda n: sqrt(n), y))
# print(ildizlar)

# toq_sonlar = list(filter(lambda n: n % 2, y))
# print(toq_sonlar)

# def tubmi(x):
# 	if x % 2 == 0 or x < 2:
# 		return False
# 	if x == 2 or x == 3:
# 		return True
# 	for i in range(3, x, 2):
# 		if x % i == 0:
# 			return False
# 	return True
	
# tub_sonlar = list(filter(tubmi, range(100)))
# print(tub_sonlar)

# class Talaba:
# 	"""Talaba Nomli Class Yaratamiz"""

# 	def __init__(self, ism, familya, yil):
# 		self.ism = ism
# 		self.familya = familya
# 		self.yil = yil

# 	def tanishtir(self):
# 		print(f"Ismim {self.ism} {self.familya} {self.yil} yilda Tu'gilganman")

# talaba1 = Talaba("Alijon", "Valiyev", 2000)
# talaba2 = Talaba("Hasan", "Umarov", 1995)

# print(talaba1.ism)
# print(talaba1.familya)
# talaba1.tanishtir()

# talaba2 = Talaba("Olim", "Olimov", 1990)
# talaba2 = Talaba("Xasan", "Xusanov", 1991)


# class Talaba:
# 	"""Talaba Nomli Class Yaratamiz"""

# 	def __init__(self, ism, familya, yil):
# 		"""Talabaning Xususiyatlari"""
# 		self.ism = ism
# 		self.familya = familya
# 		self.yil = yil

# 	def get_name(self):
# 		"""Talabaning Ismini Qaytaradi"""
# 		return self.ism

# 	def get_lastname(self):
# 		"""Talabaning Familyasini Qaytaradi"""
# 		return self.familya

# 	def get_fullname(self):
# 		"""Talabaning Ism Familyasini Qaytaradi"""
# 		return f"{self.ism} {self.familya}"

# 	def get_age(self, yil):
# 		"""Talabaning Yoshini Qaytaradi"""
# 		return yil - self.yil

# 	def tanishtir(self):
# 		print(f"Ismim {self.ism} {self.familya} {self.yil} Yilda Tu'gilganman")

# talaba1 = Talaba("Murodjon", "Xonto'rayev", 2004)
# print(talaba1.get_fullname())
# print(talaba1.get_age(2021))
# talaba1.tanishtir()
# class Talaba:
# 	def __init__(self, ism, familya, yil):
# 		"""Talabaning Xususiyatlari"""
# 		self.ism = ism
# 		self.familya = familya
# 		self.yil = yil
# 		self.bosqich = 1

# 	def get_info(self):
# 		"""Talaba Haqida Ma'lumot"""
# 		return f"{self.ism} {self.familya} {self.bosqich}- Bosqich Talabasi"

# 	def set_bosqich(self, bosqich):
# 		"""Talabaning Kursini Yangilovchi Metod"""
# 		self.bosqich = bosqich

# 	def update_bosqich(self):
# 		"""Talabaning Bosqichini 1taga Ko'paytirish"""
# 		self.bosqich += 1

# talaba1 = Talaba("Alijon", "Valiyev", 2000)
# # print(talaba1.get_info())
# # talaba1.update_bosqich()
# # print(talaba1.get_info())
# # talaba1.update_bosqich()	
# # print(talaba1.get_info())

# class Fan():
# 	def __init__(self,nomi):
# 		self.nomi = nomi
# 		self.talabalar_soni = 0
# 		self.talabalar = []

# 	def add_student(self,talaba):
# 		"""Fanga Talabalar Qo'shish"""
# 		self.talabalar.append(talaba)
# 		self.talabalar_soni += 1

# 	def get_students(self):
# 		return [talaba.get_info() for talaba in self.talabalar]	

# matematika = Fan("Oliy Matematika")
# talaba1 = Talaba("Alijon", "Valiyev", 2000)
# talaba2 = Talaba("Hasan", "Husanov", 2001)
# talaba3 = Talaba("Doston", "Xolmurodov", 2001)

# talaba1.update_bosqich()
# talaba2.update_bosqich()
# talaba3.update_bosqich()

# talaba1.update_bosqich()
# talaba2.update_bosqich()
# talaba3.update_bosqich()

# matematika.add_student(talaba1)
# matematika.add_student(talaba2)
# matematika.add_student(talaba3)

# print(matematika.talabalar_soni)

# mat_talabalar = matematika.get_students()
# print(mat_talabalar)					

# def see_methods(klass):
# 	return [method for method in dir(klass) if method.startswith('__') is False]
# print(see_methods(Talaba))	

# class Shaxs:
# 	"""Shaxslar Haqida Malumot"""

# 	def __init__(self, ism, familya, passport, yil,):
# 		"""Shaxsning Xususiyatlari"""
# 		self.ism = ism
# 		self.familya = familya
# 		self.passport = passport
# 		self.yil = yil

# 	def get_info(self):
# 		"""Shaxs haqida malumot"""
# 		info = f"{self.ism} {self.familya}. "
# 		info += f"passport:{self.passport}, {self.yil} - yilda tug'ilgan",
# 		return info

# 	def get_age(self, yil):
# 		"""Shaxsning yoshini qaytaruvchi metod"""
# 		return yil - self.yil

# shaxs1 = Shaxs("O'tkir", "Sobirov", "AC974728318", 2004)

# class Manzil:
# 	"""Manzil Saqlash Uchun class"""

# 	def __init__(self, uy, kocha, tuman, viloyat):
# 		"""Manzil Xususiyatlari"""
# 		self.__uy = uy
# 		self.kocha = kocha
# 		self.tuman = tuman
# 		self.viloyat = viloyat

# 	def get_manzil(self):
# 		"""Manzilni Ko'rish"""
# 		manzil = f"{self.viloyat} viloyati, {self.tuman} tumani,"
# 		manzil += f"{self.kocha} ko'chasi {self.uy} -uy"
# 		return manzil

# talaba1_manzil = Manzil(12, "Olmazor", "Bo'gbon", "Samarqand")

# class Talaba(Shaxs):
# 	"""Shaxslar Haqida Malumot"""

# 	__num_talabalar_soni = 0

# 	def __init__(self, ism, familya, passport, yil, idraqam, manzil, soni):
# 		"""Shaxsning Xususiyatlari"""
# 		super().__init__(ism, familya, passport, yil)
# 		self.__idraqam = idraqam
# 		self.bosqich = 1
# 		self.manzil = manzil
# 		self.soni = soni
# 		Talaba.__num_talabalar_soni +=1

# 	def get_id(self):
# 		"""Shaxsning id raqami"""
# 		return self.idraqam

# 	def get_bosqich(self):
# 		"""Talabaning Bosqichi"""
# 		return self.bosqich	

# 	def get_info(self):
# 		"""Shaxs haqida malumot"""
# 		info = f"{self.ism} {self.familya}. "
# 		info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}, {talaba1_manzil.get_manzil()}"
# 		return info

# 	@classmethod
# 	def talabalar_soni(cls):
# 		return cls.__num_talabalar_soni


# talaba1 = Talaba("Valijon", "Aliyev", "FA1138437", 2000, "000000012", talaba1_manzil, 30)
# print(talaba1.talabalar_soni())



