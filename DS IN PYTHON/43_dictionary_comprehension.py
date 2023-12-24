## new_dict = {new_key:new_value for item in list} 

## new_dict = {new_key:new_value for (key,value) in dict.items() if condition}

city_names = ['paris', 'london', 'rome','berlin','madrid']

new_dict = {city: random.randint(20, 30) for city in city_names} 
print(new_dict) 

city_temps = {city: random.randint(20,30) for city in city_names}
print(city_temps)

above_25 = {city: temp for (city, temp) in city_temps.items()}
print(above_25)