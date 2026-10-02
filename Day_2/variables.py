'''

    Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
    Write a python comment saying 'Day 2: 30 Days of python programming'
    Declare a first name variable and assign a value to it
    Declare a last name variable and assign a value to it
    Declare a full name variable and assign a value to it
    Declare a country variable and assign a value to it
    Declare a city variable and assign a value to it
    Declare an age variable and assign a value to it
    Declare a year variable and assign a value to it
    Declare a variable is_married and assign a value to it
    Declare a variable is_true and assign a value to it
    Declare a variable is_light_on and assign a value to it
    Declare multiple variable on one line

Exercises: Level 2

    Check the data type of all your variables using type() built-in function
    Using the len() built-in function, find the length of your first name
    Compare the length of your first name and your last name
    Declare 5 as num_one and 4 as num_two
    Add num_one and num_two and assign the value to a variable total
    Subtract num_two from num_one and assign the value to a variable diff
    Multiply num_two and num_one and assign the value to a variable product
    Divide num_one by num_two and assign the value to a variable division
    Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
    Calculate num_one to the power of num_two and assign the value to a variable exp
    Find floor division of num_one by num_two and assign the value to a variable floor_division
    The radius of a circle is 30 meters.
        Calculate the area of a circle and assign the value to a variable name of area_of_circle
        Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
        Take radius as user input and calculate the area.
    Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
    Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords

'''

first_name = "Banana"
last_name = 'pear'
full_name = 'Banana pear'
country = 'Fruitland'
city = 'Saccaropolis'
age = 10
year = 2026
is_married = False
is_true = True
is_light_on = True

hour, minute , second = 21, 9, 45

#Exercise 2

print(type(first_name))
print(type(last_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_light_on))
print(type(is_true))
print(type(hour))
print(type(minute))

print('The length of my first name is: ',len(first_name), 'while the lenght of my last name is: ', last_name)

num_one = 5
num_two = 4

total = sum([num_one,num_two])
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

radius = 30
area_of_circle = (30**2)* 3.14
circum_of_circle = (30*2) * 3.14


radius2 = input("Enter the circle's radius:")
area_of_circle2 = (int(radius2)**2) * 3.14
print("The area of the circle with radiuis ", radius2, "is: ", area_of_circle2)

first_name2 = input("Enter your first name: ")
last_name2 = input('Enter your last name: ')
country2 = input("Enter your country: ")
age2 = input('Enter your age: ')

print("Hello",first_name2,last_name2," happy to meet someone from ", country2, "with an age of", age2)


