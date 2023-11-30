def dzielniki(n):
    lista_dzielnikow = []
    for liczba in range(1,int(n/2+1)):
        if n % liczba == 0:
            lista_dzielnikow.append(liczba)
    return lista_dzielnikow
def wszytkie_dzielniki(liczba): # zajecia
    d = dzielniki(liczba)
    d.append(liczba)
    return d
def czy_Nalezy(tab, element):
    for x in tab:
        if element == x:
            return True
    return False
def czesc_wspolna2(lista1,lista2): ## zajecia
    wynik = []
    for e in lista1:
        if czy_Nalezy(lista2,e):
            wynik.append(e)
    return wynik

lista = [1,2,3]
lista2 = [1,3,5]
print(f"Część wspólna: {czesc_wspolna2(lista,lista2)}")

def czy_wzglednie_pierwsze(liczba1,liczba2): ## zajecia
    d1 = wszytkie_dzielniki(liczba1)
    d2 = wszytkie_dzielniki(liczba2)
    iloczyn = czesc_wspolna2(d1,d2)
    return len(iloczyn) == 1 and iloczyn[0] == 1

print(f"Czy wzglednie pierwsze : {czy_wzglednie_pierwsze(15,28)}")

array = [8,2,8,5,2,1,4,5]
def unikalnosc(lista):
    lista2 = []
    for element in lista:
        if not czy_Nalezy(lista2,element):
            lista2.append(element)
    return lista2

print(unikalnosc(array))

## wszystko co bylo i to co dzisiaj
# wynik = [8,2,5,1,4]

import random
size = int(input("Podaj rozmiar tablicy"))
def generuj(size,min = 0, max = 100):
    tab = []
    for x in range(size):
        liczba = random.randint(min,max)
        tab.append(liczba)
    return tab

print(generuj(size))
