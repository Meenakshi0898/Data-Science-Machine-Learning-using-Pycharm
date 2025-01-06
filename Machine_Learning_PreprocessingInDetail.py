import pandas as pd
from pandas import pivot
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.impute import SimpleImputer

pd.set_option('Display.max_rows', None)
pd.set_option('Display.max_columns', None)
pd.set_option('Display.width',1000)
Data=pd.read_csv('titanic_data.csv')
# print(Data)
Data.info()
print(Data.describe())

# SS=StandardScaler()
# Data['Age']=SS.fit_transform(Data[['Age']])
# print(Data['Age'].head(20))

MMS=MinMaxScaler()
Data['Age']=MMS.fit_transform(Data[['Age']])
print(Data['Age'].head(20))

# finding_nullvalues=Data['Age'].isnull()
# print(finding_nullvalues.head(20))

# Data['Age']=Data['Age'].fillna(100)
# print(Data['Age'].head(20))
# print(Data.head(20))

# Data['Age']=Data['Age'].bfill()
# print(Data['Age'].head(10))

# Data['Age']=Data['Age'].ffill()
# print(Data['Age'].head(10))

# Data['Age']=Data['Age'].fillna(Data['Age'].mean())
# print(Data['Age'].head(20))

# SI=SimpleImputer(strategy='mean')
# Data['Age']=SI.fit_transform(Data[['Age']])
# print(Data['Age'].head(10))

# SI=SimpleImputer(strategy='median')
# Data['Age']=SI.fit_transform(Data[['Age']])
# print(Data['Age'].head(10))

# SI=SimpleImputer(strategy='most_frequent')
# Data['Age']=SI.fit_transform(Data[['Age']])
# print(Data['Age'].head(10))

# Data['Age']=Data.Age.mode()
# print(Data['Age'])

SI=SimpleImputer(strategy='constant')
Data['Age']=SI.fit_transform(Data[['Age']])
print(Data['Age'].head(10))







