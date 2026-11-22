empty_tuple = ()                                       
sisters = ('Aisha', 'Zainab')                           
brothers = ('Musa', 'Ibrahim')
siblings = sisters + brothers                            
print(siblings)
print(len(siblings))                                    
family_members = siblings + ('Father name', 'Mother name') 
print(family_members)

#Exercise level 2
*sibs, father, mother = family_members 
print(sibs, father, mother)

fruits = ('mango', 'orange', 'banana')                  
vegetables = ('carrot', 'onion', 'tomato')
animal_products = ('milk', 'meat', 'eggs')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)                     
print(food_stuff_lt)

n = len(food_stuff_lt)                                   
mid = n // 2
if n % 2 == 0:
    print(food_stuff_lt[mid - 1:mid + 1])                 
else:
    print(food_stuff_lt[mid])                             
print(food_stuff_lt[:3])                                  
print(food_stuff_lt[-3:])                                

del food_stuff_tp                                         

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)            
print('Iceland' in nordic_countries)                      