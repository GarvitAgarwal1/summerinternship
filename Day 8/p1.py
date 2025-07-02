import numpy as np

random_array = np.random.rand(4, 2)
print("Random 4x2 array:\n", random_array)

empty_array = np.empty((4, 2))
print("\nEmpty 4x2 array:\n", empty_array)

zeros_array = np.zeros((3, 5))
print("\n3x5 array of zeros:\n", zeros_array)

ones_array = np.ones((4, 3, 2))
print("\n4x3x2 array of ones:\n", ones_array)