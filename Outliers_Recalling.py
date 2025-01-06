import numpy as np
import matplotlib.pyplot as plt

var = [4,6,9,20,50,-100,7,44,23,1000,56,2,6,8]
q1 = np.quantile(var,0.25)
q3 = np.quantile(var,0.75)
IQR = q3-q1
lower_range = q1-1.5*IQR
higher_range = q3+1.5*IQR
print(lower_range)
print(higher_range)

original_data = []

for x in var:
    if x < lower_range:
        pass
    elif x > higher_range:
        pass
    else :
        original_data.append(x)

print(var)
print(original_data)




