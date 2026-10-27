'''
    What is the most frequent word in the following paragraph?

    paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.

    [
    (6, 'love'),
    (5, 'you'),
    (3, 'can'),
    (2, 'what'),
    (2, 'teaching'),
    (2, 'not'),
    (2, 'else'),
    (2, 'do'),
    (2, 'I'),
    (1, 'which'),
    (1, 'to'),
    (1, 'the'),
    (1, 'something'),
    (1, 'if'),
    (1, 'give'),
    (1, 'develop'),
    (1, 'capabilities'),
    (1, 'application'),
    (1, 'an'),
    (1, 'all'),
    (1, 'Python'),
    (1, 'If')
    ]

    The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.

points = ['-12', '-4', '-3', '-1', '0', '4', '8']
sorted_points =  [-12, -4, -3, -1, -1, 0, 2, 4, 8]
distance = 8 -(-12) # 20

Exercises: Level 2

    Write a pattern which identifies if a string is a valid python variable

    is_valid_variable('first_name') # True
    is_valid_variable('first-name') # False
    is_valid_variable('1first_name') # False
    is_valid_variable('firstname') # True

Exercises: Level 3

    Clean the following text. After cleaning, count three most frequent words in the string.

    sentence = 

    print(clean_text(sentence));
    I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
    print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]
'''
import regex
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
regex1 = r'[a-zA-Z]+'

match = regex.findall(regex1,paragraph,regex.I)
sorted_match = list(map(lambda word: (match.count(word), word),match))
sorted_match.sort(reverse=True)
print(sorted_match)

string1 = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.'
numbers = regex.findall(r'-?\d+', string1, regex.I)

numbers = list(map(lambda number: int(number), numbers))
numbers.sort()
print(numbers)
distance = numbers[len(numbers)-1] -(numbers[0]) 
print(distance)

#Exercise_2
regex_variable = r'^[a-zA-Z_]+[A-Za-z0-9_]+$'
variable_name = 'Bananasplit'
match_var = regex.search(regex_variable, variable_name, regex.I)
print(False if match_var == None else True)

#Exercise_3
dirty_string = """%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?"""
cleaned_string = regex.sub(r'[@|%|#|&|;|$]','',dirty_string)
print(cleaned_string)

def three_most_frequent_words(sentence):
    list1 = list(map(lambda word: (sentence.count(word), word),sentence.split(' ')))
    print(list1)
    list1.sort(reverse=True)
    list1 = list(dict.fromkeys(list1))
    return list1[0:3]

print(three_most_frequent_words(cleaned_string))