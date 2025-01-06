import pandas as pd
df=pd.read_csv('titanic_data.csv')
print(df.head())

print('-----------------------------------------------------------------------------')
'''Syntax for printing specific rows using slicing concept'''
row_data=df[0:4]  #it will print data from 0th row to 3rd row
print(row_data)
print('-----------------------------------------------------------------------------')
row_data=df[0:-1]  #it will print data from 0th row to entire rows (runs 0 to -1)
print(row_data)
# print('-----------------------------------------------------------------------------')
# row_data=df.loc[0:4,'Embarked']  #it will print data from 0th row to 3rd row along with Embarked column
# print(row_data)
# print('-----------------------------------------------------------------------------')
# row_data=df.loc[0:4,['Embarked','Cabin']]  #it will print data from 0th row to 3rd row along with multiple columns
# print(row_data)
# print('-----------------------------------------------------------------------------')
# row_data=df.loc[:,['Embarked','Cabin']]  #it will print data from 0th row to entire row because nothing mentioned
# print(row_data)
# print('-----------------------------------------------------------------------------')
# row_data=df.loc[0:100,['Embarked','Cabin']]  #it will print data from 0th row to 100th row along with mentioned columns
# print(row_data)
# print('-----------------------------------------------------------------------------')
# '''iloc means integer locator which means the specified column in the file which nth number of column it indicates'''
# row_data=df.iloc[0:5,0:2] #it will print data from 0th row to 5th row & 0th to 2nd column
# print(row_data)