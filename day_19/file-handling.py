#Exercises: Day 19

#1. Write a function which count number of lines and number of words in a text. All the files are in the data the folder:
"""a) Read obama_speech.txt file and count number of lines and words 
   b) Read michelle_obama_speech.txt file and count number of lines and words 
   c) Read donald_speech.txt file and count number of lines and words 
   d) Read melina_trump_speech.txt file and count number of lines and words
"""

def count_line_word(filenama):
  with open(f'../data/{filenama}') as f:
      file_read = f.read()
      number_lines = len(file_read.splitlines())
      number_words = len(file_read.split())
      return (f'In {filenama} file, there are {number_lines} lines and {number_words} words')


print(count_line_word('obama_speech.txt'))
print(count_line_word('michelle_obama_speech.txt'))
print(count_line_word('donald_speech.txt'))
print(count_line_word('melina_trump_speech.txt'))

#2. Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
import json
from collections import Counter

def most_spoken_languages(filename, number_countries):
    
    # Read JSON data
    with open(filename, "r", encoding="utf-8") as f:
       countries = json.load(f)
       
    # Count all languages
    language_counter = Counter()
    for country in countries:
        for lang in country.get("languages", []):
            language_counter[lang] += 1
    
    # Get top number_countries languages
    most_common_langs = language_counter.most_common(number_countries)
    
    return most_common_langs

print(most_spoken_languages('../data/countries_data.json', 10))
print(most_spoken_languages('../data/countries_data.json', 3))

#3. Read the countries_data.json data file in data directory, create a function that
# creates a list of the ten most populated countries

def most_populated_countries(filename, number_countries):
    
    # Read JSON data
    with open(filename, "r", encoding="utf-8") as f:
       countries = json.load(f)
       
     # Sort countries by population (descending order)
    sorted_countries = sorted(
        countries,
        key=lambda x: x.get("population", 0),
        reverse=True
    )
    
    # Get top number_countries
    number = number_countries
    top_number = sorted_countries[:number]
    
    # Create a list of tuples (country, population)
    return [(country["name"], country["population"]) for country in top_number]

print(most_populated_countries(filename='../data/countries_data.json', number_countries=10))
print(most_populated_countries(filename='../data/countries_data.json', number_countries=3))
    
