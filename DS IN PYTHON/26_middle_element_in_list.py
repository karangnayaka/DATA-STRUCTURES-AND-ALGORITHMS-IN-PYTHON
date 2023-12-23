def middle(lst):
    # Return a new list containing all elements from the original list, excluding the first and last elements
    return lst[1:-1] #This line uses list slicing to create a new list containing elements from the original list (lst). The slicing notation lst[1:-1] includes all elements from index 1 (second element) up to, but not including, the element at index -1 (last element).
 

 #consider any list 
my_list = [1, 2, 3, 4]
 
print(middle(my_list))  
#In this example,the function is called with'my_list' as the input,and the result is printed