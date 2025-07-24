#Day 2: 30 Days of python programming

#LEVEL 1
first_name = 'Afi' #First name variable 
last_name = 'KOFFI' #Last name variable
full_name = 'KOFFI Afi' #Full name variable
country = 'Togo' #Country variable
city = 'Lome' #City variable
age = 35 #Age variable 
year = 2025 #Year variable
is_married = True #variable is_married
is_true = True #variable is_true
is_light_on = False #is_light_on

first_name, last_name, country, age, is_married, is_light_on = 'Afi', 'KOFFI', 'Togo', 35, True, False #Multiple variable on one line

#LEVEL 2
#Check the data type of all your variables using type() built-in function
print("Type of first_name variable :", type(first_name))
print("Type of last_name variable :", type(last_name))
print("Type of full_name variable :", type(full_name))
print("Type of country variable :", type(country))
print("Type of city variable :", type(city))
print("Type of age variable :", type(age))
print("Type of year variable :", type(year))
print("Type of is_married variable :", type(is_married))
print("Type of is_true variable :", type(is_true))
print("Type of is_light_on variable :", type(is_light_on))

#Using the len() built-in function, find the length of your first name
print("Len of First_name : ", len(first_name))

#Compare the length of first name and last name
print(len(first_name) == len(last_name))

#Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

#Add num_one and num_two and assign the value to a variable total
total = num_one + num_two

#Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two

#Multiply num_two and num_one and assign the value to a variable product
product = num_two * num_one

#Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two

#Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one

#Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two

#Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two

#Calculate the area of a circle and assign the value to a variable name of area_of_circle
r = 30
pi = 3.14
area_of_circle = pi * r * r

#Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * pi * r

#Take radius as user input and calculate the area
r_input = input("Enter radius : ")
area = pi * int(r_input) * int(r_input)

#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("Enter your First name : ")
last_name = input("Enter your Last name : ")
country = input("Enter your country : ")
age = input("Enter your age : ")

#Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords')

"""
Here is a list of the Python keywords.  Enter any keyword to get more help.
False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not
"""