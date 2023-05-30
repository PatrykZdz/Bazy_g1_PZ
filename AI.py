import numpy as np

# Dane wejściowe
rozmiar_buta = np.array([38, 42, 39, 41, 40, 39, 38, 37, 42, 40])
wzrost = np.array([165, 170, 175, 168, 172, 169, 160, 162, 170, 173])

# Jaki jest średni rozmiar buta?
sredni_rozmiar_buta = np.mean(rozmiar_buta)
print("Średni rozmiar buta:", sredni_rozmiar_buta)

# Jaki jest maksymalnie wymieniony rozmiar buta?
maks_rozmiar_buta = np.max(rozmiar_buta)
print("Maksymalny rozmiar buta:", maks_rozmiar_buta)

# Jaki jest średni wzrost osób z maksymalnym wymienionym rozmiarem buta?
sredni_wzrost_maks_rozmiar = np.mean(wzrost[rozmiar_buta == maks_rozmiar_buta])
print("Średni wzrost osób z maksymalnym rozmiarem buta:", sredni_wzrost_maks_rozmiar)

# Jaki jest najmniejszy wzrost osób z maksymalnym wymienionym rozmiarem buta?
min_wzrost_maks_rozmiar = np.min(wzrost[rozmiar_buta == maks_rozmiar_buta])
print("Najmniejszy wzrost osób z maksymalnym rozmiarem buta:", min_wzrost_maks_rozmiar)

# Jaki jest średni rozmiar buta u osób każdego wzrostu?
unikalne_wzrosty = np.unique(wzrost)
srednie_rozmiary_butow = np.array([np.mean(rozmiar_buta[wzrost == wzrost]) for wzrost in unikalne_wzrosty])
print("Średnie rozmiary butów u osób każdego wzrostu:", srednie_rozmiary_butow)

# Jaki jest średni wzrost tych osób?
sredni_wzrost_osob = np.mean(wzrost)
print("Średni wzrost osób:", sredni_wzrost_osob)

# Jaki jest najmniejszy i najwyższy wzrost u osób z rozmiarem buta 10?
wzrost_rozmiar_10 = wzrost[rozmiar_buta == 10]
min_wzrost_rozmiar_10 = np.min(wzrost_rozmiar_10)
max_wzrost_rozmiar_10 = np.max(wzrost_rozmiar_10)
print("Najmniejszy wzrost osób z rozmiarem buta 10:", min_wzrost_rozmiar_10)
print("Najwyższy wzrost osób z rozmiarem buta 10:", max_wzrost_rozmiar_10)

# Stwórz tablicę zawierającą europejski rozmiar butów dla tych osób
europejski_rozmiar_buta = rozmiar_buta + 33
print("Europejski rozmiar butów:", europejski_rozmiar_buta)


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Przedział [-2, 2]
x = np.linspace(-2, 2, 100)

# Funkcje
y1 = x
y2 = x ** 2

# Ustawienia stylu seaborn
sns.set(style='darkgrid')

# Wykres punktowy x
plt.scatter(x, y1, label='x')

# Wykres punktowy x^2
plt.scatter(x, y2, label='x^2')

# Legenda
plt.legend()

# Tytuł i etykiety osi
plt.title("Wykres punktowy")
plt.xlabel("x")
plt.ylabel("y")

# Wyświetlenie wykresu
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Wczytaj dane z pliku CSV
dane = pd.read_csv("wyniki.csv", delimiter=";")

# Zadanie 1: Ilość ogólna otrzymanych kart do głosowania
ilosc_kart = dane['Liczba kart'].sum()
print("Ilość ogólna otrzymanych kart do głosowania:", ilosc_kart)

# Zadanie 2: Procent kopert bez oświadczenia w każdym powiecie
dane['Procent kopert bez oświadczenia'] = (dane['Liczba kopert zwrotnych, w których nie było oświadczenia o osobistym i tajnym oddaniu głosu'] / dane['Liczba kopert zwrotnych']) * 100

# Wykres słupkowy procentu kopert bez oświadczenia w każdym powiecie
dane.plot(x='Kod TERYT', y='Procent kopert bez oświadczenia', kind='bar', figsize=(12, 6))
plt.xlabel('Kod TERYT')
plt.ylabel('Procent kopert bez oświadczenia')
plt.title('Procent kopert bez oświadczenia w każdym powiecie')
plt.xticks(rotation=45)
plt.show()

# Zadanie 3: Łączna suma głosów dla każdego kandydata
kandydaci = ['Robert BIEDROŃ', 'Krzysztof BOSAK', 'Andrzej Sebastian DUDA', 'Szymon Franciszek HOŁOWNIA', 'Marek JAKUBIAK', 'Władysław Marcin KOSINIAK-KAMYSZ', 'Mirosław Mariusz PIOTROWSKI', 'Paweł Jan TANAJNO', 'Rafał Kazimierz TRZASKOWSKI', 'Waldemar Włodzimierz WITKOWSKI', 'Stanisław Józef ŻÓŁTEK']
suma_glosow = dane[kandydaci].sum()

# Wykres osób z największymi liczbami głosów
suma_glosow.sort_values().plot(kind='barh', figsize=(10, 8))
plt.xlabel('Liczba głosów')
plt.ylabel('Kandydaci')
plt.title('Osoby z największymi liczbami głosów')
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Wczytanie pliku CSV
dane = pd.read_csv('wyniki.csv')

# Ilość ogólna otrzymanych kart do głosowania
ilosc_kart = dane.shape[0]
print("Ilość ogólna otrzymanych kart do głosowania:", ilosc_kart)

# Wyznaczenie procentu kopert bez oświadczenia w każdym powiecie
koperty_bez_oswiadczenia = dane[dane['Oświadczenie'] == 'Nie'].groupby('Powiat').size()
procent_kopert_bez_oswiadczenia = (koperty_bez_oswiadczenia / ilosc_kart) * 100

