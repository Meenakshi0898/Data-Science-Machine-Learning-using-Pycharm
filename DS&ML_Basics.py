'''To know which datatype it has (String or object)'''

# Name='Meena'
# print(Name)
# print(type(Name))
'''To know which datatype it has (list)'''
# my_parents=['Rajamanikcam','Lakshmi']
# print(my_parents)
# print(type(my_parents))
'''To know the datatype of specified column in the given csv file'''
import pandas as pd
Data=pd.read_csv('car_data.csv')
#  print(Data)
# column_data=Data['User ID']
# print(column_data)
# print(column_data.dtypes)
'''Dict type'''
# my_data={'name':'meenakshi','Husband':'vignesh'}
# print(my_data)
# print(type(my_data))
'''Filling null value in given csv file'''
'''First know how many null values in the entire cv file data'''
# null_data_total_count=Data.isnull().sum().sum()
# print(null_data_total_count)
'''Now filling the null value using fillna() function'''
# Data.fillna(489.32,inplace=True)
# print(Data)
'''Filling null valuse using neibourhood value'''
'''ffill() fucntion is autofill the forward data of null data'''
# Data.ffill(inplace=True)
# print(Data)
'''bfill() function is autofill the backward data of null data'''
# Data.bfill(inplace=True)
# print(Data)
'''Filling another colummn data mean(Average value of the column in the null value using mean() function'''
# Data.fillna({'User ID':Data['AnnualSalary'].mean()},inplace=True)
# print(Data)
'''Filling same colummn data mean value(Average value) of the column in the null value using mean() function'''
# Data.fillna({'User ID':Data['User ID'].mean()},inplace=True)
# print(Data)
'''Filling null valus using SKlearn library'''
# from sklearn.impute import SimpleImputer
# simple_imputing_object=SimpleImputer(strategy='mean')
# Data['User ID']=simple_imputing_object.fit_transform(Data[['User ID']])
# print(Data)


