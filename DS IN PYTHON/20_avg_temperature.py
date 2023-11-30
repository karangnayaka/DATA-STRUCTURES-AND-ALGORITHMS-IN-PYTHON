#find the number of days above average temperature

numDays = int(input("how many days's temperature? "))

total = 0
for i in range(1, numDays+1):
    nextDay = int(input("Day" + str(i) + "'s high temp:"))
    total += nextDay 

avg = round(total/numDays,2)
print("\n Average = " + str(avg))