# Narysowanie wykresu słupkowego procentu kopert bez oświadczenia w każdym powiecie
procent_kopert_bez_oswiadczenia.plot(kind='bar')
plt.xlabel('Powiat')
plt.ylabel('Procent kopert bez oświadczenia')
plt.title('Procent kopert bez oświadczenia w każdym powiecie')
plt.show()

# Obliczenie łącznej sumy głosów dla każdego kandydata
suma_glosow = dane.groupby('Kandydat')['Głosy'].sum()

# Narysowanie wykresu osób z największymi liczbami głosów
najwieksi_kandydaci = suma_glosow.nlargest(5)  # Można zmienić liczbę na inną, jeśli potrzeba więcej lub mniej kandydatów
najwieksi_kandydaci.plot(kind='bar')
plt.xlabel('Kandydat')
plt.ylabel('Suma głosów')
plt.title('Osoby z największymi liczbami głosów')
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Wczytanie pliku
dane = pd.read_csv('wyniki.csv')

# Ilość ogólna otrzymanych kart do głosowania
ilosc_kart = dane['Liczba kart'].sum()
print("Ilość ogólna otrzymanych kart do głosowania:", ilosc_kart)

# Narysowanie wykresu procentu kopert bez oświadczenia w każdym powiecie
koperty_bez_oswiadczenia = dane.groupby('Powiat')['Oświadczenie'].apply(lambda x: (x == 'Nie').mean() * 100)
koperty_bez_oswiadczenia.plot(kind='bar', figsize=(10, 6))
plt.xlabel('Powiat')
plt.ylabel('Procent kopert bez oświadczenia')
plt.title('Procent kopert bez oświadczenia w każdym powiecie')
plt.show()

# Obliczenie łącznej sumy głosów dla każdego kandydata
suma_glosow = dane.groupby('Kandydat')['Liczba głosów'].sum()
print("Łączna suma głosów dla każdego kandydata:")
print(suma_glosow)

# Narysowanie wykresu osób z największymi liczbami głosów
najwiecej_glosow = dane.groupby('Kandydat')['Liczba głosów'].sum().nlargest(5)
najwiecej_glosow.plot(kind='bar', figsize=(10, 6))
plt.xlabel('Kandydat')
plt.ylabel('Liczba głosów')
plt.title('Osoby z największymi liczbami głosów')
plt.show()


kandydaci = ["Robert BIEDROŃ", "Krzysztof BOSAK", "Andrzej Sebastian DUDA", "Szymon Franciszek HOŁOWNIA", "Marek JAKUBIAK", "Władysław Marcin KOSINIAK-KAMYSZ", "Mirosław Mariusz PIOTROWSKI",
             "Paweł Jan TANAJNO", "Rafał Kazimierz TRZASKOWSKI", "Waldemar Włodzimierz WITKOWSKI", "Stanisław Józef ŻÓŁTEK"]

ilosc_glosow_na_kandydata = {}
for kandydat in kandydaci:
    ilosc_glosow = dane[dane["XD"] == kandydat]["Liczba głosów ważnych oddanych łącznie na wszystkich kandydatów"].sum()
    ilosc_glosow_na_kandydata[kandydat] = ilosc_glosow

print("Ilość głosów na poszczególnych kandydatów:")
for kandydat, ilosc in ilosc_glosow_na_kandydata.items():
    print(f"{kandydat}: {ilosc}")

    import numpy as np

# Przykładowe dane
plec = ["M", "K", "K", "M", "M"]
wiek = [25, 30, 42, 35, 28]
miejsce_zamieszkania = ["Warszawa", "Kraków", "Gdańsk", "Wrocław", "Poznań"]
czy_pali_papierosy = ["Tak", "Nie", "Tak", "Nie", "Tak"]

# Konwersja danych na wektory numpy
plec_wektor = np.array(plec)
wiek_wektor = np.array(wiek)
miejsce_zamieszkania_wektor = np.array(miejsce_zamieszkania)
czy_pali_papierosy_wektor = np.array(czy_pali_papierosy)

# Wyświetlanie wektorów
print("Wektor 'plec':", plec_wektor)
print("Wektor 'wiek':", wiek_wektor)
print("Wektor 'miejsce zamieszkania':", miejsce_zamieszkania_wektor)
print("Wektor 'czy pali papierosy':", czy_pali_papierosy_wektor)


import numpy as np
import pandas as pd

# Tworzenie tabeli na podstawie wprowadzonych danych
kolumny = {
    'Imię': np.array(['Anna', 'Jan', 'Maria', 'Krzysztof', 'Alicja']),
    'Wiek': np.array([35, 42, 28, 50, 39]),
    'Płeć': np.array(['Kobieta', 'Mężczyzna', 'Kobieta', 'Mężczyzna', 'Kobieta']),
    'Miejsce zamieszkania': np.array(['Miasto', 'Miasto', 'Wieś', 'Miasto', 'Wieś']),
    'Palacz': np.array(['Tak', 'Nie', 'Nie', 'Tak', 'Tak'])
}

tabela = pd.DataFrame(kolumny)

# Ile osób są w tabelce?
liczba_osob = len(tabela)
print(f"Ilość osób w tabelce: {liczba_osob}")

# Ile jest kobiet?
liczba_kobiet = len(tabela[tabela['Płeć'] == 'Kobieta'])
print(f"Ilość kobiet: {liczba_kobiet}")

# Ile osób poniżej 40 roku życia pali?
liczba_palacych_poniżej_40 = len(tabela[(tabela['Wiek'] < 40) & (tabela['Palacz'] == 'Tak')])
print(f"Ilość osób poniżej 40 roku życia palących: {liczba_palacych_poniżej_40}")

# Gdzie mieszka większość palących kobiet: na wsi czy w mieście?
miejsce_palacych_kobiet = tabela[(tabela['Płeć'] == 'Kobieta') & (tabela['Palacz'] == 'Tak')]['Miejsce zamieszkania'].value_counts()
if miejsce_palacych_kobiet['Miasto'] > miejsce_palacych_kobiet['Wieś']:
    print("Większość palących kobiet mieszka w mieście.")
