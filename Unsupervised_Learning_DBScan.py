import  pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

np.random.seed(42)

cluster_1 = np.random.normal([2,2,],0.2,size=(100,2))
print(cluster_1)
print("-------------------------------------")
cluster_2 = np.random.normal([7,7,],0.2,size=(100,2))
print(cluster_2)
print("-------------------------------------")
cluster_3 = np.random.normal([9],0.2,size=(100,2))
print(cluster_3)
print("-------------------------------------")
noise = np.random.uniform(0,15,(15,2))
print(noise)
print("-------------------------------------")
data = np.vstack([cluster_1,cluster_2,cluster_3,noise])
df = pd.DataFrame(data,columns=['c1','c2'])
print(df)
print("-------------------------------------")
dbscan = DBSCAN(eps=0.5,min_samples=3)
df['cluster']=dbscan.fit_predict(df[['c1','c2']])
print(df)
print("-------------------------------------")
plt.figure(figure=(10,8))
plt.scatter(df['c1'],df['c2'],c=df['cluster'],cmap='viridis',marker='o',s=50,edgecolor='k')
plt.title('DBScan')
plt.xlabel('X Data')
plt.ylabel('Y Data')
plt.colorbar(label='Cluster Label')
plt.show()