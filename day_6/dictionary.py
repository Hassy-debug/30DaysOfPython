#Day 6
dog = {}                                                
dog['name'] = 'Bruno'                                      
dog['color'] = 'White'
dog['breed'] = 'Russian'
dog['legs'] = 4
dog['age'] = 3
print(dog)

student = {                                               
    'first_name': 'Hassana',
    'last_name': 'Abdullahi',
    'gender': 'female',
    'age': 21,
    'marital_status': 'single',
    'skills': ['Python', 'Design'],
    'country': 'Nigeria',
    'city': 'Zaria',
    'address': 'Samaru'
}
print(student)

print(len(student))                      
print(student['skills'])                 
print(type(student['skills']))           
student['skills'].append('SQL')         
student['skills'].append('Excel')
print(student['skills'])

print(list(student.keys()))              
print(list(student.values()))           
print(list(student.items()))            

student.pop('address')                   
print(student)

del dog                                  #deletes the whole dictionary