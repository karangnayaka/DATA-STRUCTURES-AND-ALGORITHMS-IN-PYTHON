
#Delete an element from dictionary

my_dict = {'name':'edu','age':24, 'address':'Mysuru','education':'master'}

del my_dict['age']
print(my_dict)

#or using pop(dict) method

my_dict1 = {'name':'edu','age':24, 'address':'Mysuru','education':'master'}
removed_element = my_dict1.pop('age',None)
print(removed_element)

# using pop item  (here last element gets deleted)

# using clear method
my_dict3 = {'name':'edu','age':24, 'address':'Mysuru','education':'master'}
my_dict3.clear()
print(my_dict3)