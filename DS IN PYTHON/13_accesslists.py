#accessing and traversing in the list

shoppingList = ['milk', 'butter', 'cheese']
print(shoppingList[1])

print('milk'in shoppingList)  #here it it nothing but the boolean expression of the statement

print("traversing")

for i in shoppingList:
    print(i)

for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i]+"+"
    print(shoppingList[i])