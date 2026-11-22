#day15 question 1

import requests
import re
from collections import Counter

url = 'http://www.gutenberg.org/files/1112/1112.txt'
text = requests.get(url).text

words = re.findall(r"[A-Za-z']+", text.lower())
print(Counter(words).most_common(10))

#quesion 2

import statistics

cats_api = 'https://api.thecatapi.com/v1/breeds'
cats = requests.get(cats_api, headers={'x-api-key': 'PASTE YOUR OWN KEY HERE'}).json() #Since I am uploading on Github I cant paste my key here
print(cats)

if not isinstance(cats, list):
    print("The API did not return a list:", cats)
    raise SystemExit

def middle(range_text):                   
    nums = [float(n) for n in re.findall(r'\d+\.?\d*', range_text)]
    if not nums:
        return None
    return sum(nums) / len(nums)

def describe(values):
    return {
        'min': min(values), 'max': max(values),
        'mean': statistics.mean(values), 'median': statistics.median(values),
        'std': statistics.stdev(values),
    }

weights = [w for w in (middle(c['weight']['metric']) for c in cats if c.get('weight')) if w]
print(describe(weights))

lifespans = [l for l in (middle(c['life_span']) for c in cats if c.get('life_span')) if l]
print(describe(lifespans))
             

countries = Counter(c['origin'] for c in cats if c.get('origin'))
print(countries)                          

breeds_by_country = {}
for c in cats:
    breeds_by_country.setdefault(c.get('origin', 'Unknown'), []).append(c['name'])
print(breeds_by_country)                  # breeds grouped by country

#question 3
import json
from collections import Counter

with open('countries_data.json', encoding='utf-8') as f:
    data = json.load(f)

largest = sorted(data, key=lambda c: c.get('area', 0), reverse=True)[:10]
print([(c['name'], c.get('area')) for c in largest])      

lang_counts = Counter(lang for c in data for lang in c['languages'])
print(lang_counts.most_common(10))                        
print(len(lang_counts))                                   

# The original restcountries API link is no longer available,
# so I used the local countries_data.json file instead.


# question 4

import requests
from bs4 import BeautifulSoup

url = 'https://archive.ics.uci.edu/ml/datasets.php'
page = requests.get(url)
print("Status:", page.status_code)              

soup = BeautifulSoup(page.text, 'html.parser')
print(soup.title.text if soup.title else "No title")

for link in soup.find_all('a')[:20]:            # getting thefirst 20 links on the page
    print(link.get('href'), '|', link.text.strip())