#Day 5
empty_list = [] 
my_list = ['apple', 'banana', 'mango', 'orange', 'pawpaw', 'guava']
print(len(my_list))             
print(my_list[0], my_list[len(my_list) // 2], my_list[-1])
mixed_data_types = ['Hassana', 21, 1.65, 'Single', 'Zaria']
print(mixed_data_types)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies)) 
print(it_companies[0], it_companies[len(it_companies) // 2], it_companies[-1])
it_companies[0] = 'Meta'                                 
print(it_companies)

it_companies.append('Tesla')
it_companies.insert(len(it_companies) // 2, 'Intel')
it_companies[1] = it_companies[1].upper()  
print('#; '.join(it_companies))           
print('Apple' in it_companies)             
print(it_companies)

it_companies.sort()               
print(it_companies)
it_companies.reverse()      
print(it_companies)
print(it_companies[:3])               
print(it_companies[-3:]) 
mid = len(it_companies) // 2
print(it_companies[mid:mid + 1])

it_companies.pop(0)
it_companies.pop(len(it_companies) // 2)
it_companies.pop()
print(it_companies)
it_companies.clear()
print(it_companies)
del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
joined = front_end + back_end
print(joined)

full_stack = joined.copy()
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)

#Exercise level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
min_age = min(ages)                  
max_age = max(ages)                 
print(ages, min_age, max_age)

ages.append(min_age)                
ages.append(max_age)
ages.sort()                          

n = len(ages)                        
if n % 2 == 0:
    median = (ages[n // 2 - 1] + ages[n // 2]) / 2   
else:
    median = ages[n // 2]                            
print(median)                        

average = sum(ages) / n
print(average)                       

age_range = max_age - min_age
print(age_range)                    

print(abs(min_age - average))
print(abs(max_age - average))       

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

mid = len(countries) // 2
if len(countries) % 2 == 0:
    print(countries[mid - 1], countries[mid]) 
else:
    print(countries[mid])                      

half = (len(countries) + 1) // 2     
first_half = countries[:half]
second_half = countries[half:]
print(first_half)
print(second_half)

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
china, russia, usa, *scandic = countries
print(china, russia, usa)
print(scandic)   