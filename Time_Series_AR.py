# import numpy as np
# import matplotlib.pyplot as plt
#
# # Set random seed for reproducibility
# np.random.seed(42)
#
# # Parameters for AR(1) process
# phi = 0.7  # AR coefficient (relationship strength)
# n = 100    # Number of data points
# noise_std = 1  # Standard deviation of random noise
#
# # Generate AR(1) Process
# Y = [10]  # Initial value
#
# for t in range(1, n):
#     noise = np.random.normal(0, noise_std)  # Random noise
#     Y_t = phi * Y[t-1] + noise             # AR(1) equation
#     Y.append(Y_t)
#
# # Plot the AR(1) Process
# plt.figure(figsize=(10, 6))
# plt.plot(Y, label="AR(1) Process", color="blue")
# plt.title("AutoRegressive Process AR(1) - Manual Implementation")
# plt.xlabel("Time Steps")
# plt.ylabel("Values")
# plt.legend()
# plt.show()
#
# import numpy
#
# data = numpy.random.normal(5,2, 10)
# print(data)
#
# import numpy
#
# data = numpy.random.uniform(10,20, 10)
# print(data)

