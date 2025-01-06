import pandas as pd
'''For print entire data in the given csv file'''
pd.set_option('display.max_rows',None)
'''To run the csv file simply '''
Data=pd.read_csv('car_data.csv')
print(Data)
print('-----------------------------------------------')
'''Alter method to run entire data of teh csv file'''
print(Data.info)
print('-----------------------------------------------')
'''To run first needed rows in the csv file'''
print(Data.head(10))
print('-----------------------------------------------')
'''For running last datas of the given csv file'''
print(Data.tail(10))
print('-----------------------------------------------')
'''Data preprocessing (Using NULL function)'''
Null_data_finding=Data.isnull().sum()
print(Null_data_finding)
print('-----------------------------------------------')
'''To know the shape of the csv file'''
File_shape=Data.shape
print(File_shape)
print('-----------------------------------------------')
'''To know entire information about the csv file'''
print(Data.info())
print('-----------------------------------------------')
'''For print column names'''
col_names=Data.columns
print(col_names)
print('-----------------------------------------------')
'''For running needed column only'''
col_based_data=Data['User ID']
print(col_based_data)
print('-----------------------------------------------')
'''For running multiple needed columns only'''
col_based_datas=Data[['User ID','Gender','Age']]
'''NOTE : double square paranthesis for multiple data command'''
print(col_based_datas)
print('-----------------------------------------------')
'''To know entire description of the csv file'''
Data_description=Data.describe()
print(Data_description)
