import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_excel('imiona.xlsx')

grupa = df.groupby(['Plec']).agg({'Liczba':['sum']})
print(grupa)
wykres = grupa.plot.bar()
wykres.set_ylabel('Mln')
wykres.set_xlabel('Plec')
wykres.legend()
plt.title('Liczba urodzen z podzialem na plec')
plt.show()