'''for Decision tree classifier algorithm execution'''
from sklearn.tree import DecisionTreeClassifier
'''for generate the dataset from python'''
from sklearn.datasets import load_iris
'''for training and testing the dataset'''
from sklearn.model_selection import train_test_split
'''for evaluate the accuracy of the model'''
from sklearn.metrics import accuracy_score
Data=load_iris()
print(Data)
print('-------------------------------------------------------------------------------------------------------------------')
print(Data.target_names)
print('-------------------------------------------------------------------------------------------------------------------')
print(Data.feature_names)

x=Data.data
y=Data.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
# print(x_test)
# print(y_test)
Model=DecisionTreeClassifier()
Model.fit(x_train,y_train)
y_prediction=Model.predict(x_test)
print(y_prediction)
# y_prediction_labels=Data.target_names[y_prediction]
# print(y_prediction_labels)
y_test_labels=Data.target_names[y_test]
print(y_test_labels)
# y_train_labels=Data.target_names[y_train]
# print(y_train_labels)
accuracy_score_check=accuracy_score(y_test,y_prediction)
print(accuracy_score_check)
# from sklearn.tree import plot_tree
# import matplotlib.pyplot as plt
# plt.figure(figsize=(12,12))
# plot_tree(Model,filled=False,feature_names=Data.feature_names,class_names=Data.target_names,rounded=True)
# plt.show()