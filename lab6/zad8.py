import numpy as np
def tablice(x,y,kierunek):
    z=x*y
    a=np.arange(z).reshape(x,y)
    if(kierunek=="pionowo"):
        if(y%2==0):
            return np.hsplit(a,y/2)
        else:
            return "liczba kolumn musi byc parzysta"
    if(kierunek=="poziomo"):
        if(x%2==0):
            return np.vsplit(a,x/2)
        else:
            return "liczba wierszy musi byc parzysta"
print(tablice(4,5,"poziomo"))