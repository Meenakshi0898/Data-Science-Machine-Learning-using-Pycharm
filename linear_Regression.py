'''for executing Linear regression algorithm'''
from sklearn.linear_model import LinearRegression
'''for training and testing my dataset'''
from sklearn.model_selection import train_test_split
'''for evaluating my model woring and accuracy'''
from sklearn.metrics import r2_score, accuracy_score
import matplotlib.pyplot as plt
import pandas as pd
'''Find linear regression with manual data'''
data={'year':[2000,2001,2002,2003,2004,2005,2006],
      'house_price':[800,900,1000,1100,1200,1300,1400]}
'''for working of linear regression the given dataset must be in dataframe model so have to convert it first as dataframe'''
Data=pd.DataFrame(data)
print(Data)
x=Data[['year']]         #independent data or featured data
y=Data['house_price']    #dependent data or target data
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)
'''now testing'''
print(x_test,y_test)
'''implementing linear regression'''
model=LinearRegression()
model.fit(x_train,y_train)
y_prediction=model.predict(x_test)
print(y_prediction)
'''for accuracy checking'''
# check_accuracy=r2_score(y_test,y_prediction)
# print(check_accuracy)
# # '''for manually mentioning year that i want to check accuracy'''
# y_prediction=model.predict(pd.DataFrame({'year':['2010','2011','2012']}))
# print(y_prediction)
# accuracy_check=r2_score(y_test,y_prediction)
# print(accuracy_check)
# plt.scatter(x_train,y_train)
# plt.plot(x_train,y_train)
# plt.show()
