from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as pli
from sklearn.metrics import confusion_matrix

# Create the dataset
data = {
    'Weather'    : ['Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 'Overcast',
                    'Sunny', 'Sunny', 'Rainy', 'Sunny', 'Overcast', 'Overcast', 'Rainy'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool',
                    'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'],
    'Humidity'   : ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal',
                    'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],
    'Windy'      : [False, True, False, False, False, True, True,
                    False, False, False, True, True, False, True],
    'Play'       : ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes',
                    'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
}

df = pd.DataFrame(data)

# Encode categorical features
le = LabelEncoder()
for column in ['Weather', 'Temperature', 'Humidity', 'Play']:
    df[column] = le.fit_transform(df[column])

# Define features (X) and target (y)
X = df[['Weather', 'Temperature', 'Humidity', 'Windy']]
y = df['Play']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Decision Tree Classifier
model = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42)
model.fit(X_train, y_train)

# Visualize the Decision Tree
plt.figure(figsize=(12, 8))
plot_tree(model, feature_names=X.columns, class_names=['No', 'Yes'], filled=True)
plt.show()

# Test the model
predictions = model.predict(X_test)
print("Predictions:", predictions)
print("actual:",y_test)

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

metric_confusion_matrix_output = confusion_matrix(y_test, predictions)
print(metric_confusion_matrix_output)
"""-----------------------Doing manual way to extracting output=---------------"""


print("-------------------Classification Report as Follows-------------------------")
metric_cr_output = classification_report(y_test, predictions)
print(metric_cr_output)