'''Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
the min, max, mean, median, standard deviation of cats' weight in metric units.
the min, max, mean, median, standard deviation of cats' lifespan in years.
Create a frequency table of country and breed of cats
Read the countries API and find
the 10 largest countries
the 10 most spoken languages
the total number of languages in the countries API
UCI is one of the most common places to get data sets for data science and machine learning. Read the content of UCL (https://archive.ics.uci.edu/ml/datasets.php). Without additional libraries it will be difficult, so you may try it with BeautifulSoup4'''

import requests
from collections import Counter

url = 'http://www.gutenberg.org/files/1112/1112.txt'

response = requests.get(url)
data = response.text
print(data)

print(type(data))
list_most_common = Counter(data.split(' ')).most_common(10)
print(list_most_common)