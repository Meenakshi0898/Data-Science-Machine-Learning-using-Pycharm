import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Generate sample data
np.random.seed(0)
data = np.random.rand(100, 4) * 10

df = pd.DataFrame(data, columns=['Feature1', 'Feature2', 'Feature3', 'Feature4'])
print(df)
# Step 1: Standardize the data
scaler = StandardScaler()
standardized_data = scaler.fit_transform(df)
print(standardized_data)
print("-----------------------------------------------")
# # Step 2: Compute covariance matrix
cov_matrix = np.cov(standardized_data.T)
print((cov_matrix))
print("-----------------------------------------------")
'''To kow details for cov'''
cov_matrix_with_details = pd.DataFrame(cov_matrix, index=df.columns, columns=df.columns)
print(cov_matrix_with_details)
print("-----------------------------------------------")
# Step 3: Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
print(eigenvalues,eigenvectors)
print("-----------------------------------------------")
# Step 4: Sort and select top 2 components
eigen_pairs = [(np.abs(eigenvalues[i]), eigenvectors[:, i]) for i in range(len(eigenvalues))]
eigen_pairs.sort(key=lambda x: x[0], reverse=True)
top_2_components = np.array([eigen_pairs[i][1] for i in range(2)])
print((top_2_components))
print("-----------------------------------------------")
# Step 5: Transform data
transformed_data = standardized_data.dot(top_2_components.T)
transformed_df = pd.DataFrame(transformed_data, columns=['Principal Component 1', 'Principal Component 2'])
print(transformed_df)
print("-----------------------------------------------")
# Output results
print('OVERALL INPUT STEPS : \n')
print("Original Data:\n", df.head())
print("-----------------------------------------------")
print("\nStandardized Data:\n", standardized_data[:5])
print("-----------------------------------------------")
print("\nCovariance Matrix:\n", cov_matrix)
print("-----------------------------------------------")
print("\nEigenvalues:\n", eigenvalues)
print("-----------------------------------------------")
print("\nEigenvectors:\n", eigenvectors)
print("-----------------------------------------------")
print("\nTop 2 Principal Components:\n", top_2_components)
print("-----------------------------------------------")
print("\nTransformed Data:\n", transformed_df.head())