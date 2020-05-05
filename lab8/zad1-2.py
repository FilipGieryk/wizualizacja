import pandas as pd
import numpy as np
import xlrd
import openpyxl
df=pd.read_excel('imiona.xlsx', sheet_name='Arkusz1')
#zadanie 1^
#   print(df[(df['Liczba'] > 1000)])
#zadabie 2.1^
#   print(df[df.Imie.str.match('Filip',case=True)])
#zadanie 2.2^
#   suma= df['Liczba'].sum()
#   print(suma)
#zadanie 2.3^
# lata = df[df['Rok']<2006]
#   print(lata['Liczba'].sum())
#zadanie 2.4^
chlopcy = df[df['Plec']== "M"]
dziewczyny = df[df['Plec']== "K"]
#   print('liczba chlopakow:\n',chlopcy['Liczba'].sum())
#   print('liczba dziewczyn:\n',dziewczyny['Liczba'].sum())
#zadanie 2.5^

#   df1 = df[['Imie','Plec','Liczba']]
#   grupa = df1.groupby(['Plec','Imie']).max()
#   posortowane = grupa.sort_values('Liczba',ascending=False)
#   print(posortowane.head(2))
#zadanie 2.7^

#zadanie 2.6
# df1 = chlopcy.groupby(['Rok','Imie']).max().sort_values(['Rok','Liczba'],ascending=[True,False]).head(17)
# print(df1)
print (chlopcy.groupby('Rok').max()['Liczba'])