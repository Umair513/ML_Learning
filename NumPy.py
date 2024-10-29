import numpy as np

arr_1d = np.array([1,2,3,4])    # creats array
print(arr_1d)
print(type(arr_1d))     # print type of object
print(arr_1d.ndim)      # determines dimensions of array

arr_2d = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
print(arr_2d)
print(arr_2d.ndim)
print(arr_2d.size)      # determine size of array
print(arr_2d.shape)     # determine shape of array
print(arr_2d.dtype)     # determine data type of array

mx_1s = np.ones(5)      # declares array of ones 
print(mx_1s)
print(type(mx_1s))
print(mx_1s.ndim)
print(mx_1s.dtype)

mx_mul = np.ones((2,3), dtype = int)
print(mx_mul)

mx_0s = np.zeros((4,4), dtype = bool)
print(mx_0s)

mx_emp = np.empty((3,3))    # decalres matrix of random numbers 
print(mx_emp)
print(mx_emp.dtype)

ar_1d = np.arange(1,11, 2)  # declare aaray of from to exculded with steps
print(arr_1d)

linespace = np.linspace(1,40, 3)    # declare array from to of given numbers
print(linespace)

arr1 = np.arange(1,10).reshape(3,3)     # resshape array in diffrent dimensions
arr2 = np.arange(1,10).reshape(3,3)
print(np.add(arr1,arr2))
print(np.subtract(arr1,arr2))
print(np.divide(arr1,arr2))
print(np.multiply(arr1,arr2))
print(arr1.dot(arr2))       # vector product of matrix
print(arr1.max())       # max value od matrix
print(arr1.argmax())    # index of max value of matrix
print(arr1.max(axis=0)) # axios 0 means col axis 1 means row
print(np.sum(arr1))     # sum of elemnts of matrix
print(np.mean(arr1))
print(np.sqrt(arr1))
print(arr1.std())       # standard devision
print(np.exp(arr1))     # exponent
print(np.log(arr1))     # natural log
print(np.log10(arr1))

mx = np.arange(1,101).reshape(10,10)
print(mx)
print(mx[0,0])
print(mx[:, 0])
print(mx[:, 0:1])
print(mx[1:4, 1:4])

arr1d = np.arange(1,17).reshape(4,4)
print(arr1d)
arr2d = np.arange(17,33).reshape(4,4)
print(arr2d)
print(np.concatenate((arr1d,arr2d)))
print(np.concatenate((arr1d,arr2d), axis=1))

print(np.split(arr1d,2))

import matplotlib.pyplot as plt

print(np.sin(180))
x_sin = np.arange(0, 3*np.pi,0.1)
print(x_sin)
y_sin = np.sin(x_sin)
print(y_sin)

plt.plot(x_sin, y_sin)
# plt.show()

import random

print(np.random.random(10))
print(np.random.random((3,3)))
print(np.random.randint(1,5))

ch_name = "Umair Soomro"
str1 = "Learning Python NumPy"
print(np.char.add(ch_name,str1))
print(np.char.lower(ch_name))
print(np.char.upper(ch_name))
print(np.char.center(ch_name,100, fillchar="*"))
print(np.char.split(ch_name))
print(np.char.replace(ch_name,"Umair", "Popal"))
print(np.char.count(ch_name,"a"))
print(np.char.find(ch_name,"U"))