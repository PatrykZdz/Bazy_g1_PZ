Dany jest szyfr, który zamienia wybrane samogłoski wg klucza:
klucz = {"a": "y", "e": "i", "i": "o", "o": "a", "y": "e"}
Np. słowo informatyka zostanie zaszyforwane na onfarmyteky. Napisz funkcję szyfrującą i deszyfrującą.

def deszyfruj(szyfrogram, klucz):
    tekst = ""
    for znak in szyfrogram:
        if znak.lower() in klucz.values():
            for k, v in klucz.items():
                if v == znak.lower():
                    if znak.islower():
                        tekst += k
                    else:
                        tekst += k.upper()
                    break
        else:
            tekst += znak
    return tekst

import math

a=[2,1,3,4]
print(a.sort())
print(a)
print(sorted(a,reverse=True))
print(a)

def calendar(n):
  months = ["May","Ferbruary","March"]
  return months.index(n)+1

def choosename(list_of_name,letter):
    return [x for x in list_of_name if x[0]>letter]

print(choosename(["Kowalski","Nowak","Kowalczyk","Raszkowski"],"A"))

def dlugosc(nazwiska):
    return [x for x in nazwiska if len(x)>6]
print (dlugosc(["Kowalski","Nowak","Kowalczyk","Raszkowski"]))

def is_sorted(nazwiska):
    return nazwiska==sorted(["Kowalski","Nowak","Kowalczyk","Raszkowski"])

print(is_sorted(["Kowalski","Nowak","Kowalczyk","Raszkowski"]))

def potegowanie_do_3(lista,mnoznik=3):
    return [x**mnoznik for x in lista]
lista6 = [1,2,3,4,5,6,7,8,9,10]
print(potegowanie_do_3(lista6))

def func(list,n1,n2,rel_tol=1e-09,abs_tol=0):
    return [x if (math.isclose(x,n1,rel_tol=rel_tol, abs_tol=abs_tol)==0) else n2 for x in list]
print(func([1,3,7,5,3,5,2],2.5,10,abs_tol=1))
print(func([1,3,7,5,3,5,2],3,2))

countries = {"Poland","France"}
print(countries)
if "Poland" in countries:
     print("It's in the countries")
else:
    print("It's not in the countries")

countries.add("Rusia")
print(countries)
countries.remove("Poland")
print(countries)

krotka = ("slow",4,True,a, [12,13])
print(krotka[-2])
print(krotka)
print(krotka[1])

def funkcja2 (krotka,el):
    krotka=(el,)
    return krotka+krotka

print(funkcja2(krotka,2))

krotkka = (1,2,3,4,5,6 ,"Warszawa")

def funk(mylist):
    for x in set (mylist):
        print(x,end=" ")
    print('\n')

def funk2(mylist):
    newlist= []
    for x in mylist:
        if x not in newlist:
            newlist.append(x)
    print(newlist)

phone = {"Anna": 9934, "Bartek": 3423}

def print_phone(phone_book):
    for x,y  in phone_book.items():
        print("{} ma number {}".format(x,y))

print(print_phone(phone))

days = {"Pon","Wt","Sroda"}
def engtopol(edays):
    pday=[]
    for i in edays:
        pday.append(edays[i])
        return pday
    print(engtopol(["Mon","Tue","Wed"]))

print(engtopol(days))

months = {"Januray":1,"February":2}
def months_orders(m):
    return months


#Ćwiczenie 1
names = ["michal", "nela", "ola","przemek"]
names_upper = []
for name in names:
    names_upper.append(name.capitalize())
print(names_upper)

name_with_l = [x for x in names if "l" in x.lower()]
print(name_with_l)

names_tuple = ("Maria","Ola","Marek")
names_tuple = tuple(x for x in names if x.endswith('a') and x[0].isupper())
print(names_tuple)

sumanames=sum([len(x)for x in names])
print(sumanames)


def prod(*args):
    p=1
    for x in args:
        p*=x
        return p

print((prod(2,4,3)))
print((prod(-2,3,5,6,7,8)))

def sumpow(n,*numbers):
    sum = 0
    for x in numbers:
        sum +=pow(x,n)
        return sum
print(sumpow(2,1,2,3))
print(sumpow(3,1,2,3))

