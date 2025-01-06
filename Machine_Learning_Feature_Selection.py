import pandas as pd
import numpy as np

Data={
    'A' : [2,-4,6,8,10],
    'B' : [5,4,3,2,1],
    'C' : [12,4,18,6,47],
    'Target' : [1,3,5,7,9]
}

Data=pd.DataFrame(Data)
print(Data)
print('---------------------------------------------------------')
correlation_threshold=0.8
corr_matrix=Data.corr()
print(corr_matrix)
print('---------------------------------------------------------')
target_correlation=corr_matrix['Target'].drop('Target')
print(target_correlation)
print('---------------------------------------------------------')
selection_feature=target_correlation[abs(target_correlation) > correlation_threshold].index.tolist()
print(selection_feature)
