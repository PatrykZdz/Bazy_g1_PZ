def czestosc(lista):
    wynik = { }
    for x in lista:
        if x in wynik:
            wynik[x]+=1
        else:
            wynik[x]=1
    return wynik

def toLower(napis): # zajecia
    tab = [napis]
    for x in tab:
        return x.lower()

##lista = [1,2,3,3,2,1]
##print(f"Liczba : Liczba wystapien\n{czestosc(lista)}")

lista2 = [5,2,5,3]
napis = "Ala ma kota"

print(f"Litera : Ilosc wystapien \n{czestosc(toLower(napis))}\n")
print(f"Liczba : Ilosc wystapien \n{czestosc(lista2)}\n")

def String(plik):
    string = open(plik)
    zawartosc = string.read()
    return zawartosc


def czy_litera(napis):
    litery = []
    for x in napis:
        if 'A' <= x <= 'Z' or 'a' <= x <= 'z':
            litery.append(x)
    return litery

#def czy_litera(napis):
 #   litera_list = []
  #  for znak in napis:
   #     if znak.isalpha():
    #        litera_list.append(znak)
 #   return litera_list

plik = "text.txt"
tekst = String(plik)
print(tekst)
teskt_lower = toLower(tekst)
litery = czy_litera(teskt_lower)
print(czestosc(litery))
