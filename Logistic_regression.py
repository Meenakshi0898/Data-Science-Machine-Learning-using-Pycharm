'''Logistic regression:-
        This regression is only gives output in between boolean type like 'yes' or 'no', 'True' or 'False'
(i.e) x-axis        - year     :2000,2001,2002,2003,2004,2005,2006,2007
                      price    :10000,20000,30000,40000,50000,60000,70000
      y-axis(Target)- purchased:1,0,1,0,1,0,1,0
      
   * Here,we find the logistic regression with the 2 objects of x-axis and y-axis that should between binary values

Another regression is classification regression like:-
        > Decision tree
        > Random forest
        > SVM'''

'''for logistic regression execution'''
from sklearn.linear_model import LogisticRegression
'''for training and testing my dataset'''
from sklearn.model_selection import train_test_split
'''for evaluating working and accuracy of my model'''
from sklearn.metrics import accuracy_score
import pandas as pd
Data={'year':[2000,2001,2003,2004,2005,2006,2007],
      'house_price':[800,9000,1000,11000,1200,10300,1400],
      'purchased':[1,0,1,0,1,0,1]}
df=pd.DataFrame(Data)
print(df)
x=df[['year','house_price']]
y=df['purchased']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=2,random_state=42)
print(x_test)
print(y_test)
Model=LogisticRegression()
Model.fit(x_train,y_train)
y_prediction=Model.predict(x_test)
print(y_prediction)
accuracy_check=accuracy_score(y_test,y_prediction)
print(accuracy_check)