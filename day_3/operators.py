age = 21                      #integer
height = 1.65                 #float 
complex_num = 2 + 3j          #complex

base = float(input("Enter base: "))                
height_t = float(input("Enter height: "))
print("The area of the triangle is", 0.5 * base * height_t)

a = int(input("Enter side a: "))                   
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
print("The perimeter of the triangle is", a + b + c)

length = float(input("Enter length: "))            
width = float(input("Enter width: "))
print("Area:", length * width)
print("Perimeter:", 2 * (length + width))

r = float(input("Enter radius: "))                 
print("Area:", 3.14 * r * r)
print("Circumference:", 2 * 3.14 * r)

slope = 2                 #y = 2x - 2
y_intercept = -2          #value of y when x = 0
x_intercept = 1           # value of x when y = 0 (2x - 2 = 0)
print(slope, x_intercept, y_intercept)

#points (2, 2) and (6, 10)
m = (10 - 2) / (6 - 2)
distance = ((6 - 2)**2 + (10 - 2)**2) ** 0.5
print(m, distance)       

print(slope == m)         #compare slope 

for x in [-5, -4, -3, -2, -1, 0]: # y = x^2 + 6x + 9
    print(x, x**2 + 6*x + 9)

print(len('python'), len('dragon'))                 
print(len('python') != len('dragon'))               

print('on' in 'python' and 'on' in 'dragon')       #True

sentence = "I hope this course is not full of jargon"
print('jargon' in sentence)                        

print('on' not in 'python' and 'on' not in 'dragon')   #False

n = len('python')                                  
print(float(n), str(float(n))) 

number = 8
print(number % 2 == 0)                 #

print(7 // 3 == int(2.7))              #True (both are 2)
print(type('10') == type(10))          #False
print(int(float('9.8')) == 10)        

hours = float(input("Enter hours: "))              
rate = float(input("Enter rate per hour: "))
print("Your weekly earning is", hours * rate)

years = int(input("Enter number of years you have lived: "))  
print("You have lived for", years * 365 * 24 * 60 * 60, "seconds.")

print("1 1 1 1 1")                                 
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")

for i in range(1, 6):
    print(i, 1, i, i**2, i**3)