from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.datasets import load_iris

# Load the iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Define the k-NN model
knn = KNeighborsClassifier()

# Define the parameter distribution to sample from
param_dist = {'n_neighbors': [1, 3, 5, 7, 9]}

# Perform a random search over the parameter distribution
random_search = RandomizedSearchCV(knn, param_dist, n_iter=5, cv=5)
random_search.fit(X, y)

# Print the best hyperparameters and the corresponding score
print("Best hyperparameters: ", random_search.best_params_)
print("Best score: ", random_search.best_score_)
