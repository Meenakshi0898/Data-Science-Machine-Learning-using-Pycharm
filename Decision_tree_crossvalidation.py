'''for Decision tree classifier algorithm execution'''
from sklearn.tree import DecisionTreeClassifier
'''for generate the dataset from python'''
from sklearn.datasets import load_iris
'''for training and testing the dataset'''
from sklearn.model_selection import cross_val_predict, cross_val_score

'''for evaluate the accuracy of the model'''
from sklearn.metrics import accuracy_score
Data=load_iris()
# print(Data)
x=Data.data
y=Data.target
# print(x)
# print(y)
# print(Data.target_names)
Model=DecisionTreeClassifier()
'''perform cross+ validation prediction'''
y_predict=cross_val_predict(Model,x,y,cv=5)
# print(y_predict)
# '''convert predicted and actual values to class names'''
y_predict_labels=Data.target_names[y_predict]
print(y_predict_labels)
print('------------------------------------------------------------------------------')
y_test_labels=Data.target_names[y]
print(y_test_labels)
'''print the comparison of actual and predicted values'''
for actual,predicted in zip(y_test_labels,y_predict_labels):
     print(f'Actual:{actual},predicted:{predicted}')
'''calculate accuracy using cross_validation'''
accuracy_score=cross_val_score(Model,x,y,cv=5,scoring='accuracy')
average_accuracy=accuracy_score.mean()
print(f'\n Average Accuracy across 5_fold cross_validation:{average_accuracy*100:3f}%')