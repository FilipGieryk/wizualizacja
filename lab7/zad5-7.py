import numpy as np

macierz = np.arange(6).reshape(2,3)
a = np.sin(macierz)
print("zadanie 5\n",a)

macierz = np.arange(6).reshape(2,3)
b= np.cos(macierz)
print ("zadanie 6\n", b)

print("zadanie 7\n",np.add(a,b))
print(a+b)