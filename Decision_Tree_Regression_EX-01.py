from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,accuracy_score
import pandas as pd
pd.set_option('display.max_columns',None)
Data = pd.read_csv('petrol_consumption.csv')
# print(Data.shape)
Data.info()
print(Data)
print('------------------------------------------------')
x=Data[['Petrol_Consumption','Average_income']]
y=Data['Petrol_tax']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=2,random_state=43)
print(x_test)
print('------------------------------------------------')
print(y_test)
print('------------------------------------------------')
DTR=DecisionTreeRegressor()
DTR.fit(x_train,y_train)
# print(x_train)
# print('------------------------------------------------')
# print(y_train)
# print('------------------------------------------------')
y_prediction=DTR.predict(x_test)
print(y_prediction)
# accuracy_check= accuracy_score(y_test,y_prediction)
# print(accuracy_check)