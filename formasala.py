# For tsikli bo'yicha masalalar (1-qism)'
# 1-masala
for son in range (1,11):
    print(son, end=" ")


# 2-masala
print("Do'stlarim:")
ismlar = ["Ali", "Vali", "Hasan", "Malika", "Zuhra"]
for ism in ismlar:
    print(f"Salom, {ism}")


# 3-masala
for son in range (1,101):
    if son % 2 == 0:
      print(son)


# 4-masala
yigindi = 0
for son in range (1,51):
    yigindi += son
    print("1 dan 50 gacha bo'lgan sonlar yig'indisi:", yigindi)


# 5-masala
matn = input("Matn kiriting: ")
uzunlik = 0
for belgi in matn:
    uzunlik += 1
    print("Matn uzunligi:", uzunlik, "belgi")


# 6-masala
for son in range (1,51):
    if son % 3 == 0:
      print(son)


# 7-masala
matn = input("Matn: ").lower()
unlilar = ["a", "e", "i", "o", "u", "а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
unlilar_soni = 0
undoshlar_soni = 0
raqamlar_soni = 0
maxsus_belgilar = 0
for belgi in matn:
    if belgi.isalpha():
        if belgi in unlilar:
            unlilar_soni = unlilar_soni + 1
        else:
            undoshlar_soni = undoshlar_soni + 1
    elif belgi.isdigit():
        raqamlar_soni += 1

    else:
        maxsus_belgilar += 1
print(f"Unlilar soni: {unlilar_soni}")
print(f"Undoshlar soni: {undoshlar_soni}")
print(f"Matndagi raqamlar: {raqamlar_soni}")
print(f"Matndagi maxsus belgilar: {maxsus_belgilar}")


# 8-masala
sonlar = [23, 67, 12, 89, 45, 34, 91, 56, 78]
eng_katta = sonlar[0]
for son in sonlar:
    if son > eng_katta:
        eng_katta = son
print("Eng katta son:", eng_katta)


# 9-masala
son = input("Son kiriting: ")
yigindi = 0
for belgi in son:
    if belgi.isdigit():
        yigindi += int(belgi)
print("Raqamlar yig'indisi:", yigindi)


# 10-masala
son = int(input("Son kiriting: "))
if son < 0:
    print("Manfiy sonlar uchun faktorial aniqlanmagan!")
else:
    faktorial = 1
    for i in range(1, son + 1):
        faktorial *= i
        print(f"{son}! = {faktorial}")
