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

#Slicing Numpy array
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_two_rows_and_columns = two_dimension_array[0:2, 0:2]
print(first_two_rows_and_columns)

#How to reverse the rows and the whole array?
print(two_dimension_array[::])

#Reverse the row and column positions
print(two_dimension_array[::-1,::-1])

#Represent missing values ?
print(two_dimension_array)
two_dimension_array[1,1] = 55
two_dimension_array[1,2] =44
print(two_dimension_array)

#Numpy Zeroes
# numpy.zeros(shape, dtype=float, order='C')
numpy_zeroes = np.zeros((3,3),dtype=int,order='C')
print(numpy_zeroes)

# Numpy Zeroes
numpy_ones = np.ones((3,3),dtype=int,order='C')
print(numpy_ones)

twoes = numpy_ones * 2
print(twoes)

#How to create repeating sequences?
a = [1,2,3]
# Repeat whole of 'a' two times
print('Tile: ', np.tile(a, 2))
# Repeat each element of 'a' two times
print('Repeat: ', np.repeat(a, 2))


#How to generate random numbers?
# One random number between [0,1)
one_random_num = np.random.random(1)
one_random_in = np.random
print(one_random_num)

# Random numbers between [0,1) of shape 2,3
r = np.random.random(size=[2,3])
print(r)
print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10))

## Random numbers between [0, 1] of shape 2, 2
rand = np.random.rand(2,2)
print(rand)

rand2 = np.random.randn(2,2)
print(rand2)

# Random integers between [0, 10) of shape 2,5
rand_int = np.random.randint(0, 10, size=[5,3])
print(rand_int)

#from scipy import stats
np_normal_dis = np.random.normal(5, 0.5, 1000) 
np_normal_dis
## min, max, mean, median, sd
print('min: ', np.min(np_normal_dis))
print('max: ', np.max(np_normal_dis))
print('mean: ', np.mean(np_normal_dis))
print('median: ', np.median(np_normal_dis))
#print('mode: ', stats.mode(np_normal_dis))
print('sd: ', np.std(np_normal_dis))

"""plt.hist(np_normal_dis, color="grey", bins=21)
plt.show()"""

#inear Algebra
#1. Dot Product
## Linear algebra
### Dot product: product of two arrays
f = np.array([1,2,3])
g = np.array([4,5,3])
### 1*4+2*5 + 3*6
print(np.dot(f, g))

### Matmul: matruc product of two arrays
h = [[1,2],[3,4]]
i = [[5,6],[7,8]]
### 1*5+2*7 = 19
np.matmul(h, i)

## Determinant 2*2 matrix
### 5*8-7*6np.linalg.det(i)
np.linalg.det(i)