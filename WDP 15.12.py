def lancuch(napis):
    wynik = {}
    for x in napis:
        if not isAlpha(x):
            continue
        x = toLower(x)
        if x in wynik:
            wynik[x]+=1
        else:
            wynik[x]=1
    return wynik

def isAlpha(znak):
    return ("a" <= znak <= "z" or "A" <= znak <= "Z")

def toLower(znak):
    if "A"<= znak <= "Z":
        return chr(ord(znak)+32)
    return znak

napis = "Llitera_spacja 5"
napis2 = "Ala ma kota"

def dictionary_max(dict):
    max_k = next(iter(dict))  # pierwszy klucz ze slownika
    max_w = dict[max_k]
    for klucz in dict:
        if dict[klucz] > max_w:
            max_k = klucz
            max_w = dict[klucz]
    return max_k,max_w

print(lancuch(napis))
print(dictionary_max(lancuch(napis)))
print(lancuch(napis2))
print(dictionary_max(lancuch(napis2)))

#chr int na litere
#ord litera na int

def wartosc_bezwgledna(liczba):
    if liczba < 0:
        liczba*=-1
    return liczba

tab = [1, 2, 5, 6, 7, 10, 15]
def oblicz_odleglosc(tab):
    wyniki = []
    for i in range(len(tab)):
        suma_pozostalych = 0
        for j in range(len(tab)):
            if j != i:
                suma_pozostalych += wartosc_bezwgledna(tab[j] - tab[i])
        wyniki.append(suma_pozostalych)
    return wyniki

tab = [1, 2, 5, 6, 7, 10, 15]
wyniki = oblicz_odleglosc(tab)
print(wyniki)