else:
    print("Większość palących kobiet mieszka na wsi.")

# Średni wiek osób palących i niepalących
sredni_wiek_palacych = tabela[tabela['Palacz'] == 'Tak']['Wiek'].mean()
sredni_wiek_niepalacych = tabela[tabela['Palacz'] == 'Nie']['Wiek'].mean()
print(f"Średni wiek osób palących: {sredni_wiek_palacych:.2f}")
print(f"Średni wiek osób niepalących: {sredni_wiek_niepalacych:.2f}")

# Maksymalny wiek osób mieszkających na wsi
maks_wiek_wies = tabela[tabela['Miejsce zamieszkania'] == 'Wieś']['Wiek'].max()
print(f"Maksymalny wiek osób mieszkających na wsi: {maks_wiek_wies}")

import numpy as np

# Tworzenie tabeli na podstawie wprowadzonych danych
A = np.array(['Anna', 'Jan', 'Maria', 'Krzysztof', 'Alicja'])
B = np.array([35, 42, 28, 50, 39])
C = np.array(['Kobieta', 'Mężczyzna', 'Kobieta', 'Mężczyzna', 'Kobieta'])
D = np.array(['Miasto', 'Miasto', 'Wieś', 'Miasto', 'Wieś'])
E = np.array(['Tak', 'Nie', 'Nie', 'Tak', 'Tak'])

# Ile osób są w tabelce?
liczba_osob = len(A)
print(f"Ilość osób w tabelce: {liczba_osob}")

# Ile jest kobiet?
liczba_kobiet = np.sum(C == 'Kobieta')
print(f"Ilość kobiet: {liczba_kobiet}")

# Ile osób poniżej 40 roku życia pali?
liczba_palacych_poniżej_40 = np.sum((B < 40) & (E == 'Tak'))
print(f"Ilość osób poniżej 40 roku życia palących: {liczba_palacych_poniżej_40}")

# Gdzie mieszka większość palących kobiet: na wsi czy w mieście?
miejsce_palacych_kobiet = D[(C == 'Kobieta') & (E == 'Tak')]
liczba_palacych_w_miescie = np.sum(miejsce_palacych_kobiet == 'Miasto')
liczba_palacych_na_wsi = np.sum(miejsce_palacych_kobiet == 'Wieś')

if liczba_palacych_w_miescie > liczba_palacych_na_wsi:
    print("Większość palących kobiet mieszka w mieście.")
else:
    print("Większość palących kobiet mieszka na wsi.")

# Średni wiek osób palących i niepalących
sredni_wiek_palacych = np.mean(B[E == 'Tak'])
sredni_wiek_niepalacych = np.mean(B[E == 'Nie'])
print(f"Średni wiek osób palących: {sredni_wiek_palacych:.2f}")
print(f"Średni wiek osób niepalących: {sredni_wiek_niepalacych:.2f}")

# Maksymalny wiek osób mieszkających na wsi
maks_wiek_wies = np.max(B[D == 'Wieś'])
print(f"Maksymalny wiek osób mieszkających na wsi: {maks_wiek_wies}")


import numpy as np
import matplotlib.pyplot as plt

# Przygotowanie danych
x = np.linspace(0, 1, 100)
y1 = x**2
y2 = np.sqrt(x)

# Tworzenie wykresu
fig, ax = plt.subplots()

# Wykres y = x^2 (ciemno-czerwony)
ax.plot(x, y1, color='darkred', label='y = x^2')

# Wykres y = sqrt(x) (granatowy)
ax.plot(x, y2, color='navy', label='y = sqrt(x)')

# Ustawienie stylu linii
ax.lines[0].set_linestyle('-')  # linia ciągła dla y = x^2
ax.lines[1].set_linestyle('--')  # linia przerywana dla y = sqrt(x)

# Legenda
ax.legend()

# Dodanie etykiet osi
ax.set_xlabel('x')
ax.set_ylabel('y')

# Dodanie tytułu wykresu
ax.set_title('Wykresy funkcji y = x^2 i y = sqrt(x)')

# Miejsce wykresów
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Miejsce podpisu
ax.annotate('y = x^2', xy=(0.6, 0.5), xytext=(0.5, 0.8),
            arrowprops=dict(arrowstyle='->', color='black'))

ax.annotate('y = sqrt(x)', xy=(0.2, 0.2), xytext=(0.3, 0.5),
            arrowprops=dict(arrowstyle='->', color='black'))

# Wyświetlenie wykresu
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Przygotowanie danych
x = np.linspace(0, 1, 100)
y1 = x**2
y2 = np.sqrt(x)

# Tworzenie wykresu
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

# Wykres y = x^2 (ciemno-czerwony)
ax1.plot(x, y1, color='darkred')
ax1.set_ylabel('y = x^2')

# Wykres y = sqrt(x) (granatowy)
ax2.plot(x, y2, color='navy')
ax2.set_xlabel('x')
ax2.set_ylabel('y = sqrt(x)')

# Miejsce wykresów
ax1.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax1.xaxis.tick_top()
ax1.tick_params(labeltop=False)
ax2.xaxis.tick_bottom()

# Dodanie linii przerywanej łączącej wykresy
d = .015
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=4,
              linestyle='-', color='black', clip_on=False)
ax1.plot([1, 1], [0, 1], transform=ax1.transAxes, **kwargs)
ax2.plot([0, 0], [0, 1], transform=ax2.transAxes, **kwargs)

# Ustawienie limitów osi Y
ax1.set_ylim([0, 1])
ax2.set_ylim([0, 1])

# Usunięcie liniowego połączenia osi Y
ax1.spines['bottom'].set_color('none')
ax2.spines['top'].set_color('none')

# Dodanie pinów do osi Y
ax1.yaxis.set_ticks_position('left')
ax1.xaxis.set_ticks_position('both')
ax2.yaxis.set_ticks_position('right')
ax2.xaxis.set_ticks_position('both')

