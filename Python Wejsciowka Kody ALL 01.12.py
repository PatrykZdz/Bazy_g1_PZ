import random

def Generuj(size, min = 0, max = 100):
    lista = []
    for x in range(size):
        liczba = random.randint(min,max)
        lista.append(liczba)
    return lista

print(Generuj(5))

def czy_Nalezy(element,lista):
    for x in lista:
        if element == x:
            return True
    return False

lista1 = [1,2,3]
element = 2
print(czy_Nalezy(element,lista1))

def czy_Zawiera(lista1, lista2):
    for x in lista2:
        if x not in lista1:
            return False
    return True

lista_1 = [1,2,3]
lista_2 = [1,2]
print(czy_Zawiera(lista_1,lista_2))

def Reverse(napis):
    napis_rev = ""
    for x in napis:
        napis_rev = x + napis_rev
    return napis_rev

print(Reverse("hello"))

def Palindrom(napis):
    if napis == Reverse(napis):
        return True
    return False

print(Palindrom("kajak"))

def mirror(napis):
    return napis+Reverse(napis)

print(mirror("linka"))

def ile_ujemnych(lista):
    wynik = 0
    for x in lista:
        if x < 0:
            wynik+=1
    return wynik

lista3 = [1,2,3,-1,-2,-3]
print(ile_ujemnych(lista3))

## Liczba doskonala liczba = suma wszystkich swoich dzielnikow

def dzielniki(liczba):
    lista = []
    for x in range(1,int(liczba/2+1)):
        if(liczba % x == 0):
            lista.append(x)
    return lista

print(dzielniki(6))

def suma_dzielnikow(lista):
    wynik = 0
    for x in lista:
        wynik += x
    return wynik

print(suma_dzielnikow(dzielniki(6)))

def czy_doskonala(liczba):
    if liczba == suma_dzielnikow(dzielniki(liczba)):
        return True
    return False

print(czy_doskonala(28))

def wszystkie_dzielniki(liczba):
    dziel = dzielniki(liczba)
    dziel.append(liczba)
    return dziel

print(wszystkie_dzielniki(6))

def czesc_wspolna(lista1, lista2):
    lista = []
    for x in lista1:
        if czy_Nalezy(x,lista2):
            lista.append(x)
    return lista

listaT1 = [1,2,3,4,5]
listaT2 = [1,2,3]
print(czesc_wspolna(listaT1,listaT2))

### Wspolnym dzielnikiem liczbe jest tylko 1
def czy_wzajmnie_pierwsze(liczba1,liczba2):
    dzielniki_liczby1 = wszystkie_dzielniki(liczba1)
    dzielniki_liczby2 = wszystkie_dzielniki(liczba2)
    CzescWspolna = czesc_wspolna(dzielniki_liczby1,dzielniki_liczby2)
    if CzescWspolna[0] == 1 and len(CzescWspolna) == 1:
        return True
    return False

print(f"Czy wzglednie pierwsze : {czy_wzajmnie_pierwsze(15,28)}")

def unikalnosc(lista):
    lista_unikalna = []
    for x in lista:
        if not czy_Nalezy(x,lista_unikalna):
           lista_unikalna.append(x)
    return lista_unikalna


lista_TEST = [1,2,3,3,2,1]
print(unikalnosc(lista_TEST))
