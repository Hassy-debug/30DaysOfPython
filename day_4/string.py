print("Thirty" + " " + "Days" + " " + "Of" + " " + "Python") 
print("Coding" + " " + "For" + " " + "All")                   
company = "Coding For All"                                     
print(company)                                                 
print(len(company))                                             
print(company.upper())                                        
print(company.lower())                                         
print(company.capitalize(), company.title(), company.swapcase())

print(company[:6])                                 
print('Coding' in company)                       
print(company.find('Coding'), company.index('Coding'))
print(company.replace('Coding', 'Python'))
print("Python for Everyone".replace("Everyone", "All"))
print(company.split(' '))    
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(', '))

print(company[0])            
print(len(company) - 1)      
print(repr(company[10]))    
print("PFE")        
print("CFA")     
print(company.index('C')) 
print(company.index('F')) 
print("Coding For All People".rfind('l'))

s = 'You cannot end a sentence with because because because is a conjunction'
print(s.index('because')) 
print(s.rindex('because')) 
print(s[31:54])         
print(s.find('because'))  
print(s[s.find('because'):s.rfind('because') + 7]) 
print(company.startswith('Coding'))
print(company.endswith('coding'))  
print('   Coding For All      '.strip())

print('30DaysOfPython'.isidentifier())  
print('thirty_days_of_python'.isidentifier())

print('# '.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))

print("I am enjoying this challenge.\nI just wonder what is next.")
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

radius = 10         
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area:.0f} meters square.")

a, b = 8, 6               
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")