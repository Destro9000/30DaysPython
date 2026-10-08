'''
  Declare an empty list
  Declare a list with more than 5 items
  Find the length of your list
  Get the first item, the middle item and the last item of the list
  Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
  Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
  Print the list using print()
  Print the number of companies in the list
  Print the first, middle and last company
  Print the list after modifying one of the companies
  Add an IT company to it_companies
  Insert an IT company in the middle of the companies list
  Change one of the it_companies names to uppercase (IBM excluded!)
  Join the it_companies with a string '#;  '
  Check if a certain company exists in the it_companies list.
  Sort the list using sort() method
  Reverse the list in descending order using reverse() method
  Slice out the first 3 companies from the list
  Slice out the last 3 companies from the list
  Slice out the middle IT company or companies from the list
  Remove the first IT company from the list
  Remove the middle IT company or companies from the list
  Remove the last IT company from the list
  Remove all IT companies from the list
  Destroy the IT companies list
  Join the following lists:
    front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    back_end = ['Node','Express', 'MongoDB']
  After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.

  _____Exercises: Level 2_____
  
  The following is a list of 10 students ages:
      ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

  Sort the list and find the min and max age
  Add the min age and the max age again to the list
  Find the median age (one middle item or two middle items divided by two)
  Find the average age (sum of all items divided by their number )
  Find the range of the ages (max minus min)
  Compare the value of (min - average) and (max - average), use abs() method
  Find the middle country(ies) in the countries list
  Divide the countries list into two equal lists if it is even if not one more country for the first half.
  ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
  '''

#------Exercise 1-------

list_1 = []
list_2 = ['Cat', 'Dog', 'Hamster', 'Parrot', 'Guinea Pig']
print(len(list_1))
print(len(list_2))
print(list_2[0])
print(list_2[round(len(list_2) / 2)])
print(list_2[-1])


mixed_data_types = ['Destro9000', 26, 178, 'Celibe', 'Sesame Street,141']
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' , 'Amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[0])
print(it_companies[round(len(it_companies) / 2)])
print(it_companies[-1])
it_companies[0] = 'Nvidia'
print(it_companies)

it_companies.append('Samsung')
print(it_companies)

it_companies.insert(2,'Lenovo')
print(it_companies)

it_companies[2].upper()
print(it_companies)

print('#'.join(it_companies))

print('Banana' in it_companies)
print('Lenovo' in it_companies)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

print(it_companies[0:3:])
print(it_companies[-3::])
print(it_companies[3:-3:])

print(it_companies.pop())
print(it_companies.pop())
print(it_companies.pop(round(len(it_companies) / 2)))

print(it_companies.clear())
del it_companies
# print(it_companies) this will throw an error because the list has been deleted so it doesnt exist anymore.

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
print(front_end)

full_stack = front_end.copy()
full_stack.insert(5,'SQL')
full_stack.insert(5,'Python')
print(full_stack)

#Exercise 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
min = ages[0]
max = ages[len(ages)-1]

print(ages)

ages.append(min)
ages.append(max)
print(ages)

ages.sort()
if len(ages)%2 == 0:
  median_value = ages[round(len(ages) / 2)]
else:
  median_value = (ages[len(ages) / 2] + ages[(len(ages) / 2)+1])/2
  
print(median_value)
sum = 0
for item in ages:
  sum += item

average = sum / len(ages)
print(average)

range_ages = max-min 
print(range_ages)

print(abs(min-average) == abs(max-average))


countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
[ch, rus, us, *scan] = countries
print(ch)
print(rus)
print(us)
print(*scan)