# Dodanie odstępu między wykresami
plt.subplots_adjust(hspace=0.05)

# Wyświetlenie wykresu
plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Przygotowanie danych
x = np.linspace(0, 1, 100)
y1 = x**2
y2 = np.sqrt(x)

# Rysowanie wykresów
fig, ax = plt.subplots()
ax.plot(x, y1, 'r-', label='y = x^2')
ax.plot(x, y2, 'b-', label='y = √x')

# Ustalenie zakresów osi x i y
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])

# Dodanie legendy
ax.legend(loc='upper left')

# Dodanie podpisów kolorów
ax.text(0.6, 0.7, 'Ciemno-czerwony', color='r')
ax.text(0.6, 0.4, 'Granatowy', color='b')

# Wyświetlenie wykresu
plt.show()


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 100)  # Tworzenie równomiernie rozłożonych punktów na przedziale [0, 1]
y1 = x**2  # Obliczanie wartości funkcji y1 = x^2
y2 = np.sqrt(x)  # Obliczanie wartości funkcji y2 = √x

# Pierwszy wykres
plt.subplot(2, 1, 1)  # Tworzenie pierwszego subplota
plt.plot(x, y1, color='darkred', label='y = x^2')  # Narysowanie wykresu funkcji y = x^2 w kolorze ciemno-czerwonym
plt.xlabel('x')  # Podpisanie osi x
plt.ylabel('y')  # Podpisanie osi y
plt.title('Wykres funkcji y = x^2')  # Tytuł wykresu
plt.legend()  # Wyświetlenie legendy z opisem funkcji

# Drugi wykres
plt.subplot(2, 1, 2)  # Tworzenie drugiego subplota
plt.plot(x, y2, color='navy', label='y = √x')  # Narysowanie wykresu funkcji y = √x w kolorze granatowym
plt.xlabel('x')  # Podpisanie osi x
plt.ylabel('y')  # Podpisanie osi y
plt.title('Wykres funkcji y = √x')  # Tytuł wykresu
plt.legend()  # Wyświetlenie legendy z opisem funkcji

plt.tight_layout()  # Dopasowanie wykresów do okna
plt.show()  # Wyświetlenie wykresów


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 100)  # Tworzenie równomiernie rozłożonych punktów na przedziale [0, 1]
y1 = x**2  # Obliczanie wartości funkcji y1 = x^2
y2 = np.sqrt(x)  # Obliczanie wartości funkcji y2 = √x

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5), sharey=True)

# Pierwszy wykres
ax1.plot(x, y1, color='darkred', label='y = x^2')  # Narysowanie wykresu funkcji y = x^2 w kolorze ciemno-czerwonym
ax1.set_xlabel('x')  # Podpisanie osi x
ax1.set_ylabel('y')  # Podpisanie osi y
ax1.set_title('Wykres funkcji y = x^2')  # Tytuł wykresu
ax1.legend()  # Wyświetlenie legendy z opisem funkcji
ax1.set_xticks(np.arange(0, 1.25, 0.25))  # Ustawienie podziałek osi x co 0.25 na przedziale [0, 1]

# Drugi wykres
ax2.plot(x, y2, color='navy', label='y = √x')  # Narysowanie wykresu funkcji y = √x w kolorze granatowym
ax2.set_xlabel('x')  # Podpisanie osi x
ax2.set_title('Wykres funkcji y = √x')  # Tytuł wykresu
ax2.legend()  # Wyświetlenie legendy z opisem funkcji
ax2.set_xticks(np.arange(0, 1.25, 0.25))  # Ustawienie podziałek osi x co 0.25 na przedziale [0, 1]

plt.tight_layout()  # Dopasowanie wykresów do okna
plt.show()  # Wyświetlenie wykresów


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 100)  # Tworzenie równomiernie rozłożonych punktów na przedziale [0, 1]
y1 = x**2  # Obliczanie wartości funkcji y1 = x^2
y2 = np.sqrt(x)  # Obliczanie wartości funkcji y2 = √x

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5), sharey=True)

# Pierwszy wykres
ax1.plot(x, y1, color='darkred', label='y = x^2')  # Narysowanie wykresu funkcji y = x^2 w kolorze ciemno-czerwonym
ax1.set_xlabel('x')  # Podpisanie osi x
ax1.set_ylabel('y')  # Podpisanie osi y
ax1.set_title('Wykres funkcji y = x^2')  # Tytuł wykresu
ax1.legend()  # Wyświetlenie legendy z opisem funkcji
ax1.set_xticks(np.arange(0, 1.25, 0.25))  # Ustawienie podziałek osi x co 0.25 na przedziale [0, 1]

# Drugi wykres
ax2.plot(x, y2, color='navy', label='y = √x')  # Narysowanie wykresu funkcji y = √x w kolorze granatowym
ax2.set_xlabel('x')  # Podpisanie osi x
ax2.set_title('Wykres funkcji y = √x')  # Tytuł wykresu
ax2.legend()  # Wyświetlenie legendy z opisem funkcji
ax2.set_xticks(np.arange(0, 1.25, 0.25))  # Ustawienie podziałek osi x co 0.25 na przedziale [0, 1]
ax2.set_yticklabels([])  # Usunięcie etykiet osi y dla drugiego wykresu

plt.tight_layout()  # Dopasowanie wykresów do okna
plt.show()  # Wyświetlenie wykresów


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 100)  # Tworzenie równomiernie rozłożonych punktów na przedziale [0, 1]
y1 = x**2  # Obliczanie wartości funkcji y1 = x^2
y2 = np.sqrt(x)  # Obliczanie wartości funkcji y2 = √x

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5), sharey=True)

