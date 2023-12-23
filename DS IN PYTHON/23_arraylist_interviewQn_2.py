#write a program to find all pairs of integers whose sum is equal to a given number

#q2 - find pairs
#leetcode 1 - two sum

def findPairs(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):  # The inner loop (j) starts from i + 1 to avoid comparing the same pair of elements 
            if nums[i] == nums[j]:
                continue
            elif nums[i] + nums[j] == target:
                print(i, j)

myList = [1,2,3,2,3,4,5,6]
findPairs(myList, 6)            #here the output will be the indices of the number whose sum will be equal to 6    


