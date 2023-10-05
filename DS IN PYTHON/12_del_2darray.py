# Deletion of an element in two dimensional array

import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14,9]])
print(twoDArray)

newTDArray = np.delete(twoDArray, 0, axis = 1)   #here when axis is equal to 1 the column get deleted and when the axis is equal to 0 the row gets deleted

print(newTDArray)

newTDArray = np.delete(twoDArray, 1, axis = 1)
print(newTDArray)