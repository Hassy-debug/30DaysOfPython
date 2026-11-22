# day 13 exercise 2 level 1

import json
from collections import Counter

def count_lines_words(filename):                        
    with open(filename, encoding='utf-8') as f:
        text = f.read()
    return len(text.splitlines()), len(text.split())

for file in ['obama_speech.txt', 'michelle_obama_speech.txt',
             'donald_speech.txt', 'melina_trump_speech.txt']:
    print(file, count_lines_words('./data/' + file))

def most_spoken_languages(filename, n):                 
    with open(filename, encoding='utf-8') as f:
        data = json.load(f)
    counts = Counter(lang for country in data for lang in country['languages'])
    return [(count, lang) for lang, count in counts.most_common(n)]
print(most_spoken_languages('./data/countries_data.json', 10))

def most_populated_countries(filename, n):              
    with open(filename, encoding='utf-8') as f:
        data = json.load(f)
    ranked = sorted(data, key=lambda c: c['population'], reverse=True)
    return [{'country': c['name'], 'population': c['population']} for c in ranked[:n]]
print(most_populated_countries('./data/countries_data.json', 10))

#level 2
import re

with open('./data/email_exchanges_big.txt', encoding='utf-8') as f:    # Q4
    text = f.read()
emails = re.findall(r'^From:.*?([\w\.-]+@[\w\.-]+)', text, re.MULTILINE)
print(emails)

def find_most_common_words(source, n):                  
    if source.endswith('.txt'):
        with open(source, encoding='utf-8') as f:
            source = f.read()
    words = re.findall(r"[A-Za-z']+", source)
    counts = Counter(words)
    return [(count, word) for word, count in counts.most_common(n)]
print(find_most_common_words('./data/obama_speech.txt', 10))

for file in ['obama_speech.txt', 'michelle_obama_speech.txt',
             'donald_speech.txt', 'melina_trump_speech.txt']:    
    print(file, find_most_common_words('./data/' + file, 10))

from stop_words import stop_words          

def clean_text(text):
    return re.sub(r'[^a-z\s]', '', text.lower())

def remove_support_words(text):
    return [w for w in text.split() if w not in stop_words]

def check_text_similarity(a, b):
    if a.endswith('.txt'):
        a = open(a, encoding='utf-8').read()
    if b.endswith('.txt'):
        b = open(b, encoding='utf-8').read()
    set_a = set(remove_support_words(clean_text(a)))
    set_b = set(remove_support_words(clean_text(b)))
    return len(set_a & set_b) / len(set_a | set_b) * 100

print(check_text_similarity('./data/michelle_obama_speech.txt',
                            './data/melina_trump_speech.txt'))   

print(find_most_common_words('./data/romeo_and_juliet.txt', 10))  

python_lines = js_lines = java_lines = 0
with open('./data/hacker_news.csv', encoding='utf-8') as f:
    for line in f:
        if re.search(r'[Pp]ython', line):
            python_lines += 1
        if re.search(r'[Jj]ava[Ss]cript', line):
            js_lines += 1
        if re.search(r'[Jj]ava(?![Ss]cript)', line):
            java_lines += 1
print(python_lines, js_lines, java_lines)