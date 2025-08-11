#Exercises: Day 20
#1. Read this url and find the 10 most frequent words. romeo_and_juliet = 'https://www.gutenberg.org/cache/epub/1513/pg1513.txt'
import requests, string
from collections import Counter

# Reading url
url = "https://www.gutenberg.org/cache/epub/1513/pg1513.txt"
response = requests.get(url)
response.raise_for_status()
text = response.text

# Clean and break into words : Lowercase and Remove punctuation
text = text.lower()
translator = str.maketrans('', '', string.punctuation)
clean_text = text.translate(translator)
words = clean_text.split()

# Count word frequency
counter = Counter(words)
most_common = counter.most_common(10)
print("The 10 most frequent in words Romeo and Juliet :")
for word, freq in most_common:
    print(f"{word}: {freq}")


#2. Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
#the min, max, mean, median, standard deviation of cats' weight in metric units.
import statistics

url = "https://api.thecatapi.com/v1/breeds"

def cats_weight_stats():
    # Fetch data
    response = requests.get(url)
    response.raise_for_status()  
    cats_data = response.json()
    
    weights = []
    
    for cat in cats_data:
        # weight in format 
        weight_str = cat.get("weight", {}).get("metric", "")
        if weight_str:
            try:
                low, high = map(float, weight_str.split(" - "))
                avg_weight = (low + high) / 2
                weights.append(avg_weight)
            except ValueError:
                pass  
    
    # Calculate statistics
    stats = {
        "min": min(weights),
        "max": max(weights),
        "mean": statistics.mean(weights),
        "median": statistics.median(weights),
        "stdev": statistics.pstdev(weights)  
    }
    
    print('The min, max, mean, median, standard deviation of cats weight in metric units:')
    return stats

print(cats_weight_stats())

#the min, max, mean, median, standard deviation of cats' lifespan in years.

def cats_lifespan_stats():
    # Fetch data
    response = requests.get(url)
    response.raise_for_status()  
    cats_data = response.json()
    
    lifespans = []
    
    for cat in cats_data:
        # life_span in format 
        life_span_str = cat.get("life_span", "")
        if life_span_str:
            try:
                low, high = map(float, life_span_str.split(" - "))
                avg_lifespan = (low + high) / 2
                lifespans.append(avg_lifespan)
            except ValueError:
                pass  
    
    # Calculate statistics
    stats = {
        "min": min(lifespans),
        "max": max(lifespans),
        "mean": statistics.mean(lifespans),
        "median": statistics.median(lifespans),
        "stdev": statistics.pstdev(lifespans)  
    }
    
    print('The min, max, mean, median, standard deviation of cats lifespan in years:')
    return stats

print(cats_lifespan_stats())


#Create a frequency table of country and breed of cats

def country_breed_frequency():
    url = 'https://api.thecatapi.com/v1/breeds'
    response = requests.get(url)
    response.raise_for_status()
    breeds = response.json()
    
    # Extract countries of origin for each breed
    countries = [breed.get("origin", "Unknown") for breed in breeds]
    
    # Count frequency of each country
    freq = Counter(countries)
    
    # Convert to sorted list (most frequent first)
    freq_sorted = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    print("Country\t\Frequency of Cat Breeds")
    print("-----------------------------------")
    for country, count in freq_sorted:
        print(f"{country:15} {count}")
    
country_breed_frequency()

#3. Read the countries API and find
#i. the 10 largest countries
 #Find countries
url = "https://countries-api-abhishek.vercel.app/countries"

response = requests.get(url)
response.raise_for_status()
countries_json = response.json()
countries_data = countries_json.get("data", {})

def get_ten_largest_countries():

    #Find countries, sorted and retrieve 10 largest 
    countries_area = [country for country in countries_data]
    sorted_countries = sorted(countries_area, key=lambda x: x.get("area"), reverse=True)
    most_ten_largest_countries = sorted_countries[:10]
    
    print("The 10 largest countries are:")
    return most_ten_largest_countries

print(get_ten_largest_countries())


#i. the 10 most spoken languages

def get_ten_most_spok_lang():

    #Get languages list
    countries_lang = [country_lg.get("languages", {}) for country_lg in countries_data]
    #Get languages string
    countries_lang_str = [lang_str for lang_list in countries_lang for lang_str in lang_list]

    #Count
    lang_count = Counter(countries_lang_str)
    most_spoken = lang_count.most_common(10)

    print("The 10 most spoken languages:")
    return most_spoken

print(get_ten_most_spok_lang())

#iii. the total number of languages in the countries API

def total_number_lang():

    #Get languages list
    countries_lang = [country_lg.get("languages", {}) for country_lg in countries_data]
    #Get languages string
    countries_lang_str = [lang_str for lang_list in countries_lang for lang_str in lang_list]

    #Count
    lang_count = Counter(countries_lang_str)
    total_number = sum(lang_count.values())

    print("The total number of languages in the countries API:")
    return total_number

print(total_number_lang())


#4. UCI is one of the most common places to get data sets for data science and machine learning. Read the content of UCL
# (https://archive.ics.uci.edu/datasets). Without additional libraries it will be difficult, so you may try it with BeautifulSoup4

from bs4 import BeautifulSoup

def most_common_places():
    url = "https://archive.ics.uci.edu/datasets"

    response = requests.get(url)
    status = response.status_code
    data_sets = response.text

    # Create BeautifulSoup objet
    soup = BeautifulSoup(data_sets, "html.parser")

    # Get data
    title = soup.title.text
    page_text = soup.get_text(strip=True)

    print(f"Places data set Title: {title}")
    return page_text

print(most_common_places())