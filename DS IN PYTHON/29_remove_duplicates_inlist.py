# Write a function to remove the duplicate numbers on given integer array/list


def remove_duplicates(lst):
    unique_lst = []
    seen = set()  #empty set seen to keep track of the elements already processed.
    for item in lst: #  For each item in lst, check if it is not in seen. If it's not in seen, append it to unique_lst and add it to the seen set.
        if item not in seen:
            unique_lst.append(item)
            seen.add(item)
    return unique_lst
 
my_list = [1, 1, 2, 2, 3, 4, 5]
print(remove_duplicates(my_list))