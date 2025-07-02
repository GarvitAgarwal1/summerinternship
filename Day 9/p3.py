import numpy as np

print("Reversing an array")

arr_to_reverse = np.array([100, 200, 300, 400])
reversed_arr = arr_to_reverse[::-1]
print("Original array:", arr_to_reverse)
print("Reversed array:", reversed_arr)