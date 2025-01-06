import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer

pd.set_option('Display.max_rows', None)
pd.set_option('Display.max_columns', None)
pd.set_option('Display.width',1000)

Data=pd.read_csv('../Day_15_25-Oct-24/titanic_data.csv')
print(Data.head(10))

OHE=OneHotEncoder(sparse_output=False)
One_hot_converted_column=OHE.fit_transform(Data[['Embarked']])
# print(One_hot_converted_column)

'''Give collumn names'''
Final_Data=pd.DataFrame(One_hot_converted_column,columns=OHE.get_feature_names_out(['Embarked']))
print(Final_Data.head(10))

'''Merging all the columns with coverted columns'''
actual_data=pd.concat([Data,Final_Data],axis=1).drop(columns=['Embarked'])
print(actual_data.head(10))
'''NOTE : axis=1 means it concate columnwise
          axis=0 means it concate rowwise'''
print('---------------------------------------------------------------------------------------------------------------------------------------------------------')
'''To display columns in sorted order (Alphabetic order)'''
Actual_Data=actual_data[sorted(actual_data.columns)]
print(Actual_Data.head(10))
print('---------------------------------------------------------------------------------------------------------------------------------------------------------')
'''To display columns in sorted order (Alphabetic reverse order)'''
Actual_Data=actual_data[sorted(actual_data.columns,reverse=True)]
print(Actual_Data.head(10))