'''

    Write a function which count number of lines and number of words in a text. All the files are in the data the folder:
        Read obama_speech.txt file and count number of lines and words
        Read michelle_obama_speech.txt file and count number of lines and words
        Read donald_speech.txt file and count number of lines and words
        Read melina_trump_speech.txt file and count number of lines and words

    Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages

    # Your output should look like this
    print(most_spoken_languages(filename='./data/countries_data.json', 10))
    [(91, 'English'),
    (45, 'French'),
    (25, 'Arabic'),
    (24, 'Spanish'),
    (9, 'Russian'),
    (9, 'Portuguese'),
    (8, 'Dutch'),
    (7, 'German'),
    (5, 'Chinese'),
    (4, 'Swahili'),
    (4, 'Serbian')]

    # Your output should look like this
    print(most_spoken_languages(filename='./data/countries_data.json', 3))
    [(91, 'English'),
    (45, 'French'),
    (25, 'Arabic')]

    Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries

    # Your output should look like this
    print(most_populated_countries(filename='./data/countries_data.json', 10))

    [
    {'country': 'China', 'population': 1377422166},
    {'country': 'India', 'population': 1295210000},
    {'country': 'United States of America', 'population': 323947000},
    {'country': 'Indonesia', 'population': 258705000},
    {'country': 'Brazil', 'population': 206135893},
    {'country': 'Pakistan', 'population': 194125062},
    {'country': 'Nigeria', 'population': 186988000},
    {'country': 'Bangladesh', 'population': 161006790},
    {'country': 'Russian Federation', 'population': 146599183},
    {'country': 'Japan', 'population': 126960000}
    ]

    # Your output should look like this

    print(most_populated_countries(filename='./data/countries_data.json', 3))
    [
    {'country': 'China', 'population': 1377422166},
    {'country': 'India', 'population': 1295210000},
    {'country': 'United States of America', 'population': 323947000}
    ]

Exercises: Level 2

    Extract all incoming email addresses as a list from the email_exchange_big.txt file.
    Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output

    # Your output should look like this
    print(find_most_common_words('sample.txt', 10))
    [(10, 'the'),
    (8, 'be'),
    (6, 'to'),
    (6, 'of'),
    (5, 'and'),
    (4, 'a'),
    (4, 'in'),
    (3, 'that'),
    (2, 'have'),
    (2, 'I')]

    # Your output should look like this
    print(find_most_common_words('sample.txt', 5))

    [(10, 'the'),
    (8, 'be'),
    (6, 'to'),
    (6, 'of'),
    (5, 'and')]

    Use the function, find_most_frequent_words to find:
        The ten most frequent words used in Obama's speech
        The ten most frequent words used in Michelle's speech
        The ten most frequent words used in Trump's speech
        The ten most frequent words used in Melina's speech
    Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of Michelle's and Melina's speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of stop words are in the data directory
    Find the 10 most repeated words in the romeo_and_juliet.txt
    Read the hacker news csv file and find out:
        Count the number of lines containing python or Python
        Count the number lines containing JavaScript, javascript or Javascript
        Count the number lines containing Java and not JavaScript
'''

import json, regex, os, csv
from collections import Counter

# Exercise 1

with open('./data/obama_speech.txt') as f:
  text = f.read()
  list_of_words = text.split(' ')
  list_of_lines = text.rstrip().split('\n')
  print(f'The number of lines are {len(list_of_lines)} and the number of words are {len(list_of_words)}')

with open('./data/michelle_obama_speech.txt') as f:
  text = f.read()
  list_of_words = text.split(' ')
  list_of_lines = text.rstrip().split('\n')
  print(f'The number of lines are {len(list_of_lines)} and the number of words are {len(list_of_words)}')
  
with open('./data/donald_speech.txt') as f:
  text = f.read()
  list_of_words = text.split(' ')
  list_of_lines = text.rstrip().split('\n')
  print(f'The number of lines are {len(list_of_lines)} and the number of words are {len(list_of_words)}')  
  
with open('./data/melina_trump_speech.txt') as f:
  text = f.read()
  list_of_words = text.split(' ')
  list_of_lines = text.rstrip().split('\n')
  print(f'The number of lines are {len(list_of_lines)} and the number of words are {len(list_of_words)}')
  
  
def most_spoken_languages(times, filename = './data/countries_data.json'):
  with open(filename, encoding='utf-8') as f:
    countries = json.load(f)
    
    lang_count ={}
    for country in countries:
      for language in country['languages']:
        lang_count[language] = lang_count.get(language, 0) +1
    
    sorted_languages = sorted(lang_count.items(), key= lambda x: x[1], reverse = True)
    return [(count, lang) for lang, count in sorted_languages[:times]] 
    # times indicate how many languages we wnat to show, in this case 10

print(most_spoken_languages(10))
    
def most_populated_countries(times, filename='./data/countries_data.json'):
  with open(filename, encoding='utf-8') as f:
    countries = json.load(f)
  
  list_countries = []
  for country in countries:
    list_countries.append({'country' : country['name'], 'population': country['population']})

  list_countries = sorted(list_countries, key= lambda x: x['population'], reverse = True)
  return list_countries[:times]
  
    
print(most_populated_countries(3))    

#Exercise 2

with open('./data/email_exchanges_big.txt') as f:
  text = f.read()
  regex_email = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
  emails = regex.findall(regex_email, text)
  #print(emails)
  
  
def find_most_common_words(data, times):
  
  if isinstance(data, (str, os.PathLike)):
    with open(data, encoding='utf-8') as f:
      text = f.read()
  elif isinstance(data, str):
    text = data
  else:
    raise TypeError(f'Expected string or path to file, not {type(data)}')
  
  list_words = text.lower().split()
  counter = Counter(list_words)
  sorted_counter = sorted(counter.items(), key=lambda x: (-x[1], x[0])) #deterministic
  return [(count, word) for word, count in sorted_counter[:times]]

print('top 10 in melina:',find_most_common_words('./data/melina_trump_speech.txt', 10))
print('top 10 in michelle:',find_most_common_words('./data/michelle_obama_speech.txt', 10))
print('top 10 in obama:',find_most_common_words('./data/obama_speech.txt', 10))
print('top 10 in donald:',find_most_common_words('./data/donald_speech.txt', 10))
print('top 10 in romeo and juliet:',find_most_common_words('./data/romeo_and_juliet.txt', 10))


with open('./data/hacker_news.csv') as f:
  read_csv = csv.reader(f, delimiter=',')
  header = next(read_csv, None)
  python_count = 0
  js_counter = 0
  total_lines = 0
  java_counter = 0
  
  for row in read_csv:
        total_lines += 1
        line_text = ' '.join(row).lower()
        if 'python' in line_text:
          python_count += 1
        elif 'javascript' in line_text:
          js_counter += 1
        elif 'java'   in line_text:
          java_counter += 1
          


print(f'Strict count (python in the whole row): {python_count}')
print(f'Strict count (javascript in the whole row): {js_counter}')
print(f'Strict count (java in the whole row): {java_counter}')
  