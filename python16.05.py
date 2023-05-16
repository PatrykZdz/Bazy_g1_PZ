import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.genfromtxt('jajka2023.csv', delimiter=";", dtype='|U16', encoding='UTF-8')
data0=np.char.replace(data,',','.')
price=data0[1::,1::]
print(price)
a=price[price !='']
print(a.astype(float))
print(np.mean(a.astype(float)))
minimum=min(a.astype(float)).astype(str)
maximum=max(a.astype(float)).astype(str)
cities=data0[0,]
print(cities)
supermarkets=data0[:,0]
wh=np.where(price==minimum)
print(wh)
print("wh0: ",wh[0])
print("wh1: ",wh[1])
answ_min=np.array([cities[wh[1]+1],supermarkets[wh[0]+1]])
print(answ_min.transpose())
answ_max=np.array([cities[np.where(price==maximum)[0]+1]])
print(answ_max.transpose())


data = pd.read_csv ('jajka2023.csv', sep=';', index_col=0, encoding='UTF=8')
data2 = data.stack( )
data3 = data2.str.replace(',', '.').astype('float')
srednia = data3.mean ( )
minCena = data3.min( )
maxCena = data3.max( )
print(data3[data3 == minCena])
print(data3[data3 == maxCena])

data4 = data3.unstack()
print(data4)
data4.plot(kind='box',rot=60)
data4.transpose().plot(kind='box',rot=60)
plt.show


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv ('penguins.csv', sep=',', index_col=False, encoding='UTF=8')
data=data.dropna()
print(data)
print(data.groupby('island').size())
data.groupby('island').size().plot.bar()
plt.show()

print(data.groupby('sex')["body_mass_g"].mean())
print(data.groupby('body_mass_g').min())
print(data.groupby('body_mass_g').max())
print(data.groupby('species')['island'].count())

print(data.groupby('species')['island'].count('Adelie'))


