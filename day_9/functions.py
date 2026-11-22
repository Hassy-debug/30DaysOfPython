#Day 9 level 1
def add_two_numbers(a, b):                    
    return a + b
print(add_two_numbers(3, 4))                  

def area_of_circle(r):                        
    return 3.14 * r * r
print(area_of_circle(5))                      

def add_all_nums(*nums):                      
    total = 0
    for n in nums:
        if not isinstance(n, (int, float)):
            return "Error: all arguments must be numbers."
        total += n
    return total
print(add_all_nums(1, 2, 3))                  
print(add_all_nums(1, 'a', 3))                

def convert_celsius_to_fahrenheit(c):        
    return c * 9 / 5 + 32
print(convert_celsius_to_fahrenheit(100))     

def check_season(month):                     
    month = month.capitalize()
    if month in ('September', 'October', 'November'):
        return 'Autumn'
    elif month in ('December', 'January', 'February'):
        return 'Winter'
    elif month in ('March', 'April', 'May'):
        return 'Spring'
    elif month in ('June', 'July', 'August'):
        return 'Summer'
    return 'Invalid month'
print(check_season('march'))                  

def calculate_slope(x1, y1, x2, y2):         
    return (y2 - y1) / (x2 - x1)
print(calculate_slope(2, 2, 6, 10))           

import math                                   
def solve_quadratic_eqn(a, b, c):
    d = b**2 - 4*a*c                          
    if d < 0:
        return "No real solution"
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    return x1, x2
print(solve_quadratic_eqn(1, -3, 2))  

def print_list(lst):                         
    for item in lst:
        print(item)

def reverse_list(lst):                        
    new = []
    for i in range(len(lst) - 1, -1, -1):
        new.append(lst[i])
    return new
print(reverse_list([1, 2, 3, 4, 5]))          
print(reverse_list(["A", "B", "C"]))          

def capitalize_list_items(lst):              
    return [item.capitalize() for item in lst]
print(capitalize_list_items(['potato', 'tomato']))

def add_item(lst, item):                      
    new = lst.copy()
    new.append(item)
    return new
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))
print(add_item([2, 3, 7, 9], 5))              

def remove_item(lst, item):                   
    new = lst.copy()
    new.remove(item)
    return new
print(remove_item(food_staff, 'Mango'))       
print(remove_item([2, 3, 7, 9], 3))           

def sum_of_numbers(n):                        
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
print(sum_of_numbers(5), sum_of_numbers(10), sum_of_numbers(100))   

def sum_of_odds(n):                           
    return sum(i for i in range(1, n + 1) if i % 2 != 0)

def sum_of_even(n):                           
    return sum(i for i in range(1, n + 1) if i % 2 == 0)
print(sum_of_odds(10), sum_of_even(10))       

#level 2
def evens_and_odds(n):
    evens = odds = 0
    for i in range(n + 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    return f"The number of odds are {odds}.\nThe number of evens are {evens}."
print(evens_and_odds(100))                    

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
print(factorial(5))                           

def is_empty(x):
    return len(x) == 0
print(is_empty([]), is_empty("hi"))           

def calculate_mean(lst):
    return sum(lst) / len(lst)

def calculate_median(lst):
    s = sorted(lst)
    n = len(s)
    if n % 2 == 0:
        return (s[n // 2 - 1] + s[n // 2]) / 2
    return s[n // 2]

def calculate_mode(lst):
    best = max(lst, key=lst.count)
    return best

def calculate_range(lst):
    return max(lst) - min(lst)

def calculate_variance(lst):
    m = calculate_mean(lst)
    return sum((x - m) ** 2 for x in lst) / len(lst)

def calculate_std(lst):
    return calculate_variance(lst) ** 0.5
data = [1, 2, 2, 3, 4]
print(calculate_mean(data), calculate_median(data), calculate_mode(data))
print(calculate_range(data), calculate_variance(data), calculate_std(data))

#level 3
import keyword


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(7), is_prime(10))            

def all_unique(lst):
    return len(lst) == len(set(lst))
print(all_unique([1, 2, 3]), all_unique([1, 2, 2]))

def same_data_type(lst):
    return len(set(type(x) for x in lst)) <= 1
print(same_data_type([1, 2, 3]), same_data_type([1, 'a']))

def is_valid_variable(name):
    return name.isidentifier() and not keyword.iskeyword(name)
print(is_valid_variable('first_name'), is_valid_variable('1name'), is_valid_variable('for'))

from countries_data import countries_data

def most_spoken_languages(data, n=10):
    counts = {}
    for country in data:
        for lang in country['languages']:
            counts[lang] = counts.get(lang, 0) + 1
    ranked = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return ranked[:n]

def most_populated_countries(data, n=10):
    ranked = sorted(data, key=lambda c: c['population'], reverse=True)
    return [(c['name'], c['population']) for c in ranked[:n]]

print(most_spoken_languages(countries_data, 10))
print(most_populated_countries(countries_data, 10))