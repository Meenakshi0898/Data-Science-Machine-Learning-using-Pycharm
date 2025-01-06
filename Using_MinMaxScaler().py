import pandas as pd
Data=pd.read_csv('car_data.csv')
column_data=Data['AnnualSalary']
print(column_data.head())
from sklearn.preprocessing import MinMaxScaler
min_max_object=MinMaxScaler()
Data['AnnualSalary']=min_max_object.fit_transform(Data[['AnnualSalary']])
print(Data['AnnualSalary'].head())