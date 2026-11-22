# day 9 list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
print([n for n in numbers if n <= 0])                  

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flat = [num for outer in list_of_lists for inner in outer for num in inner]
print(flat)                                            

tuples = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]   
print(tuples)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

flat_countries = [[item[0][0].upper(), item[0][0][:3].upper(), item[0][1].upper()]
                  for item in countries]
print(flat_countries)    

dicts = [{'country': item[0][0].upper(), 'city': item[0][1].upper()}
         for item in countries]
print(dicts)            

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_names = [item[0][0] + ' ' + item[0][1] for item in names]
print(full_names)        


slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
y_intercept = lambda m, x, y: y - m * x

m = slope(2, 2, 6, 10)
print(m)                          # 2.0
print(y_intercept(m, 2, 2))       