#Day 7 exercise level 1
age = int(input("Enter your age: "))                      
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18 - age} more years to learn to drive.")

my_age = 25                                                
your_age = int(input("Enter your age: "))
if my_age > your_age:
    diff = my_age - your_age
    if diff == 1:
        print("I am 1 year older than you.")
    else:
        print(f"I am {diff} years older than you.")
elif your_age > my_age:
    diff = your_age - my_age
    if diff == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {diff} years older than me.")
else:
    print("We are the same age.")

a = int(input("Enter number one: "))                       
b = int(input("Enter number two: "))
if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")

#level 2
score = int(input("Enter your score: "))                   
if score >= 80:
    print("A")
elif score >= 70:
    print("B")
elif score >= 60:
    print("C")
elif score >= 50:
    print("D")
else:
    print("F")

month = input("Enter a month: ").capitalize()             
if month in ('September', 'October', 'November'):
    print("The season is Autumn.")
elif month in ('December', 'January', 'February'):
    print("The season is Winter.")
elif month in ('March', 'April', 'May'):
    print("The season is Spring.")
elif month in ('June', 'July', 'August'):
    print("The season is Summer.")
else:
    print("That is not a valid month.")

fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Enter a fruit: ").lower()
if new_fruit in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(new_fruit)
    print(fruits)

#level 3
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {'street': 'Space street', 'zipcode': '02210'}
}

if 'skills' in person:
    skills = person['skills']
    print(skills[len(skills) // 2])                       

    if 'Python' in skills:
        print("The person has Python skill.")
    else:
        print("The person does not have Python skill.")

    if set(skills) == {'JavaScript', 'React'}:
        print('He is a front end developer')
    elif {'Node', 'Python', 'MongoDB'}.issubset(skills):
        print('He is a backend developer')
    elif {'React', 'Node', 'MongoDB'}.issubset(skills):
        print('He is a fullstack developer')
    else:
        print('unknown title')

if person['is_marred'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in Finland. He is married.")