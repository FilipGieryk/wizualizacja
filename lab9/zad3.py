import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_excel('imiona.xlsx')
df['Rok'] = pd.to_datetime(df.Rok, format='%Y')
df.set_index('Rok').last('5D')
print(df)
# grupa = df.groupby(['Plec']).agg({'Liczba':['sum']})

# wykres = grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6, 6))

# plt.title('Liczba urodzen w ostanich 5 latach')
# print(wykres)
# plt.show()