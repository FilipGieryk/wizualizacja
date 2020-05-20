import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_excel('imiona.xlsx')
df1 = df.groupby(['Plec'])['Liczba'].sum()
df2 = df.groupby(['Rok','Plec']).sum()['Liczba'].unstack()
df3 = df.groupby(['Rok']).sum()['Liczba']


plt.subplot(131)
df1.plot.bar(color = 'r')
plt.ylabel('ilosc narodzin w mln')
plt.xlabel('Plec')
plt.title('narodziny')

plt.subplot(132)

plt.plot(df2)
plt.ylabel('Liczba')
plt.xlabel('Rok')
plt.title('M vs K')

plt.subplot(133)
print(df3)
df3.plot.bar(color = 'g')

plt.tight_layout()
plt.show()