import pandas as pd

data = pd.read_csv('Electric_Production.csv')
print(data.head())
print(data.info())

data = pd.read_csv('Electric_Production.csv',date_format=['Date'])
print(data.head())
print(data.info())

data.set_index('DATE',inplace=True)
print(data.head())

print(type(data.index))
#
# monthly_data= data.resample('M').mean()
# print(monthly_data)