import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_excel('imiona.xlsx')
wykres = pd.pivot_table(df, index=['Rok'], aggfunc='sum', values='Liczba')
wykres.plot(subplots=False, use_index=True)
print(wykres)
plt.show()