import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df = pd.read_excel('imiona.xlsx')
df = df.groupby(['Rok','Plec']).sum()['Liczba'].unstack()


print(df)
df.plot.bar(stacked = True)
plt.ylabel('Liczba')
plt.xlabel('Rok')
plt.title('M vs K')
plt.show()