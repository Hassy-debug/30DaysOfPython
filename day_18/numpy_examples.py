# Day 18:

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

sns.set()

print('numpy:', np.__version__)
# print(dir(np))   # it is very long list, so it is switched off

#Creating numpy
python_list = [1, 2, 3, 4, 5]
print('Type:', type(python_list))
print(python_list)

two_dimensional_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
print(two_dimensional_list)

numpy_array_from_list = np.array(python_list)
print(type(numpy_array_from_list))
print(numpy_array_from_list)

# float array
numy_array_from_list2 = np.array(python_list, dtype=float)
print(numy_array_from_list2)

# boolean array
numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print(numpy_bool_array)

# multidimensional array
numpy_two_dimensional_list = np.array(two_dimensional_list)
print(type(numpy_two_dimensional_list))
print(numpy_two_dimensional_list)

# numpy array to list
np_to_list = numpy_array_from_list.tolist()
print(type(np_to_list))
print('one dimensional array:', np_to_list)
print('two dimensional array: ', numpy_two_dimensional_list.tolist())

# numpy array from tuple
python_tuple = (1, 2, 3, 4, 5)
print(type(python_tuple))
print('python_tuple: ', python_tuple)
numpy_array_from_tuple = np.array(python_tuple)
print(type(numpy_array_from_tuple))
print('numpy_array_from_tuple: ', numpy_array_from_tuple)

# Shape 
nums = np.array([1, 2, 3, 4, 5])
print(nums)
print('shape of nums: ', nums.shape)
print(numpy_two_dimensional_list)
print('shape of numpy_two_dimensional_list: ', numpy_two_dimensional_list.shape)
three_by_four_array = np.array([[0, 1, 2, 3],
                                [4, 5, 6, 7],
                                [8, 9, 10, 11]])
print(three_by_four_array.shape)

# Data type 
int_lists = [-3, -2, -1, 0, 1, 2, 3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)
print(int_array)
print(int_array.dtype)
print(float_array)
print(float_array.dtype)

#Size
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
two_dimensional_list = np.array([[0, 1, 2],
                                 [3, 4, 5],
                                 [6, 7, 8]])
print('The size:', numpy_array_from_list.size)
print('The size:', two_dimensional_list.size)