# Pierwszy wykres
ax1.plot(x, y1, color='darkred', label='y = x^2')  # Narysowanie wykresu funkcji y = x^2 w kolorze ciemno-czerwonym
ax1.set_xlabel('x')  # Podpisanie osi x
ax1.set_ylabel('y')  # Podpisanie osi y
ax1.set_title('Wykres funkcji y = x^2')  # Tytuł wykresu
ax1.legend()  # Wyświetlenie legendy z opisem funkcji
ax1.set_xticks(np.arange(0, 1.25, 0.25))  # Ustawienie podziałek osi x co 0.25 na przedziale [0, 1]
ax1.set_yticklabels(['{:.1f}'.format(tick) for tick in ax1.get_yticks()])  # Formatowanie wymiarów na osi y

# Drugi wykres
ax2.plot(x, y2, color='navy', label='y = √x')  # Narysowanie wykresu funkcji y = √x w kolorze granatowym
ax2.set_xlabel('x')  # Podpisanie osi x
ax2.set_ylabel('y')  # Podpisanie osi y
ax2.set_title('Wykres funkcji y = √x')  # Tytuł wykresu
ax2.legend()  # Wyświetlenie legendy z opisem funkcji
ax2.set_xticks(np.arange(0, 1.25, 0.25))  # Ustawienie podziałek osi x co 0.25 na przedziale [0, 1]
ax2.set_yticklabels(['{:.1f}'.format(tick) for tick in ax2.get_yticks()])  # Formatowanie wymiarów na osi y

plt.tight_layout()  # Dopasowanie wykresów do okna
plt.show()  # Wyświetlenie wykresów


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 100)  # Tworzenie równomiernie rozłożonych punktów na przedziale [0, 1]
y1 = x**2  # Obliczanie wartości funkcji y1 = x^2
y2 = np.sqrt(x)  # Obliczanie wartości funkcji y2 = √x

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5), sharey=True)

# Pierwszy wykres
ax1.plot(x, y1, color='darkred', label='y = x^2')  # Narysowanie wykresu funkcji y = x^2 w kolorze ciemno-czerwonym
ax1.set_xlabel('x')  # Podpisanie osi x
ax1.set_ylabel('y')  # Podpisanie osi y
ax1.set_title('Wykres funkcji y = x^2')  # Tytuł wykresu
ax1.legend()  # Wyświetlenie legendy z opisem funkcji
ax1.set_xticks(np.arange(0, 1.25, 0.25))  # Ustawienie podziałek osi x co 0.25 na przedziale [0, 1]
ax1.set_yticks(np.arange(0, 1.25, 0.25))  # Ustawienie podziałek osi y co 0.25 na przedziale [0, 1]
ax1.set_yticklabels(['{:.1f}'.format(tick) for tick in ax1.get_yticks()])  # Formatowanie wymiarów na osi y

# Drugi wykres
ax2.plot(x, y2, color='navy', label='y = √x')  # Narysowanie wykresu funkcji y = √x w kolorze granatowym
ax2.set_xlabel('x')  # Podpisanie osi x
ax2.set_ylabel('y')  # Podpisanie osi y
ax2.set_title('Wykres funkcji y = √x')  # Tytuł wykresu
ax2.legend()  # Wyświetlenie legendy z opisem funkcji
ax2.set_xticks(np.arange(0, 1.25, 0.25))  # Ustawienie podziałek osi x co 0.25 na przedziale [0, 1]
ax2.set_yticks(np.arange(0, 1.25, 0.25))  # Ustawienie podziałek osi y co 0.25 na przedziale [0, 1]
ax2.set_yticklabels(['{:.1f}'.format(tick) for tick in ax2.get_yticks()])  # Formatowanie wymiarów na osi y

plt.tight_layout()  # Dopasowanie wykresów do okna
plt.show()  # Wyświetlenie wykresów


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 100)  # Tworzenie równomiernie rozłożonych punktów na przedziale [0, 1]
y1 = x**2  # Obliczanie wartości funkcji y1 = x^2
y2 = np.sqrt(x)  # Obliczanie wartości funkcji y2 = √x

fig, ax = plt.subplots(figsize=(8, 6))

# Wykres funkcji y = x^2
ax.plot(x, y1, color='darkred', label='y = x^2')  # Narysowanie wykresu funkcji y = x^2 w kolorze ciemno-czerwonym

# Wykres funkcji y = √x
ax.plot(x, y2, color='navy', linestyle='dotted', label='y = √x')  # Narysowanie wykresu funkcji y = √x jako linii kropkowanej

ax.set_xlabel('x')  # Podpisanie osi x
ax.set_ylabel('y')  # Podpisanie osi y
ax.set_title('Wykresy funkcji')  # Tytuł wykresu
ax.legend()  # Wyświetlenie legendy z opisem funkcji
ax.set_xticks(np.arange(0, 1.25, 0.25))  # Ustawienie podziałek osi x co 0.25 na przedziale [0, 1]
ax.set_yticks(np.arange(0, 1.25, 0.25))  # Ustawienie podziałek osi y co 0.25 na przedziale [0, 1]

plt.tight_layout()  # Dopasowanie wykresu do okna
plt.show()  # Wyświetlenie wykresu


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 100)  # Tworzenie równomiernie rozłożonych punktów na przedziale [0, 1]
y1 = x**2  # Obliczanie wartości funkcji y1 = x^2
y2 = np.sqrt(x)  # Obliczanie wartości funkcji y2 = √x

fig, ax = plt.subplots(figsize=(8, 6))

# Wykres funkcji y = x^2
ax.plot(x, y1, color='darkred', label='y = x^2')  # Narysowanie wykresu funkcji y = x^2 w kolorze ciemno-czerwonym

# Wykres funkcji y = √x
ax.plot(x, y2, color='navy', linestyle='dotted', label='y = √x')  # Narysowanie wykresu funkcji y = √x jako linii kropkowanej

ax.set_xlabel('x')  # Podpisanie osi x
ax.set_ylabel('y')  # Podpisanie osi y
ax.set_title('Wykresy funkcji')  # Tytuł wykresu
legend = ax.legend(title='Funkcje', loc='upper right')  # Wyświetlenie legendy z tytułem i opisem funkcji
ax.set_xticks(np.arange(0, 1.25, 0.25))  # Ustawienie podziałek osi x co 0.25 na przedziale [0, 1]
ax.set_yticks(np.arange(0, 1.25, 0.25))  # Ustawienie podziałek osi y co 0.25 na przedziale [0, 1]

