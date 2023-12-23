#here to find the maximum product of 2 integers in an array  

arr = [1,3,4,5,6,]

def max_product(arr):
    arr.sort(reverse=True)
    return(arr[0]*arr[1])

print(max_product(arr))