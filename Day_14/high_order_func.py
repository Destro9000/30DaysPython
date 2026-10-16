'''

Exercises: Level 1

    Explain the difference between map, filter, and reduce.
    Explain the difference between higher order function, closure and decorator
    Define a call function before map, filter or reduce, see examples.
    Use for loop to print each country in the countries list.
    Use for to print each name in the names list.
    Use for to print each number in the numbers list.

Exercises: Level 2

    Use map to create a new list by changing each country to uppercase in the countries list
    Use map to create a new list by changing each number to its square in the numbers list
    Use map to change each name to uppercase in the names list
    Use filter to filter out countries containing 'land'.
    Use filter to filter out countries having exactly six characters.
    Use filter to filter out countries containing six letters and more in the country list.
    Use filter to filter out countries starting with an 'E'
    Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
    Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
    Use reduce to sum all the numbers in the numbers list.
    Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
    Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
    Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
    Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
    Declare a get_last_ten_countries function that returns the last ten countries in the countries list.

Exercises: Level 3

    Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
        Sort countries by name, by capital, by population
        Sort out the ten most spoken languages by location.
        Sort out the ten most populated countries.
'''
from functools import reduce
import sys
from pathlib import Path

# data/countries.py lives one folder up from this file (Day_14),
# so add the project root to sys.path before importing it
sys.path.append(str(Path(__file__).resolve().parent.parent))

from data.countries import countries as all_countries

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Exercise 1

def powerNum(num):  # This is a call function that helps in the high-order func (map, filter, reduce)
  return num**2


for country in countries:
  print(country)

for num in numbers:
  print(num)
  
for name in names:
  print(name)
  
# Exeercise 2

countries_up = list(map(lambda country : country.upper(), countries))
print(countries_up)

square_num = list(map(lambda num : num**2, numbers))
print(square_num)

names_up = list(map(lambda name : name.upper(), names))
print(countries_up)
def country_land(country):
  if country.find('land') == -1:
    return False
  else:
    return True  
  

def country_six_chars(country):
  if len(country) == 6:
    return True
  else:
    return False

def country_six_and_more(country):
  return True if len(country) >= 6 else  False

def country_start_with_e(country):
  return country.startswith('E') 

filtered_countries = list(filter(country_land, countries))
print(filtered_countries)
filtered_countries2 = list(filter(country_six_chars, countries))
print(filtered_countries2)
filtered_countries3 = list(filter(country_six_and_more, countries))
print(filtered_countries3)


countries_3 = list(map(lambda country : country.upper(),filter(country_six_chars, countries)))
print(countries_3)

def check_string(item):
  return isinstance(item, str)

def get_string_lists(lst):
  return list(filter(check_string, lst))

print(get_string_lists(['hello', 2, 2, [1,2,3]]))


def add_2_numbers(x,y):
  return int(x) + int(y)
  
number =reduce(lambda x,y : x + y , numbers)
print(number)



string_countries = reduce(lambda a,b : f'{a}+{b}', countries[:-1]) + f'and {countries[-1]} are scandinavian countries'

patterns = ('land', 'ia', 'island', 'stan')
  
def categorize_countries(countries):
  return [country for country in all_countries if any( p in country for p in patterns )]


