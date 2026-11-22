#day10 level 1

# Q1; map applies a function to every item and returns a new list of the same length.
# filter keeps only the items that pass a test, so the result can be shorter.
# reduce combines all the items into a single value, for example a sum.

# Q2; A higher-order function takes a function as an argument or returns a function.
# A closure is an inner function that remembers the variables of its outer function.
# A decorator is a function that adds extra behaviour to another function.

from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def callback(n):                       

    return n ** 2
print(list(map(callback, numbers)))
def outer(x):                         
    def inner(y):
        return x + y                   
    return inner
add5 = outer(5)
print(add5(3))                        

def shout(func):                       
    def wrapper():
        return func().upper()
    return wrapper

@shout
def greet():
    return "hello"
print(greet())             
for country in countries:
    print(country)
for name in names:
    print(name)
for number in numbers:
    print(number)  

    #level 2
print(list(map(lambda c: c.upper(), countries)))        
print(list(map(lambda n: n ** 2, numbers)))             
print(list(map(lambda n: n.upper(), names)))            

print(list(filter(lambda c: 'land' in c, countries)))  

print(list(filter(lambda c: len(c) == 6, countries)))   
print(list(filter(lambda c: len(c) >= 6, countries)))   
print(list(filter(lambda c: c.startswith('E'), countries))) 



total = reduce(lambda a, b: a + b,
               map(lambda n: n ** 2,
                   filter(lambda n: n % 2 == 0, numbers)))
print(total)    

def get_string_lists(lst):                              
    return list(filter(lambda x: isinstance(x, str), lst))
print(get_string_lists([1, 'a', 2.5, 'hello', True]))   

print(reduce(lambda a, b: a + b, numbers))              

sentence = reduce(lambda a, b: a + ', ' + b, countries[:-1])     

sentence += ', and ' + countries[-1] + ' are north European countries'
print(sentence)


from countries import countries as all_countries

def categorize_countries(pattern):                      
    return [c for c in all_countries if pattern in c]
print(categorize_countries('land'))
print(categorize_countries('ia'))
print(categorize_countries('stan'))

def count_by_first_letter():                            

    result = {}
    for c in all_countries:
        letter = c[0]
        result[letter] = result.get(letter, 0) + 1
    return result
print(count_by_first_letter())

def get_first_ten_countries():                          

    return all_countries[:10]

def get_last_ten_countries():                           
    return all_countries[-10:]
print(get_first_ten_countries())
print(get_last_ten_countries())


#level 3
from countries_data import countries_data

print(sorted(countries_data, key=lambda c: c['name'])[:5])        
print([c['name'] for c in sorted(countries_data, key=lambda c: c['capital'])][:5])   
print([c['name'] for c in sorted(countries_data, key=lambda c: c['population'])][:5])   

counts = {}
for c in countries_data:

    for lang in c['languages']:
        counts[lang] = counts.get(lang, 0) + 1
top_langs = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:10]
print(top_langs)                                                   

top_pop = sorted(countries_data, key=lambda c: c['population'], reverse=True)[:10]

print([(c['name'], c['population']) for c in top_pop])             