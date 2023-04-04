#Ćwiczenie 1
#a)
lista = list(range(15))
print(lista)

#b)
lista2 = [x** 5 for x in range(15)]
print(lista2)
def silnia(n):
    if n == 0:
        return 1
    else:
        return n*silnia(n-1)

lista3 = [silnia(x1) for x1 in range(21)]
print(lista3)

import math
e = math.e
lista4 = [e**i for i in range(20)]
print (lista4)

lista5 = ["Zbyszek","Kowalski","Kochanowski","Dawid"]
lista5 = [len(lista5) for lista5 in lista5]
print(lista5)
#c)
list1 = [ x+1 for x in range (10)]
list2 = [ (x+1)*10 for x in range (10)]
print(list1)
print(list2)
a = list1+list2
print(a)

lista_miesiecy =["styczeń", "luty", "marzec", "kwiecień", "maj", "czerwiec",
                 "lipiec", "sierpień", "wrzesień", "październik", "listopad", "grudzień"]
lista_miesiecy.sort()
print(lista_miesiecy)

def numer_miesiaca(n):
    return ["styczeń", "luty", "marzec", "kwiecień", "maj", "czerwiec", "lipiec",
            "sierpień", "wrzesień", "październik", "listopad", "grudzień"].index(n.lower())+1
print(numer_miesiaca("marzec"))
print(numer_miesiaca("styczeń"))

def nazwiska_od_litery(nazwisko,litera):
    wynik = []
    for x in nazwisko:
        if x.lower().startswith(litera.lower()):
            continue
        if x.lower()>litera.lower():
            wynik.append(x)
    return wynik

naziwska =["Dobrzynski","Angielski","Celicja","Baba"]
litera = "b"
print(nazwiska_od_litery(naziwska,litera))

def dlugosc(nazwiska):
    return [x for x in nazwiska if len(x)>6]
print (dlugosc(naziwska))

def max_min(lista):
    for x in range(len(lista)):
        if lista[x] > lista[x+1]:
            return True
        else:
            return False

liczby = [9,7,5,3,1]
liczby2 = [3,6,8,8,10]
print(max_min(liczby))
print(max_min(liczby2))


def potegowanie_do_3(lista):
    return [x**3 for x in lista]

lista6 = []
n = int(input("Podaj liczbę elementów: "))
for i in range(0,n):
    element = int(input())
    lista6.append(element)

print(potegowanie_do_3(lista6))

lista7 = []
n = int(input("Podaj liczbę elementów: "))
for i in range(0,n):
    element = float(input())
    lista7.append(element)
def func(list,n1,n2):
    for i in range(len(list)):
        if list[i] == n1:
            list[i]=n2
    return list

print(lista7)
print(func(lista7,2.0,3.0))
print("/////////")

import math
def func2(list,n1,n2,rel_tol=1e-9,abs_tol=0.0):
    for i in range(len(list)):
        if math.isclose(list[i],n1, rel_tol=rel_tol, abs_tol=abs_tol):
            list[i]=n2
    return list

print(lista7)
print(func2(lista7,2.0,3.0,rel_tol=0.5))
print("///////")
print("Ćwiczenie 2")
print("///////")
#Ćwiczenie 2

panstwa = {"Polska","Niemcy","Ukraina","UK","Litwa"}
print(panstwa)
panstwa.add("Francja")
print(panstwa)

if "Polska" in panstwa:
    print(True)
else:
    print(False)
panstwa.discard("Niemcy")
print(panstwa)

miasta1 = {"Warszawa","Poznań","Gdańsk","Wrocław"}
miasta2 = {"Warszawa","Sosnowiec","Wrocław","Sopot"}

miasta = miasta1 | miasta2
print(miasta)
print("/////////")
miasta3 = miasta1 & miasta2
print(miasta3)
print("/////////")
miasta4 = miasta1 - miasta2
print(miasta4)
print("/////////")
cities = {"Warszawa","Poznań","Gdańsk","Wrocław"}
cities2 = {"Warszawa","Wrocław"}
if cities >= cities2:
    print("Jest podzbiorem")
else:
    print("Nie jest podzbiorem")

krotka = ("Python", 3.14, True, [1, 2, 3], {"name": "John", "age": 30}, None, ("a", "b", "c"))

