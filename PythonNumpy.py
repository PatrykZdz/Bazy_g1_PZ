import numpy as np

#Cwiczenie 1
tab = np.array([10,12,14,16,18,20,22,24,26,28,30,32,34,36,38])
print("shape =",tab.shape)
print(tab.reshape(3,5))
print(tab+3)
print(tab*2)
for x in range(len(tab)):
    if(tab[x]%6==2):
        tab[x]= 0
print(tab)

def change(A,x):
  tab2 = A.copy()
  tab2[tab2==0]=x
  return tab2

macierz = np.array([1,2,3,0,0,3,5,6])
print(macierz)
tab2 = change(macierz,2)
print(tab2)

#Cwiczenie 2

A = np.array([[1,1,2],[2,1,0],[4,1,2]])
print(A.reshape(3,3))
print("")
B = np.array([[2,5,7],[2,8,0],[4,3,1]])
print(B.reshape(3,3))
print("")
print(A.reshape(3,3)+B.reshape(3,3))
print("")
iloczyn = np.dot(A,B)
print(iloczyn)
print("")
print(A.reshape(3,3)*B.reshape(3,3))
print("")
print(np.transpose(A))
print("")

print("")
print(np.power(A,5))
print("")
print(np.linalg.matrix_power(A,5))
print("")
print(np.linalg.det(B))




