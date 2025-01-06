import pandas as pd
from sklearn.feature_selection import chi2
from sklearn.feature_selection import SelectKBest

Data = {
    'feature1':[0,1,1,0,1],
    'feature2':[1,0,1,0,0],
    'feature3':[1,1,0,0,1],
    'target'  :[0,1,1,0,1]
}
Data=pd.DataFrame(Data)

'''Seperate feature and target'''
X=Data[['feature1','feature2','feature3']]
Y=Data['target']

'''Apply chi-Squared teat'''
chi2_selector=SelectKBest(score_func=chi2,k=2)  # k is the number of top feature to select
X_kbest = chi2_selector.fit_transform(X,Y)

'''Get selected feature names'''
selected_features=X.columns[chi2_selector.get_support()]

'''Display Result'''
print('Chi=Squared scores for each feature')
for feature,score in zip(X.columns,chi2_selector.scores_):
    print(f'{feature}:{score}')

print('\nSelected features based on Chi_Squared Test:')
print(selected_features.tolist())