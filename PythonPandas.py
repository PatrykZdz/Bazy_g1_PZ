import pandas as pd
import numpy as np

#Cwiczenie 1
#a)
seria1 = pd.Series([34,23,12,65])
seria2 = pd.Series(["Elo","Maria","Zofia"])
seria3 = pd.Series([1,2,3,4])
lista1 = [1,2,3,4,5]
lista1 = pd.Series(lista1)
print(lista1,"\n")
print(seria2,"\n")

lista2 = list(seria1)
print(lista2,"\n")

lista3 = np.array([1,2,3,4,5])
seria4 = pd.Series(lista3)
print(seria4)

numpy = np.array(seria1)
print(numpy)

liczby10 = np.random.uniform(-10,10,10)
seria5 = pd.Series(liczby10)
print(seria5)
### co 0,1 -

print(seria1+seria3,"\n")
print(seria1-seria3,"\n")
print(seria1*seria3,"\n")
print(seria1/seria3,"\n")

#b)
my_list = [1, 32, -37, 91, 12, 11, -5]
my_dict = {'a': [1, 3, 2], 'b': [2, 5, 7], 'c': [3, 4, 8], 'd': [4, 10, 12]}
my_array = np.array([[1, 2, 5],[-2, 3, 3], [5, 2, 6]])
my_series = pd.Series ([1, 32, -37, 91, 12, 11, -5], index=['a','b','c','d','e','f','g'])

DataFrame1 = pd.DataFrame(my_list)
DataFrame2 = pd.DataFrame(my_dict)
DataFrame3 = pd.DataFrame(my_array)
DataFrame4 = pd.DataFrame(my_series)

print(DataFrame1,"\n")
print(DataFrame2,"\n")
print(DataFrame3,"\n")
print(DataFrame4,"\n")
print(DataFrame1.values.tolist(),"\n")

#c)
data = {'a':['l1','l2','l3'], 'b':[1,-3,2], 'c':[2,8,-5], "d":[4,0.5,7]," ":[5,10,3]}
DataFrame5 = pd.DataFrame(data,index=["","",""])
print(DataFrame5,"\n")

#Cwicznie 2
df1 = pd.DataFrame([[2942, 9840, 2794, 8891, 8111, 2933, 8301, 9125],
[' Sylwia ', ' Katarzyna ', ' Teresa ', ' Tomasz ', ' Cezary ', 'Zenon', ' Filip ', ' Adrian '], [13, 31, 34, 14, 13, 28, 20, 15]]).T
df1.columns = ['ID', 'Name', ' Age ']
weight = [65, 80, 64, 69, 74, 61, 66, 61]
height = [179, 179, 151, 177, 170, 157, 151, 153]
glasses = [False, True, False, True, False, True, False, True]
df2 = pd.DataFrame([[2312, 2336, 2942, 9840, 2794, 8891, 8111, 2933], ['Anna', 'Zofia', 'Sylwia', 'Katarzyna', 'Teresa','Tomasz', 'Cezary', 'Zenon'], weight, height, glasses]).T
df2 . columns = ['ID', 'Name', 'W', 'H', 'Gl']
print(df1,"\n")
print(df2)
