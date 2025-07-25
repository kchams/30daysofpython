#Exercises - Day 3
#1- Declare your age as integer variable
age = 34

#2- Declare your height as a float variable
height = 10.6

#3- Declare a variable that store a complex number
num_complex = 5 + 7j

#4- Write a script that prompts the user to enter base and height of the triangle and calculate an area of 
# this triangle (area = 0.5 x b x h).
base = input("Enter base : ")
height = input("Enter height : ")
area = 0.5 * float(base) * float(height)
print("The area of the triangle is", int(area))

#5- Write a script that prompts the user to enter side a, side b, and side c of the
#triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = input("Enter side a: ")
side_b = input("Enter side b: ")
side_c = input("Enter side c: ")
perimeter = int(side_a) + int(side_b) + int(side_c)
print("The perimeter of the triangle is", perimeter)

#6- Get length and width of a rectangle using prompt. Calculate its area (area =
# length x width) and perimeter (perimeter = 2 x (length + width))
length =int(input("Enter length: "))
width =int(input("Enter width: "))
area_rect = length * width
perimeter_rect = 2 * (length + width)
print("The area of the rectangle is", area_rect)
print("The Perimeter of the rectangle is", perimeter_rect)

#7- Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and
# circumference (c = 2 x pi x r) where pi = 3.14.
radius_circle = float(input("Enter radius: "))
pi = 3.14
area_circle = pi * radius_circle * radius_circle
circumference_circle = 2 * pi * radius_circle
print("The area of the circle is", area_circle)
print("The circumference of the circle is", circumference_circle)

#8- Calculate the slope, x-intercept and y-intercept of y = 2x -2
x = 5
y = 2 * x -2
print("The y-intercept is", y)

#9- Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between
# point (2, 2) and point (6,10)
x1, x2 = 2, 6
y1, y2 = 2, 10
slope_2 = (y2 - y1) / (x2 - x1)
print("The slope 2 is", slope_2)

#10- Compare the slopes in tasks 8 and 9.
slope_1 = 2
print("Slope 1 == Slop 2 :", slope_1 == slope_2)

#11- Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and
#figure out at what x value y is going to be 0.
x1, x2, x3, x4, x5 = 8, 5, 2, 7, 3
y_1 = x1 **2 + 6*x1 + 9
y_2 = x2 **2 + 6*x2 + 9
y_3 = x3 **2 + 6*x3 + 9
y_4 = x4 **2 + 6*x4 + 9
y_5 = x5 **2 + 6*x5 + 9

print("For x=8, (y = x^2 + 6x + 9); y =", y_1)
print("For x=5, (y = x^2 + 6x + 9); y =", y_2)
print("For x=2, (y = x^2 + 6x + 9); y =", y_3)
print("For x=7, (y = x^2 + 6x + 9); y =", y_4)
print("For x=3, (y = x^2 + 6x + 9); y =", y_5)

#12.Find the length of 'python' and 'dragon' and make a falsy comparison statement.
len_python = len('python')
len_dragon = len('dragon')
print("Length of 'python' == 'dragon' :", len_python == len('dragon')) 
print("Length of 'python' != 'dragon' :", len_python != len('dragon'))
print("Length of 'python' < 'dragon' :", len_python < len('dragon'))
print("Length of 'python' > 'dragon' :", len_python > len('dragon'))
print("Length of 'python' <= 'dragon' :", len_python <= len('dragon'))
print("Length of 'python' >= 'dragon' :", len_python >= len('dragon'))

#13- Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("'on' is found in both 'python' and 'dragon' :", 'on' in 'python' and 'on' in 'dragon')

#14- I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print("'jargon' in 'I hope this course is not full of jargon':", 'jargon' in 'I hope this course is not full of jargon')

#15- There is no 'on' in both dragon and python
print("There is no 'on' in both dragon and python:", 'on' not in 'dragon' and 'on' not in 'python')

#16.Find the length of the text python and convert the value to float and convert it to string
python_length = len('python')
print(float(python_length))
print(str(python_length))

#17.Even numbers are divisible by 2 and the remainder is zero. How do you check
# if a number is even or not using python?
# To check this, we won to verify if number % 2 == 0
print("7 is divisible by 2 and the remainder is zero:", 7 % 2 == 0)
print("8 is divisible by 2 and the remainder is zero:", 8 % 2 == 0)
print("4 is divisible by 2 and the remainder is zero:", 4 % 2 == 0)

#18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print("Is the floor division of 7 by 3 is equal to the int converted value of 2.7 :", 7 // 3 == int(2.7))

#19. Check if type of '10' is equal to type of 10
print("Is type of '10' is equal to type of 10", type('10') == type(10))

#20. Check if int('9.8') is equal to 10
print("Check if int('9.8') is equal to 10", type('9.8') == 10)

#21. Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = input("Enter hours:")
rate_per_hour = input("Enter rate per hour:")
week_pay = int(hours) * int(rate_per_hour)
print("Your weekly earning is", week_pay)

#22.Write a script that prompts the user to enter number of years. Calculate the 
# number of seconds a person can live. Assume a person can live hundred years
num_years = input("Enter number of years you have lived:")
lived_per_seconde = int(num_years) * 365 * 60 * 60
print("You have lived for " + str(lived_per_seconde) + " seconds.")

#23. Write a Python script that displays the following table
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")