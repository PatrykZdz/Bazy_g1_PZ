import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Funkcja obliczająca metrykę euklidesową
def euklides(p, q):
    suma = 0
    for i in range(len(p)):
        suma += (p[i] - q[i]) ** 2
    return np.sqrt(suma)

# Klasyfikator KNN
def knn(k, train_data, train_labels, test_data):
    predict_class = []
    for test in test_data:
        dystanse = []
        for i in range(len(train_data)):
            dist = euklides(test, train_data[i])
            dystanse.append((dist, train_labels[i]))

        dystanse.sort(key=lambda x: x[0])
        sasiedzi = [label for _, label in dystanse[:k]]

        seria = pd.Series(sasiedzi)
        najczestsza = seria.value_counts().idxmax()
        predict_class.append(najczestsza)
    return predict_class

# Załadowanie danych i podziel na treningowe/testowe
iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# KNN
k = 3
predicted = knn(k, X_train, y_train, X_test)

# Dokładność
accuracy = np.mean(np.array(predicted) == y_test)
print(f"Dokładność: {accuracy:.2f}")
