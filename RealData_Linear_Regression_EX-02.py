from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
pd.set_option('Display.max_columns',None)
Data=pd.read_csv('insurance.csv')
# print(Data.shape)
print(Data.head())
print('-------------------------------------------------------------------')
# Data.info()
# Null=Data.isnull().sum()
# print(Null)
# Unique_Cate=Data['smoker'].nunique()
# print(Unique_Cate)
nunique_cate=Data[['sex','region']].value_counts()
print(nunique_cate)
Data['sex']=LabelEncoder().fit_transform(Data['sex'])
# print(Data['sex'])
pd.set_option('Display.max_rows', None)
Data['region']=LabelEncoder().fit_transform(Data['region'])
# print(Data['region'])
Column_cate=Data[['sex','region']].value_counts()
print(Column_cate)
x=Data[['age','sex','bmi','children','smoker','region']]
y=Data['charges']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=2,random_state=43)
print(x_test)
print('-------------------------------------------------------------------')
print(y_test)
LR=LinearRegression()
LR.fit(x_train,y_train)
y_prediction=LR.predict(x_test)
print(y_prediction)
accuracy_check=r2_score(y_test,y_prediction)
print(accuracy_check)
# plt.scatter(x_test,y_prediction)
# plt.plot(x_test,y_prediction)
# plt.show()
# print('-------------------------------------------------------------------')
# y_predict=LR.predict(x_train)
# print(y_predict)
# accuracy_check=r2_score(y_train,y_predict)
# print(accuracy_check)
# plt.scatter(x_train,y_predict,c='orange')
# plt.plot(x_train,y_predict)
# plt.xlabel('BMI')
# plt.ylabel('CHARGES')
# plt.title('Charges vs BMI')
# plt.show()
