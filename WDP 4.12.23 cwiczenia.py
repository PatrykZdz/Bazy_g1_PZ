def łańcuch(napis): # jest juz git
    wynik = {}
    for x in napis:
       #if(isalpha_wdp(x)== True):
        if not isalpha_wdp(x):
            continue
            x = to_lower_wdp(x) # tu cos nie dziala
        if x in wynik:
            wynik[x]+=1
        else:
            wynik[x]=1
    return wynik

def isalpha2(napis): # moje
    for litera in napis:
        if "a" <= litera <= "z" or "A" <= litera <= "Z":
            return True
    return False

def isalpha_wdp(znak): # zajecia
    return ("a"<= znak and znak <="z") or ("A" <= znak and znak <= "Z")

#def lowerCase(znak): # zajecia moze byc lower
 #   if "A"<= znak <= "Z":
  #      return znak.lower() # moze byc lower

def to_lower_wdp(znak): # zajecia V
    if "A" <= znak <= "Z":
        return chr(ord(znak)+32)

#chr int na litere
#ord litera na int

napis = "Llitera_spacja 5"
napis2 = "Ala ma kota"
print(łańcuch(napis))

def dictionary_max(d):
  max_k = next(iter(d)) # pierwszy klucz ze slownika
  max_w = d[max_k]
  for klucz in d:
    if d[klucz] > max_w:
        max_k = klucz
        max_w = d[klucz]
  return max_k,max_w

print(dictionary_max(łańcuch(napis)))


#1 2  5 6 7 10 15
#1 >= 1+4+5+6+9+14 = 39
#2 >= 1+3+4+5+8+13 = 34
#itd
# najmniejsza suma odleglosci punktow od pozostalej

## Dokonczyc 
tab = [1,2,5,6,7,10,15]
def sumy_odleglosci(tab):
    wynik = 0
    liczba = tab[0]
    for x in range(len(tab),0,-1):
        wynik = x-liczba
    return wynik

print(sumy_odleglosci(tab))
















#def łańcuch2(d):
 #   wynik = {}
  #  for k in d:
   #     if k >= 'a' and k <= 'z':
    #        wynik[k]=d[k]

    #return wynik
# Jezeli sa pytania to pytajcie 6 osob lacznie
