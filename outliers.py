'''Outliers means the un-uniform range in the given data which is less value or bigger value of the data range '''
'''EDA means Exploratory data analysis which means the data pattern,data organisation and data distribution via some graph using either matplotib and seaborn'''
'''Finding outliers using boxplot() function'''
# import pandas as pd
import matplotlib.pyplot as plt
# var=[10,20,30,-2,50,100,202,60]
# x=pd.DataFrame({'score':var})
# print(x)
# plt.boxplot(x['score'])
# plt.show()
# plt.figure(figsize=(8,8))
# plt.boxplot(x['score'])
# plt.title('Finding Outliers')
# plt.grid(True)
# plt.show()
'''outlier deduction is always finds first 25% of the data then 50% of the data then 75% of the data like it increases quantile of data'''
import numpy as np
var=[10,20,40,-2,35,44,400,202,35]
q1=np.quantile(var,0.25)
print(q1)
q2=np.quantile(var,0.50)
print(q2)
q3=np.quantile(var,0.75)
print(q3)
IQR=q3-q1
'''IQR=inter quantile range'''
print(IQR)
lower_range=q1-IQR*1.5
higher_range=q3+IQR*1.5
print(lower_range)
print(higher_range)
plt.figure(figsize=(8,8))
plt.boxplot(var)
plt.title('FINDING OUTLIERS')
plt.show()
'''Outliers removal'''
# cleaned_data=[]
# for x in var:
#     if x<lower_range:
#         pass
#     elif x>higher_range:
#         pass
#     else:
#         cleaned_data.append(x)
#
#         print(var)
#         print(cleaned_data)
'''Simplifier way to remove outliers'''
# cleaned_data=[]
# for x in var:
#     if not(x<lower_range or x>higher_range):
#         cleaned_data.append(x)
#         print(var)
#         print(cleaned_data)
#         print(sorted(cleaned_data))
'''Simplifier way to remove outliers using list comprehension previews'''



