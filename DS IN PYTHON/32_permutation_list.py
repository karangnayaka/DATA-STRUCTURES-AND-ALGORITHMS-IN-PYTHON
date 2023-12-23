
#Check whether the lists are permuted to each other


def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()

    if list1 == list2:
        return True
    else:
        return False
    
list1 = [1, 2, 3]
list2 = [3, 1, 2]    
print(permutation(list1, list2))