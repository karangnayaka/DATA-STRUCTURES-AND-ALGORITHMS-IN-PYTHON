# Missing number

def missing_number(arr, n):
    # Calculate the sum of the expected sequence from 1 to n
    expected_sum = (n * (n + 1)) // 2
    
    # Calculate the sum of the elements in the given array
    actual_sum = sum(arr)
    
    # Find the missing number by subtracting the actual sum from the expected sum
    missing_number = expected_sum - actual_sum
    
    return missing_number