plt.tight_layout()  # Dopasowanie wykresu do okna
plt.show()  # Wyświetlenie wykresu


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Wczytanie danych z pliku CSV
data = pd.read_csv('http://wmii.uwm.edu.pl/~muranova/WD2022-23/titanic.csv')

# Ile kobiet z pierwszej klasy przeżyło?
women_survived = len(data[(data['Sex'] == 'female') & (data['Pclass'] == 1) & (data['Survived'] == 1)])
print("Liczba kobiet z pierwszej klasy, które przeżyły:", women_survived)

# Jaki był średni wiek mężczyzn, którzy nie przeżyli?
mean_age_men_not_survived = data[(data['Sex'] == 'male') & (data['Survived'] == 0)]['Age'].mean()
print("Średni wiek mężczyzn, którzy nie przeżyli:", mean_age_men_not_survived)

# Narysuj wykres punktowy zależności opłaty(fare) od wieku pasażera, kolorem zaznacz płeć
plt.scatter(data['Age'], data['Fare'], c=np.where(data['Sex'] == 'male', 'blue', 'red'))
plt.xlabel('Wiek')
plt.ylabel('Opłata (Fare)')
plt.title('Zależność opłaty od wieku pasażera (z podziałem na płeć)')
plt.show()

# Narysuj wykres słupkowy procentu osób, które przeżyły, w zależności od klasy
survival_percentage_by_class = data.groupby('Pclass')['Survived'].mean() * 100
survival_percentage_by_class.plot(kind='bar', color='green')
plt.xlabel('Klasa')
plt.ylabel('Procent przeżytych')
plt.title('Procent osób, które przeżyły, w zależności od klasy')
plt.xticks(rotation=0)
plt.ylim(0, 100)
plt.show()


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Wczytanie danych z pliku CSV
data = pd.read_csv('http://wmii.uwm.edu.pl/~muranova/WD2022-23/titanic.csv', sep=',')

# Ile kobiet z pierwszej klasy przeżyło?
women_survived = len(data[(data['Sex'] == 'female') & (data['Pclass'] == 1) & (data['Survived'] == 1)])
print("Liczba kobiet z pierwszej klasy, które przeżyły:", women_survived)

#


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Wczytanie danych z pliku CSV
data = pd.read_csv('http://wmii.uwm.edu.pl/~muranova/WD2022-23/titanic.csv', sep=',')
data.columns = ['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked', 'Class', 'Who', 'Adult_male', 'Embark_town', 'Alive', 'Alone']

# Ile kobiet z pierwszej klasy przeżyło?
women_survived = len(data[(data['Sex'] == 'female') & (data['Pclass'] == 1) & (data['Survived'] == 'yes')])
print("Liczba kobiet z pierwszej klasy, które przeżyły:", women_survived)

# Jaki był średni wiek mężczyzn, którzy nie przeżyli?
mean_age_men_not_survived = data[(data['Sex'] == 'male') & (data['Survived'] == 'no')]['Age'].mean()
print("Średni wiek mężczyzn, którzy nie przeżyli:", mean_age_men_not_survived)

# Narysuj wykres punktowy zależności opłaty (fare) od wieku pasażera, kolorem zaznacz płeć
plt.scatter(data['Age'], data['Fare'], c=np.where(data['Sex'] == 'male', 'blue', 'red'))
plt.xlabel('Wiek')
plt.ylabel('Opłata (Fare)')
plt.title('Zależność opłaty od wieku pasażera (z podziałem na płeć)')
plt.show()

# Narysuj wykres słupkowy procentu osób, które przeżyły, w zależności od klasy
survival_percentage_by_class = data.groupby('Class')['Survived'].apply(lambda x: (x == 'yes').mean() * 100)
survival_percentage_by_class.plot(kind='bar', color='green')
plt.xlabel('Klasa')
plt.ylabel('Procent przeżytych')
plt.title('Procent osób, które przeżyły, w zależności od klasy')
plt.xticks(rotation=0)
plt.ylim(0, 100)
plt.show()

import pandas as pd

# Wczytanie danych z pliku CSV
data = pd.read_csv('http://wmii.uwm.edu.pl/~muranova/WD2022-23/titanic.csv', sep=',')
data.columns = ['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked', 'Class', 'Who', 'Adult_male', 'Embark_town', 'Alive', 'Alone']

# Ile kobiet z pierwszej klasy przeżyło?
women_survived = data[(data['Sex'] == 'female') & (data['Pclass'] == 1) & (data['Survived'] == 'yes')].shape[0]
print("Liczba kobiet z pierwszej klasy, które przeżyły:", women_survived)

import pandas as pd

# Wczytanie danych z pliku CSV
data = pd.read_csv('http://wmii.uwm.edu.pl/~muranova/WD2022-23/titanic.csv', sep=',')
data.columns = ['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked', 'Class', 'Who', 'Adult_male', 'Embark_town', 'Alive', 'Alone']

# Mapowanie wartości "yes" jako 1 i "no" jako 0 dla kolumny "Survived"
data['Survived'] = data['Survived'].map({'yes': 1, 'no': 0})

# Ile kobiet z pierwszej klasy przeżyło?
women_survived = data[(data['Sex'] == 'female') & (data['Pclass'] == 1) & (data['Survived'] == 1)].shape[0]
print("Liczba kobiet z pierwszej klasy, które przeżyły:", women_survived)


import pandas as pd

# Wczytanie danych z pliku CSV
data = pd.read_csv('http://wmii.uwm.edu.pl/~muranova/WD2022-23/titanic.csv', sep=',')
data.columns = ['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked', 'Class', 'Who', 'Adult_male', 'Embark_town', 'Alive', 'Alone']

