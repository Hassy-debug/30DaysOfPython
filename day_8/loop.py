#day 8 level1
for i in range(11):          
    print(i)

n = 0
while n <= 10:
    print(n)
    n += 1

for i in range(10, -1, -1):  
    print(i)

n = 10
while n >= 0:
    print(n)
    n -= 1

for i in range(1, 8):        
    print('#' * i)

for row in range(8):                 
    for col in range(8):
        print('#', end=' ')
    print()

for i in range(11):                  
    print(f"{i} x {i} = {i * i}")

for tool in ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']:  
    print(tool)

for i in range(0, 101, 2):           
    print(i)

for i in range(1, 101, 2):           
    print(i)

#Level 2
total = 0
for i in range(101):
    total += i
print(f"The sum of all numbers is {total}.")      

evens = 0
odds = 0
for i in range(101):
    if i % 2 == 0:
        evens += i
    else:
        odds += i
print(f"The sum of all evens is {evens}. And the sum of all odds is {odds}.")  

#level3
from countries import countries                    
for country in countries:
    if 'land' in country:
        print(country)

fruits = ['banana', 'orange', 'mango', 'lemon']
for fruit in fruits[::-1]:
    print(fruit)

from countries_data import countries_data          

languages = set()
counts = {}
for country in countries_data:
    for lang in country['languages']:
        languages.add(lang)
        counts[lang] = counts.get(lang, 0) + 1
print(len(languages))                                

top_languages = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:10]
print(top_languages)                                 

top_pop = sorted(countries_data, key=lambda c: c['population'], reverse=True)[:10]
for c in top_pop:
    print(c['name'], c['population'])                