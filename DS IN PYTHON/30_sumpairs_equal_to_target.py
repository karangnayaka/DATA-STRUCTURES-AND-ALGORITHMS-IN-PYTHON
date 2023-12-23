#collect sum pairs equal to the target value

def pair_sum(arr, target_sum):
    result = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                result.append(f"{arr[i]}+{arr[j]}")
    return result
 

arr = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]

target_sum = int(input("Enter the target sum: "))
      
print(pair_sum(arr,target_sum))