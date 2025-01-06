import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
Data=pd.read_csv('weatherAUS.csv')
# print(Data.head())
# print(Data.info)
# Data_shape=Data.shape
# print(Data_shape)
# print(Data.info())
# print(Data.dtypes)
# Finding_null=Data.isnull().sum()
# print(Finding_null)
# column_calling=Data['Rainfall']
# print(column_calling)
# column_names=Data.columns
# print(column_names)
'''To drop or remove any column in the Csv file'''
# Data.drop(['Evaporation'],axis=1,inplace=True)
# print(Data.head())
# column_names=Data.columns
# print(column_names)
'''To view categorical data which means 'O' represents Object or string,name form otherwise numbers'''
categorical=[var for var in Data.columns if Data[var].dtype=='O']
print(categorical)
'''Checking null data in the finded categorical data'''
cat1=[var for var in categorical if Data[var].isnull().sum()!=0]
print(Data[cat1].isnull().sum())
