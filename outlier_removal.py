import numpy as np
import matplotlib.pyplot as plt
var=[10,20,40,-2,35,44,400,202,35]
q1=np.quantile(var,0.25)
print(q1)
q2=np.quantile(var,0.50)
print(q2)
q3=np.quantile(var,0.75)
print(q3)
IQR=q3-q1    #IQR=inter quantile range
print(IQR)
lower_range=q1-IQR*1.5
higher_range=q3+IQR*1.5
print(lower_range)
print('---------------------------------------------')
print(higher_range)
# plt.figure(figsize=(8,8))
# plt.boxplot(var)
# plt.title('FINDING OUTLIERS')
# plt.show()
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
# print(var)
# print(cleaned_data)
# print(sorted(cleaned_data))
'''Simplifier way to remove outliers using list comprehension'''
# cleaned_data=[x for x in var if not (x < lower_range or x > higher_range)]
# print(var)
# print(cleaned_data)
# print(sorted(cleaned_data))