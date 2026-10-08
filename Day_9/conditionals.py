'''Exercises: Level 1

    Get user input using input(“Enter your age: ”).
    If user is 18 or older, give feedback: You are old enough to drive. 
    If below 18 give feedback to wait for the missing amount of years. Output:

    Enter your age: 30
    You are old enough to learn to drive.
    Output:
    Enter your age: 15
    You need 3 more years to learn to drive.

    Compare the values of my_age and your_age using if … else. 
    Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input.
    You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences,
    and a custom text if my_age = your_age. Output:

    Enter your age: 30
    You are 5 years older than me.

    Get two numbers from the user using input prompt.
    If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.
    Output:

    Enter number one: 4
    Enter number two: 3
    4 is greater than 3

Exercises: Level 2

    Write a code which gives grade to students according to theirs scores:

      ```sh
      90-100, A
      80-89, B
      70-79, C
      60-69, D
      0-59, F
      ```

    Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
    The following list contains some fruits:

    ```sh
    fruits = ['banana', 'orange', 'mango', 'lemon']
    ```

If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

Exercises: Level 3

    Here we have a person dictionary. Feel free to modify it!

            person={
        'first_name': 'Asabeneh',
        'last_name': 'Yetayeh',
        'age': 250,
        'country': 'Finland',
        'is_married': True,
        'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
        'address': {
            'street': 'Space street',
            'zipcode': '02210'
        }
        }

 * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:

    Asabeneh Yetayeh lives in Finland. He is married.
    
    '''
    
    
    
# Exercise 1


'''age = int(input('Enter your age: '))
print('You are old enough to drive') if age >= 18 else print(f'You need {18-age} more years before you can drive')'''



'''
my_age = 25
your_age = int(input('Enter your age: '))

if my_age == your_age:
  print('We age both {} years old',(my_age))
elif my_age > your_age and my_age-your_age == 1:
  print(f"I'm {my_age-your_age} year older than you ")
elif my_age > your_age and my_age-your_age > 1:
  print(f"I'm {my_age-your_age} years older than you ")
elif my_age < your_age and your_age-my_age == 1:
  print(f"You're {your_age-my_age} year older than me ")
else:
  print(f"You're {your_age-my_age} years older than me ")
  

number1 = int(input('Enter the first number: '))
number2 = int(input('Enter the second number: '))

if number1 > number2:
  print(f'{number1} is bigger than {number2}')
elif number1 == number2:
  print(f'{number1} is equal to {number2}')
else:
  print(f'{number1} is smaller than {number2}')
  
  
  
#_____Exercise 2______

score = int(input('Enter your score: '))

if score > 100 or score < 0:
  print('Enter a correct score!!')
elif  100 >= score >= 90:
  print('Your score is A')
elif  89 >= score >= 80:
  print('Your score is B')
elif  79 >= score >= 70:
  print('Your score is C')
elif  69 >= score >= 60:
  print('Your score is D')
else:
  print('Your score is F')
  
  
  
month= input('Enter a month').capitalize()

if month == 'January' or month == 'February' or month =='December':
  print('The season is Winter')
elif month == 'March' or month == 'April' or month =='May':
  print('The season is Spring')
elif month == 'June' or month == 'July' or month =='August':
  print('The season is Summer')
elif month == 'September' or month == 'October' or month =='November':
  print('The season is Spring')
else:
  print('Enter a right month!!')
  
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('Enter a fruit: ').lower()

if fruit in fruits:
  print('The fruit is already in the list')
else:
  fruits.append(fruit)
  print(fruits)'''
  
person={
        'first_name': 'Marco',
        'last_name': 'Fidanza',
        'age': 25,
        'country': 'Italy',
        'is_married': False,
        'skills': ['JavaScript', 'HTML', 'C++', 'MongoDB', 'Python'],
        'address': {
            'street': 'Sesame Street',
            'zipcode': '14100'
        }
        }


if 'skills' in person: 
  print(person['skills'][round(len(person['skills']) / 2)])
  print('Python' in person['skills'])
  
