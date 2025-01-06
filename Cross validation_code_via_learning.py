from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score

# load the iris dataset
data=load_iris()
X = data.data
Y = data.target

# Define the model
model = DecisionTreeClassifier(random_state=42)

# Perform 5 fold cross validation
cv_score=cross_val_score(model,X,Y,cv=5)
print('cross_validation_score:',cv_score)
print('Mean cross_validation_score:',cv_score.mean())

'''Cross validation will not be help us in the selection of best parameter or best combination of input dats
 rather,it will just highlight the efficiency of dataset or balance of the dataset'''