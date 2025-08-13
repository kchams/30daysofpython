#Exercises: Day 22
#1. Scrape the following website and store the data as json file(url ='http://www.bu.edu/president/boston-university-facts-stats/').

import requests
from bs4 import BeautifulSoup
import json

url ='http://www.bu.edu/president/boston-university-facts-stats/'

response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')

print(soup.title)
print(soup.title.get_text())

print(response.status_code)
#tables = soup.find_all('table', {'cellpadding':'3'})
print(response.headers)
#data_json = response.json()

facts_data = []
for li in soup.find_all('li'):
    text = li.get_text(strip=True)
    if text:  # Avoid empty lines
        facts_data.append(text)

print(facts_data)

with open('bu_facts.json', 'w', encoding='utf-8') as f:
    json.dump(facts_data, f, ensure_ascii=False, indent=4)

print(f"Scraped {len(facts_data)} facts and saved to bu_facts.json")