'''Exercises: Level 1

    Iterate 0 to 10 using for loop, do the same using while loop.

    Iterate 10 to 0 using for loop, do the same using while loop.

    Write a loop that makes seven calls to print(), so we get on the output the following triangle:

      #
      ##
      ###
      ####
      #####
      ######
      #######

    Use nested loops to create the following:

    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #

    Print the following pattern:

    0 x 0 = 0
    1 x 1 = 1
    2 x 2 = 4
    3 x 3 = 9
    4 x 4 = 16
    5 x 5 = 25
    6 x 6 = 36
    7 x 7 = 49
    8 x 8 = 64
    9 x 9 = 81
    10 x 10 = 100

    Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

    Use for loop to iterate from 0 to 100 and print only even numbers

    Use for loop to iterate from 0 to 100 and print only odd numbers

Exercises: Level 2

    Use for loop to iterate from 0 to 100 and print the sum of all numbers.

The sum of all numbers is 5050.

    Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

    The sum of all evens is 2550. And the sum of all odds is 2500.

Exercises: Level 3

    Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
    This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
    Go to the data folder and use the countries_data.py file.
        What are the total number of languages in the data
        Find the ten most spoken languages from the data
        Find the 10 most populated countries in the world
'''
# ____Exercise 1_____

for i in range(11):
  print(i)
  
i =  0
while i <= 10:
  print(i)
  i += 1
  
for i in range(10,-1,-1):
  print(i)
  
y = 10
while y >= 0:
  print(y)
  y -= 1
  
  
string = '#'

for i in range(10):
  print(string)
  string += '#'
  
  
string2 = '#'

for i in range(9):
  
  for y in range(8):
    string2 += ' #'
  
  print(string2)
  string2 = '#'
    
  
for i in range(11):
  print(f'{i} x {i} = {i*i}')
  

list = ['Python', 'Numpy','Pandas','Django', 'Flask']

for item in list:
  print(item)
  
for i in range(101):
  if(i % 2 == 0):
    print(i)
    
for i in range(101):
  if(not i % 2 == 0):
    print(i)
    
  #_______Exercise 2________
sum = 0
i = 0

while i <=100:
  sum += i
  i+=1
else:
  print(f'The sum of the first 100 numbers is {sum}')
  
sum_even = 0
sum_odd = 0
for i in range(101):
  if i % 2 ==0:
    sum_even += i
  else:
    sum_odd += i
else:
  print(f'The sum of the even numbers is {sum_even}, while the sum of the odd numbers is {sum_odd}')
    
    
#______ Exercise 3 ________


countries = [
  'Afghanistan','Albania','Algeria','Andorra','Angola','Antigua and Barbuda',
  'Argentina','Armenia','Australia','Austria','Azerbaijan','Bahamas','Bahrain',
  'Bangladesh','Barbados','Belarus','Belgium','Belize','Benin','Bhutan','Bolivia',
  'Bosnia and Herzegovina','Botswana','Brazil','Brunei','Bulgaria','Burkina Faso','Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];
for country in countries:
  if country.find('land') != -1:
    print(country)
    
    
fruits = ['banana', 'orange', 'mango', 'lemon'];
fruit_rev = []


i = len(fruits)-1
while i >= 0:
  fruit_rev.append(fruits[i])
  print(fruit_rev)
  i-= 1
