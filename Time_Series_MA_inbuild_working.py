import numpy as np

theta = 10
noise_std = 1
n=100
mu=0
errors = np.random.normal(0, noise_std, n)  # Random noise (white noise)
Y = [mu + errors[0]]  # Initial value
for t in range(1,10):
    Y_t = mu + errors[t] + theta * errors[t - 1]  # MA(1) equation
    Y.append(Y_t)
print(Y)
# print(Y_t)