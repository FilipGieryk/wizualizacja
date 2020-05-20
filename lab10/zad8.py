import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random



wartosci = []
def rzucaj (n):
    for x in range(n):
        wartosci.append(random.choice(range(1,13)))
    plt.hist(wartosci,bins=12,edgecolor='black')
    plt.xlabel('liczba oczek')
    plt.ylabel('ilosc wypadnietych razy')
    plt.show()
rzucaj (200)
  
