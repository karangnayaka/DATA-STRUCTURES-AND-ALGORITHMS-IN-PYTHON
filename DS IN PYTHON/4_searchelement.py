#linear search  
#searching for an element in an array

import array

my_array = array.array('i', [1,2,3,4])

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        return 0
    
print(linear_search(my_array, 2))