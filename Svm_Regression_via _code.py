import  pandas as pd
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


Data = {
        'Size (sq ft)': [500,750,1000,1250,1500,1750,2000,2250],
        'Price ($)'   : [150000,200000,250000,300000,350000,400000,450000,500000],
}

df = pd.DataFrame(Data)

X = Data['Size (sq ft)']
Y = Data['Price ($)']# Convert to pandas DataFrame
df = pd.DataFrame(Data)

# Features (X) and Target (y)
X = df[["Size (sq ft)"]]
y = df["Price ($)"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features (important for SVR)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create and train the SVR model
svr = SVR(kernel="linear", C=1.0, epsilon=10000)
svr.fit(X_train_scaled, y_train)

# Make predictions
y_pred = svr.predict(X_test_scaled)

# Display actual vs. predicted prices
results = pd.DataFrame({"Actual": y_test, "Predicted": y_pred})
print(results)

support_indices = svr.support_
support_vectors = X_train.iloc[support_indices]
support_vectors_scaled = X_train_scaled[support_indices]
support_prices = y_train.iloc[support_indices]
# Visualize the results
plt.scatter(X, y, color="blue", label="Actual data")
plt.plot(X, svr.predict(scaler.transform(X)), color="red", label="SVR model")
plt.scatter(support_vectors,support_prices,color="yellow",label="support vector",zorder = 5)
plt.xlabel("Size (sq ft)")
plt.ylabel("Price ($)")
plt.title("SVR for House Prices")
plt.legend()
plt.show()

