import numpy as np 

wektor = np.arange(12)
a=wektor.reshape(3,4)
b=wektor.reshape(4,3)
c=wektor.reshape(2,6)
for a in a.flat:
    print(a)
for b in b.flat:
    print(b)
for c in c.flat:
    print(c)