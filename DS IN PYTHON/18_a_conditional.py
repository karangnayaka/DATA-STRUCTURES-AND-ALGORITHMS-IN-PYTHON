prev_list = [-1, 10, -20,2,-90,60,45,20]
new_list = [number if number > 0 else 'negative number' for number in prev_list]
print(new_list)

# or

def get_number(number):
    if number > 0:
        return number
    else:
        return 'negative number'
new_list = [get_number(number) for number in prev_list] 
print(new_list)   