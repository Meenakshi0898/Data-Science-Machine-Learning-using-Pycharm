import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd

# Train your Linear Regression model
data={'year':[2000,2001,2002,2003,2004,2005,2006],
      'house_price':[800,900,1000,1100,1200,1300,1400]}

Data=pd.DataFrame(data)
x=Data[['year']]         #independent data or featured data
y=Data['house_price']    #dependent data or target data
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)
model=LinearRegression()
model.fit(x_train,y_train)


# Save the model
with open("linear_regression_model_01.pkl", "wb") as obj:    #wb = write binary
    pickle.dump(model,obj)

