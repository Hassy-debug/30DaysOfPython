# Day 11
#Exception handling and packing unpacking execise

names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']

*nordic_countries, es, ru = names

print(nordic_countries)   # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
print(es)                 #Estonnia
print(ru)                 # Russia
try:
    age = int(input("Enter your age: "))
    print(10 / age)
except ValueError:
    print("Please enter a number, not text.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
else:
    print("No error happened.")
finally:
    print("This always runs.")
def total(*numbers):          
    return sum(numbers)
    print(total(1, 2, 3, 4))      

def profile(**info):          # packing: keyword arguments collected into a dictionary
    return info
print(profile(name='Hassana', city='Zaria'))

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion']
print([{'fruit': f, 'veg': v} for f, v in zip(fruits, vegetables)])

