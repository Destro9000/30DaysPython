'''Create an empty dictionary called dog
Add name, color, breed, legs, age to the dog dictionary
Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
Get the length of the student dictionary
Get the value of skills and check the data type, it should be a list
Modify the skills values by adding one or two skills
Get the dictionary keys as a list
Get the dictionary values as a list
Change the dictionary to a list of tuples using items() method
Delete one of the items in the dictionary
Delete one of the dictionaries'''

dog = {}

dog['name'] = 'Woof'
dog['color'] = 'brown'
dog['breed'] = 'german shepherd'
dog['legs'] = 'four'
dog['age'] = 3

print(dog)
  

student = {
  'first_name': 'Marco',
  'last_name': 'Fidanza',
  'gender':'male',
  'age': 23, 
  'marital status': 'celibe',
  'skills': ['drawing', 'programming', 'thinking'],
  'country': 'italy', 
  'city': 'Paris',
  'address': 'sesame street, 123'
}

print(len(student))
print(type(student['skills']))
student['skills'].append('Cooking')
print(student['skills'])

print(student.keys())
print(student.values())
print(student.items())

student.pop('age')
print(student)

del student
