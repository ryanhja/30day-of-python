# Day 24: 30 Days of python programming

import numpy as np

# Python list
numbers = [21, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(numbers), ": ", numbers)

multi_dimensional_numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(type(multi_dimensional_numbers), ": ", multi_dimensional_numbers)

# Numpy Array
array_numbers = np.array(numbers)
print(type(array_numbers), ": ", array_numbers)

numpy_multi_dimensional = np.array(multi_dimensional_numbers)
print(type(numpy_multi_dimensional), ": ", numpy_multi_dimensional)

# Numpy Data type
arrays_float = np.array(numbers, dtype=float)
print(type(arrays_float), ": ", arrays_float)

# To list
numpy_to_list = numpy_multi_dimensional.tolist()
print(numpy_to_list)

# Length
print(len(numpy_multi_dimensional))

# Shape
print(numpy_multi_dimensional.shape)

# Size
print(numpy_multi_dimensional.size)

# Operational
print(array_numbers + 10)
print(array_numbers - 10)
print(array_numbers * 10)
print(array_numbers / 10)
print(array_numbers % 10)

#
