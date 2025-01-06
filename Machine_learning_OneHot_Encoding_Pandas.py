import pandas as pd

pd.set_option('Display.max_rows', None)
pd.set_option('Display.max_columns', None)
pd.set_option('Display.width',1000)

Data=pd.read_csv('titanic_data.csv')
print(Data.head(10))

OHEP=pd.get_dummies(Data['Embarked'],prefix='Embarked')
Final_Data=pd.concat([Data,OHEP],axis=1).drop(columns=['Embarked'])
print(Final_Data.head(10))