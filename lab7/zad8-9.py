import numpy as np

macierz = np.arange (4,13).reshape(3,3)

for a in macierz:
    print(a)
for b in macierz.flat:
    print(b)