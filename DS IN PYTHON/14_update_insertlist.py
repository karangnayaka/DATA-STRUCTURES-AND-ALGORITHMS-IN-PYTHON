#update and insert an elements in a list

#update - List

myList = [1, 2, 3, 4, 5, 6, 7]
print(myList)
myList[2] = 33
print(myList)

#insertion - List
print("Inserting a element in a list")
myList1 = [1, 2, 3, 4, 5, 6, 7]
print(myList1)
myList1.insert(0,11)
print(myList1)

#insertion(append method)
myList1.append(55)
print(myList1)

#extending a list
myList1.extend(myList)
print(myList1)