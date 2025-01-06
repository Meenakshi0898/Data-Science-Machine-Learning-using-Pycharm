from sklearn.datasets import load_iris
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# Load iris dataset
Data=load_iris()
x = Data.data
y = Data.target

# Apply t-SNE
x_tsne = TSNE(n_components=3,random_state=42).fit_transform(x)

# Plot the result
plt.scatter(x_tsne[:,0],x_tsne[:,2],c=y,cmap='viridis',alpha=0.7)
plt.colorbar(label='Target Label')
plt.title('t_SNE Visualizaiton')
plt.xlabel('Dimention 1')
plt.ylabel('Dimention 2')
plt.show()