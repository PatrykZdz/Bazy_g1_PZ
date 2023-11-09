# rozne wersje
def czy_Nalezy(lista,element):
    if element in lista:
        return True
    return False

lista = [5,3,1,4,2]
print(czy_Nalezy(lista,5))

def czy_Nalezy2(lista,element):
    for x in lista:
        if x == element:
           return True
    return False
print(czy_Nalezy2(lista,3))

def czy_Nalezy3(lista,element): # To bez in dobrze chyba
    index = 0
    while index < len(lista):
        if(lista[index] == element):
            return True
        index+=1
    return False

print(czy_Nalezy3(lista,3))
# Rozne wersje
def czy_Zawiera(lista1,lista2):
    for element in lista2:
        if element not in lista1:
            return False
    return True


def czy_zawiera2(lista1, lista2):
    for element2 in lista2:
        zawiera_element = False
        for element1 in lista1:
            if element1 == element2:
                zawiera_element = True
                break
        if not zawiera_element:
            return False
    return True

def czy_zawiera3(lista1, lista2):
    index2 = 0
    while index2 < len(lista2):
        element2 = lista2[index2]
        zawiera_element = False
        index1 = 0
        while index1 < len(lista1):
            element1 = lista1[index1]
            if element1 == element2:
                zawiera_element = True
                break
            index1 += 1
        if not zawiera_element:
            return False
        index2 += 1
    return True



lista1 = [5,3,1,4,2]
lista2 = [3,1]
print(czy_Zawiera(lista1,lista2))
print(czy_zawiera2(lista1,lista2))
print(czy_zawiera3(lista1,lista2))


#zad 1
#a)
listaA = []
for x in range(1,11):
    listaA.append(x)
print(listaA)
#b)
listaB = []
for x in range(0,21,2):
    listaB.append(x)
print(listaB)
#c)
listaC = []
for x in range(1,11):
    listaC.append(x**2)
print(listaC)
#d)
listaD = []
for x in range(10):
    listaD.append(0)
print(listaD)
#e)
listaE = []
for x in range(5):
    for y in range(2):
        listaE.append(y)
print(listaE)
#f)
listaF = []
for x in range(2):
    for y in range(5):
        listaF.append(y)
print(listaF)


####
# Wersja krotsza
# (a) 1 2 3 4 5 6 7 8 9 10
lista_a = [i for i in range(1, 11)]

# (b) 0 2 4 6 8 10 12 14 16 18 20
lista_b = [i * 2 for i in range(11)]

# (c) 1 4 9 16 25 36 49 64 81 100
lista_c = [i**2 for i in range(1, 11)]

# (d) 0 0 0 0 0 0 0 0 0 0
lista_d = [0] * 10

# (e) 0 1 0 1 0 1 0 1 0 1
lista_e = [i % 2 for i in range(10)]

# (f) 0 1 2 3 4 0 1 2 3 4
lista_f = [i % 5 for i in range(10)]

# Wydruk wyników
print(" ")
print("Lista (a):", lista_a)
print("Lista (b):", lista_b)
print("Lista (c):", lista_c)
print("Lista (d):", lista_d)
print("Lista (e):", lista_e)
print("Lista (f):", lista_f)


#zad 3
def ile_ujemnych(lista):
    wynik = 0
    for x in lista:
        if x < 0:
            wynik+=1
    return wynik

lista_test = [1,2,-4,-6]
print(ile_ujemnych(lista_test))

#zad4
def iloczyn(lista):
    wynik = 1
    for x in lista:
        wynik*=x
    return wynik
lista_test2 = [1,2,3,4,5]
print(iloczyn(lista_test2))

#zad 5
def minmax(lista):
    min = lista[0]
    max = lista[0]
    for x in lista:
        if (max < x):
            max = x
        if  (min > x):
            min = x
    krotka = (max, min)
    return krotka

a = [31,28,31,30,31,30,31,31]

print(minmax(a))

'''
#a)
listaA = []
x = 1
while x <= 10:
    listaA.append(x)
    x += 1
print(listaA)

#b)
listaB = []
x = 0
while x <= 20:
    listaB.append(x)
    x += 2
print(listaB)

#c)
listaC = []
x = 1
while x <= 10:
    listaC.append(x**2)
    x += 1
print(listaC)

#d)
listaD = []
x = 0
while x < 10:
    listaD.append(0)
    x += 1
print(listaD)

#e)
listaE = []
i = 0
while i < 5:
    j = 0
    while j < 2:
        listaE.append(j)
        j += 1
    i += 1
print(listaE)

#f)
listaF = []
i = 0
while i < 2:
    j = 0
    while j < 5:
        listaF.append(j)
        j += 1
    i += 1
print(listaF)'''
