import pickle
from sklearn.linear_model import LinearRegression

# Train your Linear Regression model
model = LinearRegression()
X_train = [[1], [2], [3], [4]]
y_train = [2, 4, 6, 8]
model.fit(X_train, y_train)


# Save the model
with open("linear_regression_model.pkl", "wb") as obj:    #wb = write binary
    pickle.dump(model, obj)