# Mapowanie wartości "yes" jako 1 i "no" jako 0 dla kolumny "Survived"
data['Survived'] = data['Survived'].map({'yes': 1, 'no': 0})

# Jaki był średni wiek mężczyzn, którzy nie przeżyli?
mean_age_men_not_survived = data[(data['Sex'] == 'male') & (data['Survived'] == 0)]['Age'].mean()
print("Średni wiek mężczyzn, którzy nie przeżyli:", mean_age_men_not_survived)

import pandas as pd
import matplotlib.pyplot as plt

# Wczytanie danych z pliku CSV
data = pd.read_csv('http://wmii.uwm.edu.pl/~muranova/WD2022-23/titanic.csv', sep=',')
data.columns = ['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked', 'Class', 'Who', 'Adult_male', 'Embark_town', 'Alive', 'Alone']

# Mapowanie wartości "yes" jako 1 i "no" jako 0 dla kolumny "Survived"
data['Survived'] = data['Survived'].map({'yes': 1, 'no': 0})

# Narysowanie wykresu punktowego zależności opłaty (fare) od wieku pasażera
plt.scatter(data['Age'], data['Fare'], c=data['Sex'].map({'male': 'blue', 'female': 'pink'}))
plt.xlabel('Wiek pasażera')
plt.ylabel('Opłata (fare)')
plt.title('Zależność opłaty od wieku pasażera')
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Wczytanie danych z pliku CSV
data = pd.read_csv('http://wmii.uwm.edu.pl/~muranova/WD2022-23/titanic.csv', sep=',')
data.columns = ['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked', 'Class', 'Who', 'Adult_male', 'Embark_town', 'Alive', 'Alone']

# Mapowanie wartości "yes" jako 1 i "no" jako 0 dla kolumny "Survived"
data['Survived'] = data['Survived'].map({'yes': 1, 'no': 0})

# Grupowanie danych według klasy i obliczanie procentu osób, które przeżyły
survival_percentages = data.groupby('Pclass')['Survived'].mean() * 100

# Narysowanie wykresu słupkowego
plt.bar(survival_percentages.index, survival_percentages)
plt.xlabel('Klasa')
plt.ylabel('Procent przeżytych')
plt.title('Procent osób, które przeżyły, w zależności od klasy')
plt.xticks(survival_percentages.index)
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

# Wczytanie danych z wbudowanej bazy "iris" w seaborn
data = sns.load_dataset("iris")

# Narysowanie wykresu punktowego zależności szerokości płatka od długości płatka
sns.scatterplot(data=data, x="petal_length", y="petal_width", hue="species", size="sepal_length", sizes=(20, 200), palette="Greens")

# Ustawienie nazw osi
plt.xlabel('Długość płatka (petal_length)')
plt.ylabel('Szerokość płatka (petal_width)')

# Wyświetlenie legendy
plt.legend(title='Gatunek')

# Wyświetlenie wykresu
plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

# Wczytanie danych z wbudowanej bazy "iris" w seaborn
data = sns.load_dataset("iris")

# Narysowanie wykresu punktowego z zaznaczonymi gatunkami, rozmiarem działki kielicha i kolorem szerokości działki kielicha
sns.scatterplot(data=data, x="petal_length", y="petal_width", hue="species", style="species", size="sepal_length", sizes=(20, 200), palette="Greens")

# Ustawienie nazw osi
plt.xlabel('Długość płatka (petal_length)')
plt.ylabel('Szerokość płatka (petal_width)')

# Wyświetlenie wykresu
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

# Wczytanie danych z wbudowanej bazy "iris" w seaborn
data = sns.load_dataset("iris")

# Narysowanie wykresu punktowego z zaznaczonymi gatunkami, rozmiarem działki kielicha i kolorem szerokości działki kielicha
scatter = sns.scatterplot(data=data, x="petal_length", y="petal_width", hue="species", style="species", size="sepal_length", sizes=(20, 200), palette="Greens")

# Ustawienie nazw osi
plt.xlabel('Długość płatka (petal_length)')
plt.ylabel('Szerokość płatka (petal_width)')

# Przesunięcie legendy na prawo
plt.legend(title='Gatunek', loc='center left', bbox_to_anchor=(1, 0.5))

# Dodanie etykiet do legendy
sepal_width_labels = [2.0, 2.5, 3.0, 3.5, 4.0]
sepal_length_labels = [4.8, 5.4, 6.0, 6.6, 7.2, 7.8]
species_labels = ['setosa', 'versicolor', 'virginica']

# Utworzenie słownika z etykietami dla każdego punktu w legendzie
legend_labels = {label: (sepal_width, sepal_length) for label, sepal_width, sepal_length in zip(species_labels, sepal_width_labels, sepal_length_labels)}

# Dodanie etykiet do legendy
for label, (sepal_width, sepal_length) in legend_labels.items():
    scatter.plot([], [], marker='o', markersize=10, label=label, markerfacecolor='green', markeredgecolor='green')
    plt.text(1.05, 0.5, f'sepal_width {sepal_width}  senpal_length {sepal_length}', transform=plt.gca().transAxes, verticalalignment='center')

# Wyświetlenie wykresu
plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

# Wczytanie danych z wbudowanej bazy "iris" w seaborn
data = sns.load_dataset("iris")

# Mapowanie wartości sepal_width na kolor
sepal_width_colors = {2.0: 'limegreen', 2.5: 'darkgreen', 3.0: 'green', 3.5: 'forestgreen', 4.0: 'darkolivegreen'}

# Mapowanie wartości sepal_length na rozmiar czarnego kółka
sepal_length_sizes = {4.8: 50, 5.4: 75, 6.0: 100, 6.6: 125, 7.2: 150, 7.8: 175}

# Utworzenie słownika z oznaczeniami dla każdego gatunku
species_markers = {'setosa': 'o', 'versicolor': 'x', 'virginica': 's'}