def sumpow2(*numbers, n=2):
    sum = 0
    for x in numbers:
        sum +=pow(x,n)
        return sum
print(sumpow2(1,2,3,n=2))
print(sumpow2(1,2,2,n=3))

def mean(*args):
    return sum(args)/len(args)

print(mean(1,2,3,2))

def gmean(*args):
    return pow(prod(*args),1/len(args))
print(gmean(2,4,8))

def sumlen(*args):
    s = 0
    for x in args:
        s *= len(x)
    return s

print(sumlen("michal", "nela", "ola","przemek"))


def func1(**kwargs):
    for x,y in kwargs.items():
        print("{} ma numer {}".format(x,y))

func1(Anna = 1234)
thisdic= dict(Anna=1234)
print(thisdic)
func1(**thisdic)

def mean2(*args):
    s=0
    for x in args:
        s +=x
    return s/len(args)

def func2(**kwargs):
    salaries = [x for x in kwargs.values()]
    return mean2(*salaries),pow((salaries[-1])/salaries[0],1/(len(salaries)-1))*100-100

print(func2(January = 1000,February = 1500, March = 1800))

#Ćwicznie 1
class Fruit:
    def __init__(self,color,weight):
        self.color = color
        self.weight = weight
    def __str__(self):
        return str("color "+str(self.color)+"\n weight:"+str(self.weight))
    def __add__(self,other):
        return Fruit(' ',self.weight+other.weight)
class Apple(Fruit):
    def __init__(self,color,weight):
        self.color = color
        self.weight = weight
    def isfresh(self):
        if(self.color == "red" or self.color == "green"):
            return True
        else:
            return False
class Banan(Fruit):
    def __init__(self,color,weight):
        self.color = color
        self.weight = weight
    def isfresh(self):
        if(self.color == "yellow"):
            return True
        else:
            return False
class Orange(Fruit):
    def __init__(self,color,weight):
        self.color = color
        self.weight = weight
    def isfresh(self):
        if(self.color == "orange"):
            return True
        else:
            return False
my_fruit=Banan("yellow,",350)
my_fruit2=Fruit("pomaranczowe",250)
print(my_fruit+my_fruit2)
print(my_fruit.isfresh())
#Ćwiczenie 2
class Account:
    def __init__(self,account_number,balance=0):
        self.account_number = account_number
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        if (amount > self.balance):
            print("Brak srodkow")
        else:
            self.balance -= amount
    def transfer(self,amount,to_account):
        if amount > self.balance:
            print("Brak srodkow")
        else:
            self.withdraw(amount)
            to_account.deposit(amount)
class PrivatAccount(Account):
    def __init__(self,account_number,balance = 0,salary = 0):
        self.account_number=account_number
        self.balance=balance
        self.salary = salary
    def pay_salary(self):
        self.deposit(self.salary)
class FirmAccount(Account):
    def Przelewy(self,transfer_to_ZUS,transfer_to_US):
        self.transfer_to_ZUS=transfer_to_ZUS
        self.transfer_to_US=transfer_to_US
