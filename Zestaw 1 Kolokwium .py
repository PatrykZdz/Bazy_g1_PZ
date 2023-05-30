Kolumny : Nazwa_rzeki Kontynent Długość_w_km Powierzchnia_dorzecza_w_tys_km2 Liczba_państw_przez_które_przeplywa
Ile rzek s¡ w tabelce? (5%) Ile s¡ w Eurazji ?(5%) Wypisz nazwy rzek, który zaczynaj¡
si¦ z liter pó¹niejszych w alfabecie, ni» 'N' (5%) Ile rzek przepªywaj¡ wi¦cej ni» przez 2
Pa«stwa?(5%) Wypisz nazwy rzek z dªugo±ci¡ nie mniejsz¡ ni» 4500 km, który s¡ w Eurazji
lub w Afryce (5%). Posortuj nazwy wszystkich rzek wedªug powierzchni malej¡co.


Wypisz nazwy rzek, który zaczynaj¡ si¦ z liter pó¹niejszych w alfabecie, ni» 'N'
Wypisz nazwy rzek z dªugo±ci¡ nie mniejsz¡ ni» 4500 km, który s¡ w Eurazji lub w Afryce

Narysuj wykresy funkcji y = x
3
(ciemno czerwony) na [0, 2] oraz y =
√3 x(ciemno-zielony) na [0, 512]
w jednym okienku na dwóch wykresach, podpisuj¡c który kolor odpowiada której funkcji. Kolory,
typ linii, miejsca wykresów oraz miejsce podpisu musz¡ by¢ taki same jak na obrazku.



# Cwiczenie 1.1
import numpy as np


plec = np.array(["Mezczyzna","Kobieta","Mezczyzna","Mezczyzna","Kobieta","Mezczyzna",
                 "Kobieta","Mezczyzna","Kobieta","Mezczyzna","Mezczyzna","Kobieta","Kobieta"
                 ,"Mezczyzna","Mezczyzna","Kobieta","Mezczyzna"])
wiek = np.array([20,30,21,34,45,21,17,18,19,23,36,69,34,58,23,44,12])
miejsce_zamieszkania = np.array(["Wies","Miasto","Wies","Miasto","Wies","Miasto","Miasto","Miasto",
                                 "Wies","Miasto","Miasto","Wies","Miasto","Miasto","Wies","Wies","Miasto"])
czy_pali_Pan_Pani_papierosy = np.array(["Tak","Tak","Tak","Nie","Nie","Tak","Nie","Nie","Tak","Nie","Nie",
                                        "Tak","Tak","Tak","Nie","Nie","Nie"])

tabela = np.array([plec,wiek,miejsce_zamieszkania,czy_pali_Pan_Pani_papierosy])
print(tabela)

# Ile osób są w tabelce?
liczba_osob = len(plec)
print(liczba_osob)

# Ile jest kobiet?
liczba_kobiet = np.sum(plec == "Kobieta")
print(liczba_kobiet)

# Ile osób poniżej 40 roku życia pali?
liczba_palacych_poniżej_40 = np.sum((wiek < 40) & (czy_pali_Pan_Pani_papierosy== 'Tak'))
print(liczba_palacych_poniżej_40)

# Gdzie mieszka większość palących kobiet: na wsi czy w mieście?
miejsce_palacych_kobiet = miejsce_zamieszkania[(plec == 'Kobieta') & (czy_pali_Pan_Pani_papierosy== 'Tak')]
liczba_palacych_w_miescie = np.sum(miejsce_palacych_kobiet == 'Miasto')
liczba_palacych_na_wsi = np.sum(miejsce_palacych_kobiet == 'Wieś')

if liczba_palacych_w_miescie > liczba_palacych_na_wsi:
    print("Większość palących kobiet mieszka w mieście.")
else:
    print("Większość palących kobiet mieszka na wsi.")

# Średni wiek osób palących i niepalących
sredni_wiek_palacych = np.mean(wiek[czy_pali_Pan_Pani_papierosy == 'Tak'])
sredni_wiek_niepalacych = np.mean(wiek[czy_pali_Pan_Pani_papierosy == 'Nie'])
print(f"Średni wiek osób palących: {sredni_wiek_palacych:.2f}")
print(f"Średni wiek osób niepalących: {sredni_wiek_niepalacych:.2f}")

# Maksymalny wiek osób mieszkających na wsi
maks_wiek_wies = np.max(wiek[miejsce_zamieszkania == 'Wies'])
print(f"Maksymalny wiek osób mieszkających na wsi: {maks_wiek_wies}")

#Cwiczenie 1.2 niedokonczone

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 100)  # Tworzenie równomiernie rozłożonych punktów na przedziale [0, 1]
y1 = x**2  # Obliczanie wartości funkcji y1 = x^2
y2 = np.sqrt(x)  # Obliczanie wartości funkcji y2 = √x

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5), sharey=True)

# Pierwszy wykres
ax1.plot(x, y1, color='darkred', label='x^2')  # Narysowanie wykresu funkcji y = x^2 w kolorze ciemno-czerwonym
ax1.legend()  # Wyświetlenie legendy z opisem funkcji
ax1.set_xticks(np.arange(0, 1.25, 0.25))  # Ustawienie podziałek osi x co 0.25 na przedziale [0, 1]
legend = ax1.legend(title='Wykres', loc='upper left')  # Wyświetlenie legendy z tytułem i opisem funkcji

# Drugi wykres
ax2.plot(x, y2, color='navy', label='√x',linestyle='dotted')  # Narysowanie wykresu funkcji y = √x w kolorze granatowym
ax2.set_xticks(np.arange(0, 1.25, 0.25))  # Ustawienie podziałek osi x co 0.25 na przedziale [0, 1]

plt.tight_layout()  # Dopasowanie wykresów do okna
plt.show()  # Wyświetlenie wykresów


#Zadanie 1.3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Wczytanie danych z pliku CSV
data = pd.read_csv('titanic.csv', sep=',')
data.columns = ['survived', 'pclass', 'sex', 'age', 'sibSp', 'parch', 'fare', 'embarked', 'class', 'who', 'adult_male', 'embark_town', 'alive', 'alone']

# Ile kobiet z pierwszej klasy przeżyło?
women_survived = len(data[(data['sex'] == 'female') & (data['pclass'] == 1) & (data['survived'] == 1)])
print("Liczba kobiet z pierwszej klasy, które przeżyły:", women_survived)

# Jaki był średni wiek mężczyzn, którzy nie przeżyli?
mean_age_men_not_survived = data[(data['sex'] == 'male') & (data['survived'] == 0)]['age'].mean()
print("Średni wiek mężczyzn, którzy nie przeżyli:", mean_age_men_not_survived)

# Narysowanie wykresu punktowego zależności opłaty (fare) od wieku pasażera
plt.scatter(data['age'], data['fare'], c=data['sex'].map({'male': 'blue', 'female': 'pink'}))
plt.xlabel('Wiek pasażera')
plt.ylabel('Opłata (fare)')
plt.title('Zależność opłaty od wieku pasażera')
plt.show()

# Grupowanie danych według klasy i obliczanie procentu osób, które przeżyły
survival_percentages = data.groupby('pclass')['survived'].mean() * 100

# Narysowanie wykresu słupkowego
plt.bar(survival_percentages.index, survival_percentages)
plt.xlabel('Klasa')
plt.ylabel('Procent przeżytych')
plt.title('Procent osób, które przeżyły, w zależności od klasy')
plt.xticks(survival_percentages.index)
plt.show()

#zadanie 1.4
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