print(krotka[3])
print(krotka[3:5])
print(krotka[-3])
#b)
print("///////")
def funkcja (krotka,element,wynik):
    if wynik == "dodac":
        krotka2 = krotka+(element,)
    elif wynik == "usunac":
        krotka2 = tuple(x for x in krotka if x != element)
    else:
        print("Błąd można dodac albo usunac")
    return krotka2

krotkka = (1,2,3,4,5,6 ,"Warszawa")

print(funkcja(krotkka,9,"dodac"))
print(funkcja(krotkka,3,"usunac"))

print("///////")
lista8 = [1,2,3,3,2,1]
def funkcja3(lista):
    lista_bez_powtorzen = list(set(lista))
    return lista_bez_powtorzen

print(funkcja3(lista8))

#Ćwiczenie 4
#a)
slownik = {"Piotr":54398324, "Adam":123457860,"Agnieszka":123654765}
print(slownik["Piotr"])

def phone_numbers(slownik):
    for x,y in slownik.items():
        print(x,"ma numer",y)

print(phone_numbers(slownik))
print("/////////")
del slownik["Adam"]
slownik["Marcin"]= 932423454
slownik["Piotr"] = 342234543
print(slownik)
print("////////")
#b)

def translate_days_to_english(polish_days):
    translations = {
        "poniedziałek": "Monday",
        "wtorek": "Tuesday",
        "środa": "Wednesday",
        "czwartek": "Thursday",
        "piątek": "Friday",
        "sobota": "Saturday",
        "niedziela": "Sunday"
    }
    english_days = []
    for day in polish_days:
        english_days.append(translations.get(day.lower(), day))
    return english_days


def translate_days_from_english(english_days):
    translations = {
        "monday": "poniedziałek",
        "tuesday": "wtorek",
        "wednesday": "środa",
        "thursday": "czwartek",
        "friday": "piątek",
        "saturday": "sobota",
        "sunday": "niedziela"
    }
    polish_days = []
    for day in english_days:
        polish_days.append(translations.get(day.lower(), day))
    return polish_days


polish_days = ["poniedziałek", "wtorek", "środa", "czwartek", "piątek", "sobota", "niedziela"]
english_days = translate_days_to_english(polish_days)
print(english_days)

english_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
polish_days=translate_days_from_english(english_days)
print(polish_days)

print("///////")
def sort_months(months):
    month_numbers = {
        "styczeń": 1,
        "luty": 2,
        "marzec": 3,
        "kwiecień": 4,
        "maj": 5,
        "czerwiec": 6,
        "lipiec": 7,
        "sierpień": 8,
        "wrzesień": 9,
        "październik": 10,
        "listopad": 11,
        "grudzień": 12
    }
    sorted_months = sorted(months, key=lambda month: month_numbers[month.lower()])
    return sorted_months

months = ["maj", "luty", "sierpień", "listopad", "kwiecień", "wrzesień", "czerwiec", "styczeń", "lipiec", "marzec", "październik", "grudzień"]
sorted_months = sort_months(months)
print(sorted_months)

def roman_to_arabic(roman_numeral):
    roman_numerals = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000
    }
    arabic_numeral = 0
    i = 0
    while i < len(roman_numeral):
        if i+1 < len(roman_numeral) and roman_numerals.get(roman_numeral[i:i+2]) is not None:
            arabic_numeral += roman_numerals[roman_numeral[i:i+2]]
            i += 2
        else:
            arabic_numeral += roman_numerals[roman_numeral[i]]
            i += 1
    return arabic_numeral

print(roman_to_arabic("V"))
print(roman_to_arabic("XIV"))
print(roman_to_arabic("CXXIX"))

def arabic_to_roman(number):
    arabic_to_roman_numerals = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }
    roman_numeral = ""
    for arabic_numeral, roman_symbol in arabic_to_roman_numerals.items():
        while number >= arabic_numeral:
            roman_numeral += roman_symbol
            number -= arabic_numeral
    return roman_numeral

print(arabic_to_roman(5))
print(arabic_to_roman(14))
print(arabic_to_roman(129))

#Ćwiczenie 5
def is_palindrome(word):
    return word == word[::-1]
print(is_palindrome("kajak"))  # True
print(is_palindrome("python"))  # False
