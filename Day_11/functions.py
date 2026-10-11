'''Exercises: Level 1

    Declare a function add_two_numbers. It takes two parameters and it returns a sum.
    Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
    Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
    Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
    Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
    Write a function called calculate_slope which return the slope of a linear equation
    Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
    Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
    Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"])) 
# ["C", "B", "A"]

    Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
    Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]

    Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]

    Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

    Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
    Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

Exercises: Level 2

    Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.

    print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.

    Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
    Call your function is_empty, it takes a parameter and it checks if it is empty or not
    Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
    Write a function called greet which takes a default argument, name. If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name.

    greet()
    # "Hello, Guest!
    greet("Alice")
    # "Hello, Alice!"

    Create a function called show_args to take an arbitrary number of named arguments and print their names and values.

    show_args(name="Alice", age=30, city="New York")
    # Received: name: Alice, age: 30, city: New York
    show_args(name="Bob", pet="Fluffy, the bunny")
    # Received: name: Bob, pet: Fluffy, the bunny

Exercises: Level 3

    Write a function called is_prime, which checks if a number is prime.
    Write a functions which checks if all items are unique in the list.
    Write a function which checks if all the items of the list are of the same data type.
    Write a function which check if provided variable is a valid python variable
    Go to the data folder and access the countries-data.py file.

    Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
    Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
'''

# ____Exercise 1_____

def add_two_numbers(num1, num2):
  return num1 + num2

print(add_two_numbers(12,12))

def area_of_circle(r):
  return 3.14 * r**2

print(area_of_circle(10))

def sum_all_numbers(*nums):
  sum = 0
  for num in nums:
    if(type(num) != int or type(num) != float):
      print(f'"{num}" is is not a number!!')
    else:
      sum += num
  
  return sum

print( sum_all_numbers('hello', 12 ,12, 23, [1,2,3,4]))

def convert_celsius_to_fahrenheit(celcius):
  return f'{(celcius * 9/5) + 32}°F'

print(convert_celsius_to_fahrenheit(32))

def check_season(month):
  month = month.capitalize()
  if month == 'January' or month == 'February' or month =='December':
    return 'The season is Winter'
  elif month == 'March' or month == 'April' or month =='May':
    return 'The season is Spring'
  elif month == 'June' or month == 'July' or month =='August':
    return 'The season is Summer'
  elif month == 'September' or month == 'October' or month =='November':
    return 'The season is Spring'
  else:
    return 'Enter a right month!!'
  
print(check_season('hello'))

def solve_quadratic_eqn(a,b,c):
  delta = b**2 - 4*a*c
  return f'x1: {(-b + delta)/(2*a)}, x2: {(-b - delta)/(2*a)}'

print(solve_quadratic_eqn(12,4,5))

def print_list(list):
  for item in list:
    return item 

def reverse_list(list):
  i= len(list)-1
  rev_list = []
  
  while i >= 0:
    rev_list.append(list[i])
    i -= 1
  
  return rev_list

print(reverse_list(["A", "B", "C"]))

def capitalize_list_items(list):
  
  for i in range(len(list)):
    if type(list[i]) == str:
      list[i] = list[i].capitalize()
  
  return list


print(capitalize_list_items(["a", "b", "c"]))

def add_item(list, item):
  list.append(item)
  return list

print(add_item(["a", "b", "c"], "d"))

def remove_item(list, item):
  if(item in list):
    list.remove(item)
  else:
    print('The item is not in the list')
    
  return list

print(remove_item(["a", "b", "c"], "a"))

def sum_of_numbers(number):
  sum = 0
  
  for i in range(number+1):
    sum += i

  return sum

print(sum_of_numbers(5))

def sum_of_even(number):
  sum = 0
  
  for i in range(number+1):
    if i %2 == 0:
      sum += i

  return sum

print(sum_of_even(5))

def sum_of_odd(number):
  sum = 0
  
  for i in range(number+1):
    if i %2 != 0:
      sum += i

  return sum

print(sum_of_odd(5))
# ________Exercise 2_______

def evens_and_odds(num):
  count_odd = 0
  count_even = 0
  
  for i in range(num + 1):
    if i%2 == 0:
      count_even += 1
    else:
      count_odd += 1
      
  return f'The number of evens are {count_even}\nThe number of odds are {count_odd}'

print(evens_and_odds(100))

def factorial(num):
  fact = 1
  if ( num == 0): 
      return 'The factorial is 1'
  for i in range(1, num + 1):
    fact *= i
    
  return fact

print(factorial(4))

def is_empty(item):
  pass

def greet(user = 'Guest'):
  return 'hello, {}'.format(user)

print(greet())
print(greet('Diana'))