#Ćwiczenie 3
class Romanian:
    def Na_Rzymskie(self,wartosc):
        wartosci = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        symbole = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        rzymska_liczba = ""
        i = 0
        while wartosc> 0:
            for _ in range(wartosc//wartosci[i]):
                rzymska_liczba +=symbole[i]
                wartosc -= wartosci[i]
            i+=1
        return rzymska_liczba
    def Na_Arabskie(self, roman_numeral):
        self.roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        arabic_numeral = 0
        previous_value = 0
        i = len(roman_numeral) - 1
        while i >= 0:
            current_value = self.roman_dict[roman_numeral[i]]
            if current_value >= previous_value:
                arabic_numeral += current_value
            else:
                arabic_numeral -= current_value
            previous_value = current_value
            i -= 1
        return arabic_numeral
    def dodowanie(self,other):
        return Romanian(self.Na_Arabskie()+other.to_Na_Arabskie().to_Na_Rzymskie)
print(Romanian().Na_Rzymskie(549))
print(Romanian().Na_Arabskie("DXLIX"))



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






# Cwiczenie 0.1
def funkcja(lista):
    list_no_repeat = set(lista)
    for x in list_no_repeat:
        print(x)

lista1 = [1,2,3,3,2,1]
funkcja(lista1)

# Cwiczenie 0.2
wyraz = "qwemewqawqemeqwa"
for x in range(len(wyraz)-1,2,-4):
    print(wyraz[x], end='')
print()
# Cwiczenie 0.3
def Fibonacci(n):
    if (n==0 or n==1):
        return n
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
print(Fibonacci(10))

def fib_i(n):
    if n == 0: return 0
    elif n == 1: return 1
    p, w = 0, 1
    for i in range(n-1):
        p, w = w, p+w
    return w

print(fib_i(10))

# Cwiczenie 0.4
def iloczyn_poteg(n, *args):
    iloczyn = 1
    for x in args:
        iloczyn *= x ** n
    return iloczyn

wynik = iloczyn_poteg(2, 1, 2, 3, 4, 5)
print(wynik)

# Cwiczenie 0.5
tab = ['apple', 'banana', 'pomergranate', 'plum', 'orange', 'melon', 'cherry', 'watermelon']
tab2 = [len(x) for x in tab if 'u' in x or 'o' in x]
print(tab2)

tab = ['apple', 'banana', 'pomergranate', 'plum', 'orange', 'melon', 'cherry', 'watermelon']
tab2 = [len(word) for word in tab if 'u' in word or 'o' in word]
print(tab2)

def silnia(n):
    if (n==0 or n == 1):
        return 1
    else:
        return n*silnia(n-1)
def Newton(n,k):
    if k > n:
        return 0
    else:
        return silnia(n)/(silnia(k)*silnia(n-k))
print("Wynik = ",Newton(5,2))

class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __add__(self, other):
        result = [0] * max(len(self.coefficients), len(other.coefficients))
        for i in range(len(result)):
            if i < len(self.coefficients):
                result[i] += self.coefficients[i]
            if i < len(other.coefficients):
                result[i] += other.coefficients[i]
        return Polynomial(result)

    def __sub__(self, other):
        result = [0] * max(len(self.coefficients), len(other.coefficients))
        for i in range(len(result)):
            if i < len(self.coefficients):
                result[i] += self.coefficients[i]
            if i < len(other.coefficients):
                result[i] -= other.coefficients[i]
        return Polynomial(result)

    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
        result = ''
        for i in range(len(self.coefficients)-1, -1, -1):
            if self.coefficients[i] != 0:
                if i == len(self.coefficients)-1:
                    result += f"{self.coefficients[i]}x^{i}"
                elif i == 0:
                    result += f" {'+' if self.coefficients[i] > 0 else '-'} {abs(self.coefficients[i])}"
                else:
                    result += f" {'+' if self.coefficients[i] > 0 else '-'} {abs(self.coefficients[i])}x^{i}"
        return result


p1 = Polynomial([2, 0, -1, 3]) # 2x^3 - x^2 + 3x + 2
p2 = Polynomial([1, -1, 1]) # x^2 - x + 1

print(p1) # 2x^3 - 1x^2 + 3x + 2
print(p2) # 1x^2 - 1x + 1

p3 = p1 + p2
print(p3) # 2x^3 + 0x^2 + 2x + 3

p4 = p1 - p2
print(p4) # 2x^3 - 2x^2 + 4x + 1

print(p1.degree()) # 3
print(p2.degree()) # 2

# Cwiczenie 1
def funkcja(lista):
    list_no_repeat = set(lista)
    for x in list_no_repeat:
        print(x)
lista1 = [1,2,3,3,2,1]
funkcja(lista1)

# Cwiczenie 2
tekst = "Lubie placki"
tekst_co_4 = ""
tekst= ''.join(filter(str.isalpha,tekst))
for x in range(3,len(tekst),4):
    tekst_co_4 = tekst_co_4+tekst[x]

tekst_co_4 = tekst_co_4[::-1]
print(tekst_co_4)

#Cwiczenie 3
def Fibbonaci(n):
    if(n==1 or n==2):
        return 1
    else:
        return Fibbonaci(n-1)+Fibbonaci(n-2)
print(Fibbonaci(10))
def Fibbonaci2(n):
    if (n==1 or n==2):
        return 1
    p, w = 0,1
    for x in range(n-1):
        p,w = w,p+w
    return w
print(Fibbonaci2(10))

#Cwiczenie 4

def funkcja2(*args,n):
    wynik = 1
    for x in args:
        wynik *= x**n
    return wynik

wynik = funkcja2(1,2,3,4,5, n=2)
print(wynik)

#Cwiczenie 5

lista2 = ['apple', 'banana', 'pomergranate', 'plum', 'orange', 'melon', 'cherry', 'watermelon']
lista3 = [len(x) for x in lista2 if "u" in x or "o"in x]
print(lista3)

#Cwiczenie 6

def Newton(n,k):
    if(0<=k<=n):
        return "Bład"
    else:
        return



def symbol_newtona(n, k):
    if k > n:
        return 0
    else:
        numerator = 1
        denominator = 1
        for i in range(1, k+1):
            numerator *= n - i + 1
            denominator *= i
        return numerator // denominator

result = symbol_newtona(5, 2)
print(result)


class Polynomial:
    def __init__(self, coef):
        self.coef = coef

    def __str__(self):
        s = ""
        for i in range(len(self.coef)-1, 0, -1):
            s += str(self.coef[i])+("x^")+str(i)
            if self.coef[i-1]>=0:
                s+='+'
        s += str(self.coef[0])
        return (s)

    def __add__(self, other):
        s = []
        if len(self.coef) > len(other.coef):
           for i in range(0, len(other.coef)):
               s.append(self.coef[i]+other.coef[i])
           for i in range(len(other.coef), len(self.coef)):
               s.append(self.coef[i])
        else:
            for i in range(0, len(self.coef)):
                s.append(self.coef[i] + other.coef[i])
            for i in range(len(self.coef), len(other.coef)):
                s.append(other.coef[i])
        return Polynomial(s)

    def __sub__(self, other):
        s = []
        if len(self.coef) > len(other.coef):
           for i in range(0, len(other.coef)):
               s.append(self.coef[i]-other.coef[i])
           for i in range(len(other.coef), len(self.coef)):
               s.append(self.coef[i])
        else:
            for i in range(0, len(self.coef)):
                s.append(self.coef[i] - other.coef[i])
            for i in range(len(self.coef), len(other.coef)):
                s.append(- other.coef[i])
        return Polynomial(s)
    




a = Polynomial([2, 3, 4])
b = Polynomial([1, 4, 2, 2])
print(f'{a}+{b}={a+b}')
print(f'{a}-({b})={a-b}')


class Polynomial:
    def __init__(self, coef):
        self.coef = coef

    def __str__(self):
        s = ""
        for i in range(len(self.coef)-1, 0, -1):
            s += str(self.coef[i])+("x^")+str(i)
            if self.coef[i-1]>=0:
                s+='+'
        s += str(self.coef[0])
        return (s)

    def __add__(self, other):
        s = []
        if len(self.coef) > len(other.coef):
           for i in range(0, len(other.coef)):
               s.append(self.coef[i]+other.coef[i])
           for i in range(len(other.coef), len(self.coef)):
               s.append(self.coef[i])
        else:
            for i in range(0, len(self.coef)):
                s.append(self.coef[i] + other.coef[i])
            for i in range(len(self.coef), len(other.coef)):
                s.append(other.coef[i])
        return Polynomial(s)

    def __sub__(self, other):
        s = []
        if len(self.coef) > len(other.coef):
           for i in range(0, len(other.coef)):
               s.append(self.coef[i]-other.coef[i])
           for i in range(len(other.coef), len(self.coef)):
               s.append(self.coef[i])
        else:
            for i in range(0, len(self.coef)):
                s.append(self.coef[i] - other.coef[i])
            for i in range(len(self.coef), len(other.coef)):
                s.append(- other.coef[i])
        return Polynomial(s)



a = Polynomial([2, 3, 4])
b = Polynomial([1, 4, 2, 2])
print(f'{a}+{b}={a+b}')
print(f'{a}-({b})={a-b}')
class Romanian:
    def __init__(self, number):
        if isinstance(number, str):
            self.number = number
            romanian_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
            n = 0
            # 4 (IV) and 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM)
            number = number.replace('IV', 'IIII')
            number = number.replace('IX', 'VIIII')
            number = number.replace('XL', 'XXXX')
            number = number.replace('XC', 'LXXXX')
            number = number.replace('CD', 'CCCC')
            number = number.replace('CM', 'DCCCC')
            for i in number:
                n += romanian_numerals[i]
            self.value = n
        elif isinstance (number, int):
            self.value = number
            num = [1, 4, 5, 9, 10, 40, 50, 90,
                   100, 400, 500, 900, 1000]
            sym = ["I", "IV", "V", "IX", "X", "XL",
                   "L", "XC", "C", "CD", "D", "CM", "M"]
            i = 12
            s = ''
            while number:
                div = number // num[i]
                number %= num[i]

                while div:
                    s += sym[i]
                    div -= 1
                i -= 1
            self.number = s


    def __str__(self):
        return str(self.number)

    def __add__(self, s):
        return Romanian(self.value+s.value)

    def __sub__(self, s):
        return Romanian(self.value-s.value)

    def __mul__(self, s):
        return Romanian(self.value*s.value)

    def __len__(self):
        return len(self.number)

    def __getitem__(self, item):
        return self.number[item]



print('1984=', Romanian(1984))
print('MCMLXXXIV=', Romanian('MCMLXXXIV').value)
a = Romanian('MCMLXXXIV')
b = Romanian('MXXIV')
print(a-b)
print((a-b).value)

class Account:
    def __init__(self,  number, balance = 0):
        self.balance = balance
        self.number = number

    def __str__(self):
        return str(self.number) + ': ' + str(self.balance)

    def in_transfer (self, acc, amount = 200):
        self.balance -= amount
        acc.balance += amount

    def out_transfer(self, amount = 100):
        self.balance -= amount

    def in_payment(self, amount = 0):
        self.balance += amount


acc1 = Account ('AM12378', 3000)
acc2 = Account('FG78190')
print(acc1)
print(acc2)
acc1.in_transfer(acc2)
print(acc1)
print(acc2)
acc1.in_payment(30)
print(acc1)


#https://www.w3schools.com/python/python_inheritance.asp
class PrivatAccount (Account):
    def slip_payments(self):
        self.balance -= 1000


class FirmAccount (Account):
    def __init__(self,  number, balance = 100000):
        self.balance = balance
        self.number = number

    def zus_payment(self):
        self.balance-=10000

    def salary(self, *acc):
        for i in acc:
            self.balance -= 2500
            i.balance += 2500


uwm_account = FirmAccount('UWM1234')
print(uwm_account)
my_acc = PrivatAccount ('PR2345', 3000)
another_acc = PrivatAccount('PR4567')
print(my_acc)
print (another_acc)
uwm_account.salary(my_acc,another_acc)
print(uwm_account)
print(my_acc)
print (another_acc)
my_acc.slip_payments()
print(my_acc)
my_acc.in_transfer(another_acc,200)
print(my_acc)
print (another_acc)


class Character:
    def __init__(self, name='Unknown', life=0, points=0):
        self.name = name
        if (life > 0) and (life <= 100):
            self.life = life
        else:
            print ('Warning: not correct life, life is set to 0')
            self.life = 0
        if points > 0:
            self.points = points
        else:
            print('Warning: not correct points, points are set to 0')
            self.points = 0

    def change_life(self, life):
        if (life >= 0) and (life <= 100):
            self.life = life

    def __str__(self):
        return str(self.name) + ': life ' + str(self.life) + ', points ' + str(self.points)


class Archer(Character):
    def __init__(self, name='Unknown', life=0, points=0, skill=0):
        Character.__init__(self, name, life, points)
        if skill > 0:
            self.skill = skill

    def __str__(self):
        return Character.__str__(self) + ', skill ' + str(self.skill)

    def attack_power(self):
        return self.skill * self.points * self.life / 100


class Warrior(Character):
    def __init__(self, name='Unknown', life=0, points=0, power=0):
        Character.__init__(self, name, life, points)
        if power > 0:
            self.power = power

    def __str__(self):
        return Character.__str__(self) + ', power ' + str(self.power)

    def attack_power(self):
        if self.life >= 20:
            return self.power * self.points * self.life / 100
        else:
            return self.power * self.points * 1.5


a = Archer('A', 30, 20, 5)
print(a)
a.change_life(120)
print(a)
a.change_life(10)
print(a)
print(a.attack_power())

b = Warrior('W', 30, 20, 5)
print(b)
print(b.attack_power())
b.change_life(10)
print(b)
print(b.attack_power())

c = Character('C',150,30)
print(c)
