#EXERCICES - DAY 1
# 1- The python version 
#C:\Users\admin\CODING\PYTHON\30daysofpython>python --version
#Python 3.12.0 

# 2- Operations
print(3 + 4) #Addition(+)
print(3 - 4) #Subtraction(-)
print(3 * 4) #Multiplication(*)
print(3 % 4) #Modulus(%)
print(3 / 4) #Division(/)
print(3 ** 4 ) #Exponential(**)
print(3 // 4) #Floor division operator(//)

# 3- Strings on the python interactive shell
print("KONDO") #Name
print("Chamsiya") #Family name
print("Togo") #Country
print("I am enjoying 30 days of python") #I am enjoying 30 days of python

# 4- Data types of the following data
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type("Your name"))
print(type("Your family name"))
print(type("Your country"))

#EXERCICE 3
# 1-
print(5) #Integer
print(6.2) #Float
print(1 +3j) #Complex
print("Hello Word") #String
print(True) #Boolean
print([1, 8, "You", 9]) #List
print(('Name', 'Family name', 'Country')) #Tuple
print({3.14, 9.81, 2,7}) #Set
print({'First_name': 'Asabeneh', 'last_name': 'encoreayeh', 'country': 'Togo'}) #Dictionary

# 2- Find an Euclidian distance between (2, 3) and (10, 8)

from math import dist

a = (2, 3)
b = (10, 8)

print(dist(a, b))
