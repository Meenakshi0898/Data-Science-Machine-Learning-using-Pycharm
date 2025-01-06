import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


candy = pd.read_csv('candy_production.csv',
            index_col='date',
            parse_dates=True)
print(candy)
print(candy.info())

# # change the plot style into fivethirtyeight
plt.style.use('dark_background')

# # Plot and show the time series on axis ax1
fig, ax1 = plt.subplots()
candy.plot(ax=ax1, figsize=(12,10))
plt.title('Monthly production of candy in US')
plt.xlabel('Date')
plt.ylabel('Production')
plt.show()

"""----------------------"""

candy_train = candy.loc[:'2006']
candy_test = candy.loc['2007':]

# # Create an axis
fig, ax = plt.subplots()

# Plot the train and test sets on the axis ax
candy_train.plot(ax=ax, figsize=(12,10))
candy_test.plot(ax=ax)
plt.title('train - test split of the monthly production of candy in US')
plt.xlabel('Date')
plt.ylabel('Production')
plt.show()



