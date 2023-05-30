import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Dane wejściowe
rozmiar_buta = np.array([38, 42, 39, 41, 40, 39, 38, 37, 42, 40])
wzrost = np.array([153, 154, 154, 155, 172, 169, 160, 162, 170, 173])

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

# Jaki jest najmniejszy i najwyższy wzrost u osób z rozmiarem buta 10, jeśli istnieją?
if np.any(rozmiar_buta == 10):
    wzrost_rozmiar_10 = wzrost[rozmiar_buta == 10]
    min_wzrost_rozmiar_10 = np.min(wzrost_rozmiar_10)
    max_wzrost_rozmiar_10 = np.max(wzrost_rozmiar_10)
    print("Najmniejszy wzrost osób z rozmiarem buta 10:", min_wzrost_rozmiar_10)
    print("Najwyższy wzrost osób z rozmiarem buta 10:", max_wzrost_rozmiar_10)
else:
    print("Brak danych dla rozmiaru buta 10")

# Stwórz tablicę zawierającą europejski rozmiar butów dla tych osób
europejski_rozmiar_buta = rozmiar_buta + 33
print("Europejski rozmiar butów:", europejski_rozmiar_buta)


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



# Wczytanie pliku
dane = pd.read_csv('wyniki.csv', sep=';')

# Obliczenie ilości ogólnej otrzymanych kart do głosowania
ilosc_kart = dane["XD"].sum()

# Wyświetlenie wyniku
print("Ilość ogólna otrzymanych kart do głosowania:", ilosc_kart)

kandydaci = ["Robert BIEDROŃ", "Krzysztof BOSAK", "Andrzej Sebastian DUDA", "Szymon Franciszek HOŁOWNIA", "Marek JAKUBIAK", "Władysław Marcin KOSINIAK-KAMYSZ", "Mirosław Mariusz PIOTROWSKI",
             "Paweł Jan TANAJNO", "Rafał Kazimierz TRZASKOWSKI", "Waldemar Włodzimierz WITKOWSKI", "Stanisław Józef ŻÓŁTEK"]

suma_glosow = dane["Liczba głosów ważnych oddanych łącznie na wszystkich kandydatów"].sum()

print("Łączna liczba głosów dla wszystkich kandydatów: ", suma_glosow)

kandydaci = ["Robert BIEDROŃ", "Krzysztof BOSAK", "Andrzej Sebastian DUDA", "Szymon Franciszek HOŁOWNIA", "Marek JAKUBIAK", "Władysław Marcin KOSINIAK-KAMYSZ", "Mirosław Mariusz PIOTROWSKI",
             "Paweł Jan TANAJNO", "Rafał Kazimierz TRZASKOWSKI", "Waldemar Włodzimierz WITKOWSKI", "Stanisław Józef ŻÓŁTEK"]

ilosc_glosow_na_kandydata = {}
for kandydat in kandydaci:
    ilosc_glosow = dane[dane[kandydaci] == kandydat]["Liczba głosów ważnych oddanych łącznie na wszystkich kandydatów"].sum()
    ilosc_glosow_na_kandydata[kandydat] = ilosc_glosow

print("Ilość głosów na poszczególnych kandydatów:")
for kandydat, ilosc in ilosc_glosow_na_kandydata.items():
    print(f"{kandydat}: {ilosc}")

