# day 114 level 1 exercise

import random
import string

chars = string.ascii_letters + string.digits      

def random_user_id():                             
    return ''.join(random.choice(chars) for _ in range(6))
print(random_user_id())

def user_id_gen_by_user():                        
    n = int(input("Number of characters: "))
    count = int(input("Number of IDs: "))
    ids = [''.join(random.choice(chars) for _ in range(n)) for _ in range(count)]
    return '\n'.join(ids)
print(user_id_gen_by_user())                      

def rgb_color_gen():                              
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"
print(rgb_color_gen())

#level 2

def list_of_hexa_colors(n):
    return ['#' + ''.join(random.choice('0123456789abcdef') for _ in range(6))
            for _ in range(n)]

def list_of_rgb_colors(n):
    return [f"rgb({random.randint(0,255)}, {random.randint(0,255)}, {random.randint(0,255)})"
            for _ in range(n)]

def generate_colors(kind, n):
    if kind == 'hexa':
        return list_of_hexa_colors(n)
    elif kind == 'rgb':
        return list_of_rgb_colors(n)
    return "Choose 'hexa' or 'rgb'"

print(generate_colors('hexa', 3))
print(generate_colors('hexa', 1))
print(generate_colors('rgb', 3))
print(generate_colors('rgb', 1))

#level 3

def shuffle_list(lst):
    new = lst.copy()          
    random.shuffle(new)
    return new
print(shuffle_list([1, 2, 3, 4, 5]))

def seven_unique_numbers():
    return random.sample(range(10), 7)    
print(seven_unique_numbers())