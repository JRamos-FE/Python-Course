import numpy as np

ar = np.array(12)
print(ar)

ar1 = np.array([1, 3, 5, 7, 9])  # Simple array
print(ar1)
print(ar1.ndim)

ar2 = np.array([[1, 3, 5, 7, 9], [2, 4, 6, 8, 20]])  # 2D array
print(ar2)
print(ar2.ndim)

ar3d = np.array([[[2, 3], [3, 4]], [[5, 6], [7, 8]]])  # 3D array
print(ar3d)
print(ar3d.ndim)
print(ar3d.shape)

ar13d = np.array([1, 3, 5, 7, 9], ndmin=4)  # Array dimension assigned with ndmin
print(ar13d)
print(ar13d.ndim)
print(ar13d.shape)

arf = np.array([1.1, 2.2, 3.3])  # Float type array
print(arf.dtype)

mat1 = np.zeros((3, 4))  # Matrix of zeros
print(mat1)

mat2 = np.ones(3)  # Matrix of ones
print(mat2)

mat3 = np.empty((3, 4))  # Non initialized garbage values
print(mat3)

mat4 = np.eye(3)  # Identity matrix of 3x3
print(mat4)

mat5 = np.diag([2, 3])  # Square matrix of diagonal assigned values
print(mat5)

mat6 = np.arange(0, 12, 4)  # Array creation for a given range as well as the counter
print(mat6)

mat7 = np.linspace(0, 10, 5)  # Array creation given starting point and ending point along with number of elements
print(mat7)

# Array slicing with indices
arr11 = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
arr22 = np.array([[2, 4, 6, 8], [1, 3, 5, 7], [11, 22, 33, 44], [10, 20, 30, 40]])
print(arr11[4])  # Array slicing index
print(arr22[2, 3])  # 2D array slicing method
print(arr11[2:9])  # Slicing from starting and ending index
print(arr11[1:8:3])  # Slicing from starting and ending given a counter
print(arr22[:, 0:2])  # Slicing given start and end, none in this case, and final start and end
print(arr22[1:4:2, 1:4:2])  # Extracting particular numbers from an array by using skipping counter


# Reshaping arrays
arrs1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(arrs1.reshape(3, 4))  # From 1 dimension into 2 dimension
print(arrs1.reshape(3, 2, 2))  # From 1 dimension into 3 dimension
arrs1 = arrs1.reshape(3, 2, 2)  # Converting from 1 dimension into 3 dimension
arrs1 = arrs1.flatten()  # Using flatten method to reshape down into 1 dimensional array
print(arrs1)