#Mathematical operations
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
print('+ 10:', numpy_array_from_list + 10)
print('- 10:', numpy_array_from_list - 10)
print('* 10:', numpy_array_from_list * 10)
print('/ 10:', numpy_array_from_list / 10)
print('% 3:', numpy_array_from_list % 3)
print('// 10:', numpy_array_from_list // 10)
print('** 2:', numpy_array_from_list ** 2)

# Checking data types 
numpy_int_arr = np.array([1, 2, 3, 4])
numpy_float_arr = np.array([1.1, 2.0, 3.2])
numpy_bool_arr = np.array([-3, -2, 0, 1, 2, 3], dtype='bool')
print(numpy_int_arr.dtype)
print(numpy_float_arr.dtype)
print(numpy_bool_arr.dtype)

#Converting types 
numpy_int_arr = np.array([1, 2, 3, 4], dtype='float')
print(numpy_int_arr)
numpy_int_arr = np.array([1., 2., 3., 4.], dtype='int')
print(numpy_int_arr)
print(np.array([-3, -2, 0, 1, 2, 3], dtype='bool'))
numpy_float_list = np.array([1.1, 2.0, 3.2])      # the page uses this name without creating it
print(numpy_float_list.astype('int').astype('str'))

# Multi-dimensional arrays
two_dimension_array = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(type(two_dimension_array))
print(two_dimension_array)
print('Shape: ', two_dimension_array.shape)
print('Size:', two_dimension_array.size)
print('Data type:', two_dimension_array.dtype)

# Getting items
two_dimension_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('First row:', two_dimension_array[0])
print('Second row:', two_dimension_array[1])
print('Third row: ', two_dimension_array[2])

print('First column:', two_dimension_array[:, 0])
print('Second column:', two_dimension_array[:, 1])
print('Third column: ', two_dimension_array[:, 2])
print(two_dimension_array)

#Slicing 
print(two_dimension_array[0:2, 0:2])
print(two_dimension_array[::])

# reverse rows and columns
print(two_dimension_array[::-1, ::-1])

#Changing values 
print(two_dimension_array)
two_dimension_array[1, 1] = 55
two_dimension_array[1, 2] = 44
print(two_dimension_array)

# Zeros and ones 
numpy_zeroes = np.zeros((3, 3), dtype=int, order='C')
print(numpy_zeroes)
numpy_ones = np.ones((3, 3), dtype=int, order='C')
print(numpy_ones)
twoes = numpy_ones * 2
print(twoes)

#Reshape and flatten
first_shape = np.array([(1, 2, 3), (4, 5, 6)])
print(first_shape)
reshaped = first_shape.reshape(3, 2)
print(reshaped)
flattened = reshaped.flatten()
print(flattened)

#Stacking 
np_list_one = np.array([1, 2, 3])
np_list_two = np.array([4, 5, 6])
print(np_list_one + np_list_two)
print('Horizontal Append:', np.hstack((np_list_one, np_list_two)))
print('Vertical Append:', np.vstack((np_list_one, np_list_two)))

# Random numbers
print(np.random.random())                              # one random float
print(np.random.random(5))                             
print(np.random.randint(0, 11))                        
print(np.random.randint(2, 10, size=4))                # one row of 4
print(np.random.randint(2, 10, size=(3, 3)))           

# normal distribution: np.random.normal(mu, simga, size)
normal_array = np.random.normal(79, 15, 80)
print(normal_array)

plt.hist(normal_array, color="grey", bins=50)
plt.show()

# Matrix
four_by_four_matrix = np.matrix(np.ones((4, 4), dtype=float))
print(four_by_four_matrix)
np.asarray(four_by_four_matrix)[2] = 2
print(four_by_four_matrix)

#range and arange 
lst = range(0, 11, 2)
print(lst)
for l in lst:
    print(l)

print(np.arange(0, 20, 1))      # whole numbers
print(np.arange(1, 20, 1))      # natural numbers
print(np.arange(1, 20, 2))      # odd numbers
print(np.arange(2, 20, 2))      # even numbers

#linspace and logspace
print(np.linspace(1.0, 5.0, num=10))
print(np.linspace(1.0, 5.0, num=5, endpoint=False))
print(np.logspace(2, 4.0, num=4))

#Size of an item 
x = np.array([1, 2, 3], dtype=np.complex128)
print(x)
print(x.itemsize)

# Indexing and slicing
np_list = np.array([(1, 2, 3), (4, 5, 6)])
print(np_list)
print('First row: ', np_list[0])
print('Second row: ', np_list[1])

#Statistical functions 
np_normal_dis = np.random.normal(5, 0.5, 100)
print(np_normal_dis)
print('min: ', two_dimension_array.min())      
print('max: ', two_dimension_array.max())      
print('mean: ', two_dimension_array.mean())    
print('sd: ', two_dimension_array.std())       

print(two_dimension_array)
print('Column with minimum: ', np.amin(two_dimension_array, axis=0))
print('Column with maximum: ', np.amax(two_dimension_array, axis=0))
print('=== Row ==')
print('Row with minimum: ', np.amin(two_dimension_array, axis=1))
print('Row with maximum: ', np.amax(two_dimension_array, axis=1))

#Repeating sequences
a = [1, 2, 3]
print('Tile:   ', np.tile(a, 2))
print('Repeat: ', np.repeat(a, 2))

# More random numbers
one_random_num = np.random.random()
print(one_random_num)
print(np.random.random(size=[2, 3]))
print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10))
print(np.random.rand(2, 2))
print(np.random.randn(2, 2))
print(np.random.randint(0, 10, size=[5, 3]))

#min, max, mean, median, mode, standarddeviation 
np_normal_dis = np.random.normal(5, 0.5, 1000)   # mean, standard deviation, samples
print('min: ', np.min(np_normal_dis))
print('max: ', np.max(np_normal_dis))
print('mean: ', np.mean(np_normal_dis))
print('median: ', np.median(np_normal_dis))
print('mode: ', stats.mode(np_normal_dis))
print('sd: ', np.std(np_normal_dis))

plt.hist(np_normal_dis, color="grey", bins=21)
plt.show()

#Linear algebra
f = np.array([1, 2, 3])
g = np.array([4, 5, 3])
print(np.dot(f, g))                    

h = [[1, 2], [3, 4]]
i = [[5, 6], [7, 8]]
print(np.matmul(h, i))                 
print(np.linalg.det(i))                

#Chessboard pattern
Z = np.zeros((8, 8))
Z[1::2, ::2] = 1
Z[::2, 1::2] = 1
print(Z)

#Numpy vs python list
new_list = [x + 2 for x in range(0, 11)]
print(new_list)
np_arr = np.array(range(0, 11))
print(np_arr + 2)

#Temperature vs pressure
temp = np.array([1, 2, 3, 4, 5])
pressure = temp * 2 + 5
print(pressure)

plt.plot(temp, pressure)
plt.xlabel('Temperature in oC')
plt.ylabel('Pressure in atm')
plt.title('Temperature vs Pressure')
plt.xticks(np.arange(0, 6, step=0.5))
plt.show()

#Normal distribution plot
mu = 28
sigma = 15
samples = 100000
x = np.random.normal(mu, sigma, samples)
ax = sns.histplot(x, kde=True)         # the page uses sns.distplot which newer seaborn removed
ax.set(xlabel="x", ylabel='y')
plt.show()
