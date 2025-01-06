'''To standardise the selected column using StandardScaler() function'''
from itertools import count

import pandas as pd
Data=pd.read_csv('car_data.csv')

column_data=Data['AnnualSalary']
print(column_data.head())

from sklearn.preprocessing import StandardScaler
Data=pd.read_csv('car_data.csv')

Standard_data=StandardScaler()
Data['AnnualSalary']=Standard_data.fit_transform(Data[['AnnualSalary']])
print(Data['AnnualSalary'].head())

'''How to know the standard deviation and mean(Average) manually'''
# var=[30,34,56,12,78,90,19,200]
# my_data=pd.Series(var)
# print(my_data)
# std_deviation=my_data.std()
# print(std_deviation)
# mean=my_data.mean()
# print(mean)
# count=my_data.count()
# print(count)
# std=Data[['AnnualSalary']].std()
# print(std)
# mean=Data[['AnnualSalary']].mean()
# print(mean)
# std=my_data[0:4].std()
# print(std)
# std=Data[['AnnualSalary']].std()
# print(std)
