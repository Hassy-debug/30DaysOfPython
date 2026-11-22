#day 12 level 111

import re
from collections import Counter

paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."

words = re.findall(r'\w+', paragraph)
counts = Counter(words)
result = sorted([(count, word) for word, count in counts.items()], reverse=True)
print(result)          
print(result[0])       # the most frequent word: (6, 'love')
text = ('The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 '
        'in the negative direction, 0 at origin, 4 and 8 in the positive direction.')

points = re.findall(r'-?\d+', text)
print(points)                         

sorted_points = sorted(int(p) for p in points)
print(sorted_points)                  

distance = sorted_points[-1] - sorted_points[0]
print(distance)                       


#level 2

def is_valid_variable(name):
    return re.fullmatch(r'[A-Za-z_][A-Za-z0-9_]*', name) is not None

print(is_valid_variable('first_name'))    

print(is_valid_variable('first-name'))    
print(is_valid_variable('1first_name'))   
print(is_valid_variable('firstname'))     


#level    3

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(text):
    return re.sub(r'[^A-Za-z\s.?]', '', text)

def most_frequent_words(text, n=3):
    words = re.findall(r'\w+', text)
    counts = Counter(words)
    ranked = sorted([(c, w) for w, c in counts.items()], reverse=True)
    return ranked[:n]

cleaned_text = clean_text(sentence)
print(cleaned_text)
print(most_frequent_words(cleaned_text))    