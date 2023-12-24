
my_dict = {'name':'edu','age':24, 'address':'Mysuru','education':'master'}

###copy method
dict = my_dict.copy()

print(my_dict)
print(dict)

###from keys 
newDict = {}.fromkeys([1,2,3], 0)   #([seq],values)
print(newDict)

### get Method   -- returns specific value

print(my_dict.get('age',27))  ## here we get 26 as output


##items()
print(my_dict.items())


##key() method

print(my_dict.keys())   ## it describes the entities in the relation

## popitem() it deletes last item and it returns it

print(my_dict.popitem())

## setdefault()  dictionary.setdefault(key,default_value)
print(my_dict.setdefault('name','added')) ##here it returns the specific value
print(my_dict.setdefault('name1','added')) ##it adds a value to the dictionaries
print(my_dict)

## values  -- dictionary.values() -- it returns the values of the entities
print(my_dict.values())

## update() -- it updates the key in the dictionaries
##if the key is already present in the dictionary it update the new vaue

new_dict = {'a':1, 'b':2,'c':3}
my_dict.update(newDict)
print(my_dict)


