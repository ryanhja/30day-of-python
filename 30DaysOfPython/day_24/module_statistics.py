# Day 24: 30 Days of python programming

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Python list
numbers = [21, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(numbers), ": ", numbers)

multi_dimensional_numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(type(multi_dimensional_numbers), ": ", multi_dimensional_numbers)

# Numpy Array
print("\nNumpy Array")
array_numbers = np.array(numbers)
print(type(array_numbers), ": ", array_numbers)

numpy_multi_dimensional = np.array(multi_dimensional_numbers)
print(type(numpy_multi_dimensional), ": ", numpy_multi_dimensional)

# Convert data type
print("\nConvert data type")
arrays_float = np.array(numbers, dtype=float)
print(type(arrays_float), ": ", arrays_float)

# To list
print("\nConvert to Python List")
numpy_to_list = numpy_multi_dimensional.tolist()
print(numpy_to_list)

# Length
print("\nLength")
print(len(numpy_multi_dimensional))

# Shape
print("\nShape")
print(numpy_multi_dimensional.shape)

# Size
print("\nSizing")
print(numpy_multi_dimensional.size)

# Operational
print("\nOperational")
print(array_numbers + 10)
print(array_numbers - 10)
print(array_numbers * 10)
print(array_numbers / 10)
print(array_numbers % 10)

# Numpy data type
print("\nData Type")
print(array_numbers.dtype)
print(arrays_float.dtype)

# Get items
print("\nGet Items")
first_row = numpy_multi_dimensional[0]
second_row = numpy_multi_dimensional[1]
third_row = numpy_multi_dimensional[2]

print(first_row)
print(second_row)
print(third_row)

# Slicing
print("\nSlicing")
first_two_row = numpy_multi_dimensional[0:2, 0:3]
print(first_two_row)

# Reverse data
print("\nReverse array")
print(numpy_multi_dimensional[::-1, ::-1])

# Numpy Zeroes
print("\nNumpy Zeroes")
numpy_zeros = np.zeros((3, 4), dtype=int)
print(numpy_zeros)

# Numpy Ones
print("\nNumpy Ones")
numpy_ones = np.ones((3, 4), dtype=int)
print(numpy_ones)

# Numpy Twos
print("\nNumpy Twos")
numpy_twos = numpy_ones * 2
print(numpy_twos)

# Reshape
print("\nReshape")
reshape_numpy_ones = numpy_ones.reshape(4, 3)
print(reshape_numpy_ones)

# Numpy Random
print("\nRandom")
numpy_random_int = np.random.randint(5, 50, size=(5, 5))
print(numpy_random_int)

print("\n")
numpy_random_normal = np.random.normal(79, 5, 50)
print(numpy_random_normal)

# Seaborn
print("\nSeaborn")
sns.set()
plt.hist(numpy_random_normal, color="grey", bins=50)


four_by_four_matrix = np.matrix(np.ones((4,4), dtype=float))
print(four_by_four_matrix)

lst = range(0, 11, 2)
print(list)