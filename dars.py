# def son_hisobla():
# 	son = int(input("Sonni Kiriting: "))
# 	if son%2==0:
# 		print("Bu Son Juft Son")
# 	else:
# 		print("Bu Son Toq Son")

# son_hisobla()	

# def son_hisobla():
# 	son1 = int(input("Sonni Kiriting: "))
# 	son2 = int(input("Sonni Kiriting: "))
# 	if son1 > son2:
# 		print(f"{son1} katta {son2}dan")
# 	elif son1 < son2:
# 		print(f"{son1} kichik {son2}dan")
# 	else:
# 		print("Sonlar Teng")

# son_hisobla()

# def son_hisobla():
# 	x = int(input("Sonni Kiriting: "))
# 	y = 2
# 	print(f"Bu Son {x} Bu Son {y}")
# son_hisobla()


# def son_hisobla():
# 	son = int(input("Sonni Kiriting: "))
# 	for a in range(2,11):
# 		if son % a:
# 			print(f"{son} {a} ga Qoldiqsiz Bo'linmaydi")

# son_hisobla()


# ishora = True
# while ishora:
# 	bozorlik = input("Ro'yhat kiriting: ")
# 	print("Ro'yxatni To'xtatish Un 'exit' deb yozing")
# ishora = 'exit'
# ishora = False
# royxat = list['non, yog']
# if bozorlik == royxat:
# 	print("Bu Mahsulot Bizda Bor Narxi = 100.000")

# f_bozorlik = []
# mahsulotlar = {
# 	"non": 2000,
# 	"shakar": 8000,
# 	"yog": 90000,
# 	"go'sht": 70000,
# 	"kartoshka": 5000
# }
# while True:
# 	bozorlik = (input("Ro'yxatni Kiriting: "))
# 	f_bozorlik.append(bozorlik)
# 	skil = input("Yana Mahsulot Qo'shasizmi (ha/yo'q) ")
# 	if skil == "yo'q":
# 		break				
# for m in mahsulotlar:
# 	if m in f_bozorlik:
# 		print(f"{m} narxi {mahsulotlar[m]}")
# 		for n in f_bozorlik:
# 			if n not in mahsulotlar:
# 				print(f"{n} mahsulot bizda yo'q uzur")

# def toliq_ism_yasa(ism, familiya):
# 	"""Toliq ism qaytaruvchi Dastur"""
# 	toliq_ism = f"{ism} {familiya}"
# 	return toliq_ism

# talaba1 = toliq_ism_yasa("olim", "hakimov")
# talaba2 = toliq_ism_yasa("hakim", "olimov")
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
# print(f"{talaba1} darsga kechikib keldi")	

# def toliq_ism_yasa(ism, familiya, otasining_ismi=""):
# 	"""Toliq ism qaytaruvchi funksiya"""
# 	if otasining_ismi:
# 		toliq_ism = f"{ism} {otasining_ismi} {familiya}"
# 	else:
# 		toliq_ism = f"{ism} {familiya}"
# 	return toliq_ism.title()

# talaba1 = toliq_ism_yasa("olim", "hakimov")
# talaba2 = toliq_ism_yasa("hakim", "olimov" "")
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

# def avto_info(kompaniya, model, rangi, karobka, yili, narhi=None):
# 	avto = {
# 	"kompaniya": kompaniya,
# 	"model": model,
# 	"rang": rangi,
# 	"karobka": karobka,
# 	"yil": yili,
# 	"narh": narhi,
# 	}
# 	return avto

# avto1 = avto_info("GM", "Malibu", "Qora", "Avtomat", 2018)
# avto2 = avto_info("GM", "Gentra", "Oq", "Mexanika", 2016, 15000)
# avtolar = [avto1, avto2]
# print("Onlayn Bozordagi Mavjud Avtomabillar: ")
# for avto in avtolar:
# 	if avto["narh"]:
# 		narh = avto["narh"]
# 	else:
# 		narh = "Nomalum"
# 	print(f"{avto['rang']} {avto['model']} Narhi: {narh}")

# def ism_info(ismi, familiya, t_yili, email, manzili=None,):
# 	ism = {
# 	"ism": ismi,
# 	"familiya": familiya,
# 	"manzil": manzili,
# 	"email": email,
# 	"t_yil": t_yili,
# 	}
# 	return ism

# ism1 = ism_info("Eshon", "Xojamnazarov", "1991", "xojamnazarov12@gmail.com")
# ism2 = ism_info("Behruz", "Xamdamov", "2003", "hamdamov34@gmail.com", "Lo'li Mahalla")
# ismlar = [ism1, ism2]
# print("Shaxslarning Ma'lumoti")
# for ism in ismlar:
# 	if ism["manzil"]:
# 		manzili = ism["manzil"]
# 	else:
# 		manzili = "Nomalum"
# 	print(f"{ism['ism']} {ism['familiya']} {ism['t_yil']} {ism['email']} manzili: {manzili}")

