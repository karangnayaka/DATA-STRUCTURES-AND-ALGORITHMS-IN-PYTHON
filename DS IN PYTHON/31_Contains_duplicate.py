#return true if any value appears at least twice in the array, and return false if every element is distinct.

def contains_duplicate(nums):
    seen = set()   #here the set seen is initialized with null then if the value is not in the seen it gets added to seen
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
 
# Example usage
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
print(contains_duplicate(nums)) 

#the basic idea to implement this function is to add the elements to seen while adding the elements if the values in the seen repeated then it confirms that the list has duplicates