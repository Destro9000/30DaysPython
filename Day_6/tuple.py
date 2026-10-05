# Tuple = ordered and unchangeable

'''Exercises: Level 1
Create an empty tuple
Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
Join brothers and sisters tuples and assign it to siblings
How many siblings do you have?
Modify the siblings tuple and add the name of your father and mother and assign it to family_members

Exercises: Level 2
Unpack siblings and parents from family_members
Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
Change the about food_stuff_tp tuple to a food_stuff_lt list
Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
Slice out the first three items and the last three items from food_stuff_lt list
Delete the food_stuff_tp tuple completely
Check if an item exists in tuple:
Check if 'Estonia' is a nordic country

Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')'''

# _______Exercise 1________

a_tuple = (1,2,3,4,5,6)
numbers = [1,2,3,4,5,6]
a_tuple_1 = tuple(numbers)

brothers = ('Mario', 'Giovanni', 'Mariosca', 'Franco')
sisters = ('Sara', 'Giovanna', 'Grace', 'Mimosa')

siblings = brothers + sisters
print(len(siblings))

siblings = list(siblings)
siblings.append('Mamma')
siblings.append('Papa')
family_members = tuple(siblings)

print(family_members)

# _______Exercise 2________

parents = family_members[-2:]
print(parents)

siblings_2 = family_members[:-2:]
print(siblings_2)

fruits = ('apple','pear','watermelon')
vegetables = ('broccoli', 'green beans', 'potato')
animal_prod = ('food', 'sand', 'toys')
food_stuff_tp = fruits + vegetables + animal_prod

food_stuff_tp = list(food_stuff_tp)
print(food_stuff_tp)

last_3_items = food_stuff_tp[-3:]
print(last_3_items)
first_3_items = food_stuff_tp[0:3]
print(first_3_items)

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
