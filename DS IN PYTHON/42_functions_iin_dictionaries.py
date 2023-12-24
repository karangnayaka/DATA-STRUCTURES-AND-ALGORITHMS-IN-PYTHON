## functions in dictionaries

my_dict = {
    3:"three",
    5:"five",
    9:"nine",
    2:"two",
    1:"one",
    4:"four"
}

## len function returns the number of pairs in the dictionaries
print(len(my_dict))

## all() function -- it returns true if all the functions are true
print(all(my_dict))
## if one of the value is false also it returns false

##any() function
print(my_dict) #it returns true if any one of the value is true

## sorted()function   -- it sorts the values in the dictionaries
print(sorted(my_dict))