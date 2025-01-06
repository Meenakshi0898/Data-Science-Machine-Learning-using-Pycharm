import numpy
c = 5 #constant value added manually to get increasing value according to the data
phi = 0.7
noise_std = 1
y = [100]
for t in range(1,10):
    noise = numpy.random.normal(0, noise_std)
    # print(noise)
    data = c + phi * y[t-1] + noise
    y.append(data)
print(y)

print("-----------------------------------------------------")
c = 5 #constant value added manually to get increasing value according to the data
phi = 0.7
noise_std = 1
y = [100,90]
for t in range(1,10):
    noise = numpy.random.normal(0, noise_std)
    # print(noise)
    data = c + phi * y[t-1] + noise
    y.append(data)
print(y)