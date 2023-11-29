# arrays vs Lists

#Similarities 
# 1)Both dtata structures are mutable
# 2)Both can be indexed and iterated through
# )they can be both sliced


#Differences
import numpy as np

myarray = np.array([1,2,3,4,5,6])
myList = [1,2,3,4,5]

print(myarray/2) 
# here when we perform the operation on array it satisfies divisions and some computations
#so when we run print(myarray) it gives op as [0.5 1.  1.5 2.  2.5 3. ]

# but for print(myList) we cannot perform this type of computations
#So its better to use arrays for performing operations


#2) In arrays all elements have to be same data type but for lists it can be different datatype