# Narysowanie wykresu punktowego z odpowiednimi parametrami
scatter = sns.scatterplot(data=data, x="petal_length", y="petal_width", hue="species", style="species",
                          size="sepal_length", sizes=sepal_length_sizes.values(), palette="Greens",
                          legend=False)

# Dodanie punktów i etykiet do legendy
for sepal_width, color in sepal_width_colors.items():
    scatter.plot([], [], marker='o', markersize=10, label=f'sepal_width {sepal_width}', color=color)

for sepal_length, size in sepal_length_sizes.items():
    scatter.plot([], [], marker='o', markersize=size, label=f'sepal_length {sepal_length}', color='black')

for species, marker in species_markers.items():
    scatter.plot([], [], marker=marker, markersize=10, label=species, color='black')

# Ustawienie orientacji legendy na pionową (leci w dół)
scatter.legend(title='Legenda', loc='center left', bbox_to_anchor=(1, 0.5), frameon=False, labelspacing=1, title_fontsize='12',
               handlelength=3, handletextpad=1, borderpad=1)

# Ustawienie tytułów osi
plt.xlabel('Długość płatka (petal_length)')
plt.ylabel('Szerokość płatka (petal_width)')

# Wyświetlenie wykresu
plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("iris")

sepal_width_colors = {2.0: 'limegreen', 2.5: 'darkgreen', 3.0: 'green', 3.5: 'forestgreen', 4.0: 'darkolivegreen'}
sepal_length_sizes = {4.8: 50, 5.4: 75, 6.0: 100, 6.6: 125, 7.2: 150, 7.8: 175}
species_markers = {'setosa': 'o', 'versicolor': 'x', 'virginica': 's'}

# Przeskalowanie rozmiarów markerów na podstawie wartości sepal_length
size_values = [sepal_length_sizes[length] for length in data['sepal_length']]

scatter = sns.scatterplot(data=data, x="petal_length", y="petal_width", hue="species", style="species",
                          size=size_values, sizes=(50, 200), palette="Greens", legend=False)

for sepal_width, color in sepal_width_colors.items():
    scatter.plot([], [], marker='o', markersize=10, label=f'sepal_width {sepal_width}', color=color)

for sepal_length, size in sepal_length_sizes.items():
    scatter.plot([], [], marker='o', markersize=size, label=f'sepal_length {sepal_length}', color='black')

for species, marker in species_markers.items():
    scatter.plot([], [], marker=marker, markersize=10, label=species, color='black')

scatter.legend(title='Legenda', loc='center left', bbox_to_anchor=(1, 0.5), frameon=False, labelspacing=1, title_fontsize='12',
               handlelength=3, handletextpad=1, borderpad=1)

plt.xlabel('Długość płatka (petal_length)')
plt.ylabel('Szerokość płatka (petal_width)')

plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("iris")

sepal_width_colors = {2.0: 'limegreen', 2.5: 'darkgreen', 3.0: 'green', 3.5: 'forestgreen', 4.0: 'darkolivegreen'}
sepal_length_sizes = {4.8: 50, 5.4: 75, 6.0: 100, 6.6: 125, 7.2: 150, 7.8: 175}
species_markers = {'setosa': 'o', 'versicolor': 'x', 'virginica': 's'}

# Przeskalowanie rozmiarów markerów na podstawie wartości sepal_length
size_values = [sepal_length_sizes.get(length, 0) for length in data['sepal_length']]

scatter = sns.scatterplot(data=data, x="petal_length", y="petal_width", hue="species", style="species",
                          size=size_values, sizes=(50, 200), palette="Greens", legend=False)

for sepal_width, color in sepal_width_colors.items():
    scatter.plot([], [], marker='o', markersize=10, label=f'sepal_width {sepal_width}', color=color)

for sepal_length, size in sepal_length_sizes.items():
    scatter.plot([], [], marker='o', markersize=size, label=f'sepal_length {sepal_length}', color='black')

for species, marker in species_markers.items():
    scatter.plot([], [], marker=marker, markersize=10, label=species, color='black')

scatter.legend(title='Legenda', loc='center left', bbox_to_anchor=(1, 0.5), frameon=False, labelspacing=1, title_fontsize='12',
               handlelength=3, handletextpad=1, borderpad=1)

plt.xlabel('Długość płatka (petal_length)')
plt.ylabel('Szerokość płatka (petal_width)')

plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

# Wczytanie danych z wbudowanej bazy "iris" w seaborn
data = sns.load_dataset("iris")

# Narysowanie wykresu punktowego z zaznaczonymi gatunkami, rozmiarem działki kielicha i kolorem szerokości działki kielicha
scatter = sns.scatterplot(data=data, x="petal_length", y="petal_width", hue="species", style="species", size="sepal_length", sizes=(20, 200), palette="Greens")

# Ustawienie nazw osi
plt.xlabel('Długość płatka (petal_length)')
plt.ylabel('Szerokość płatka (petal_width)')

# Przesunięcie legendy na prawo
legend = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), frameon=False)

# Usunięcie ramki z legendy
legend.set_frame_on(False)

# Dodanie etykiet do legendy
sepal_width_labels = [2.0, 2.5, 3.0, 3.5, 4.0]
sepal_length_labels = [4.8, 5.4, 6.0, 6.6, 7.2, 7.8]
species_labels = ['setosa', 'versicolor', 'virginica']

# Utworzenie słownika z etykietami dla każdego punktu w legendzie
legend_labels = {label: (sepal_width, sepal_length) for label, sepal_width, sepal_length in zip(species_labels, sepal_width_labels, sepal_length_labels)}

# Dodanie etykiet do legendy
for label, (sepal_width, sepal_length) in legend_labels.items():
    scatter.plot([], [], marker='o', markersize=10, label=label, markerfacecolor='green', markeredgecolor='green')
    plt.text(1.05, 0.5, f'sepal_width {sepal_width}  senpal_length {sepal_length}', transform=plt.gca().transAxes, verticalalignment='center')

# Wyświetlenie wykresu
plt.show()
