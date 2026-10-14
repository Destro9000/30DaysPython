'''

Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

output
[1, 2, 3, 4, 5, 6, 7, 8, 9]

Using list comprehension create the following list of tuples:

[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]

Flatten the following list to a new list:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

Change the following list to a list of dictionaries:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[{'country': 'FINLAND', 'city': 'HELSINKI'},
{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
{'country': 'NORWAY', 'city': 'OSLO'}]

Change the following list of lists to a list of concatenated strings:

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output
['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']

Write a lambda function which can solve a slope or y-intercept of linear functions.
'''

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_numbers = [i for i in numbers if i <= 0]
print(filtered_numbers)

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lst = [i for k in list_of_lists for i in k]
print(lst)

num = [0,1,2,3,4,5,6,7,8,9,10]
new_list = [tuple([k**i for i in range(6)]) for k in num ]
print(new_list)


countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries = [[i[0].upper(), i[0][0:3].upper(), i[1].upper()] for sublist in countries for i in sublist ]
print(flattened_countries)


names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
name_joined = [ ' '.join(i) for sublist in names for i in sublist]
print(name_joined)

dictionary_countries = [{'country': i[0], 'city': i[1]} for sublist in countries for i in sublist ]
print(dictionary_countries)

slope = lambda x1,x2,y1,y2: (y2-y1)/(x2-x1)
y_intercept = lambda y1, x1, m: y1-x1*m