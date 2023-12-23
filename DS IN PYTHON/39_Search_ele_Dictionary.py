#Searching for an element in an dictionary

my_dict = {'name':'edu','age':24, 'address':'Mysuru'}

def searchDict(dict,value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return 'The value does not exist'    

print(searchDict(my_dict,24))