# son = int(input("Birinchi Sonni Kiriting: "))			
# son2 = int(input("Ikkinchi Sonni Kiriting: "))
# if son > son2:
# 	print(f"{son} katta {son2} dan")
# else:
# 	print(f"{son2} katta {son} dan")

# def summa(*sonlar):
# 	"""Kiritilgan Sonlar Yig'indisini hisoblaydigan funksiya"""
# 	yigindi = 0
# 	for son in sonlar:
# 		yigindi += son
# 	return yigindi
	
# print(summa(1, 2))
# print(summa(1, 2, 3, 4, 5))
# print(summa(4, 5, 6, 7))

# def summa(x, y, *sonlar):
# 	"""Kiritilgan Sonlar Yig'indisini Hisoblaydigan Funksiya"""
# 	return x + y + sum(sonlar)

# print(summa(1, 2))
# print(summa(1, 2, 3, 4, 5))
# print(summa(4, 5, 6, 7))
# print(summa(2))

# def avto_info(Kompaniya, Model, **Malumotlar):
# 	"""Avto Haqidagi Ma'lumotlarni Lug'at Ko'rinishida Qaytaruvchi Funksiya"""
# 	Malumotlar["Kompaniya"] = Kompaniya
# 	Malumotlar["Model"] = Model
# 	return Malumotlar

# avto1 = avto_info("GM", "Malibu", Rang="Qora", Yil=2018)
# avto2 = avto_info("Kia", "K5", Rang="Oq", narh=35000, Yil=2020, Karobka="Avtomat")
# avto3 = avto_info("GM", "Gentra", Rang="Qora", narh=11000, Yil=2018, Karobka="Mexanika")
# print(avto1)
# print(avto2)
# print(avto3)

# def talaba_info(familiya, ismi, **malumotlar):
# 	"""Talbalar Haqida Malumotlarni Lugat Ko'rinishida Qaytaruvchi Funksiya"""
# 	malumotlar["familiya"] = familiya
# 	malumotlar["ismi"] = ismi
# 	return malumotlar

# talaba1 = talaba_info("Alimov", "Odil", otasining_ismi="Berdiqulovich", t_yili=2002, kurs="3-kurs")	
# talaba2 = talaba_info("Hamdamov", "Ulug'bek", otasining_ismi="Nematovich", t_yili=2000, kurs="2-kurs")
# print(talaba1)
# print(talaba2)


# from random import *
# tahmin = ""
# parol = input("Buziladigan Parolni Kirgizing: ")
# harflar = ['a', 'b', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', "o'", 'sh', 'ch', 'ng']
# while(tahmin !=parol):
# 	tahmin = ""
# 	for harf in range(len(parol)):
# 		tahmin_harf=harflar[randint(0, 25)]
# 		tahmin=str(tahmin_harf) + str(tahmin)
# 		print(tahmin)
# print("Password is Hack3d")	
# tugatish = input(f"Password is <<{tahmin}>> Dasturdan Chiqish Un Istalgan Tugmani Bosing")

# n = 0
# print("Keling Sonni Topish O'yinini O'ynaymiz")
# print("Men 1 dan 10gacha Son O'yladim Siz Sonni Topa Olasizmi?")
# while True:
# 	n+=1
# 	son = (input("Son: "))
# 	if son == 10:
# 		print(f"Tabriklayman Siz {n} ta Tahmin Bilan Sonni Topdingiz !!!") 	
# 	elif son > 10:
# 		print(f"Yo'q Men O'ylagan Son {son} dan Kichkina")
# 	elif son < 10:
# 		print(f"Yo'q Men O'ylagan Son {son} dan Katta")


# import main

# avto1 = main.avto_info("GM", "Malibu", "Qora", "Avtomat", 2020, 400000)
# main.info_print(avto1)

# import math

# x = 400
# print(math.sqrt(x))

# import random as rm 

# raqamlar = ['99.345.43.83', '88.908.82.83', '99.971.22.11', '97.929.33.00', '94.123.43.23']
# while True:
# 	raqam = rm.choice(raqamlar)
# 	if raqam == '88.908.82.83':
# 		print(f"{raqamlar[1]} O'yin Go'libi")
# 	else:
# 		print(f"{raqam} O'yin G'olibi Emas")
# 	savol = input("Yana O'ynaysizmi (xa yoki yo'q): ")
# 	if savol == "yo'q":
# 		break


