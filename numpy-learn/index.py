# -*-coding:utf8-*-
import numpy as np

# a = [0, 1, 2]
# b = [17, 18, 19]
# c = [27, 28, 29]
# z = [a, b, c]
# print np.sum(z, axis=0)

x1 = np.array([[5, 5], [4, 4], [3, 3], [2, 2], [10, 10],[1,1]])
x2 = np.array([[1, 1]])

y = np.abs(x1 - x2)
# y = np.sum(y, axis=1)
y1 = np.argmin(y)
print y1

# distances = np.sum(np.abs(self.xtr - testData[i, :]), axis=1)


# xtr.shape = [50000, 3072]
# testData.shape = [10000,3072]

# arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# row_r1 = arr1[1, :]
# print row_r1

# a = np.array([1, 2, 3])  # Create a rank 1 array
# print type(a)            # Prints "<type 'numpy.ndarray'>"
# print a.shape            # Prints "(3,)"
# print a[0], a[1], a[2]   # Prints "1 2 3"
# a[0] = 5                 # Change an element of the array
# print a                  # Prints "[5, 2, 3]"
#
# b = np.array([[1,2,3],[4,5,6]])   # Create a rank 2 array
# print b                           # 显示一下矩阵b
# print b.shape                     # Prints "(2, 3)"
# print b[0, 0], b[0, 1], b[1, 0]   # Prints "1 2 4"
