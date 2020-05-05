import pandas as pd
import xlrd
import openpyxl
import datetime as dt
df = pd.read_csv('zamowienia.csv',delimiter=';')
#   print(df.Sprzedawca.unique())
#zadanie 3.1^

#   print(df.sort_values(by='Utarg', ascending=False).head(5))
#zadanie 3.2^

#   print(df.groupby(['Sprzedawca']).size())
#zadanie 3.3^

#   print(df.groupby(['Kraj']).size())
#zadanie 3.4^

# df['Data zamowienia'] = pd.to_datetime(df['Data zamowienia'])
# start_date = '01-01-2005'
# end_date = '31-12-2005'
# mask = (df['Data zamowienia'] >= start_date) & (df['Data zamowienia'] <= end_date)
# rok = df.loc[mask]
# final = rok.loc[rok['Kraj'] == 'Polska']
# print(final.groupby(['Kraj']).size())
#zadanie 3.5^

# df['Data zamowienia'] = pd.to_datetime(df['Data zamowienia'])
# start_date = '01-01-2004'
# end_date = '31-12-2004'
# mask = (df['Data zamowienia'] >= start_date) & (df['Data zamowienia'] <= end_date)
# rok = df.loc[mask]
# print (rok.mean(axis = 0))
#zadanie 3.6^


# df['Data zamowienia'] = pd.to_datetime(df['Data zamowienia'])
# start_date1 = '01-01-2004'
# end_date1 = '31-12-2004'
# start_date2 = '01-01-2005'
# end_date2 = '31-12-2005'
# mask = (df['Data zamowienia'] >= start_date1) & (df['Data zamowienia'] <= end_date1)
# mask2 = (df['Data zamowienia'] >= start_date2) & (df['Data zamowienia'] <= end_date2)
# rok2004 = df.loc[mask]
# rok2005 = df.loc[mask2]
# rok2004.to_csv (r'C:\Users\Midget\Desktop\zamowienia_2004.csv')
# rok2005.to_csv (r'C:\Users\Midget\Desktop\zamowienia_2005.csv')
#zadanie 3.7^
