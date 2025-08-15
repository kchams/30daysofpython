#Exercises: Day 24
#1. Repeat all the examples

import numpy as np

print('numpy:', np.__version__)

#Creating python List
python_list = [1,2,3,4,5]

# Checking data types
print('Type:', type (python_list)) 
print(python_list) 

two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
print(two_dimensional_list) 

# Creating Numpy(Numerical Python) array from python list
numpy_array_from_list = np.array(python_list)
print(type (numpy_array_from_list))
print(numpy_array_from_list) 

#Creating float numpy arrays
numy_array_from_list2 = np.array(python_list, dtype=float)
print(numy_array_from_list2) 

#Creating a boolean a numpy array from list
numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print(numpy_bool_array) 

#Creating multidimensional array using numpy
two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
numpy_two_dimensional_list = np.array(two_dimensional_list)
print(type (numpy_two_dimensional_list))
print(numpy_two_dimensional_list)

#Converting numpy array to list
np_to_list = numpy_array_from_list.tolist()
print(type (np_to_list))
print('one dimensional array:', np_to_list)
print('two dimensional array: ', numpy_two_dimensional_list.tolist())

#Numpy array from tuple
# Creating tuple in Python
python_tuple = (1,2,3,4,5)
print(type (python_tuple)) 
print('python_tuple: ', python_tuple) 
numpy_array_from_tuple = np.array(python_tuple)
print(type (numpy_array_from_tuple)) 
print('numpy_array_from_tuple: ', numpy_array_from_tuple) 


#Shape of numpy array
nums = np.array([1, 2, 3, 4, 5])
print(nums)
print('shape of nums: ', nums.shape)
print(numpy_two_dimensional_list)
print('shape of numpy_two_dimensional_list: ',
numpy_two_dimensional_list.shape)
three_by_four_array = np.array([[0, 1, 2, 3],
[4,5,6,7],
[8,9,10, 11]])
print(three_by_four_array.shape)


#Data type of numpy array
int_lists = [-3, -2, -1, 0, 1, 2,3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)
print(int_array)
print(int_array.dtype)
print(float_array)
print(float_array.dtype)

#Size of a numpy array
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
two_dimensional_list = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

print('The size:', numpy_array_from_list.size) 
print('The size:', two_dimensional_list.size) 

# Mathematical Operation
# Addition
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_plus_original = numpy_array_from_list + 10
print(ten_plus_original)

# Subtraction
print('original array: ', numpy_array_from_list)
ten_minus_original = numpy_array_from_list - 10
print(ten_minus_original)

#Multiplication
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list * 10
print(ten_times_original)

#Division
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list / 10
print(ten_times_original)

## Modulus; Finding the remainder
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list % 3
print(ten_times_original)

# Floor division: the division result without the remainder
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list // 10
print(ten_times_original)

# Exponential is finding some number the power of another:
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list ** 2
print(ten_times_original)

#Int, Float numbers
numpy_int_arr = np.array([1,2,3,4])
numpy_float_arr = np.array([1.1, 2.0,3.2])
numpy_bool_arr = np.array([-3, -2, 0, 1,2,3], dtype='bool')
print(numpy_int_arr.dtype)
print(numpy_float_arr.dtype)
print(numpy_bool_arr.dtype)

#Converting types
#1. Int to Float
numpy_int_float = np.array([1,2,3,4], dtype = 'float')
print(numpy_int_arr)

#2. Float to Int
numpy_int_arr = np.array([1., 2., 3., 4.], dtype = 'int')
print(numpy_int_arr)

#3. Int ot boolean
numpy_int_bool = np.array([-3, -2, 0, 1,2,3], dtype='bool')
print(numpy_int_bool)

#4. Int to str
numpy_int_str = numpy_int_float.astype('int').astype('str')
print(numpy_int_str)

#Multi-dimensional Arrays
# 2 Dimension Array
two_dimension_array = np.array([(1,2,3),(4,5,6), (7,8,9)])
print(type (two_dimension_array))
print(two_dimension_array)
print('Shape: ', two_dimension_array.shape)
print('Size:', two_dimension_array.size)
print('Data type:', two_dimension_array.dtype)

#Getting items from a numpy array
# 2 Dimension Array
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_row = two_dimension_array[0]

second_row = two_dimension_array[1]
third_row = two_dimension_array[2]
print('First row:', first_row)
print('Second row:', second_row)
print('Third row: ', third_row)

first_column= two_dimension_array[:,0]
second_column = two_dimension_array[:,1]
third_column = two_dimension_array[:,2]
print('First column:', first_column)
print('Second column:', second_column)
print('Third column: ', third_column)
print(two_dimension_array)