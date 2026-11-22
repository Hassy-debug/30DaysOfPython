it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))                          
it_companies.add('Twitter')                       
it_companies.update(['Tesla', 'Intel', 'Nvidia'])   
it_companies.remove('IBM')                        
print(it_companies)

it_companies.discard('Nokia')    # fine, no error
# it_companies.remove('Nokia')   # this would give a KeyError

#Exercise 2
print(A.union(B))                  
print(A.intersection(B))           
print(A.issubset(B))               
print(A.isdisjoint(B))             
print(A.union(B), B.union(A))      
print(A.symmetric_difference(B))   

#Exercise level 3
age_set = set(age)                                 
print(len(age), len(age_set))                      

sentence = "I am a teacher and I love to inspire and teach people"   
words = set(sentence.split())
print(len(words), words)              

del A, B