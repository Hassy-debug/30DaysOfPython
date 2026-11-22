#Day 2: 30 Days of Python Programming
first_name = "Hassana"
last_name = "Abdullahi"
full_name = first_name + " " + last_name
country = "Nigeria"
city = "Zaria"
age = 21
year = 2026
is_married = False
is_true = True
is_light_on = False
a, b, c = 1, 2, 3           #multiple variable

print(type(first_name), type(last_name), type(country), type(city), type(age), type(year), type(is_married))
print(len(first_name))
print(len(first_name) > len(last_name))

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two
print(total, diff, product, division, remainder, exp, floor_division)

pi = 3.14
radius = 30
area_of_circle = pi * radius ** 2
circum_of_circle = 2 * pi * radius
print(area_of_circle, circum_of_circle)
radius = float(input("Enter radius: "))
print(pi * radius ** 2)

first_name = input("First name: ")
last_name = input("Last name: ")
country = input("Country: ")
age = input("Age: ")

help("keywords")