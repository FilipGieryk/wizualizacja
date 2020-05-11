import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('zamowienia.csv', delimiter=';')
ilosc = (df.groupby(['Sprzedawca']).size())
wykres = ilosc.plot.bar()
wykres.set_ylabel('ilosc')
wykres.set_xlabel('sprzedawca')
wykres.legend(['Liczba zamowien'])
plt.title('ilosc zamowien sprzedawcow')
plt.show()