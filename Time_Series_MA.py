import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Parameters for MA(1) Process
np.random.seed(42)
theta = 0.5  # Coefficient for lagged error
n = 100      # Number of time steps
mu = 0       # Mean of the process
noise_std = 1

# Generate MA(1) Data
errors = np.random.normal(0, noise_std, n)  # Random noise (white noise)
Y = [mu + errors[0]]  # Initial value
print(errors)
for t in range(1, n):
    Y_t = mu + errors[t] + theta * errors[t-1]  # MA(1) equation
    Y.append(Y_t)

# Convert to DataFrame for Visualization
# df = pd.DataFrame({'Y': Y, 'Error': errors})
# df['Lagged_Error'] = df['Error'].shift(1)  # Lagged errors

# # Plot the MA(1) Process
# plt.figure(figsize=(10, 6))
# plt.plot(Y, label="MA(1) Process")
# plt.title("Moving Average Process MA(1)")
# plt.xlabel("Time Steps")
# plt.ylabel("Values")
# plt.legend()
# plt.show()
#
# # Scatter Plot: Y_t vs Lagged Errors
# plt.scatter(df['Lagged_Error'][1:], df['Y'][1:], alpha=0.7)
# plt.title("Scatter Plot: Y_t vs Lagged Error (ε_(t-1))")
# plt.xlabel("Lagged Error (ε_(t-1))")
# plt.ylabel("Y_t")
# plt.grid()
# plt.show()
#
# # Display First 10 Values
# print("First 10 Values of the MA(1) Process:")
print(df.head(10))

#[10,20,30,40,50]