import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Sample dataset with four features
data = {
    'feature1': [2.5, 0.5, 2.2, 1.9, 3.1, 2.3, 2, 1, 1.5, 1.1],
    'feature2': [2.4, 0.7, 2.9, 2.2, 3, 2.7, 1.6, 1.1, 1.6, 0.9],
    'feature3': [1.5, 2.3, 3.0, 2.7, 3.2, 3.1, 2.6, 1.8, 2.1, 1.7],
    'feature4': [2.3, 2.4, 1.7, 2.5, 2.8, 2.9, 2.5, 2.2, 1.5, 2.0]
}
Data=pd.DataFrame(data)
print('Original data')
print(Data)

# Standardization feature
Scaler=StandardScaler()
Data_scaled=Scaler.fit_transform(Data)

# Apply PCA to reduce to 2 components
pca =PCA(n_components=2)
Data_pca=pca.fit_transform(Data_scaled)

# Convert the result into a DataFrame for easier interpretation
df_pca = pd.DataFrame(Data_pca, columns=['a', 'b'])
print("\nData after PCA (2 Principal Components):")
print(Data_pca)