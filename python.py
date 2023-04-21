Napisz klase Frac liczb wymiernych, w którym beda one przechowywac sie jako para liczb calkowitych(licznik i mianownik)
Zaimplementuj: konstruktor, mozliwosc wyswietlania przy pomocy print a/b, odejmowanie, iloraz, porownanie.
  przykladowe uzycie print(Frac(2,6)-Frac(1,5))
  wynik na konsoli 4/30
  przykladowe uzycie print(Frac2,6)==Frac(1,3))
  wynik na konsoli: True



class Frac:
    def __init__(self, licznik, mianownik=1):
        self.licznik = licznik
        self.mianownik = mianownik
        self._skroc()

    def __str__(self):
        return f"{self.licznik}/{self.mianownik}"

    def __sub__(self, other):
        licznik = self.licznik * other.mianownik - other.licznik * self.mianownik
        mianownik = self.mianownik * other.mianownik
        return Frac(licznik, mianownik)

    def __truediv__(self, other):
        licznik = self.licznik * other.mianownik
        mianownik = self.mianownik * other.licznik
        return Frac(licznik, mianownik)

    def __eq__(self, other):
        return self.licznik == other.licznik and self.mianownik == other.mianownik

    def _skroc(self):
        def nwd(a, b):
            while b:
                a, b = b, a % b
            return a

        d = nwd(self.licznik, self.mianownik)
        self.licznik //= d
        self.mianownik //= d









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
