#Dictionaries - A dictionary is a collection which is unordered, changeable and indexed

#Dictionaries are implemented using hash tables which provides fast access to values

#Create dictionary

my_dict = dict()
print(my_dict)

my_dict2 = {}  # creating empty dictionaries in python
print(my_dict2)

#####
eng_sp = dict(one='uno', two='bos', three='tres')
print(eng_sp)

#####
eng_sp2 = {'one':'uno', 'two':'bos', 'three':'tres'}
print(eng_sp2)

#####
eng_sp3 = [('one','uno'), ('two','dos'),('three','trees')]
eng_sp3 = dict(eng_sp3)
print(eng_sp3)

