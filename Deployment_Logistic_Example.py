import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd

# Train your Logistic Regression model
data={'year':[2000,2001,2003,2004,2005,2006,2007],
      'house_price':[800,9000,1000,11000,1200,10300,1400],
      'purchased':[1,0,1,0,1,0,1]}
Data=pd.DataFrame(data)
x=Data[['year','house_price']]         #independent data or featured data
y=Data['purchased']    #dependent data or target data
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)
model=LogisticRegression()
model.fit(x_train,y_train)


# Save the model
with open("logistic_regression_model_01.pkl", "wb") as obj:    #wb = write binary
    pickle.dump(model,obj)

