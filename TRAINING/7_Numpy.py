"""

                        ############## NUMPY #############

-- Numeric-Python (Numpy), is a Python library that is used for numeric and scientific operations.
-- It serves as a building block for many libraries available in Python.

-- NumPy is a Python library used for working with arrays, linear algebra, fourier transform, and matrices.
-- A numpy array is similar to a list. NumPy stands for Numerical Python and it is an open source project.
-- The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.

-- Arrays are very frequently used in data science, where speed and resources are very important.
-- NumPy is usually imported under the np alias.
-- It's usually fixed in size and each element is of the same type.
-- We can cast a list to a numpy array by first importing numpy:         //// import numpy as np  ////


############# One Dimensional Numpy #############


-- We then cast the list as follows:
a = np.array([0, 1, 2, 3, 4])
a

##### Checking NumPy Version -->> print(np.__version__)   -->> 1.22.3

##### Type -->> type(a)   -->>  numpy.ndarray

           -->> a.dtype  -->> dtype('int32')

b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])
print(b)

//Output//
[  3.1   11.02   6.2  213.2    5.2 ]

b[0]=11.23
b[4] = 0
print(b)

//Output//
[ 11.23  11.02   6.2  213.2    0.  ]



########## Slicing ##########

-- Like lists, we can slice the numpy array. Slicing in python means taking the elements from the given index to another given index.
-- We pass slice like this: [start:end].The element at end index is not being included in the output.

c = b[1:4]
print(c)

//Output//
[ 11.02   6.2  213.2 ]

# Set the fourth element and fifth element to 300 and 400
b[3:5] = 300, 400
print(b)

//Output//
[ 11.23  11.02   6.2  300.   400.  ]



######### We can also define the steps in slicing, like this: [start:end:step]. ##########

DEFAULT -->> start=0 , end=last element , step=1

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2])                           ---->>>> [2 4]


#########  Assign Value with List  #########

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr[1::2])                          ---->>>> [2 4 6 8] only even numbers

select = [0, 2, 3, 4]
print(select)                            ---->>>> [0, 2, 3, 4]

arr[select] = 100
print(arr)                              ---->>>> [100   2 100 100 100   6   7   8]

print(arr.size)                         ---->>>> 8
print(arr.ndim)                         ---->>>> 1
print(a.shape)                          ---->>>> (8,)



#########  Numpy Statistical Functions #########

a = np.array([-1, 2, 3, 4, 5])

a = np.array([-1, 2, 3, 4, 5])
mean = a.mean()
print(mean)                               ---->>>> 2.6

standard_deviation=a.std()
print(standard_deviation)                 ---->>>> 2.0591260281974

max_a =a.max()
print(max_a)                              ---->>>> 5

min_a =a.min()
print(min_a)                              ---->>>> -1

np.median(a)

############ Finding the index of minimum and maximum values: ##########


#creating a list of 5 horsepower values
horsepower = [130, 165, 150, 150, 140]
#creating a numpy array from horsepower list
horsepower_arr = np.array(horsepower)
print("Index of Minimum horsepower: ", np.argmin(horsepower_arr))
print("Index of Maximum horsepower: ", np.argmax(horsepower_arr))


#########  Numpy Statistical Functions #########

######### Array Addition - The operation is equivalent to vector addition: #########

u = np.array([1, 0])
print(u)                              ---->>>> [1 0]
v = np.array([0, 1])
print(v)                              ---->>>> [0 1]
z = np.add(u, v)
print(z)                              ---->>>> [1 1]


arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])
arr3 = np.add(arr1, arr2)
print(arr3)                            ---->>>> [30, 32, 34, 36, 38, 40]



######### Array Subtraction - The operation is equivalent to vector subtraction: #########

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])
arr3 = np.subtract(arr1, arr2)
print(arr3)



#########  Array Multiplication - This is equivalent to multiplying a vector by a scaler #########

x = np.array([4, 28])
print(x)                            ---->>>> [4 28]
y = np.array([2, 3])
print(y)                            ---->>>> [2 1]
z = np.multiply(x, y)
print(z)                            ---->>>> [8 112]    ( corresponding elements are multiplied ).



#########  Array Division - This is equivalent to dividing a vector by a scaler #########

x = np.array([4, 28])
print(x)                            ---->>>> [4 28]
y = np.array([2, 3])
print(y)                            ---->>>> [2 4]
z = np.divide(x, y)
print(z)                            ---->>>> [2. 7.]



#########  Dot Product #########

X = np.array([3, 5])
Y = np.array([2, 4])

print(np.dot(X, Y))                ---->>>> 26



#########  Adding Constant to a Numpy Array #########

u = np.array([1, 2, 3, -1])
u+1
print(u)                           ---->>>> [2 3 4 0]



#########  Mathematical Functions #########

# The value of pi
np.pi

# Create the numpy array in radians
x = np.array([0, np.pi/2 , np.pi])

# Calculate the sin of each elements
y = np.sin(x)
print(y)                               --->>> [0.0000000e+00 1.0000000e+00 1.2246468e-16]


###### Linspace ######

Linspace returns evenly spaced numbers over a specified interval.
start : start of interval range
stop : end of interval range
num : Number of samples to generate.by default =50

numpy.linspace(start, stop, num = int value)

# Makeup a numpy array within [-2, 2] and 9 elements

print(np.linspace(-2, 2, num=9))         --->>> [-2. , -1.5, -1. , -0.5,  0. ,  0.5,  1. ,  1.5,  2. ]


#####----#####
import matplotlib.pyplot as plt
x = np.linspace(0, 2*np.pi, num=100)
y = np.sin(x)
plt.plot(x, y)
plt.show()


########

arr1 = np.array([1, 2, 3])
print(arr1)
for x in arr1:
  print(x)

[1 2 3]
1
2
3


#######  Arange #######

-- This method returns evenly spaced values between the given intervals excluding the end limit.
-- The values are generated based on the step value and by default, the step value is 1.

#step value = 2
np.arange(0,10,2)              #[0,2,4,6,8]



$############# Two Dimensional Numpy #############

import numpy as np
a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]

# Convert list to Numpy Array
# Every element is the same type

A = np.array(a)
print(A)                    --->>>
                                                                                                            [[11 12 13]
                                                                                                            [21 22 23]
                                                                                                            [31 32 33]]
print(A.ndim)                --->>>          2
print(A.shape)               --->>>          returns a tuple -- (3, 3)
print(A.size)                --->>>          9

'dtype' refers to the data type of the data contained by the array. Numpy supports multiple datatypes like integer, float, string, boolean etc.



######### Changing dtype ###########

car_attributes = [[18, 15, 18, 16, 17],[130, 165, 150, 150, 140],[307, 350, 318, 304, 302]]
#converting dtype
car_attributes_arr = np.array(car_attributes, dtype = 'float')


# Access the element on the second row and third column
A[1, 2]
## OR BELOW CAN ALSO BE USED ##
A[1][2]                 --->>>          23

# Access the element on the first row and first and second columns
A[0][0:2]               --->>>        [11 12]

# Access the element on the first and second rows and third column
A[0:2, 2]                --->>>        [13 23]



################

X = np.array([[1, 0], [0, 1]])
Y = np.array([[2, 1], [1, 2]])
Z = X + Y
print(Z)

[[3 1]
 [1 3]]



 ############# MATRIX ##########

We can also perform matrix multiplication with the numpy arrays A and B as follows:
First, we define matrix A and B:

A = np.array([[0, 1, 1], [1, 0, 1]])            # 2*3
B = np.array([[1, 1], [1, 1], [-1, 1]])         # 3*2


# Calculate the dot product( Matrix multiplication since both have 3 common in shape we can , Output will be 2*2)

Z = np.dot(A,B)
print(Z)

###[[0 2]
### [0 2]]

print(np.sin(Z))

###[[0.         0.90929743]
### [0.         0.90929743]]


#We use the numpy attribute T to calculate the transposed matrix

C = np.array([[1,1],[2,2],[3,3]])
print(C.T)


###[[1 2 3]
### [1 2 3]]




########### Used to calculate total operation time (ARRAY v/s NUMPY) ############

import time
start_time = time.time()
list1 = list(range(1,1000000))
list2 = list(range(2,1000001))
list3 = []
for i in range(len(list1)):
    list3.append(list1[i] + list2[i])
print("--- %s milliseconds ---" % (1000*time.time() - 1000*start_time))

start_time = time.time()
a = np.arange(1,1000000)
b = np.arange(2,1000001)
c = a+b
print("--- %s milliseconds ---" % (1000*time.time() - start_time*1000))
print('Duration(ms): {}'.format(1000*time.time() - 1000*start_time))



######### Following are the benefits of using Numpy: ##########

-- As the array size increases, Numpy can execute more parallel operations, thereby making computation faster.
-- When the array size gets close to 5,000,000, NumPy gets around 120 times faster than Python List.
-- NumPy has many optimized built-in mathematical functions.
-- These functions helps in performing variety of complex mathematical computations faster and with very minimal code.
-- Another great feature of NumPy is that it has multidimensional array data structures that can represent vectors and matrices.
-- This can be useful as lot of machine learning algorithms rely on matrix operations.





######### Querying/searching in an array ##########

-- Given a condition, 'where' function returns the indexes of the array where the condition satisfies.
-- Using these indexes, the respective values from the array can be obtained.


horsepower = [130, 165, 150, 150, 140]
horsepower_arr = np.array(horsepower)

x = np.where(horsepower_arr >= 150)
print(x)                                                # gives the indices
                                                        # With the indices , we can find those values
horsepower_arr[x]




########## Filter data ###########

-- Getting some elements out of an existing array based on certain conditions and creating a new array out of them is called filtering.


horsepower = [130, 165, 150, 150, 140]
horsepower_arr = np.array(horsepower)

filter_arr = horsepower_arr > 135              #creating filter array
newarr = horsepower_arr[filter_arr]

print(filter_arr)                     --->>>            [False  True  True  True  True]
print(newarr)                         --->>>           [165 150 150 140]




########## Sorting an array ##########

-- The  numpy array can be sorted by passing the array to the function sort(array) or by array.sort
-- The difference is that the :
    array.sort() function modifies the original array by default,
    whereas the sort(array) function does not.



horsepower = [130, 165, 150, 150, 140]
horsepower_arr = np.array(horsepower)

print('original array: ', horsepower_arr)                             #                      original array:  [130 165 150 150 140]

print('Sorted array: ', np.sort(horsepower_arr))                      # using sort(array)    Sorted array:  [130 140 150 150 165]

print('original array after sorting: ', horsepower_arr)               #                      original array after sorting:  [130 165 150 150 140]

horsepower_arr.sort()
print('original array after sorting: ', horsepower_arr)               # using array.sort     original array after sorting:  [130 140 150 150 165]





                ########## Vectorized operations ##########

-- Numpy provides various mathematical functions such as sum(), add(), sub(), log(), sin() etc. which uses vectorization.

np.add()                --->>>
np.subtract()           --->>>
np.negative()           --->>>
np.multiply()           --->>>
np.divide()             --->>>
np.floor_divide()       --->>>
np.power()              --->>>
np.mod()                --->>>

-- In addition to arithmetic operations, several other mathematical operations like exponents, logarithms and trigonometric functions are also available in Numpy.
-- This makes Numpy a very useful tool for scientific computing.


student_marks_arr = np.array([78, 92, 36, 64, 89])
print(np.sum(student_marks_arr))
additional_marks = [2, 2, 5, 10, 1]

                               #### we need to award additional marks to existing marks
student_marks_arr += additional_marks
print(student_marks_arr)

                                #### using vectorized operration
student_marks_arr = np.add(student_marks_arr, additional_marks)
print(student_marks_arr)




######### Broadcasting #########

-- "Broadcasting" refers to the term on how Numpy handles arrays with different shapes during arithmetic operations.
-- Array of smaller size is stretched or copied across the larger array.

import numpy as np

array1=np.array([5, 10, 15])                # Array 1
array2=np.array([5])                        # Array 2

array3= array1 * array2                     # While multiplying it is stretching the array2 to make it same shape of array1
print(array3)                               # [25 50 75]


-- shape of first array is 1x3 and the shape of second array is 1x1, according to broadcasting rules,
        the second array gets stretched to match the shape of first array and the shape of the resulting array is 1x3.
-- shape of first array is 3x3 and the shape of second array is 1x3, according to broadcasting rules,
       the second array gets stretched to match the shape of first array and the shape of the resulting array is 3x3.
-- shape of first array is 3x1 and the shape of second array is 1x3, according to broadcasting rules,
       both first and second arrays get stretched and the shape of the resulting array is 3x3.

Example :

students_marks = np.array([[67, 45],[90, 92],[66, 72],[32, 40]])        #Students marks in 4 subjects
students_marks
                                                                        #Now the teacher wants to award extra five marks in Chemistry and extra ten marks in Physics.
students_marks += [5,10]                 #Broadcasting  -- marks 4*2 array and additional marks is 1*2 so it will broadcast to 4 rows of equal value to get 4*2 as output
print(students_marks)






############# Image as a Numpy matrix #################

-- Images are stored as arrays of hundreds, thousands or even millions of picture elements called as pixels.
        Therefore, images can also be treated as Numpy array, as they can be represented as matrix of pixels.
-- Certain basic operations and manipulations can be carried out on images using Numpy and scikit-image package.
        Scikit-image is an image processing package.
-- The package is imported as skimage.

import matplotlib.pyplot as plt                                                         #Using matplotlib.pyplot to visualize the image
import os.path                                                                          #Importing path and skimage i/o library

from skimage.io import imread
from skimage import data_dir
#reading the astronaut image
img = imread(os.path.join(data_dir, "C:\\Users\\rival\\Downloads\\1681815333719.jpeg"))
plt.imshow(img)
print(img)
                                                                                        ####### Properties of image
print('Type of image: ', type(img))
print('Dimensions of image: ', img.ndim)
print('Shape of image:', img.shape)



############ Indexing and selection ############

Slicing  Cropping Image :

img_slice = img.copy()
img_slice = img_slice[300:500,360:480]                       # for x-axis starts from bottom-left and for y-axis starts from top-left
plt.figure()
plt.imshow(img_slice)


######### Assigning the values corresponding to the sliced image as 0:

img[300:500,360:480,:] = 0     ## The place where the sliced image was present initially, is now filled with black color because 0 is assigned  to the values corresponding to the sliced image.
plt.imshow(img)


######### Replacing the ‘rocket’ back to its original place:

img[300:500,360:480,:] = img_slice
plt.imshow(img)




######### Zeroes and Ones #########

Returns an array of given shape filled with zeros/ones:

print(np.zeros(5))                     #1D   [0. 0. 0. 0. 0.]

print(np.zeros([2,3]))                 #2D   [[0. 0. 0.]
                                       #      [0. 0. 0.]]

print(np.ones(5))                     #1D   [1. 1. 1. 1. 1.]

print(np.ones([2,3]))                 #2D   [[1. 1. 1.]
                                       #      [1. 1. 1.]]


#########  Full and Eye  #########

## Full : Returns an array of given shape, filled with given value, irrespective of datatype.
## Eye : Returns an identity matrix for the given shape.


print(np.full(5,8))                             #number=5, value=8       [8 8 8 8 8]

print(np.full([3,3],'numpy'))                   #shape=[3,3], value=numpy        [['numpy' 'numpy' 'numpy']
                                                #                                 ['numpy' 'numpy' 'numpy']
                                                #                                 ['numpy' 'numpy' 'numpy']]


print(np.eye(3))                                       #3x3 identity matrix    [[1. 0. 0.]
                                                       #                        [0. 1. 0.]
                                                       #                        [0. 0. 1.]]





########### Random ###########

print(np.random.randint(1,10, size=5))                      # random integer values low=1, high=10, number of values=5     [5 8 2 9 2]

## -->> Similarly, two-dimensional arrays of random numbers  can also be created by passing the shape instead of number of values.

x = np.random.randint(100, size=(3, 5))             #  random integer values high=100, shape = (3,5)
print(x)                                            #  [[30 77 59 91 22]
                                                    #   [ 4 21 56 63  9]
                                                    #   [88 88 59 15 94]]
print(type(x))                                      #   <class 'numpy.ndarray'>


## -->> To generate a random number from a predefined set of values present in an array, the choice() method can be used.

x = np.random.choice([9, 3, 7, 5])                        #returns a single random value from the array    3
print(x)



x = np.random.choice([9, 3, 7, 5], size=(3, 5))           # returns 3*5 random values from the array
print(x)                                                  #  [[3 5 7 7 3]
                                                          #   [5 9 3 3 5]
                                                          #   [9 5 7 9 3]]
print(type(x))                                            # <class 'numpy.ndarray'>
"""

import numpy as np

steps_arr = [[1, 6012], [2, 7079], [3, 6886], [4, 7230], [5, 4598], [6, 5564], [7, 6971], [8, 7763], [9, 8032],
             [10, 9569]]
steps = np.array(steps_arr)
extra_steps = np.array([0, 2000])
Total_steps = steps + extra_steps

filter_arr = Total_steps > 9000
print(Total_steps[filter_arr])
print(np.sort(Total_steps))
